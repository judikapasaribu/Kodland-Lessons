#The following codes can only run in Kodland platform.
#If you want to run it in your local computer, some settings must be adjusted.

#pgzero

WIDTH = 600 # Lebar window
HEIGHT = 300 # Tinggi window
TITLE = "Judul Game" # Judul untuk window game
FPS = 30 # Jumlah frame per detik

#buat karakter disini
alien = Actor('alien', (50, 240))
background = Actor("background")

def draw():
  background.draw()
  alien.draw()
