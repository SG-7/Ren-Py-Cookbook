# This contains older code that can be repurposed or learned from.
# I will try to add to this when I discover cool or new bits of code.

# Other Images
image white = "#FFFFFF"
image black = "#000000"
# These are "images" that just fills the screen with one color.

# CTC (Click-to-Continue) Indicator
image ctc_blink:
    "ctc.png" # This will be the image that shows at the bottom-right of dialog.
    linear 0.6 alpha 1.0 # in .6 seconds, the alpha will become 100%
    linear 0.6 alpha 0.0 # in .6 seconds, the alpha will become 0%
    repeat
# ctc="ctc_blink", ctc_position="nestled" must be added in the definition of each character for the indicator to be added to their dialog box.

# Narrator & Other
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
## "narrator" is a special character reserved by Ren'Py that can be customized with a definition.
define question = Character("???", show_two_window=True, ctc="ctc_blink", ctc_position="nestled")
# Note: the "show_two_window=True" argument causes the name to be shown in a separate textbox positioned at left just above the regular textbox.

# Characters
define ac = Character("Alarm Clock", show_two_window=True, color="#ff0000", what_prefix='"', what_suffix='"', ctc="ctc_blink", ctc_position="nestled")
# The "what_prefix" and "what_suffix" set what is shown around the dialog this character says.

# Custom Transitions
## Remove any unused transitions before final release.
define moveinrightdissolve = ComposeTransition(dissolve, after=moveinright)
define moveinleftdissolve = ComposeTransition(dissolve, after=moveinleft)
define moveoutrightdissolve = ComposeTransition(dissolve, before=moveoutright)
define moveoutleftdissolve = ComposeTransition(dissolve, before=moveoutleft)
### Needs research to make sure the transitions I made don't already exist in an easier form.

# Pre-Menu popup (Splashscreen)
## Will be changed once logo and animation has been completed.
label splashscreen:
    #$ renpy.movie_cutscene('splash.ogv') # video file to be used instead of image with pauses.
    scene black
    with Pause(1)
    show text "{size=56}Ninja Haven Studios{/size}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show rating with dissolve
    with Pause(1)
    show demo with dissolve
    with Pause(2)
    return

# Debug Menu at the start.
label start:
    scene black
    menu:
        "What do you want to do?"
        "Play Game?":
            jump quiz # Takes you to quiz.
        "Test Scripts":
            jump test # Add this label to test a certain script.
    return
# This is a quiz to jump to a certain story point based on cumulative answers.
label quiz:
    $ q = 0 # This initializes the "q" variable and sets it's value to "0"
    menu:
        "Someone attacks you, what do you do?"
        "Attack": # Human
            $ q += 1
            jump quiz2
        "Defend": # Kaimuran
            jump quiz2
    return
label quiz2:
    menu:
        "Which would you choose?"
        "The lives of many over a few.": # kaimuran
            $ q += 1
            jump quiz3
        "The lives of a few over many.": # Human
            jump quiz3
    return
label quiz3:
    menu:
        "How do you work best?"
        "In a group.": # Human
            $ q += 1
            jump results
        "Alone": # Kaimuran
            jump results
    return
label results:
    if q >= 2: # scores the test and if your result is 2 or greater you go to the Earth story.
        jump humanq
    else: # otherwise you go the the Kaimura story.
        jump kaimuraq
    return

# Results
## Added as a way to not go in too blindly.
label humanq:
    menu:
        "Are you sure you want to play as Eve?"
        "Yes - Human Side":
            jump human
        "No":
            jump kaimuraq
    return
label kaimuraq:
    menu:
        "Are you sure you want to play as Aryana?"
        "Yes - Kaimuran Side":
            jump kaimura
        "No":
            jump humanq
    return

# Image based Ending Credits
## Pause times may need to be adjusted depending on the amout of people.
label credits:
    #$ renpy.movie_cutscene('credits.ogv')
    ## When using a video, you may only need the final pause statement.
    scene black
    with Pause(1) # 1 Second Pause
    show htsa with dissolve # Title Card
    with Pause(1)
    show write with dissolve # Writers Card
    with Pause(1)
    show bgart with dissolve # Background Artists Card
    with Pause(1)
    show cart with dissolve # Concept Artists Card
    with Pause(1)
    show prog with dissolve # Programmers Card
    with Pause(1)
    show tests with dissolve # Play-testers Card
    with Pause(1)
    show renpy with dissolve # Ren'Py Card
    with Pause(1)
    show thanks with dissolve # Special Thanks Card
    with Pause(2) # 2 Second Pause before returning to Title Screen
    return
