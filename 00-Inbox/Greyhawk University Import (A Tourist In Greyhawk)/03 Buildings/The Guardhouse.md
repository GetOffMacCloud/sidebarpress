---
publish: true
tags:
  - Category/Place
MyContainer: "[[02. World/Hubs/Ritterstadt.md|Ritterstadt]]"
MyCategory: Military
obsidianUIMode: preview
image: Template_Place_Placeholder.png
---

> [!NOTE] Parent Hub: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

> [!column|no-i no-t]
>> [!info|no-title] Image
>> ![[Template_Place_Placeholder.png]]
>
>> [!note|no-title] The Guardhouse
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

The Guardhouse is the garrison barracks of Ritterstadt — a long, narrow building of pine timber built flush against the eastern wall of the Ritter's Hall's palisade. It sleeps eight soldiers in two rows of rope-and-straw bunks, with a weapons rack at one end and a small hearth at the other. It smells permanently of boot leather, wet wool, and woodsmoke.

The garrison is commanded by **Captain Hildegard Stahlwulf**, who maintains a spartan personal billet at the far end of the building screened off by a heavy curtain. A duty roster is nailed to the door in Hildegard's precise hand, rotated weekly. Two soldiers are on watch at all times: one at the Wachturm, one patrolling the palisade circuit.

Beside the barracks, a small yard is used for morning drills. The soldiers are not elite troops — they are village-hardened men and women who can fight, track, and survive a northern uplands winter. They are not to be underestimated.

![[The Guardhouse — GM#GM Secret|no-h clean]]

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

![[The Guardhouse — GM#GM Notes|no-h clean]]

# Services

The Guardhouse is not open to civilians for services. The garrison operates under the Ritter's authority.

| Interaction | Condition |
|---|---|
| Report a threat or crime | Open to all villagers at any time; soldier on duty will log it and inform the Captain |
| Request armed escort | Requires Ritter's approval; see The Ritter's Hall |
| Speak with Captain Hildegard | She keeps a short "open door" window each morning after drills — first hour of the forenoon |

# Rumours

| d6 | Rumour |
|---|---|
| 1 | "Hildegard ran four extra drill sessions this week. She only does that when she expects trouble." |
| 2 | "Young Ewald keeps drawing maps. I saw him with a piece of charcoal and a board. When I asked what he was sketching, he said 'the hills.' Why would a soldier need to sketch the hills?" |
| 3 | "The Captain came back from a solo patrol two nights ago with a cut on her sword arm she hadn't left with. She hasn't said what happened." |
| 4 | "One of the soldiers told me they found tracks in the snow east of the palisade. Big ones. Not wolf. Not bear. They didn't say what." |
| 5 | "Hildegard refused a direct order from the Vogt last tenday. Just flat refused. First time I've ever seen anyone do that to him." |
| 6 | "The empty bunk in the barracks — they haven't taken down Pieter's things yet. Seven weeks now. The others won't touch them either." |

# Image
![[Template_Place_Placeholder.png|500]]
