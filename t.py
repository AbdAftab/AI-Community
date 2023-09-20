import pygame
import time

from bot import Bot

# Function to render multiline text
def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]
    space_width, _ = font.size(' ')

    max_width, max_height = 500, 0
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space_width
        x = pos[0]
        y += word_height

# Initialize Pygame
pygame.init()

# Create a screen with width=800 and height=600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bot Conversation')

# Colors
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    clock = pygame.time.Clock()
    x = 0

    bot1 = Bot("Bot 1", likes=["Outdoors"], dislikes=["Waking Up"])
    bot2 = Bot("Bot 2", likes=["Reading"], dislikes=["Noise"])

    current_weather = "Raining"
    bot1.perform_activity("Just woke up", current_weather)

    conversation_text = ''

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw the screen black
        screen.fill(BLACK)
        
        # Draw the bots (represented as green rectangles)
        pygame.draw.rect(screen, GREEN, (150, 250, 50, 50))
        pygame.draw.rect(screen, GREEN, (600, 250, 50, 50))

        # Add text above the bots to indicate who they are
        font = pygame.font.SysFont(None, 36)
        text = font.render('Bot 1', True, WHITE)
        screen.blit(text, (150, 220))

        text = font.render('Bot 2', True, WHITE)
        screen.blit(text, (600, 220))

        text = font.render('How was your day?', True, WHITE)
        screen.blit(text, (550, 180))

        # Add conversation text above the bots
        conversation_font = pygame.font.SysFont(None, 18)
        blit_text(screen, conversation_text, (150, 180), conversation_font)

        # Update the display
        pygame.display.update()

        # Run the conversation logic and update the conversation text
        if x == 0:
            conversation_text = bot2.converse_with(bot1)
            x += 1
        time.sleep(5)  # Pause for 5 seconds to simulate conversation time

        # Slow down to see the drawing
        clock.tick(30)

if __name__ == "__main__":
    main()
