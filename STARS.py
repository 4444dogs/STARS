##Importng Libraries
import pgzrun
import pygame

# Code Below Here

#Setting Up the Window
WIDTH = 1300
HEIGHT = 700
TITLE = "STARS"


# Characters

# Rocket Ship
rocketship = Actor("rocketship")
rocketship.pos = 1200, 600
 # Mars
mars = Actor("mars")
mars.pos = 700, 300
# Mars (Realistic)
mars_real = Actor("mars_real")
mars_real.pos = 1000, 500
# Earth
earth = Actor("earth")
earth.pos = 100, 500
# Saturn
saturn = Actor("saturn")
saturn.pos = 400, 300
# Saturn (Realistic)
saturn_real = Actor("saturn_real")
saturn_real.pos = 1000, 500
# The Sun
sun = Actor("sun")
sun.pos = 1100, 300
# The Sun (Realisistic)
sun_real = Actor("sun_real")
sun_real.pos = 1000, 500
# Janssen
janssen = Actor("janssen")
janssen.pos = 80, 80
# Janssen (Realistic)
janssen_real = Actor("janssen_real")
janssen_real.pos = 1000, 500
#TRAPPIST-1 e
t1e = Actor("t1e")
t1e.pos = 80, 200
#TRAPPIST-1 e (Realistic)
t1e_real = Actor("t1e_real")
t1e_real.pos = 1000, 500
#Proxima Centauri b
pcb = Actor("pcb")
pcb.pos = 80, 320
#Proxima Centauri b (Realistic)
pcb_real = Actor("pcb_real")
pcb_real.pos = 1000, 500
#KELT-9 b
k9b = Actor("k9b")
k9b.pos = 80, 440
#KELT-9 b (Realistic)
k9b_real = Actor("k9b_real")
k9b_real.pos = 1000,500


left = False

def draw():
  global traveled_to_mars
  global left
  def normal():
      screen.fill("black")
      rocketship.draw()
      mars.draw()
      saturn.draw()
      sun.draw()
      janssen.draw()
      t1e.draw()
      pcb.draw()
      k9b.draw()
  normal()
  #Mars Code
  traveled_to_mars = rocketship.colliderect(mars)
  def at_mars():
    global left
    screen.clear()
    screen.draw.text("Mars", topleft=(10, 10), fontsize = 60)
    screen.draw.text("Mars is named after the roman god of war.", topleft=(10, 80), fontsize = 24)
    screen.draw.text("The Average Temperature of Mars is -81°F or -63°C", topleft=(10, 120), fontsize = 24)
    screen.draw.text("The paremater of Mars is around 2,106.1 miles.", topleft=(10, 160), fontsize = 24)
    screen.draw.text("Mars travels around the sun at 14.5 miles per second!", topleft=(10, 200), fontsize = 24)
    screen.draw.text("Mars is the 4th planet from the sun!", topleft=(10, 240), fontsize = 24)
    screen.draw.text("Mars actually has weather!", topleft=(10, 280), fontsize = 24)
    screen.draw.text("Mars formed when gravity pulled swirling gas and dust into a ball!", topleft=(10, 320), fontsize = 24)
    screen.draw.text("Mars only has two Moons!", topleft=(10, 360), fontsize = 24)
    mars_real.draw()
    earth.draw()
    if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 1200, 600
  if traveled_to_mars:
      at_mars()
  #Saturn Code
  traveled_to_saturn = rocketship.colliderect(saturn)
  def at_saturn():
      global left
      screen.clear()
      screen.draw.text("Saturn", topleft=(10, 10), fontsize = 60)
      screen.draw.text("A year on Saturn is 10,759 Earth days!", topleft=(10, 80), fontsize = 24)
      screen.draw.text("Saturn is the sixth planet from the sun.", topleft=(10, 120), fontsize = 24)
      screen.draw.text("Saturn's nickname is the ringed planet!", topleft=(10, 160), fontsize = 24)
      screen.draw.text("Saturn is 886 million miles away from the sun!", topleft=(10, 200), fontsize = 24)
      screen.draw.text("A day on saturn is only 10.7 hours!", topleft=(10, 240), fontsize = 24)
      screen.draw.text("Saturn has 53 known moons and 29 unknown moons!", topleft=(10, 280), fontsize = 24)
      saturn_real.draw()
      earth.draw()
      if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 1200, 600
  if traveled_to_saturn:
      at_saturn()
  #Sun Code
  traveled_to_sun = rocketship.colliderect(sun)
  def at_sun():
    global left
    screen.clear()
    screen.draw.text("The Sun", topleft=(10, 10), fontsize = 60)
    screen.draw.text("The Sun is a star!", topleft=(10, 80), fontsize = 24)
    screen.draw.text("The Sun is at the center of our galaxy.", topleft=(10, 120), fontsize = 24)
    screen.draw.text("Over one million earths could fit in side the sun!", topleft=(10, 160), fontsize = 24)
    screen.draw.text("The sun is almost a perfect sphere", topleft=(10, 200), fontsize = 24)
    screen.draw.text("The sun is all colors mixed together but to us it appears white.", topleft=(10, 240), fontsize = 24)
    screen.draw.text("The sun is the closest star to our planet.", topleft=(10, 280), fontsize = 24)
    screen.draw.text("The surface of the sun is 27 million°F!", topleft=(10, 320), fontsize = 24)
    earth.draw()
    sun_real.draw()
    if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 1200, 600
    
    
  if traveled_to_sun:
    at_sun()

  # Janssen Code
  traveled_to_janssen = rocketship.colliderect(janssen)
  def at_janssen():
    global left
    screen.clear()
    screen.draw.text("Janssen (55 Cancri e)", topleft=(10, 10), fontsize = 60)
    screen.draw.text("A year on Janssen is 0.7 days!", topleft=(10, 80), fontsize = 24)
    screen.draw.text("Janssen orbits the sun Copernicus, which is simular to our sun!", topleft=(10, 120), fontsize = 24)
    screen.draw.text("Janssen might be made out of diamonds!", topleft=(10, 160), fontsize = 24)
    screen.draw.text("There might be possible volcano activity on Janssen.", topleft=(10, 200), fontsize = 24)
    earth.draw()
    janssen_real.draw()
    if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 1200, 600
    
  if traveled_to_janssen:
    at_janssen()

  # TRAPPIST-1 e
  traveled_to_t1e = rocketship.colliderect(t1e)
  def at_t1e():
    global left
    screen.clear()
    screen.draw.text("TRAPPIST-1 e", topleft=(10, 10), fontsize = 60)
    screen.draw.text("TRAPPIST-1 e is able to be habitable by humans!", topleft=(10, 80), fontsize = 24)
    screen.draw.text("A year on TRAPPIST-1 e is 6.1 days!", topleft=(10, 120), fontsize = 24)
    screen.draw.text("It would take humans 716,000 years to reach TRAPPIST-1 e!", topleft=(10, 160), fontsize = 24)
    screen.draw.text("Liquid water could be on TRAPPIST-1 e!", topleft=(10, 200), fontsize = 24)
    screen.draw.text("TRAPPIST-1 e's max temperature is 6 degrees!", topleft=(10, 240), fontsize = 24)
    earth.draw()
    t1e_real.draw()
    if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 1200, 600

  if traveled_to_t1e:
    at_t1e()
  
  # Proxima Centauri b
  traveled_to_pcb = rocketship.colliderect(pcb)
  def at_pcb():
    screen.clear()
    global left
    screen.draw.text("Proxima Centauri b", topleft=(10, 10), fontsize = 60)
    screen.draw.text("Proxima Centauri b could be habitable by humans!", topleft=(10, 80), fontsize = 24)
    screen.draw.text("Proxima Centauri b is in the solar system, Proxima Centauri, which is the closest to ours yet it would still take thousands of years to reach!", topleft=(10, 120), fontsize = 24)
    screen.draw.text("Proxima Centauri b is likely to have liquid water!", topleft=(10, 160), fontsize = 24)
    screen.draw.text("In a car, it would take 47 million years to reach Proxima Centauri B!", topleft=(10, 200), fontsize = 24)
    earth.draw()
    pcb_real.draw()
    if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 1200, 600
  if traveled_to_pcb:
      at_pcb()
  
  #KELT-9 b Code
  traveled_to_k9b = rocketship.colliderect(k9b)
  def at_k9b():
    screen.clear()
    global left
    screen.draw.text("KELT-9 b", topleft=(10, 10), fontsize = 60)
    screen.draw.text("KELT- b is the worlds hottest planet averaging around 7,800 degrees farenheight!", topleft=(10, 80), fontsize = 24)
    screen.draw.text("KELT-9 b is about 2.8 times larger than Jupiter!", topleft=(10, 120), fontsize = 24)
    screen.draw.text("A year on KELT-9 b is 1.5 days!", topleft=(10, 160), fontsize = 24)
    earth.draw()
    k9b_real.draw()
    if left == True:
        left = False
        screen.clear()
        normal()
        rocketship.pos = 1200, 600
  if traveled_to_k9b:
    at_k9b()

        


      
      
  
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

