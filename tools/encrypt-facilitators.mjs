#!/usr/bin/env node
/* Builds facilitators/index.html from a private source file and a passcode.

   Usage (from the repository root):
     node tools/encrypt-facilitators.mjs /path/outside/the/repo/facilitators-source.html "the passcode"

   The source file and the passcode must never be committed to this repository.
   Only the encrypted page this script writes is safe to publish. */
import { pbkdf2Sync, randomBytes, createCipheriv } from "node:crypto";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, "..");
const [, , sourcePath, passcode] = process.argv;

if (!sourcePath || !passcode) {
  console.error('Usage: node tools/encrypt-facilitators.mjs <source.html> "<passcode>"');
  process.exit(1);
}
if (!relative(root, resolve(sourcePath)).startsWith("..")) {
  console.error("Keep the source file outside this repository so it cannot be committed by mistake.");
  process.exit(1);
}

const tidy = (code) => code.trim().toLowerCase().replace(/[\s_.,]+/g, "-").replace(/-+/g, "-");

// The delegate floor plan, with Conference Suite 3 marked for the team.
let plan = readFileSync(join(here, "floorplan.svg"), "utf8");
plan = plan
  .replace('<rect class="plan-line" x="262" y="275" width="90" height="36"/>',
           '<rect class="plan-staffroom" x="262" y="275" width="90" height="36"/>')
  .replace('<text x="307" y="297">Conference Suite 3</text>', "")
  .replace("<!-- labels shown on wider screens -->",
           '<g class="plan-key-staff"><rect x="291.5" y="277.5" width="31" height="31"/><text x="307" y="300.5">S</text></g>\n  <!-- labels shown on wider screens -->')
  .replace("The prayer room and toilets are in the middle, beside the Conference Theatre.",
           "Conference Suite 3, at the bottom, is the base for facilitators and the conference team.");
if (!plan.includes("plan-staffroom") || !plan.includes("plan-key-staff")) {
  console.error("Could not mark Conference Suite 3 on the plan. Has tools/floorplan.svg changed?");
  process.exit(1);
}

let source = readFileSync(sourcePath, "utf8").replace(/<!--[\s\S]*?-->/, "").trim();
if (!source.includes("{{PLAN}}")) console.warn("Note: no {{PLAN}} placeholder in the source.");
source = source.replace("{{PLAN}}", plan);

const iter = 600000;
const salt = randomBytes(16);
const iv = randomBytes(12);
const key = pbkdf2Sync(tidy(passcode), salt, iter, 32, "sha256");
const cipher = createCipheriv("aes-256-gcm", key, iv);
const data = Buffer.concat([cipher.update(source, "utf8"), cipher.final(), cipher.getAuthTag()]);

const payload = JSON.stringify({
  v: 1, iter, salt: salt.toString("base64"), iv: iv.toString("base64"), data: data.toString("base64"),
});
const updated = new Date().toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
const page = readFileSync(join(here, "facilitators-shell.html"), "utf8")
  .replace("{{PAYLOAD}}", payload)
  .replace("{{UPDATED}}", updated);

mkdirSync(join(root, "facilitators"), { recursive: true });
writeFileSync(join(root, "facilitators", "index.html"), page);
console.log(`wrote facilitators/index.html (${page.length} bytes, ${source.length} characters encrypted)`);
