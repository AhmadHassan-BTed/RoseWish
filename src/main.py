import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.engine.game import GameEngine


def main():
    try:
        engine = GameEngine()
        engine.run()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception:
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
