# The script ofleur the game goes in this file.

# Declare characters used by this game
define fleur = Character("Fleur", kind=character_base, callback=speaker("fleur"))

# The game starts here.
label start:

    # Plays the music file in the audio folder
    play music "audio/music/bgm_utopia.wav"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bg halidom courtyard day at default_bg

    # This shows a character sprite.
    # show []
    show fleur normal at default_pt

    # These display lines dialogue.
    fleur "There has been some progress."
    fleur "The menu looks slightly more Dragalia now."

    show balloon left at default_emo_l
    show note at default_emo_l

    fleur "It even makes sound effects."

    hide balloon
    hide note

    fleur "Somehow the history screen also hides the textbox."

    show fleur normal at shake

    fleur "No idea how to make it not do that..."
    fleur "I still have no idea how to make this user friendly though."
    fleur "There's just inherently going to be some coding involved."
    fleur "I think I'll clean this up a bit tomorrow and dump it onto Github."
    fleur "There must be someone much more experienced in Ren'Py right."
    fleur "In unrelated news I need an OC so I can stop talking through Fleur."

    # This ends the game.

    return
