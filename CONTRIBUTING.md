# Contributing to Rose Day Wishing Game

First off, thank you for considering contributing to the Rose Day Wishing Game! It's people like you who make the open-source community such an amazing place.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Bugs

- Check the [issue tracker](https://github.com/AhmadHassan-BTed/Rose-Day-Wishing-Game/issues) to see if the bug has already been reported.
- If not, create a new issue using the bug report template.
- Provide a clear and concise description of the bug and steps to reproduce it.

### Suggesting Enhancements

- Check the [issue tracker](https://github.com/AhmadHassan-BTed/Rose-Day-Wishing-Game/issues) for similar suggestions.
- Create a new issue using the feature request template.
- Explain why this enhancement would be useful and how it should work.

### Pull Requests

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/amazing-feature`).
3. Make your changes.
4. Ensure your code follows the project's style (run `ruff check .`).
5. Commit your changes (`git commit -m 'Add amazing feature'`).
6. Push to the branch (`git push origin feature/amazing-feature`).
7. Open a Pull Request.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AhmadHassan-BTed/Rose-Day-Wishing-Game.git
   cd Rose-Day-Wishing-Game
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```
4. Copy `.env.example` to `.env` and customize it.
5. Run the game:
   ```bash
   python src/main.py
   ```

## Style Guidelines

- Use PEP 8 for Python code.
- Use type hints wherever possible.
- Write descriptive commit messages.
- Document new functions and classes.
