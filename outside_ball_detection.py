import SimpleCV as s
img=s.Image(r"http://i.imgur.com/8vrJAWN.png") # Replace with local copy for faster processing
img2=img.hueDistance(s.Color.YELLOW) # get hueDistance image
low=35 # Use step 7 to get these variables
high=50
i2_stretched=img2.stretch(low,high) # Keep only the ball in greyscale (not black or white) and convert rest to black or white
i2_diff=img-i2_stretched.stretch(high,high) # Subtract white part of the previous image from original image
i2_stretched_2= i2_stretched.invert().stretch(255-low,255-low)
i_new=(i2_diff-i2_stretched_2) # Subtract black part of i2_stretched image from original image
blob_ball=i_new.morphOpen().findBlobs()[-1:] # Find the largest blob
blob_ball.draw(width=3,color=s.Color.AQUAMARINE) # Draw blob with width 3
blob_ball.show() # Show detected blob