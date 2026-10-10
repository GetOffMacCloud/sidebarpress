---
publish: false
type: Timepiece
campaign: "Ritterstadt — Greyhawk University (West Marches)"
calendar: "Greyhawk Common Year, pinned to 576 CY"
clock_model: "Live — real date → 364-day Greyhawk calendar (exact day-of-year)"
current_date: "0576-06-02"
note: "current_date is a static fallback; the live value is computed below and updates on open."
---
# ⏲️ Ritterstadt Timepiece — West Marches

> [!info] How this clock works
> The in-game date is **pinned to 576 CY** and tracks **real time**. Today's real-world date is mapped onto the 364-day Greyhawk calendar by **exact day-of-year** — the four 7-day festival weeks (Needfest, Growfest, Richfest, Brewfest) occupy real calendar space. It recomputes every time you open this note: no buttons, no maintenance.

## 🕰️ Current In-Game Date

```dataviewjs
// ── Greyhawk 576 CY calendar engine ───────────────────────────
const YEAR = 576;
const UNITS = [
  ["Needfest",7,true],["Fireseek",28,false],["Readying",28,false],["Coldeven",28,false],
  ["Growfest",7,true],["Planting",28,false],["Flocktime",28,false],["Wealsun",28,false],
  ["Richfest",7,true],["Reaping",28,false],["Goodmonth",28,false],["Harvester",28,false],
  ["Brewfest",7,true],["Patchwall",28,false],["Ready'reat",28,false],["Sunsebb",28,false]
];
// Weekday anchor (provisional): day 1 of the year = Starday. Adjust if you have a canon weekday.
const WEEKDAYS = ["Starday","Sunday","Moonday","Godsday","Waterday","Earthday","Freeday"];
function ghDate(n){
  n = ((n - 1) % 364 + 364) % 364 + 1;            // wrap into 1..364
  let acc = 0;
  for (const [name,len,fest] of UNITS){
    if (n <= acc + len){
      const day = n - acc;
      const wd  = WEEKDAYS[(n - 1) % 7];
      const label = fest ? `${name} (day ${day}), ${YEAR} CY` : `${day} ${name}, ${YEAR} CY`;
      return { label, wd, n, name, day, fest };
    }
    acc += len;
  }
}
// ── Live: real date → day-of-year, pinned to 576 ──────────────
const now = new Date();
let doy = Math.floor((now - new Date(now.getFullYear(),0,0)) / 86400000); // 1-based day-of-year
if (doy > 364) doy = 364;  // clamp the 365th/366th real day onto the last Greyhawk day
const g = ghDate(doy);
dv.paragraph(`> ## 🗓️ **${g.label}**\n> *${g.wd}*  ·  day ${g.n} of 364  ·  real ${now.toDateString()}`);
```

## Greyhawk Calendar Reference

| # | Month | Season | ≈ Real month |
|---|-------|--------|--------------|
| — | **Needfest** (festival) | Midwinter | turn of year |
| 01 | Fireseek | Winter | January |
| 02 | Readying | Spring | February |
| 03 | Coldeven | Spring | March |
| — | **Growfest** (festival) | Early Spring | late March |
| 04 | Planting | Low Summer | April |
| 05 | Flocktime | Low Summer | May |
| 06 | Wealsun | Low Summer | June |
| — | **Richfest** (festival) | Midsummer | late June |
| 07 | Reaping | High Summer | July |
| 08 | Goodmonth | High Summer | August |
| 09 | Harvester | High Summer | September |
| — | **Brewfest** (festival) | Harvest | late September |
| 10 | Patchwall | Autumn | October |
| 11 | Ready'reat | Autumn | November |
| 12 | Sunsebb | Winter | December |

Each month is 28 days; each festival is 7 days; the year is 364 days. Weekday cycle: Starday · Sunday · Moonday · Godsday · Waterday · Earthday · Freeday.

## Notes

- **Year is fixed at 576 CY.** Only the month/day move with real time, so the campaign never ages out of 576.
- **Translation rule:** real day-of-year *N* → Greyhawk day *N* of the 364-day year (festival weeks included). The last 1–2 real days of a Gregorian year clamp onto Sunsebb 28.
- **Weekday anchor is provisional** (year-day 1 = Starday). If the West Marches has an established weekday for a known date, tell me and I'll re-anchor the `WEEKDAYS` index.
- This replaces the prose date in the Player Primer ("12th of Planting, 576 CY") as the live source of truth. Update the Primer line if you want it to match, or leave it as flavour for session zero.
