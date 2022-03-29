# Character file for Fleur
# A tutorial on how to put a character in the runner!

# Notes:
# Comments starts with the # symbol, when you are done with the character file
# you can safely remove unecessary comments

# For each emotion, we define three things
# - A composite image that will be shown
# - An eye part (used by composite)
# - A mouth part (used by composite)

# Composite image

# Stacking the base, eye part, and face part image together to create a
# composite image
image fleur normal = Composite(
    # (width, height): size of resulting sprite, should not change for other characters
    (1024, 1024),
    # (x position, y position), image:
    # This places the base image at the center of the composite
    (0, 0), "portrait_output/110319_01/110319_01_base.png",
    (447, 297), "fleur eyes normal",
    (447, 297), WhileSpeaking("fleur", "fleur mouth normal", "portrait_output/110319_01/110319_01_parts_c018.png")
)

image fleur eyes normal:
    "portrait_output/110319_01/110319_01_parts_c000.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "portrait_output/110319_01/110319_01_parts_c001.png"
    .25
    repeat

image fleur mouth normal:
    "portrait_output/110319_01/110319_01_parts_c018.png"
    .2
    "portrait_output/110319_01/110319_01_parts_c019.png"
    .2
    repeat