init python:
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, 0.1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

    def play_sweat(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000000.wav", channel="sound")
    def play_notice(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000001.wav", channel="sound")
    def play_note(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000002.wav", channel="sound")
    def play_angry(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000003.wav", channel="sound")
    def play_exclaimation(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000004.wav", channel="sound")
    def play_question(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000005.wav", channel="sound")
    def play_bad(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000006.wav", channel="sound")
    def play_sleep(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000007.wav", channel="sound")
    def play_inspiration(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000008.wav", channel="sound")
    def play_heart(trans, st, at):
        renpy.play("audio/sound/emotion/in_emotion_000009.wav", channel="sound")

define character_base = Character(ctc="ctc_arrow", ctc_position="fixed")

image base:
    "#000000"

image ctc_arrow:
    xpos 0.89
    ypos 0.835
    xanchor 0
    yanchor 0
    "gui/ctc/next.png"
    linear 0.5 ypos 0.838
    repeat

transform default_pt:
    xalign 0.5
    yalign 0
    zoom 1.1
    alpha 0
    linear 0.3 alpha 1

transform default_bg:
    xalign 0.5
    yalign 0

transform default_emo_l:
    xalign 0.225
    yalign 0.175

transform shake:
    xalign 0.5
    linear 0.15 xalign 0.6
    linear 0.3 xalign 0.4
    linear 0.15 xalign 0.5

image balloon left:
    "emotion/bubble_l.png"
    parallel:
        linear 0.033 zoom 0.543
        linear 0.033 zoom 0.791
        linear 0.033 zoom 0.94
        linear 0.033 zoom 1.023
        linear 0.033 zoom 1.023
        linear 0.033 zoom 1.043
        linear 0.033 zoom 1.018
        linear 0.033 zoom 0.988
        linear 0.033 zoom 0.988
        linear 0.033 zoom 0.983
        linear 0.033 zoom 0.995
        linear 0.033 zoom 1


image sweat:
    function play_sweat
    "emotion/sweat.png"

image notice_1:
    function play_notice
    "emotion/notice_1.png"

image notice_2:
    "emotion/notice_2.png"

image notice_3:
    "emotion/notice_3.png"

image note:
    "emotion/note.png"
    parallel:
        linear 0.033 zoom 1.008
        linear 0.033 zoom 1.38
        linear 0.033 zoom 1.603
        linear 0.033 zoom 1.726
        linear 0.033 zoom 1.726
        linear 0.033 zoom 1.751
        linear 0.033 zoom 1.702
        linear 0.033 zoom 1.613
        linear 0.033 zoom 1.468
        linear 0.033 zoom 1.235
        linear 0.033 zoom 0.762
        linear 0.1 zoom 0.762
        linear 0.033 zoom 1

    parallel:
        linear 0.033 xoffset 7
        linear 0.033 xoffset -35
        linear 0.033 xoffset -60
        linear 0.033 xoffset -74
        linear 0.033 xoffset -74
        linear 0.033 xoffset -77
        linear 0.033 xoffset -73
        linear 0.033 xoffset -64
        linear 0.033 xoffset -50
        linear 0.033 xoffset -28
        linear 0.033 xoffset 17
        linear 0.1 xoffset 19
        linear 0.033 xoffset 6

    parallel:
        linear 0.033 yoffset 0
        linear 0.033 yoffset -37
        linear 0.033 yoffset -59
        linear 0.033 yoffset -72
        linear 0.033 yoffset -72
        linear 0.033 yoffset -74
        linear 0.033 yoffset -70
        linear 0.033 yoffset -64
        linear 0.033 yoffset -52
        linear 0.033 yoffset -34
        linear 0.033 yoffset 2
        linear 0.1 yoffset 2
        linear 0.033 yoffset -7

    function play_note

    block:
        linear 0.033 rotate 12.543
        linear 0.033 rotate 4.769
        linear 0.033 rotate 1.643
        linear 0.033 rotate -14.166
        linear 0.033 rotate -17.565
        linear 0.033 rotate 2.22
        linear 0.033 rotate 7.744
        linear 0.033 rotate 9.831
        linear 0.033 rotate 0
        linear 0 rotate 3.469
        linear 0.033 rotate -3.675
        linear 0.033 rotate -3.501
        linear 0.033 rotate 0
        linear 0 rotate -3.312
        linear 0.867 rotate 0
        linear 0 rotate 18.955
        linear 0.033 rotate -14.166
        linear 0.033 rotate -17.565
        linear 0.033 rotate 2.22
        linear 0.033 rotate 7.744
        linear 0.033 rotate 9.831
        linear 0.033 rotate 0
        linear 0 rotate 3.469
        linear 0.033 rotate -3.675
        linear 0.033 rotate -3.501
        linear 0.033 rotate 0
        linear 0 rotate -3.312
        linear 0.533 rotate 0
        0.5
        repeat


image angry:
    function play_angry
    "emotion/angry.png"

image exclaimation:
    function play_exclaimation
    "emotion/exclaimation.png"

image question:
    function play_question
    "emotion/question.png"

image bad:
    function play_bad
    "emotion/bad.png"

image sleep:
    function play_sleep
    "emotion/sleep.png"

image inspiration:
    function play_inspiration
    "emotion/inspiration.png"

image heart:
    function play_heart
    "emotion/heart.png"