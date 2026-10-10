---
publish: true
tags:
  - Category/Place
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Philosophy
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] St. Erika's Chapel
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

St. Erika's Chapel is a small stone chapel — the second stone structure in Ritterstadt, built two generations ago by the current Ritter's grandfather as an act of piety after surviving a catastrophic blizzard. It is dedicated to **Saint Erika of the Long Night**, a localized aspect of Pholtus venerated specifically on the northern uplands frontier as the guardian of travelers in darkness and the patroness of those who endure winter.

The chapel is plain and severe inside: four rows of rough-hewn pews, an altar of pale limestone, and a single stained-glass window above the altar depicting a woman in white robes holding a lantern aloft against a black sky. The lamp in the depiction is always shown as the only light in the darkness — a common motif in frontier Pholtine iconography. Candles burn on the altar at all hours; it is the duty of the village to keep them lit.

**Vater Sigmund Wolfherz** has served here for over thirty years. He is the keeper of the village's birth, death, and marriage records — the only complete institutional memory Ritterstadt has.

![[St. Erika's Chapel — GM#GM Secret|no-h clean]]

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

![[St. Erika's Chapel — GM#GM Notes|no-h clean]]

# Services

| Service | Cost | Notes |
|---|---|---|
| Healing (herbalist care) | Free (donation welcome) | Healer's kit equivalent; Sigmund sees to all villagers |
| Last rites / burial preparation | Free | Village duty; no cost to families |
| Marriage ceremony | 1 gp (waived for poor) | Sigmund records the union in the ledger |
| Birth registration | Free | Required by the Ritter's charter within 30 days of birth |
| Consultation (advice, counsel) | Free | Sigmund is a listener; come with problems |
| Access to village records | Sigmund's discretion | He will share public records; some pages are sealed |
| Prayer and sanctuary | Free | The chapel is open at all hours; no one is turned away |

# Rumours

| d6 | Rumour |
|---|---|
| 1 | "Sigmund has a locked box in the sacristy. I've never seen him open it. He keeps it under the floorboards behind the altar." |
| 2 | "He refused to give last rites to old Brenner when he died. Just refused. Said some men don't go where the candle leads. He wouldn't say more." |
| 3 | "Sigmund was muttering to himself after evening prayers last Godsday. I didn't catch all of it. But I heard him say: 'Hassenrath was right.'" |
| 4 | "The candles on the altar went out all at once last winter. Every one. No wind. No draft. Just — out. Sigmund relit them and didn't say a word about it." |
| 5 | "His eyesight is almost gone now. But he still reads those old ledgers. I don't know how." |
| 6 | "There's a year in the records — about forty years back — where there are no entries at all. I asked him once what happened. He said: 'A hard winter.' He was lying." |

# Image
![[Template_Place_Placeholder.png|500]]
