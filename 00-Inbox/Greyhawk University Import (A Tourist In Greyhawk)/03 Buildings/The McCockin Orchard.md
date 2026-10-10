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
>> [!note|no-title] The McCockin Orchard
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
> option(1, 🛒Goods),
> option(2, 🛠️Services),
> option(3, 🤐Rumours),
> class(tabbed)
> )]
> ~~~
> >[!tabbed-box]
> > >[!div-m|no-title]
> > > ![[#Goods|no-h clean]]
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

The McCockin Orchard spreads across several acres of south-facing slope on the outskirts of Ritterstadt — row after row of old, carefully tended apple trees that produce, by common consent and commercial fact, the best apples in the Sepia Uplands. The thin, stony soil that fights every farmer in the region somehow does not fight here. The trees are pruned to a discipline the garrison would envy, the drystone boundary walls are mortared and true, and the cider-house at the orchard's heart runs its great oak press from first frost until deep winter.

The orchard is the source of **McCockin Cider** — the hamlet's one genuinely valuable tradeable commodity. Casks of it travel the Sepia route with every pack-merchant willing to carry them and command serious prices as far away as Verbobonc and the City of Greyhawk. The cider has made the McCockins the wealthiest family in Ritterstadt, wealthier by a comfortable margin than the Ritter himself — a fact everyone in the village knows and no one says at volume.

The **McCockin estate house** stands above the cider-house on the highest ground of the property: two full storeys of dressed stone and seasoned timber, glazed windows, a slate roof brought up the trade road at staggering expense, and a long covered porch that looks down the rows toward the village. **Chuck McCockin** — Bethany's grandfather — built it with cider money and his own two hands on the frame, and it is, without rival, the finest building in the area — finer than the Ritter's Hall, a comparison the family is careful never to make aloud.

**Grant McCockin**, Bethany's father, runs the orchard and the cider trade. He is a philanthropist by conviction and the **largest financial supporter of the University's Ritterstadt Field Station** — endowment gifts, equipment funds, and quiet coverage of more than one student's tuition shortfall have all come out of the orchard's profits. He is generous, shrewd, and entirely unapologetic about being both at once. His wife, **Winifred Simmons**, manages the trade contracts and the ledgers; the hyphen in their daughter's name was her one non-negotiable condition of marriage.

The family made its money within living memory. It was **Chuck** who made it: a stubborn smallholder who planted the first rows himself, tree by tree, grafted and pruned and replanted through the bad years his neighbors still talk about, and lived long enough to press the cider that paid for the slate roof. Grant grew his father's orchard into a trade empire, but the village remembers Chuck with dirt on his knees — and so do the McCockins, which is why **[[Bethany McCockin-Simmons|Bethany]]** grew up hauling crates and working the press alongside the hired hands rather than watching from the porch. Her brewer's tools proficiency was learned in the cider-house; her folk-hero ease among common people was learned in these rows.

![[The McCockin Orchard — GM#GM Secret|no-h clean]]

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

![[The McCockin Orchard — GM#GM Notes|no-h clean]]

# Goods

Sold from the cider-house door; the serious volume moves by contract through Winifred.

| Item | Cost | Notes |
|---|---|---|
| McCockin Cider (common, by the mug) | 2 cp | Sold at the cider-house door in season; the Grey Wolf and Fiend's Rest both stock it |
| McCockin Cider (small cask, 5 gal) | 8 sp | The travelling standard; holds its quality on the road |
| McCockin Reserve (sealed cask, aged) | 6 gp | Wax-sealed, stamped with the apple-and-bee mark; a recognized trade good as far as Verbobonc |
| Fresh apples (per bushel, in season) | 3 cp | Seconds and windfalls; the best fruit goes to the press |
| Apple brandy (bottle, limited) | 2 gp | Winter distillation, small batches; Grant calls it "the accountant's share" |
| Cider vinegar (jug) | 4 cp | Kitchen staple; always available |

# Services

| Service | Cost / Condition | Notes |
|---|---|---|
| Harvest work (room, board + wage) | 3 sp/day | Late Patchwall through first frost; no questions asked of able hands |
| Cask contract (trade volume) | Negotiated with Winifred | Pack-merchants and consortium buyers only; she reads contracts like a battle map |
| Letter of introduction | Grant's discretion | To University faculty, City merchants, or Perrenland factors — not sold, *granted* |
| University sponsorship inquiries | By appointment | Grant hears funding proposals on the porch, Godsday afternoons |
| Hospitality (guest rooms) | Free to invited guests | The estate keeps two fine guest rooms; an invitation is a mark of standing in the hamlet |

# Rumours

| d6 | Rumour |
|---|---|
| 1 | "The McCockins' trees fruit heavy even in the years the rest of us lose half the crop to frost. Old Hanz says the orchard sits on kind ground. He says it like it means something more than it sounds." |
| 2 | "Grant paid for the new University equipment sheds outright — didn't blink. Money like that in a hamlet like this. And still he's out in the rows at dawn with sap on his hands." |
| 3 | "They say the Ritter's Hall went quiet when the slate for the McCockin roof came up the road. Konrad sent a letter of congratulations. Took him three weeks." |
| 4 | "Never touch the big ring of trees at the middle of the orchard. The pickers won't work them without a McCockin standing there. First pressing gets poured at those roots every year — 'for luck.' Old Chuck started that, and Chuck didn't plant those trees. They were already there." |
| 5 | "Winifred Simmons once voided a Consortium contract over a single altered word and made them cart the casks back up the hill. They signed her paper the following week. Nobody alters her paper now." |
| 6 | "The daughter's off adventuring for the University — the paladin girl. Wealthiest family in the uplands and she sleeps in a barracks bunk and buys her own ale at the Wolf. Grant tells anyone who asks that it's the best money he never had to spend." |

# Image
![[Template_Place_Placeholder.png|500]]
