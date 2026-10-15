---
publish: false # was true in A Tourist In Greyhawk vault; review before shipping
tags:
  - Category/Place
  - ritterstadt
  - farmstead
type: Location
status: Active
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Nesting
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`
> Part of [[The Farmsteads]] — one of eleven family longhouses in Ritterstadt's residential cluster.

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] The Beckenhaus Farmstead
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

One of the eleven longhouses in Ritterstadt's farmstead cluster, roughly central in the residential grouping, slightly east of The Big Barn. From the outside it is unremarkable: dark timber, thatch roof, a small attached byre, a kitchen garden that has been more productive in other years. The Beckenhaus family has lived here for two years, moved up from Edgerton after three bad harvests.

### The Family

| Name | Role | Age | Notes |
| :--- | :--- | :---: | :--- |
| **Gottfried Beckenhaus** | Father / Patriarch | ~60 | Quiet, methodical, slower than he used to be. Works the field daily without complaint. |
| **Ilse Beckenhaus** | Mother | ~57 | The center of gravity in this household. Knows more than she says. Covers for Kurt without explanation. |
| **Kurt Beckenhaus** | Eldest son | ~28 | The one going to the forest on moonless nights. See [[Kurt Beckenhaus]]. |
| **Marta-elder Beckenhaus** | Kurt's wife | ~25 | Named the same as the daughter for reasons that seemed sensible at the time. Exhausted. Scared. Trying to hold normal together. |
| **Marta Beckenhaus** | Kurt's daughter | 6 | Sick since midsummer. Wasting illness — weight loss, pallor, poor sleep, recurring fever. |
| **Pieter Beckenhaus** | Kurt's son | 7 | Healthy and oblivious in the way of seven-year-old boys. Currently the family's only uncomplicated thing. |

### The Longhouse

The Beckenhaus longhouse follows standard Ritterstadt construction: a single large main room with a central hearth, sleeping lofts accessed by a ladder, a back room used for storage and food preparation, and a byre attached to the east wall where two goats and a small number of chickens live through winter. The byre can be accessed from outside through a low door, which is how Kurt leaves on moonless nights without waking anyone — except Ilse, who hears it and does not move.

**Notable features inside:**
- A small carved wooden figure on the mantle — Pelor's sun-disc, crudely made. Standard.
- A second figure, tucked behind the first, barely visible: a smooth river-stone with a line scored around its equator. Not Perrenlander. Not Oeridian. Flan — a *wundstein*, a found-object ward stone. Ilse's, from her mother.
- Little Marta's pallet near the hearth, separated from the family sleeping loft so she doesn't disturb them when she's restless. She's always restless.
- A bark-parchment under the hearthstone that Kurt thinks no one knows about. It has words on it — the words he says at the tree. They are not correct words, ritually speaking, but they are words said with genuine intent, which is a different kind of correct.

![[The Beckenhaus Farmstead — GM#GM Secret|no-h clean]]

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

![[The Beckenhaus Farmstead — GM#GM Notes|no-h clean]]

# Rumours

| d4 | Rumour |
|---|---|
| 1 | "The Beckenhaus girl has been sick since Reaping and nothing's helped. Sad business. I've heard her coughing through the wall on cold nights." |
| 2 | "Kurt Beckenhaus is out sometimes at night — late, past the second bell. I've seen him crossing toward the tree-line. His wife says he can't sleep. Maybe so." |
| 3 | "Ilse Beckenhaus makes me uncomfortable and I couldn't tell you why. She's perfectly pleasant. She just looks at you like she knows what you're going to do before you do it." |
| 4 | "They came from Edgerton two years back. Three bad harvests, same as half the eastern villages. Good workers, quiet family. It's a shame about the little one." |

# Image
![[Template_Place_Placeholder.png|500]]
