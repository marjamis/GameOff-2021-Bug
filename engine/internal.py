import sys
import pygame

def ExitGame():
    """Clean up processes"""
    pygame.display.quit()
    pygame.quit()
    sys.exit()
