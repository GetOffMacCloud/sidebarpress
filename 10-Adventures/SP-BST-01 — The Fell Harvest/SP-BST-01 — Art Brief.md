---
type: art-brief
adventure: "SP-BST-01"
section: internal
publish_order: 0
publish: false
---

# SP-BST-01 — Art Brief: *The Fell Harvest*

Back to [[SP-BST-01-The-Fell-Harvest]] · Index: [[65-Bestiary/00 — Bestiary Index]] · Board: [[SP-BST-01 — Board]]

**What we're making (Greybeard, 2026-10-24):** creature plates (78), villain splashes (23), the cover and three chapter openers (4), and specimen spot art (12), about 117 images. **No tokens are generated.** Greybeard's token maker builds them from the plates, so every plate is composed for it.

> [!info] One plate does three jobs
> **Plate** (in the book) → **FGU portrait** (a crop of the plate) → **token** (Greybeard's token maker, fed the plate). Generate each creature once; the portrait and token are crops of that plate.

---

## Style anchors

**Plate spine:** every creature prompt already ends with it, in that creature's own note under *Art Prompt*.
> *full figure centered with the head and shoulders in the upper middle of the frame and clear space on every side, naturalist field-guide plate, a single creature studied in full on a plain warm parchment ground, oil on board, muted umber, bone, moss and slate palette, soft overcast light, eerie and restrained, folk-horror mood, no text*

**Scene spine:** for splashes, openers, and the cover.
> *dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent color, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text*

**Locking the look**
1. Generate the first five plates: [[Straw Double]], [[Bell-Wight]], [[Kikimora]], [[Vyrathax, the Crimson Tyrant]], and [[The Marrowmother]]. Together they cover the range from humble to grand.
2. Pick the one that best fits the book and record its URL here: **`--sref` = ________**.
3. Add that `--sref` to every later prompt. Keep `--seed 26500` throughout.

**Avoid throughout:** heroic posing, glowing magic beyond the one accent color, gore, busy backgrounds on plates, modern faces, and smiling heroes.

---

## Composition rules for plates (token-maker friendly)
- The whole creature is in frame, and no part touches the edge.
- The head and shoulders sit in the **upper middle third**. Your token maker crops there.
- The background is plain parchment with nothing behind the head, so the cutout stays clean.
- **Huge and serpentine creatures** (the dragons, the Marrowmother, Sylvarith) curl or coil to fit the frame rather than being cropped. If a plate can't give a clean head crop, generate one extra **head study** for the token: the same prompt, swapping "full figure" for "head and shoulders portrait".

---

## Sizes and files
All files go in `99-Assets/SP-BST-01/`. Name every file exactly after the creature note, so links never break.

| Asset | Prompt `--ar` | Render at | File | Book size (Homebrewery) |
|---|---|---|---|---|
| Creature plate | 3:4 | 1200 × 1600 | `plates/<Creature>.png` | `{width:8cm}` (one column) |
| FGU portrait | crop of the plate | 600 × 800 | `portraits/<Creature> — Portrait.png` | — |
| Token | from the token maker | 512 × 512, transparent | `tokens/<Creature> — Token.png` | — |
| Villain splash | 2:3 | 1400 × 2100 | `splashes/<Creature> — Splash.png` | full page, `{width:17cm}` |
| Chapter opener | 1:3 | 945 × 2835 | `openers/<Name>.png` | `{width:8cm}`, a full column |
| Cover | 2:3 | 2550 × 3300 (print) | `openers/Cover.png` | — |
| Spot art | 1:1 | 1000 × 1000 | `spot/<Name>.png` | `{width:4cm}` |

Use **PNG** throughout. Host images on Imgur, a GitHub raw link, or Homebrewery's own uploader, never Discord, whose links expire. Homebrewery sizes images with `{width:Ncm}`, never `height`.

---

## Tracker: plates, portraits and tokens
Every creature note carries `art_plate`, `portrait`, and `token` in its frontmatter (`todo → generated → approved → placed`). Update a field as each image is done, and these tables update themselves.

```dataview
TABLE WITHOUT ID
  file.link AS "Creature", cr AS "CR", section AS "Chapter",
  art_plate AS "Plate", portrait AS "Portrait", token AS "Token"
FROM "65-Bestiary"
WHERE type = "creature"
SORT choice(art_plate = "placed", 4, choice(art_plate = "approved", 3, choice(art_plate = "generated", 2, 1))) ASC, file.name ASC
```

**Progress:** `$= const c = dv.pages('"65-Bestiary"').where(p => p.type == "creature"); const done = k => c.where(p => p[k] == "approved" || p[k] == "placed").length; "Plates " + done("art_plate") + "/" + c.length + " · Portraits " + done("portrait") + "/" + c.length + " · Tokens " + done("token") + "/" + c.length`

---

## Villain splashes (23)
These are full-page action scenes, one per Rogues' Gallery villain. Each shows the villain in its lair with small figures for scale. Prompts are below. Track them with `art_splash` in each villain's frontmatter.

```dataview
TABLE WITHOUT ID file.link AS "Villain", cr AS "CR", art_splash AS "Splash"
FROM "65-Bestiary"
WHERE section = "rogues-gallery" AND type = "creature"
SORT file.name ASC
```

> [!example]- Splash prompts (click to open)
> **Braknor Skullrend**
> ```
> A towering horned fiend with scarred dark red hide charging head-down along a narrow stone labyrinth corridor toward three small adventurers, his ember-edged greataxe raised and trailing sparks, split skulls swinging from his belt, dust and broken masonry bursting from the walls where his horns scrape, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of ember orange, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Dorukai Thunderclub**
> ```
> A blue-skinned ogre-mage in heavy chain mail descending on a column of storm wind into a mountain pass, a colossal stone-and-iron hammer raised overhead and forked lightning arcing from it to the rocks, small travelers and pack mules scattering on the path below, black storm clouds churning above, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of pale lightning blue, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Drevnar Soulreaver**
> ```
> A fallen paladin in blackened plate walking slowly through the smoke of a burned roadside shrine, his dark sword drinking the light, a widening ring of withered grey grass spreading from his feet, a kneeling defeated knight in the foreground with a broken holy symbol, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of tarnished gold, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Eylandra Stormchant**
> ```
> A merfolk storm-priestess in pale coral armor rising on a spinning waterspout above a shipwreck on a reef, arms raised to a low storm sky, lightning crawling across the waves toward a small longboat of rowing sailors, rain sheeting sideways, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of storm green, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Glazryth, the Pale Terror**
> ```
> A gaunt white dragon bursting up through the snow crust of a glacier in an explosion of ice, a sheer blue ice wall behind it holding a row of frozen people standing mid-scream, a small roped party of mountaineers tumbling backward on the slope, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of glacial blue, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **The Gluttonwretch**
> ```
> A monstrous undead turkey the size of a hay-wagon landing on a long harvest banquet table in a candlelit manor hall, gravy-dark ichor splashing, red crystal cranberry shards bursting from its wings, plates and goblets and roast fowl sliding toward its gaping beak, richly dressed guests fleeing and one guest still eating helplessly, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of cranberry red, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Gorzak the Flaymaster**
> ```
> A gnoll warlord in scorched black plate standing on a hill of the fallen at dusk, a long barbed spear across his shoulders trailing dark smoke, his hyena pack feeding behind him, flayed hides hanging like banners from crossed spears, a burning caravan in the distance, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of dull yellow eyes, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Grakh Unscarred**
> ```
> A grizzled grey-tusked orc warlord driving a notched iron war-standard into cracking earth at the mouth of a tunnel, his open breastplate showing eleven tally-scars above clean unbroken skin, his war-band of scarred raiders and hounds surging past him out of the dark, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of rust red, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Mortenia's Echo, the Silent Sister**
> ```
> A sanctum of nine veiled stone saints, the central statue on a dais cracking open to release a translucent veiled spirit with one finger to her lips, the eight lesser statues along the walls turning their heads toward a small party of adventurers frozen in the doorway, dust drifting in a single shaft of grey light, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of cold candle gold, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Saiyora's Echo, the Iron Sister**
> ```
> An undead woman knight in rusted rent plate holding a long stone stair before sealed catacomb doors, her notched greatsword sweeping down at a shield-bearing adventurer on the steps below, grey ghost-light where her face should be, broken weapons of earlier challengers scattered on the stair, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of rust orange, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Sister Amarantha Wick, the Bell-Keeper**
> ```
> A gaunt undead nun in a habit sewn with hundreds of tiny iron bells walking between leaning headstones at night, every grave topped by a small bell on a post, one bell ringing as a hand pushes up through the soil beneath it, a lantern-bearing gravedigger watching from behind a yew tree, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of lantern amber, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Sorrowbay, the Chained Sire**
> ```
> A huge grey wolf taller than a carthorse leading a pack of iron-collared wolves out of a dark pine forest onto a moonlit road, a broken runed collar and snapped chain at his throat, a lone mounted warden raising a whistle to his lips in the foreground, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of cold iron grey-blue, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Sylvarith, the Venomous Wyrm**
> ```
> A long serpentine green dragon rising from a black lake in a drowned forest, smiling, poisonous vapor curling from its jaws, the gilded roof of a sunken manor just below the surface, a small rowboat of nervous scholars holding up a ledger and a lantern, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of venom green, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Tharazul, the Desert Storm**
> ```
> A walking sandstorm crossing a desert at dusk against the wind, a vast blue dragon visible at its heart in a flash of lightning, glassy fulgurite spires standing in the dunes, a small camel caravan bracing in the foreground, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of electric sapphire, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **The Endless Howl**
> ```
> A huge black wolf with smoldering ash-flecked fur loping out of a burning forest, head thrown back mid-howl, embers pouring from its jaws, scorched paw prints across a field, villagers at a palisade in the foreground covering their ears, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of ember orange, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **The Marrowmother**
> ```
> A huge hollow spider of lashed bones descending on grey silk threads from the roof of a vast cavern, silk-wrapped bodies hanging around it, its brood of bone-beasts (an antlered skeleton, a skeletal hound, a bone-maul brute) climbing up from the floor toward a small torchlit party, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of torchlight amber, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **The Ninefold Voice**
> ```
> A giant grey-and-black shrike perched in a vast black thorn tree hung with impaled carcasses on a moor at dusk, beak open as if calling, a lone traveler on the road below turning toward the tree as if hearing a familiar voice, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of dried-blood red, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Velka's Echo, the Veiled Sister**
> ```
> A gaunt unnaturally tall undead woman in layered grey funeral veils unfolding from a ledge above sealed catacomb doors, yard-long hooked fingers reaching down toward an unaware torch-bearing adventurer below, shadows pooling around her, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of torchlight amber, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Vespera Pixiecoil, the Prism-Coiled**
> ```
> A tiny fox-sized fey dragon with butterfly wings somersaulting above an impossible spring meadow, rainbows scattering from her wings, flowers in impossible colors blooming in spirals, a small party of armored adventurers below laughing helplessly while their weapons sprout blossoms, the scene beautiful but subtly wrong, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of prismatic color, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Vyrathax, the Crimson Tyrant**
> ```
> A huge crimson dragon sprawled on a broken stone throne in a burned-out dwarven hall, a dead king's crown hooked over one horn, a court of terrified humans and dwarves kneeling in grey ash before it, a lone envoy standing upright in the foreground, smoke curling to a shattered vaulted ceiling, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of blood crimson, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Zarathryx, Champion of the Dragon Queen**
> ```
> A massive dragon scaled crimson on one flank and storm-blue on the other standing at the head of a war-host beneath five colored banners, flame curling from one side of its jaws and lightning from the other, lowering its head toward a small knot of envoys under a flag of truce, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of crimson and storm blue, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Zhulkar Boneweaver**
> ```
> A towering undead sorcerer woven from hundreds of bones rising from a throne of skulls in a valley of whispering bleached bone under a murky green pall, green fire in its ribcage, skeletons clawing up from the ground at its gesture toward a small party at the valley's edge, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of necrotic green, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```
> **Zykryss, the Shadowed Doom**
> ```
> A huge black dragon surging out of the dark water of a vaulted cistern beneath a city, acid streaming from its jaws and smoking on eroded columns, two yellow eyes blazing, a small party on a crumbling stone walkway raising lanterns, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of acid yellow-green, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
> ```

---

## Cover and chapter openers (4)
- [ ] **Cover**: generated · approved · placed
- [ ] **Opener: The Bestiary**: generated · approved · placed
- [ ] **Opener: The Rogues' Gallery**: generated · approved · placed
- [ ] **Opener: Appendices**: generated · approved · placed

**Cover:** leave the upper third for the title.
```
A harvest field at dusk under a swollen orange moon, wheat cut and bound in sheaves, a tall scarecrow in the foreground whose shadow on the stubble is the shape of a horned beast, shapes of half-seen creatures moving in the uncut wheat behind it (antlers, wings, a long serpentine neck), a distant village with lit windows, empty dark sky in the upper third for a title, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of harvest-moon orange, low overcast light, eerie and restrained, folk-horror mood, cinematic composition, no text --ar 2:3 --v 8.1 --style raw --seed 26500
```

**Opener: The Bestiary:** a naturalist's desk.
```
Extreme vertical composition, a naturalist's cluttered desk seen from above in candlelight, pinned grey moths on a card, a sketchbook open to a drawing of a bone stag, specimen jars holding a coiled serpent and a tiny antlered hare, a green-bronze collar ring, quills and spilled ink, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of candle gold, low overcast light, eerie and restrained, folk-horror mood, no text --ar 1:3 --v 8.1 --style raw --seed 26500
```

**Opener: The Rogues' Gallery:** the portrait hall.
```
Extreme vertical composition, a long dim gallery wall hung with dark oil portraits in heavy frames stacked floor to ceiling, a crowned red dragon, a veiled nun, a horned fiend, a bone-woven sorcerer, the lowest frame empty with a small brass plate beneath it, a single candle on the floor, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of candle gold, low overcast light, eerie and restrained, folk-horror mood, no text --ar 1:3 --v 8.1 --style raw --seed 26500
```

**Opener: Appendices:** the tally.
```
Extreme vertical composition, an old leather ledger lying open on a stone table, columns of tally marks in brown ink, small knucklebones used as counters along its margins, a balance scale holding a wheat sheaf on one pan and a skull on the other, dark fantasy oil painting on board, muted umber, bone, moss and slate palette with a single restrained accent of dried-ink brown, low overcast light, eerie and restrained, folk-horror mood, no text --ar 1:3 --v 8.1 --style raw --seed 26500
```

---

## Specimen spot art (12)
Small, page-end fillers drawn as field-guide specimens. Spine: *isolated specimen study on a plain warm parchment ground, naturalist field-guide illustration, oil on board, muted umber, bone, moss and slate palette, soft overcast light, no text --ar 1:1 --v 8.1 --style raw --seed 26500*

| ✓ | Specimen | Pairs with | Prompt subject (+ spine) |
|---|---|---|---|
| [ ] | Ledger and quill | [[Ledger Hag]] | an old leather ledger with a long black quill laid across it, one page signed in faded red ink |
| [ ] | Grave-bronze collar ring | [[Bone Beast Template]] | a ring of old green bronze cut with a triple spiral, a few vertebrae still threaded through it |
| [ ] | Pinned hush-moth | [[Hush-Moth Swarm]] | a single grey moth pinned to a card, its wings patterned like a closed mouth, grey dust beneath it |
| [ ] | Anchor bone | [[Tithe-Reaper]] | a single human finger bone tied with a frayed length of hangman's rope |
| [ ] | Cranberry shard | [[Gluttonwretch]] | a jagged fist-sized shard of red crystal shaped like a cranberry, glistening with dark gravy |
| [ ] | Spindle and snarl | [[Kikimora]] | a small wooden spindle wrapped in hopelessly tangled red and white thread |
| [ ] | Cracked clapper | [[Bell-Wight]] | a heavy iron bell clapper split down its length, a frayed rope sally knotted to it |
| [ ] | Toll cairn | [[Toll-Troll]] | a small cairn of odd payments: a rag doll, a lute string, a lock of hair, three coins |
| [ ] | Runed collar | [[Iron-Marked Wolf]] | a broken iron wolf collar etched with runes, a link of snapped chain attached |
| [ ] | Prism scale | [[Vespera Pixiecoil, the Prism-Coiled]] | a single small dragon scale throwing tiny rainbows across the parchment |
| [ ] | Firesparker | [[Kobold Pyrotechnic]] | a hand-made kobold firework rocket of bamboo and waxed paper with a short fuse |
| [ ] | Antler nub | [[Wolpertinger]] | a tiny forked roebuck antler no bigger than a thumb beside a speckled pheasant feather |

---

## Workflow per creature
1. Copy the **Art Prompt** from the creature's note, add the locked `--sref`, and generate.
2. Save the pick as `plates/<Creature>.png` and set `art_plate: generated`. Set it to `approved` once it's chosen for the book.
3. Crop the head and shoulders to 600 × 800 → `portraits/…`, and set `portrait: approved`.
4. Run the plate through the token maker → `tokens/…`, and set `token: approved`.
5. In FGU, attach the portrait and token to the NPC record (after the FGU Import).
6. At packaging, embed the plate in the entry with `{width:8cm}` and set `art_plate: placed`.
