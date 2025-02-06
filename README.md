# This Repo isn't finished - Still not working properly!

# We made a "Avatar the last air bender" themed Risk (The game).

### The SVG files is made for the K40 Wissperrer for laser cutting our Risk map in 4 pieces of 500x400x3 mm wood.

### The Size of the board is 930x650 mm.

## Components

| Component                                                                                                                                                                                                                                                                                                                                                                                                                     | Usage                         | Count | 
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-------| 
| [Neopixel 12 LED](https://aliexpress.com/item/1005006167807434.html?spm=a2g0o.productlist.main.5.26f7CRBCCRBCeW&algo_pvid=32fcd5ab-5a81-4220-9f5e-dd8dc404c123&algo_exp_id=32fcd5ab-5a81-4220-9f5e-dd8dc404c123-2&pdp_npi=4%40dis%21ILS%214.10%213.58%21%21%218.25%217.20%21%402101246417388327523304021e5c11%2112000036083924276%21sea%21IL%210%21ABX&curPageLogUid=X2L4VXplmldc&utparam-url=scene%3Asearch%7Cquery_from%3A) | Visual player turn indicator  | 4     | 
| [16x2 I2C LCD](https://aliexpress.com/item/1005006771130640.html?spm=a2g0o.productlist.main.27.209d2c22RQtn2c&algo_pvid=2d060c8d-ef2a-4622-8d4e-46815d054447&algo_exp_id=2d060c8d-ef2a-4622-8d4e-46815d054447-13&pdp_npi=4%40dis%21ILS%213.63%213.63%21%21%217.31%217.31%21%402101062a17388329461538299e965c%2112000038243210778%21sea%21IL%210%21ABX&curPageLogUid=dzleC3lLw7KP&utparam-url=scene%3Asearch%7Cquery_from%3A)  | Textual player turn indicator | 2     |
| [esp32](https://aliexpress.com)                                                                                                                                                                                                                                                                                                                                                                                               | Micro-controller              | 1     |
| [random button](https://aliexpress.com/item/1005007129582055.html?spm=a2g0o.productlist.main.3.62403cfaFxeBkY&algo_pvid=31227d83-2566-4c72-b367-50813b60bc9c&algo_exp_id=31227d83-2566-4c72-b367-50813b60bc9c-1&pdp_npi=4%40dis%21ILS%214.27%214.27%21%21%211.18%211.18%21%40210141f717388335114606541e449d%2112000039500296151%21sea%21IL%210%21ABX&curPageLogUid=vX29gzUJMbA6&utparam-url=scene%3Asearch%7Cquery_from%3A)   | Changes player turn           | 4     |
| [Custom PCB](http://oshwalab.com)                                                                                                                                                                                                                                                                                                                                                                                             | Connect everything            | 1     |

## Pinout

| esp32 | Use        |
|-------|------------|
| 13    | button     |
| 18    | Neopixel 1 |
| 19    | Neopixel 2 |
| 5     | Neopixel 3 |
| 14    | Neopixel 4 |
| 16    | I2C SDA    |
| 17    | I2C SCL    |

## Special Thank to Gal Arbel, Dan Katzenellenbogen and Tomer Ozer.

1. [Tomer Ozer Github page](https://github.com/TomerOzer)
2. [Gal Arbel Github page](https://github.com/galarb)
3. [Dan Katzenellenbogen Github page](https://github.com/Dan-Katzenellenbogen)

