import pygame

class Display():

    def __init__(self):
        pygame.init()

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        self.width = 1620
        self.height = 900
        self.size = (self.width, self.height)
        self.display = pygame.display.set_mode(self.size)
        self.OFFSET_X =  int(self.width/2)
        self.OFFSET_Y = int(self.height/2)
        pygame.display.set_caption("PARABOLA")
        self.display.fill(self.WHITE)

    def draw_source(self, lightSource):
        for source in lightSource:
            x = source[0] # + self.OFFSET_X
            y = source[1] + self.OFFSET_Y
            pygame.draw.circle(self.display, self.RED,( x, y), 2, 2)


    def display_to_screen(self):
        """This is needed to display everything to the screen"""
        pygame.display.update()

        running = True
        while running:
            for event in pygame.event.get():  # this gets any event on the screen
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
        quit()