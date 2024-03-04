import pygame
from pygamevideo import Video

pygame.init()
window = pygame.display.set_mode((1280, 720))

# Load the video from the specified dir
video = Video("Gallowdance.mp4")

# Start the video
video.play()

# Main loop
while True:
  ...

  # Draw video to display surface
  # this function should be called every frame
  video.draw_to(window, (0, 0))

  # Update pygame display
  pygame.display.flip()