image bg halidom courtyard day = Composite(
    # vvv Size of the resulting image, you shouldn't have to change this
    (1024, 1024),
    # vvv Replace all instances of 110319_01 to the appropriate character ID
    (0, 0), "background/halidom/courtyard/day/Sty_bg_0027_100_00.png",
    (0, 0), "bg halidom courtyard day cloud_1",
    (0, 0), "bg halidom courtyard day cloud_2",
    (0, 0), "bg halidom courtyard day cloud_3",
    (0, 0), "background/halidom/courtyard/day/Sty_bg_0027_100_04_front.png",
    (0, 0), "lighting daylight"
)

image bg halidom courtyard day cloud_1:
  "background/halidom/courtyard/day/Sty_bg_0027_100_01.png"
  xpan 180
  linear 780.0 xpan -180
  repeat

image bg halidom courtyard day cloud_2:
  "background/halidom/courtyard/day/Sty_bg_0027_100_02.png"
  xpan 180
  linear 390.0 xpan -180
  repeat

image bg halidom courtyard day cloud_3:
  "background/halidom/courtyard/day/Sty_bg_0027_100_03.png"
  xpan 180
  linear 180.0 xpan -180
  repeat

image lighting daylight:
  "background/lighting/tx_foil_Luminescence.png"
  additive 1
  alpha 0.25