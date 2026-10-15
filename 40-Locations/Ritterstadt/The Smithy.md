---
publish: false # was true in A Tourist In Greyhawk vault; review before shipping
tags:
  - Category/Place
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Industrial
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] The Smithy
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
> option(1, 🛒Selling),
> option(2, 🛠️Services),
> option(3, 🤐Rumours),
> class(tabbed)
> )]
> ~~~
> >[!tabbed-box]
> > >[!div-m|no-title]
> > > ![[#Selling|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Services|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Rumours|no-h clean]]

---

# General

Select Settlement: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

Select Category: `INPUT[inlineSelect(option(Commerce), option(Agriculture), option(Military), option(Philosophy), option(Industrial), option(Nesting), option(Government)):MyCategory]`

The Smithy is the beating heart of Ritterstadt's survival — a low, broad building of stone and timber set near the center of the village, its forge chimney perpetually trailing grey smoke into the cold uplands sky. Anvil strikes echo here from before first light until after dark in the busy seasons, and the smell of hot iron and coal is woven into everything within fifty feet.

**Brunhilde "Bruni" Hammerschlag** has run the forge alone since her husband Dietrich died three winters ago — taken by a pack of winter wolves in the northern pass while he was checking his traplines. She inherited the tools, the clients, and the calluses. She learned the trade from Dietrich, and she is better at it than he was. She will not be told otherwise.

Bruni is the most practically essential person in Ritterstadt. Without her, the palisade fittings rot, the mill-wheel rusts, the soldiers' weapons dull and break, and the farmers lose their plowshares. She knows this. So does everyone else. It gives her a degree of informal authority that is extraordinary for a tradesperson in a village with a lord.

![[The Smithy — GM#GM Secret|no-h clean]]

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

![[The Smithy — GM#GM Notes|no-h clean]]

# Selling

Stock is limited. Bruni keeps only what she's made recently.

| Item | Cost | Availability |
|---|---|---|
| Dagger | 2 gp | Usually 1–2 in stock |
| Hand Axe | 5 gp | 1 in stock |
| Spearhead (unshafted) | 8 sp | 2–3 available |
| Horseshoes (set of 4) | 2 gp | Always in stock |
| Iron tools (hammer, tongs, saw blade) | 1–5 gp | Most in stock |
| Iron fittings, brackets, hinges | 5 sp per piece | Built to order |
| Iron rations-tin (watertight box) | 3 sp | Useful; always a few |
| Chain links (loose) | 1 sp per foot | Useful for improvised binding |

# Services

| Service | Cost | Time |
|---|---|---|
| Weapon repair (minor) | 5 sp | Same day |
| Weapon repair (major) | 2 gp | 2 days |
| Armor repair (minor) | 8 sp | 1 day |
| Armor repair (major) | 3–5 gp | 3–5 days |
| Custom weapon commission | PHB price +25% | 3–7 days |
| Tool repair | 2 sp | Same day |
| Horseshoeing (per horse) | 5 sp | Same day |
| Iron-shod boots (re-fitting) | 1 sp | Same day |

# Rumours

| d6 | Rumour |
|---|---|
| 1 | "Bruni doesn't sleep much. You can see the forge glow under her door well past midnight. I asked her once what she's working on. She said 'nothing.' But there's no ash to account for that much coal." |
| 2 | "Dietrich's tools are all still hanging in the smithy. She hasn't moved a single one. The village boys won't even touch them — she's made it very clear." |
| 3 | "She turned down a commission from the Vogt last tenday. An iron chest, he wanted. She told him she was too busy. I've never seen her too busy for paid work before." |
| 4 | "Something in her coal store smells wrong. Not coal-wrong. Something metallic and hot, even in winter. I mentioned it to her and she changed the subject so fast I nearly fell over." |
| 5 | "The wolves that killed Dietrich were tracked back to a cave above the snowline. The hunters found the cave — but they found something else in it, too. They won't say what. They came back quiet." |
| 6 | "I saw her crying in the smithy late at night last Godsday, just sitting on her anvil stool with her hands in her lap. When she saw me looking she went back to work like nothing happened. She didn't even wipe her face." |

# Image
![[Template_Place_Placeholder.png|500]]
