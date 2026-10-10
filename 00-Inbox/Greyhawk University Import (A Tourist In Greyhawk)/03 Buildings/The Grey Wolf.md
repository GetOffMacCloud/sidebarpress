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
>> [!note|no-title] The Grey Wolf
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
> option(1, 🍺Menu),
> option(2, 🛏️Rooms),
> option(3, 🛒Goods),
> option(4, 🤐Rumours),
> class(tabbed)
> )]
> ~~~
> >[!tabbed-box]
> > >[!div-m|no-title]
> > > ![[#Menu|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Rooms|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Goods|no-h clean]]
> >
> > > [!div-m|no-title]
> > > ![[#Rumours|no-h clean]]

---

# General

Select Settlement: `INPUT[suggester(optionQuery(#Category/Hub)):MyContainer]`

Select Category: `INPUT[inlineSelect(option(Commerce), option(Agriculture), option(Military), option(Philosophy), option(Industrial), option(Nesting), option(Government)):MyCategory]`

*The Grey Wolf* is Ritterstadt's old village inn — the settlement's social center long before the University arrived, and still the place where the hamlet's own people drink. It is the locals' house: where a villager has a quiet ale without it being anyone's business, where domestic news and grievances circulate, where the families that have farmed the uplands for a generation feel at home. It is a low, broad building of dark timber with a carved wolf's head above the door (one ear has been broken off since before anyone can remember), a common room with six scarred tables, a hearth large enough to roast a full elk, and two small private rooms upstairs for paying guests.

> [!info] The Grey Wolf vs. the Fiend's Rest
> Ritterstadt now has two houses, and they serve different crowds. The **Grey Wolf** is the *old village inn* — quiet, domestic, locals-first, run by Lotte. The newer **[[The Fiend's Rest Public House]]** is the *University-and-road house* — louder, transient, home to the Job Board, the commission back-room, and the adventurer/scholar/merchant trade. Villagers who want peace drink here; Questers and travellers on University business drink there.

**Lotte Kesselring** owns it, runs it, brews the ale, cooks the stew, changes the beds, and keeps the peace with a hand the size of a dinner plate and a voice that carries through walls. She is 34, a widow (her husband Tobias died of a fever five years ago), and she has not slowed down once. She is warm, blunt, funny, and observant. If something is happening in Ritterstadt, she knows about it within a day. If something is going to happen, she usually knows about it first.

The Grey Wolf is also where a villager — or a careful outsider — can buy basic provisions beyond bread and water — rope, candles, salt, preserved meat — because Lotte has quietly begun stocking these things, and the Ritter has tacitly allowed it since it brings coin to the village. (The Fiend's Rest caters more to the through-traffic of merchants and Questers; Lotte's stock is steadier and her prices kinder to locals.)

![[The Grey Wolf — GM#GM Secret|no-h clean]]

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

![[The Grey Wolf — GM#GM Notes|no-h clean]]

# Menu

| Item | Price | Notes |
|---|---|---|
| Ritterstadt Dark Ale | 3 cp | Brewed by Lotte; thick, slightly bitter, excellent |
| Birch-sap mead | 5 cp | Seasonal (spring); sweet and strange |
| Pine resin wine | 4 cp | Acquired taste; travelers usually decline a second |
| Elk stew | 4 cp | Always available; the elk varies with the season |
| Black bread | 1 cp | Dense, filling, goes with everything |
| Salted fish | 2 cp | Lake Quag provenance; dried and smoked |
| Traveller's Board | 8 cp | Stew, bread, fish, and a drink |
| Spirits (local grain spirit) | 2 sp | Potent; DC 13 Constitution or disadvantage on Wisdom checks for 1 hour |

# Rooms

| Room | Price/Night | Notes |
|---|---|---|
| Common room (floor pallet + blanket) | 3 cp | Cold floor; company guaranteed |
| Small room (upstairs, 1 bed) | 4 sp | Cramped but private; iron latch on door |
| Large room (upstairs, 1 bed + table) | 7 sp | Best room; overlooks the village square |
| Stable (horse + straw + lock) | 2 sp | Behind the inn; Lotte's boy tends the animals |

# Goods

Lotte stocks basic traveller supplies behind the bar, no sign posted.

| Item | Cost | Notes |
|---|---|---|
| Rope (hempen, 50 ft) | 1 gp | One or two in stock |
| Candles (10) | 1 sp | Always available |
| Tinderbox | 5 sp | Usually 1–2 in stock |
| Salt (1 lb) | 5 cp | Always available |
| Preserved meat (1 week rations) | 4 sp | Smoked elk or rabbit |
| Blanket (wool) | 5 sp | Heavy uplands weave; warm |
| Torches (5) | 1 sp | Always available |

# Rumours

Roll d8 or choose; each reflects a real hook or background detail.

| d8 | Rumour |
|---|---|
| 1 | "A man came through three tendays ago. Southerner by his accent. Didn't eat, didn't drink — just asked about the road north and whether anyone had been trading with the villages up past the snowline. I told him the road north goes nowhere. He didn't believe me." |
| 2 | "Young Ewald from the barracks was here last Starday, deep in his cups. He was talking in his sleep by the third hour. I only caught a few words. Names, mostly. Names I didn't recognize. Not from around here." |
| 3 | "The Vogt hasn't been in for two weeks. He always comes in on Godsday evening. Something's keeping him busy." |
| 4 | "Grauer growled at the Vogt last month. First time I've ever seen him growl at someone he knows. Ackermann didn't notice. But I did." |
| 5 | "There's a hunting party overdue from the northern pass. Three days late now. The Ritter hasn't sent anyone to look for them." |
| 6 | "Old Hanz had three ales last Freeday and started talking about the hill above the snowline. He called it by a name in an old language. When I asked him to repeat it he said he didn't know what I meant and went home." |
| 7 | "Bruni came in last night and sat by the fire for two hours without saying a word to anyone. She had grease on her hands but she'd clearly washed her face. She only does that when something's wrong at the smithy." |
| 8 | "Vater Sigmund was here yesterday, which he almost never is. He sat with Hanz for an hour, very quiet. When they left, I noticed Sigmund had left something on his chair. A folded piece of paper. I didn't read it. I burned it." |

# Image
![[Template_Place_Placeholder.png|500]]
