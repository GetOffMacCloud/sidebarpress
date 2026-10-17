---
publish: false
name: The Fiend's Rest Public House
tags:
  - Category/Place
type: Place
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Commerce
location: "[[Ritterstadt]]"
proprietor: Karet
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] The Fiend's Rest Public House
>> ~~~meta-bind
>> INPUT[select(
>> option(1, ℹ️General Info),
>> option(2, 🏃‍♂️‍➡️NPCs),
>> option(3, 📝GM Notes),
>> class(tabbed)
>> )]
>> ~~~
>>>[!tabbed-box-maxh]
>>> >[!div-m|no-title]
>>> > ![[#General|no-h clean]]
>>>
>>> >[!div-m|no-title]
>>> > ![[#NPCs|no-h clean]]
>>>
>>> > [!div-m|no-title]
>>> > ![[#GM Notes|no-h clean]]

> [!NOTE|no-title]
> ~~~meta-bind
> INPUT[select(
> option(1, 🗺️Sub-Areas),
> option(2, 🤐Rumours),
> class(tabbed)
> )]
> ~~~
> >[!tabbed-box]
> > >[!div-m|no-title]
> > > ![[#Sub-Areas|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Rumours|no-h clean]]

---

# General

Select Settlement: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

Select Category: `INPUT[inlineSelect(option(Commerce), option(Agriculture), option(Military), option(Philosophy), option(Industrial), option(Nesting), option(Government)):MyCategory]`

*The Fiend's Rest* is Ritterstadt's public house and the operational heart of the University's commission system. It is where the Job Board lives, where travellers and pack-merchants take a room, and where every rumour in the Sepia Uplands eventually surfaces over ale. If the Wachturm is the hamlet's secret and the Ritter's Hall its authority, the Fiend's Rest is its nervous system — the one room where soldiers, scholars, trappers, and road-merchants all end up in the same firelight.

The common room opens onto the **corkboard** by the door, where the day's contracts are pinned. Behind the hearth is a **back room** with a single long table, tallow candles, and a hand-drawn survey map held to the wall with a mining pick — the room where commissions are briefed and debriefed away from the common crowd. [[Drunik Runevault]] runs Mining Consortium business from that table; the Questers took both the [[Greyhawk University/05. The Hamlet of Ritterstadt/Buildings & Infrastructure/The Fiend's Rest Public House/The Job Board/0001 - The Rust-Red Extraction]] briefing and its debrief there.

**Karet** keeps the house — pours, cooks, lets the rooms, and runs the board. She is observant, dry, and unflappable, and she coined the term *"Sharkenbearnado"* on first hearing the Questers' account of the aerial selachian swarm — a coinage the University has formally deprecated and entirely failed to suppress.

Pack-merchants on the Sepia route quarter here when in town (e.g. Mistress Vehlda Brett out of Verbobonc), making it the hamlet's informal trade post as well as its tavern.

**The Hush Tradition.** The Fiend's Rest maintains a standing tradition: *any patron who reports walking through the Hush on a recent journey is owed a free ale.* The offer is rarely redeemed. Of those who redeem it, several have refused to discuss what they felt inside. Ritterstadt locals consider the Hush bad luck and leave it at that.

> [!NOTE|ghost] GM Secret
> **Karet's Hush ledger — the buried treasure.** Karet keeps a small ledger of redeemed free-ale claims, noting *where* each patron reported walking through the Hush. Five years of dots on a hand-drawn map. The dots form **six clusters** — the stress points of the binding network. A party that befriends her (or buys enough rounds) can study it; a character who looks long enough sees the pattern. The same map a Boneheart operative would kill for is sitting in the publican's apron pocket. This is one of the most powerful and least obvious tools available in the campaign — pair it with [[Sigmund Holt]]'s working theory for the full picture.

# NPCs

`BUTTON[button_person]` The following people are associated with this place.

```base
properties:
  file.name:
    displayName: Person
  note.char_race:
    displayName: Race
  note.char_gender:
    displayName: Gender
  note.char_age:
    displayName: Age
views:
  - type: cards
    name: People - Cards
    filters:
      and:
        - file.folder == "Greyhawk University/05. The Hamlet of Ritterstadt/Town NPCs"
        - list(MyContainer).contains(this)
        - char_status.contains("Alive")
    order:
      - file.name
      - char_age
      - char_gender
      - char_race
    image: note.image
  - type: table
    name: People - Table
    filters:
      and:
        - file.folder == "Greyhawk University/05. The Hamlet of Ritterstadt/Town NPCs"
        - list(MyContainer).contains(this)
        - char_status.contains("Alive")
    order:
      - file.name
    sort:
      - property: file.name
        direction: ASC
    columnSize:
      file.name: 182
```

# GM Notes

- **The board as session ignition.** A job-board post going up is the moment a party officially "owns" an adventure. Rumour precedes the post; the post is the formal commission. See [[Jobs, Quests, and Inquiries]].
- **The back room.** Private briefings and debriefs happen here, behind the hearth, where Drunik keeps the pinned survey map. Use it whenever a commission needs to be handed over or reported out of common earshot.
- **Two houses, two crowds.** Ritterstadt has two drinking establishments and they are deliberately distinct. [[The Grey Wolf]] is the *old village inn* — quiet, domestic, locals-first, run by Lotte Kesselring, the place residents go for peace and a fair price. The **Fiend's Rest** is the *University-and-road house* — louder and transient, home to the Job Board, the commission back-room, and the through-traffic of Questers, scholars, and pack-merchants on University business. When a scene wants village gossip and settled domestic life, use the Grey Wolf; when it wants commissions, strangers, and rumour off the road, use the Fiend's Rest.

# Sub-Areas

- **[[Jobs, Quests, and Inquiries|The Job Board]]** — the corkboard where formal commissions are posted
- **[[The Heat Map|The Map Room]]** — the pinned-map back room used for briefings

## Adventure Use
- [[SP-PBS-01-The-False-Arrow]] — Scene 0 (Kartner reads Brennin's request from the Job Board)
- [[SP-PBS-03-The-Red-Cord]] — Hook 1 (Goldwaage's commission under the Warden's seal)

# Rumours

The Fiend's Rest is the default surface for Ritterstadt rumours — roll on or draw from the active [[Rumor Dashboard]] when the party lingers in the common room. On market days, the room fills and gossip runs hot.

# Image
![[Template_Place_Placeholder.png|500]]
