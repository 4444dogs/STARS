##Importng Libraries
import pgzrun
import pygame

# Code Below Here

#Setting Up the Window
WIDTH = 800
HEIGHT = 600
TITLE = "STARS by Bobby Joe"


# Characters

    # Rocket Ship
rocketship = Actor("rocketship") # Rocket Ship Texture is a Placeholder
rocketship.pos = 100, 100
    # Mars
mars = Actor("mars")
mars.pos = 500, 500
    # Mars (Realistic)
mars_real = Actor("mars_real")
mars_real.pos = 600, 400
    # Earth
earth = Actor("earth")
earth.pos = 100, 500
    

left = False

def draw():
  global traveled_to_mars
  global left
  def normal():
      screen.fill("black")
      rocketship.draw()
      mars.draw()
  normal()
  traveled_to_mars = rocketship.colliderect(mars)
  def at_mars():
    global left
    screen.clear()
    screen.draw.text("Mars", topleft=(10, 10), fontsize = 60)
    screen.draw.text("Mars is named after the roman god of war.", topleft=(10, 80), fontsize = 24)
    screen.draw.text("The Average Temperature of Mars is -81°F or -63°C", topleft=(10, 120), fontsize = 24)
    mars_real.draw()
    earth.draw()
    if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 100, 100
  if traveled_to_mars:
      at_mars()

      
      
  
# Backround Music
music.play('bgmusic')
music.set_volume(0.5)

# Movement
def update():
  if keyboard.left:
    rocketship.x = rocketship.x - 2
  elif keyboard.right:
    rocketship.x = rocketship.x + 2
  elif keyboard.up:
        rocketship.y = rocketship.y - 2
  elif keyboard.down:
    rocketship.y = rocketship.y + 2

    
def on_mouse_down():
    global left
    left = False
    if earth.collidepoint(earth.pos):
      left = True

# Code Above Here

##Running the Program
pgzrun.go()





