
label Ryann_Lorem_LoremBrick:

if HasBrick == True:
     Lo think "Wait, why do you have a brick?"
     menu:
         "I was going to smash the window.":
              c "I was gonna smash this window with it."
              Lo relieved "Seriously?"
              c "No, I was joking."
              Lo normal "Oh, good. I thought you weren't for a second there."
              Lo "Anyway lets keep looking."
              m "I dropped the brick on the ground and went to help Lorem search."
              $ HasBrick = False

         "Its a gift for you.":
              Lo think "You got me a... brick?"
              Lo "Does this have some kind of meaning for humans?"
              menu:
                   "Yes.":
                        c "Yes, it does."
                        Lo "Oh, um... Thank you then."
                        $ HasBrick = False
                        $ LoremHasBrick = True

                   "No.":
                        c "No not really."
                        Lo "Uhm... Ok then..."
                        c "(Why did I even take this in the first place?)"
                        $ HasBrick = False

         "I dont know.":
              c "I dont really know, I just saw it so I picked it up."
              Lo "That's..."
              Lo "Well, im pretty sure you wont need it so you can just get rid of it."
              c "Alright."
              $ HasBrick = False

     $ lorem3windows = True
     jump lorem3searchmenu

else:
    pass
