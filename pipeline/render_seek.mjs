// Generic seek(t) renderer with subframe motion blur (the product-launch-motion technique).
//   node render_seek.mjs <html> <outDir> <seconds> [--fps 60] [--sub 4] [--workers 3] [--stills t1,t2,...]
// Loads the page, waits for window.READY, calls window.seek(t) and screenshots (JPEG q95).
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
const require = createRequire("C:/Users/priya/AppData/Local/npm-cache/_npx/a9cd07ed041d113a/node_modules/");
const puppeteer = require("puppeteer-core");
const args = process.argv.slice(2);
const html = path.resolve(args[0]), out = path.resolve(args[1]), secs = parseFloat(args[2]);
const opt = (k, d) => { const i = args.indexOf("--" + k); return i < 0 ? d : args[i + 1]; };
const FPS = +opt("fps", 60), SUB = +opt("sub", 4), WORKERS = +opt("workers", 3), stills = opt("stills", null);
fs.mkdirSync(out, { recursive: true });
const launch = () => puppeteer.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: "new",
  args: ["--no-sandbox", "--font-render-hinting=none", "--force-color-profile=srgb"] });
async function mkPage(browser) {
  const p = await browser.newPage(); await p.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await p.goto(pathToFileURL(html).href); await p.waitForFunction("window.READY === true", { timeout: 30000 }); await p.evaluate("document.fonts.ready"); return p;
}
if (stills) {
  const browser = await launch(); const p = await mkPage(browser);
  for (const t of stills.split(",").map(Number)) { await p.evaluate((tt) => window.seek(tt), t); await p.screenshot({ path: path.join(out, `still-${t.toFixed(2)}.png`) }); }
  await browser.close(); process.exit(0);
}
const total = Math.round(secs * FPS * SUB);
const subT = (i) => Math.floor(i / SUB) / FPS + ((i % SUB) - (SUB - 1) / 2) / (FPS * SUB);
let next = 0, done = 0;
const browsers = [];
async function worker() {
  const browser = await launch(); browsers.push(browser); const p = await mkPage(browser);
  while (true) {
    const i = next++; if (i >= total) break;
    const f = path.join(out, `s${String(i).padStart(6, "0")}.jpg`);
    if (!fs.existsSync(f)) { await p.evaluate((tt) => window.seek(tt), Math.max(0, subT(i))); await p.screenshot({ path: f, type: "jpeg", quality: 95 }); }
    if (++done % 500 === 0) console.log("frames", done, "/", total);
  }
}
await Promise.all(Array.from({ length: WORKERS }, worker));
for (const b of browsers) await b.close(); console.log("RENDER_DONE", total); process.exit(0);
