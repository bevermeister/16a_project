import pygame

# button class
class Button():
    """
    Defining a button class with functions to be called when the game needs a usable button.

    """
    def __init__(self, x, y, image, scale):
        """
        Button class constructor to initialize the object.
            Args:
                x (int): x coordinate of rectangle
                y (int): y coordinate of rectangle
                image (int): image used for the button
                scale (int): scale factor used to shrink or enlarge the width/height
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.clicked = False
    
    def draw(self, surface, pressed):
        """
        Draw the button and give commands for when it is pressed.
            Args:
                surface (tuple): the background screen that the button will show up on
                pressed (int): whether or nor button is clicked on or not
            Returns:
                action (boolean): the purpose of the button/what it activates when it is pressed
        """
        action = False
        # get position of mouse
        pos = pygame.mouse.get_pos()

        # check where mouse is and click conditions
        if self.rect.collidepoint(pos):
            if pressed == 1:
                action = True

        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
