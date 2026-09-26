"""
Snack Attack! - Arcade Snake & Snack Game in Python
Desktop entry point script. Safe for Vercel serverless deployment scanning.
"""
import os
import sys

# Expose WSGI callable in case Vercel framework scanner inspects main.py
try:
    from api.index import app, handler, application
except Exception:
    app = None


def main():
    try:
        # Center the game window on user's screen
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        import traceback
        import pygame
        from game import Game

        # Create window icon
        icon_surf = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.circle(icon_surf, (220, 30, 40), (16, 18), 12)
        pygame.draw.circle(icon_surf, (255, 120, 130), (12, 14), 4)
        pygame.draw.line(icon_surf, (95, 55, 20), (16, 8), (17, 3), 2)
        pygame.draw.polygon(icon_surf, (60, 200, 50), [(17, 6), (25, 3), (21, 10)])

        # Initialize pygame
        pygame.init()
        try:
            pygame.display.set_icon(icon_surf)
        except Exception:
            pass

        # Start game engine
        print("Starting Snack Attack!...")
        game = Game()
        game.run()
        print("Game closed gracefully.")
    except Exception as e:
        import traceback
        print("\n" + "=" * 50)
        print("AN ERROR OCCURRED WHILE RUNNING THE GAME:")
        print("=" * 50)
        traceback.print_exc()
        print("=" * 50)
        try:
            input("\nPress Enter to exit...")
        except Exception:
            pass
        sys.exit(1)


if __name__ == "__main__":
    main()
