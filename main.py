import pygame

# Internal dependencies
from engine.screen import Screen
from engine.events import Events

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Project Plant")
        pygame.display.set_icon(pygame.image.load("./media/images/active/plant.png"))
        # pygame.mixer.music.load('./media/music/background.wav')
        # pygame.mixer.music.play(-1)

        self.clock = pygame.time.Clock()
        self.screen = Screen()
        self.events = Events(self.screen.plant)

    def process_input(self):
        # Checks for any events that need to be actioned, such as the keyboard/mouse
        self.events.check()

    def update(self):
        """Updates the games state. Currently this is done elsewhere but should it be here?"""
        pass

    def render(self):
        # Updates the screen for changes
        self.screen.update()
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def run(self):
        self.clock.tick(60)

    def start(self):
        """This starts the game loop which will perform all the operations to make the game a game."""
        while True:
            self.process_input()
            self.update()
            self.render()
            self.run()


if __name__ == '__main__':
    game = Game()
    game.start()
