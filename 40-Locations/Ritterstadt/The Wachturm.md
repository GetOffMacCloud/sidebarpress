---
publish: false # was true in A Tourist In Greyhawk vault; review before shipping
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
>> [!note|no-title] The Wachturm
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

The Wachturm is the oldest structure in Ritterstadt and the only one built entirely of stone. It rises at the northern edge of the village — a squat, square tower of grey limestone, perhaps four stories high, with arrow slits on three sides and a flat crenelated roof from which one can see across the Sepia Uplands for miles on a clear day. An iron bell hangs from a timber frame on the roof; its ring carries to every corner of Ritterstadt and can be heard at the outlying farms in still weather.

The tower predates the current village by at least a century. No one is entirely sure who built it. The stonework is different from anything in the region — tighter fitting, with strange geometric carvings worn smooth at the base of the walls. The locals say the Old People built it. They do not elaborate on who the Old People were.

The ground floor is used for storage. The upper floors are accessible by a worn stone stair. The duty soldier stationed here spends most of their watch wrapped in furs, staring north.

![[The Wachturm — GM#GM Secret|no-h clean]]

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

![[The Wachturm — GM#GM Notes|no-h clean]]

# Rumours

| d4 | Rumour |
|---|---|
| 1 | "I pulled watch in the tower last Starday. Around the third hour, I heard something under the floor. Like a very large thing breathing very slowly. I didn't look. I won't look." |
| 2 | "The carvings at the base of the tower glow sometimes. Just a little. Blue, like cold fire. Only in deep winter, only at the new moon." |
| 3 | "They say the tower was here before the town. Before the Sepia Uplands road. Before the empire. Who builds a watchtower with no road to watch?" |
| 4 | "Hildegard iron-barred the sub-floor trapdoor herself. Nobody asked her to. Nobody asked her why, either. We all just... didn't." |

# Image
![[Template_Place_Placeholder.png|500]]
