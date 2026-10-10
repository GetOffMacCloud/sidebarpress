---
publish: false
type: Timepiece
current_date: 21st of Goodmonth, 576 CY
census_count: 12
time_offset: 49
epoch_oerth_day: 238
current_weather: Grey overcast, a slow steady drizzle
active_global_effects:
  - Nomad Migration (returning — herders drifting back down the Sepia toward winter pasture)
current_season: Goodmonth (Autumn)
---

# 🕰️ Chronometer of Oerth

%%
GREYHAWK CALENDAR — 364 days/year
12 months × 28 days + 4 festival weeks × 7 days

Day 1    Needfest    (7d, festival)       — Midwinter
Day 8    Fireseek    (28d)                — Winter
Day 36   Readying    (28d)                — Spring
Day 64   Coldeven    (28d)                — Spring
Day 92   Growfest    (7d, festival)       — Spring Festival
Day 99   Planting    (28d)                — Early Summer
Day 127  Flocktime   (28d)                — Summer
Day 155  Wealsun     (28d)                — Summer
Day 183  Richfest    (7d, festival)       — Midsummer
Day 190  Reaping     (28d)                — High Summer
Day 218  Goodmonth   (28d)                — Autumn
Day 246  Harvester   (28d)                — Autumn
Day 274  Brewfest    (7d, festival)       — Harvest Festival
Day 281  Patchwall   (28d)                — Late Autumn
Day 309  Ready'reat  (28d)                — Early Winter
Day 337  Sunsebb     (28d)                — Deep Winter

Campaign Epoch: epoch_oerth_day 98 = Growfest 7 = April 8, 2026
Current: epoch_oerth_day 236 = Goodmonth 19 = July 6, 2026 (real ↔ in-game 1:1 plus time_offset 49 from the narrative skip of 2026-07-06)
To skip time narratively: increase epoch_oerth_day (and time_offset) by the number of days to advance.
%%

## 🗓️ Current Status
> [!tip] The [[Town State Dashboard|Town Engine]] runs alongside this calendar. The engine reads `current_date`, `epoch_oerth_day`, `current_weather`, and `active_global_effects` from this note; it writes back the date on each daily generation.

- **Date:** `$= dv.current().current_date`
- **Season:** `$= dv.current().current_season`
- **Weather:** `$= dv.current().current_weather`
- **Census:** `$= dv.current().census_count` / 50 souls
- **Engine status:** [[Town State Dashboard|see Town State Dashboard]] · last automated roll **28 Wealsun, 576 CY**; 29 Wealsun – 19 Goodmonth skipped narratively and hand-reconciled 2026-07-06

---

## 🌪️ Regional Modifiers
> [!caution] Current World Hazards
> - **Blackfrost (East Mark):** *Ended.* The Bloom spent itself around 18 Wealsun; no Survival penalty remains. (Source note kept dormant in case it left something behind.)
> - **Lake Quag Mists:** Navigation near the shore is currently at Disadvantage.
> - **Nomad Migration:** Autumn return — herders are drifting back down the Sepia toward winter pasture. No mechanical effect; useful for cover and for picking up travel news at the well.

---

## 🏛️ University & Town Standing
- **Total Gold Surrendered:** `$= dv.pages('"Greyhawk University/04. Campaign Logs/Session Notes"').gold_earned.array().reduce((acc, val) => acc + (val || 0), 0)` gp
- **Town Prosperity Avg:** `$= Math.round(dv.pages('"Greyhawk University/05. The Hamlet of Ritterstadt/Town Services"').prosperity_level.array().reduce((acc, val) => acc + (val || 0), 0) / dv.pages('"Greyhawk University/05. The Hamlet of Ritterstadt/Town Services"').length)`
- **Master Threat (engine):** `$= dv.page("Greyhawk University/05. The Hamlet of Ritterstadt/Town Engine/_State/Town State Dashboard").master_threat` / 10

---

## 📜 Recent Events
*Record major world-shifting events here so you don't forget them.*
- **0576-01-01:** Ritterstadt officially opened the doors to Greyhawk University.
- **0576-01-05:** The Blacksmith reported a shortage of ore; "Rust-Red Extraction" commissioned.
- **0576-Planting-12:** Campaign Timepiece set; Blackfrost Bloom at peak intensity.
- **0576-Flocktime-21:** [[Town State Dashboard|Town Engine]] installed; calendar advanced to real-world parity. Blackfrost waning; Iuz tap node intensity 6 and rising; Goric Ashendelf's caravan in town short of manifest.
