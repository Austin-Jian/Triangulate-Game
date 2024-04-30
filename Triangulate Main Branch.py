import pygame, sys
from pygame.locals import QUIT
import random 
import math

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((800, 600))
# https://topsoj.com/mathgym/triangulate

# Define colour scheme and backgrounds
white = (255, 255, 255)
black = (0, 0, 0)
font_SansBold = pygame.font.SysFont("freesansbold", 90)
font_Sans = pygame.font.SysFont("freesans", 50)

menu_background = pygame.image.load("Triangulate_Menu_Background.png")
menu_background = pygame.transform.scale(menu_background, (800, 600))
menu_button = pygame.image.load("Triangulate_Menu_Button.png")
return_menu = pygame.image.load("Triangulate_Return_Button.png")
menu_graphic = pygame.image.load("Triangulate_Menu_Graphic.png")
menu_graphic = pygame.transform.scale(menu_graphic, (260, 260))

# Button class
class Button():
  # Defines button stuff
  def __init__(self, x, y, image, scale):
    height = image.get_height()
    width = image.get_width()

    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x,y)
    self.clicked = False

  def draw(self):
    # Assigns bool value to the button
    action = False

    # Menu mouse position
    menu_pos = pygame.mouse.get_pos()

    # Check if mouse is over or clicking the buttons
    if self.rect.collidepoint(menu_pos):
      # If button was clicked and it was not already clicked
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        action = True
    
    # Resets self.clicked so you can click button multiple times
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False

    # Draws button
    window.blit(self.image, (self.rect.x, self.rect.y))

    # Returns would return true in the game loop when clicked
    return action


# Centroid practice (medians intersect)
def centroid():

  # Coordinates of the triangle
  coordx1 = random.randint(90, 420)
  coordx2 = random.randint(90, 420)
  coordx3 = random.randint(90, 420)
  coordy1 = random.randint(200, 530)
  coordy2 = random.randint(200, 530)
  coordy3 = random.randint(200, 530)

  # Correct centroid
  # Midpoint of 2 sides
  midpointx23 = (coordx2 + coordx3)/2
  midpointy23 = (coordy2 + coordy3)/2
  midpointx12 = (coordx1 + coordx2)/2
  midpointy12 = (coordy1 + coordy2)/2
  
  # Equation of 2 lines
  slope1 = (midpointy23 - coordy1)/(midpointx23 - coordx1)
  y_intercept1 = coordy1 - (slope1 * coordx1)
  slope2 = (midpointy12 - coordy3)/(midpointx12 - coordx3)
  y_intercept2 = coordy3 - (slope2 * coordx3)

  # Find x and y coordinates of centroid
  centroid_x = (y_intercept2 - y_intercept1)/(slope1 - slope2)
  centroid_y = centroid_x * slope1 + y_intercept1

  # Title
  text = font_SansBold.render("Centroid Practice", True, white)
  textRect = text.get_rect()
  textRect.center = (400, 100)

  # Defines square where triangle spawns
  square_position = (80, 190)
  square_dimension = (350, 350)
  square = pygame.Rect(square_position, square_dimension)

  # Score
  score_sum = 0
  score_text = font_Sans.render(f"Total Score:", True, white)
  click_square = True

  # Game loop
  while True:

    # Menu background, title, graphics
    window.blit(menu_background, (0, 0))
    window.blit(text, textRect)

    # Title
    window.blit(score_text, (450, 280))
    updated_score = font_Sans.render(f"{score_sum}", True, white)
    window.blit(updated_score, (450, 340))

    # Draw the square and the triangle spawns
    pygame.draw.rect(window, white, square, 2)
    pygame.draw.polygon(window, white, 
      ((coordx1, coordy1), (coordx2, coordy2), (coordx3, coordy3)), 3)
    
    # Event handler
    for event in pygame.event.get():
      # When X is clicked the program stops
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

      # When button is clicked 
      if pygame.mouse.get_pressed()[0] and click_square:
        pos_x, pos_y = pygame.mouse.get_pos()
        if square.collidepoint(pos_x, pos_y):
          # Calculate score
          distance = math.sqrt((pos_x - centroid_x)**2 + (pos_y - centroid_y)**2)
          score_sum += distance * 3
          click_square = False
        
    pygame.display.update()


# Practice Menu
def practice():

  #Caption
  pygame.display.set_caption("Practice")

  # Title
  text = font_SansBold.render("Practice", True, white)
  textRect = text.get_rect()
  textRect.center = (400, 100)


  # Defines the buttons
  centroid_button = Button(65, 160, menu_button, 0.65)
  circumcenter_button = Button(65, 250, menu_button, 0.65)
  incenter_button = Button(65, 340, menu_button, 0.65)
  orthocenter_button = Button(65, 430, menu_button, 0.65)
  return_button = Button(660, 480, return_menu, 0.15)

  # Game loop
  while True:
    # Menu background, title, graphics
    window.blit(menu_background, (0, 0))
    window.blit(text, textRect)

    # Draws button
    if centroid_button.draw():
      centroid()
    if circumcenter_button.draw():
      print("Circumecenter")
    if incenter_button.draw():
      print("Incenter")
    if orthocenter_button.draw():
      print("Orthocenter")
    if return_button.draw():
      main_menu()
                         
    # Event handler
    for event in pygame.event.get():
      # When X is clicked the program stops
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()

# Main menu
def main_menu():

  # Caption  
  pygame.display.set_caption("Main Menu")

  # Defines the title of the menu
  text = font_SansBold.render("Triangulate", True, white)
  textRect = text.get_rect()
  textRect.center = (400, 100)

  # Defining buttons
  play_button = Button(65, 160, menu_button, 0.65)
  practice_button = Button(65, 250, menu_button, 0.65)
  option_button = Button(65, 340, menu_button, 0.65)
  leaderboard_button = Button(65, 430, menu_button, 0.65)

  # Game loop
  while True:
    # Menu background, title, graphics
    window.blit(menu_background, (0, 0))
    window.blit(text, textRect)
    window.blit(menu_graphic, (470, 200))

    # Draws button
    if play_button.draw():
      print("Start")
    if practice_button.draw():
      practice()
    if option_button.draw():
      print("Options")
    if leaderboard_button.draw():
      print("Leaderboard")
                         
    # Event handler
    for event in pygame.event.get():

      # When X is clicked the program stops
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()

main_menu()
