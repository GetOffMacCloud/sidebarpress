---
publish: false # was true in A Tourist In Greyhawk vault; review before shipping
tags:
  - Category/Place
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Government
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] The Ritter's Hall
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
> option(1, 🛠️Services),
> option(2, 🤐Rumours),
> class(tabbed)
> )]
> ~~~
> >[!tabbed-box]
> > >[!div-m|no-title]
> > > ![[#Services|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Rumours|no-h clean]]

---

# General

Select Settlement: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

Select Category: `INPUT[inlineSelect(option(Commerce), option(Agriculture), option(Military), option(Philosophy), option(Industrial), option(Nesting), option(Government)):MyCategory]`

The Ritter's Hall is the seat of power in Ritterstadt — a long, low hall of dark timber and river stone, surrounded by a stout timber palisade that doubles as the town's inner defensive wall. The hall is old, its blackened roof-beams hung with antlers and the smoke-darkened banners of a dozen forgotten campaigns. A great hearth dominates the center of the main hall; it has not gone cold in living memory. The Ritter's chair — more throne than seat — sits on a low dais at the far end, flanked by two iron braziers.

The complex includes the Ritter's private quarters, a small armory, a grain store, a stable for the lord's horses, and the quarters of the Vogt. The Guardhouse barracks are built hard against the palisade wall to the east.

The palisade is the sturdiest structure in Ritterstadt — sharpened pine stakes, reinforced with iron brackets forged by the village smithy, with a fighting platform along the interior and a single iron-banded gate facing the village square.

![[The Ritter's Hall — GM#GM Secret|no-h clean]]

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

![[The Ritter's Hall — GM#GM Notes|no-h clean]]

# Services

| Service | Cost / Condition | Notes |
|---|---|---|
| Audience with the Ritter | Free (scheduled) | Held every tenday at midday; urgent matters may be heard sooner |
| Official Village Seal on documents | 5 sp | The Vogt applies the seal; requires Ritter's verbal approval |
| Access to village emergency stores | Ritter's authorization only | Not sold — dispensed in dire need |
| Hire of a village soldier (escort) | 1 gp/day | Requires Ritter's approval; 2 soldiers maximum |
| Right of shelter in the palisade | Civic duty / No cost | Opens during attacks, extreme weather, or Ritter's declaration |

## Adventure Use
- [[SP-PBS-03-The-Red-Cord]] — Scene 1 (the Hundred's letter; the "torn" half-banner among Gerhard's standards, which is cut clean and is the climax key)

# Rumours

| d6 | Rumour |
|---|---|
| 1 | "The Ritter's been locked in the hall with the Vogt three nights running. Someone from the south came through last month. I don't know what they said, but Konrad's been grey in the face ever since." |
| 2 | "His wolfhounds howled all night last Godsday. They don't do that unless something's wrong. They're war-dogs, those two — they know things." |
| 3 | "I heard the Vogt arguing with Konrad about timber rights. The old-growth pines to the north. Why would anyone sell those? There's nothing worth that much coin." |
| 4 | "The Ritter's been in a foul temper since the last caravan from Ungra Balan was late. He's waiting for something. Or someone." |
| 5 | "Old Sigmund refused to bless the hall again this Highsun. Said the smoke didn't rise right. The Ritter was furious." |
| 6 | "There's a room at the back of the hall that's always locked. They say it was the old Ritter's study. Nobody goes in. Konrad included." |

# Image
![[Template_Place_Placeholder.png|500]]
