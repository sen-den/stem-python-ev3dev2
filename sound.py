from ev3dev2.sound import Sound
sound = Sound()

# Play a 200Hz tone for 2 seconds and then wait 0.4 seconds
# before playing the next tone, 800Hz for 1 second
# followed by a 3 second delay
sound.tone([
  (200, 2000, 400),
  (800, 1000, 3000)
])
