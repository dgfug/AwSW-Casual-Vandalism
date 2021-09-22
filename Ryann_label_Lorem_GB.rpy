
label Ryann_Lorem_GetBrick:
scene np2x at Pan ((0, 0), (0, 360), 8.0) with dissolveslow
play sound "fx/steps/clean2.wav"

m "While walking to the school area I noticed a loose brick on the ground along the path."
menu:
     "[[Take the brick.]":
                play sound "fx/rocks1.ogg"
                m "I picked up the brick off the ground and stashed it under my clothes."
                $ HasBrick = True

     "[[Leave the brick.]":
                "I decided to ignore it and continue walking."
                $ HasBrick = False

jump Ryann_Lorem_GB_end
