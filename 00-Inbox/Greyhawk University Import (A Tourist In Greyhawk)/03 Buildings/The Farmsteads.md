---
publish: true
tags:
  - Category/Place
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Nesting
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] The Farmsteads
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
> option(1, 🤐Rumours),
> class(tabbed)
> )]
> ~~~
> >[!tabbed-box]
> > >[!div-m|no-title]
> > > ![[#Rumours|no-h clean]]

---

# General

Select Settlement: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

Select Category: `INPUT[inlineSelect(option(Commerce), option(Agriculture), option(Military), option(Philosophy), option(Industrial), option(Nesting), option(Government)):MyCategory]`

The Farmsteads represent the living quarters of Ritterstadt's common population: approximately eleven family longhouses of dark timber and thatch, arranged in a loose cluster between the Ritter's Hall and the Mill. Each longhouse typically houses one family (4–8 people) along with their animals in an attached byre. In deep winter, the shared warmth of livestock is not a luxury.

The farmsteads are not prosperous. The soil of the Sepia Uplands is thin and stony, and the growing season is short. The farming families of Ritterstadt subsist primarily on: rye bread, root vegetables (turnips, parsnips), salted and smoked meat from the autumn hunt and slaughter, dried fish from Lake Quag (traded up the road), wild forage, and whatever the forest provides. It is enough. Most years.

The communal stable and barn — a large, central building the villagers call **The Big Barn** — also serves as the village's emergency shelter, festival hall, and the location of the annual autumn slaughter, which is the year's most important communal event. When the bell on the Wachturm rings, villagers who cannot reach the palisade go to The Big Barn, whose walls are thick.

![[The Farmsteads — GM#GM Secret|no-h clean]]

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

![[The Farmsteads — GM#GM Notes|no-h clean]]

# Rumours

| d4 | Rumour |
|---|---|
| 1 | "Kurt Beckenhaus has been out at night again. His mother's been covering for him. Something about his daughter — she's been sick since midsummer and nothing helps her." |
| 2 | "The Renner family had their best milch cow die last month. No reason anyone could find. Three days later, the Brauer family lost a pig. People are starting to whisper about ill luck." |
| 3 | "We've been short on feed this winter. The hay didn't dry properly before the first frost — Gerold miscalculated. If we get a long winter, The Big Barn is going to be very crowded with hungry animals." |
| 4 | "There's talk of a family wanting to leave for the south come spring — the Voigts. They've had three hard years and the youngest boy nearly didn't make it through last winter. Can't blame them. Won't be the first." |

# Image
![[Template_Place_Placeholder.png|500]]
