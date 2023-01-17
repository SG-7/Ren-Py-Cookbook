# This contains older code that can be repurposed or learned from.
# I will try to add to this when I discover cool or new bits of code.
# Much of this code was ripped directly from an old game project, thus the notes about release and endings.

# Other Images
image white = "#FFFFFF"
image black = "#000000"
# These are "images" that just fills the screen with one color.

# CTC (Click-to-Continue) Indicator
image ctc_blink:
    "ctc.png" # This will be the image that shows at the bottom-right of dialog.
    linear 0.6 alpha 1.0
    linear 0.6 alpha 0.0
    repeat
# Note: be sure to add the following to each "character" you want the ctc to show in.
# ctc="ctc_blink", ctc_position="nestled"

# Narrator & Other
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
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
    # Older splash screen made with images and dissolves. You'd probably opt for a video file now.
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

# Start of the game.
label start:
    scene black
    # jump quiz # Before final release, uncomment the code before this, then delete the following code until the next comment block.
    menu:
        "What do you want to do?"
        "Play Game?": # Takes you to quiz.
            jump quiz
        "Test Scripts": # Remove before release.
            jump test
    return
    # Delete the above code before final release.
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
    if q >= 2:
        jump humanq
    else:
        jump kaimuraq
    return

# Results
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

# All four endings jump to the code below.

# We would call this block near the beginning of the game.
label varibles:
    $ eu = 0
    return

# These would go  at the end of each route to mark one of the endings.
# One for each ending your novel has, if there are multiple endings.
label end_1:
    $ eu += 1
    "Just showing how this works."
    call credits
    "[eu]/4 - The first ending."
    return

label credits:
    # This code block can be "call"ed from the ending it relates to.
    # This is also an older block for making credits from images.
    #$ renpy.movie_cutscene('credits.ogv')
    scene black
    with Pause(1)
    show htsa with dissolve
    with Pause(1)
    show write with dissolve
    with Pause(1)
    show bgart with dissolve
    with Pause(1)
    show cart with dissolve
    with Pause(1)
    show prog with dissolve
    with Pause(1)
    show tests with dissolve
    with Pause(1)
    show renpy with dissolve
    with Pause(1)
    show thanks with dissolve
    with Pause(2)
    # This will return back to the ending to add how many endings have been unlocked and say which ending it is.
    return
