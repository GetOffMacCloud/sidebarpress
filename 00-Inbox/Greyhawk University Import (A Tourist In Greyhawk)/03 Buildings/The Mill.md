---
publish: true
tags:
  - Category/Place
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Agriculture
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] The Mill
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

The Mill sits at the southern edge of Ritterstadt where a cold, fast-running stream cuts down from the uplands through a limestone gully. The waterwheel is large and heavy, iron-fitted, turning year-round except for the deepest freeze of midwinter when the brook ices solid and the miller uses hand-grinding querns until the thaw.

**Old Hanz Korngut** has been the miller since before most living residents of Ritterstadt were born. He is 68, nearly toothless, with enormous hands and a back that bends like a wind-worked pine. He grinds the village's grain, dries and stores surplus, and knows more about the uplands — the old paths, the old names, the old dangers — than anyone else alive in Ritterstadt. He doesn't volunteer this information. If you ask him something, he will tell you a story. The story will eventually contain the answer.

The mill also serves as the unofficial storehouse for the village's grain surplus. Hanz keeps a meticulous log in chalk on the mill wall (covered by a wooden hatch) of every bushel in and out. It is not sophisticated accounting, but it has never been wrong.

![[The Mill — GM#GM Secret|no-h clean]]

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

![[The Mill — GM#GM Notes|no-h clean]]

# Services

| Service | Cost | Notes |
|---|---|---|
| Grain grinding (per bushel) | 5 cp | Standard village rate; Ritter's tithe taken automatically |
| Grain storage (per month, per bushel) | 2 cp | Surplus storage; Hanz logs it in |
| Flour (per 10 lb sack) | 3 sp | Ground from stored grain; available for purchase |
| Dried legumes (per lb) | 2 cp | From village garden surplus |
| Beeswax (per block) | 8 cp | Traded from a local beekeeper family |
| Knowledge of the uplands paths | Not for sale | But shareable over a good evening and a flask |

# Rumours

| d6 | Rumour |
|---|---|
| 1 | "Old Hanz knows where every path in the uplands goes. I asked him once about the path north of the treeline. He said: 'That one goes somewhere you don't want to.' And he wouldn't say more." |
| 2 | "The grain stores are running light for the season. I checked the log. Three months of just slightly too much being drawn. It's subtle. But it's there." |
| 3 | "He talks to himself at the millstone. Not prayer — something else. I caught a few words once. Old language. Not Common. Not Flan either, as far as I could tell." |
| 4 | "Hanz's cat killed something last fortnight that wasn't a rat. It left it on the doorstep. Hanz buried it before anyone got a good look, but I saw the paws. Six of them." |
| 5 | "He was a young man when the old Ritter held this village. He was here during the gap in the chapel records — the eleven years when nothing was written down. If you want to know what happened, he's the only one left who knows." |
| 6 | "He dreams badly in winter. The whole mill shakes sometimes, early in the morning, before he's fully awake. He says it's the waterwheel. The waterwheel is frozen." |

# Image
![[Template_Place_Placeholder.png|500]]
