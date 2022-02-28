import pygame

# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.clicked = False
    
    def draw(self, surface,pressed):
        action = False
        # get position of mouse
        pos = pygame.mouse.get_pos()

        # check where mouse is and click conditions
        if self.rect.collidepoint(pos):
            if pressed == 1:
                action = True

        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        return action
