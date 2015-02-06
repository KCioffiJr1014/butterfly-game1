import pygame


class Button:
    def __init__(self, location, unHighlighted,  highlighted):
        self.unHighlightedImage = pygame.image.load(unHighlighted)
        self.highlightedImage = pygame.image.load(highlighted)
        self.image = self.unHighlightedImage
        self.rect = self.image.get_rect()
        self.clicked = False
        self.place(location)

        
        def click(self, pt):
                if self.collidePoint(pt):
                        self.clicked = True
                        self.image = self.clickedImage
                else:
                        self.clicked = False
                        self.image = self.baseImage
                        
        def release(self, pt):
                if self.clicked and self.collidePoint(pt):
                        return True
                else:
                        self.clicked = False
                        self.image = self.baseImage
                        return False
    def place(self, pos):
                self.rect.center = pos
    
    def click(self, pt):
        if self.collidePoint(pt):
            self.clicked = True
            self.image = self.highlightedImage
        else:
            self.clicked = False
            self.image = self.unHighlightedImage
           
    def collidePoint(self, pt):
        if self.rect.right > pt[0] and self.rect.left < pt[0]:
            if self.rect.bottom > pt[1] and self.rect.top < pt[1]:          
                return True
        return False
                
    def release(self, pt):
        if self.clicked and self.collidePoint(pt):
                return True
        else:
                self.clicked = False
                self.image = self.unHighlightedImage
                return False
        
    def update(self, width, height):
        pass
