#!/usr/bin/env node
/* Builds facilitators/index.html from a private source file and a passcode.

   Usage (from the repository root):
     node tools/encrypt-facilitators.mjs /path/outside/the/repo/facilitators-source.html "the passcode"

   The source file and the passcode must never be committed to this repository.
   Only the encrypted page this script writes is safe to publish. */
import { pbkdf2Sync, randomBytes, createCipheriv, createHash } from "node:crypto";
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

// The delegate floor plan, with the partitioned half of Conference Room 2 marked as the team base.
let plan = readFileSync(join(here, "floorplan.svg"), "utf8");
plan = plan
  .replace('<rect class="plan-staff" x="262" y="33" width="45" height="42"/>',
           '<rect class="plan-staffroom" x="262" y="33" width="45" height="42"/>')
  .replace("<!-- labels shown on wider screens -->",
           '<g class="plan-key-staff"><rect x="269" y="38.5" width="31" height="31"/><text x="284.5" y="61.5">S</text></g>\n  <!-- labels shown on wider screens -->')
  .replace("and the left-hand half is for staff only.",
           "and the left-hand half is the team base for facilitators and the conference team.");
if (!plan.includes("plan-staffroom") || !plan.includes("plan-key-staff")) {
  console.error("Could not mark the team base on the plan. Has tools/floorplan.svg changed?");
  process.exit(1);
}

let source = readFileSync(sourcePath, "utf8").replace(/<!--[\s\S]*?-->/, "").trim();
if (!source.includes("{{PLAN}}")) console.warn("Note: no {{PLAN}} placeholder in the source.");
source = source.replace("{{PLAN}}", plan);

// Fingerprint added to each stylesheet and script address, so a browser never
// pairs a new page with an older copy it has kept.
const version = (path) => createHash("sha256").update(readFileSync(join(root, path))).digest("hex").slice(0, 10);

const iter = 600000;
const salt = randomBytes(16);
const iv = randomBytes(12);
const key = pbkdf2Sync(tidy(passcode), salt, iter, 32, "sha256");
const cipher = createCipheriv("aes-256-gcm", key, iv);
const data = Buffer.concat([cipher.update(source, "utf8"), cipher.final(), cipher.getAuthTag()]);

const payload = JSON.stringify({
  v: 1, iter, salt: salt.toString("base64"), iv: iv.toString("base64"), data: data.toString("base64"),
});
// "Monday 12 October 2026 at 11.05am", in Nottingham time.
const parts = Object.fromEntries(new Intl.DateTimeFormat("en-GB", {
  timeZone: "Europe/London", weekday: "long", day: "numeric", month: "long", year: "numeric",
  hour: "numeric", minute: "2-digit", hour12: true,
}).formatToParts(new Date()).map((p) => [p.type, p.value]));
const updated = `${parts.weekday} ${parts.day} ${parts.month} ${parts.year} at ${parts.hour}.${parts.minute}${parts.dayPeriod.toLowerCase()}`;
const page = readFileSync(join(here, "facilitators-shell.html"), "utf8")
  .replace("{{PAYLOAD}}", payload)
  .replaceAll("{{UPDATED}}", updated)
  .replace("{{CSS_V}}", version("assets/site.css"))
  .replace("{{FCSS_V}}", version("assets/facilitators.css"))
  .replace("{{FJS_V}}", version("assets/facilitators.js"));

mkdirSync(join(root, "facilitators"), { recursive: true });
writeFileSync(join(root, "facilitators", "index.html"), page);
console.log(`wrote facilitators/index.html (${page.length} bytes, ${source.length} characters encrypted)`);
