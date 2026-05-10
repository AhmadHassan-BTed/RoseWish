# Setup & Installation Guide

This guide will help you get the Rose Day Wishing Game running on your local machine.

## Platform Support

- **Windows**: Fully supported.
- **macOS**: Supported (requires Homebrew for some dependencies).
- **Linux**: Supported (requires SDL2 development libraries).

## Step-by-Step Installation

### 1. Clone the Repo
```bash
git clone https://github.com/AhmadHassan-BTed/Rose-Day-Wishing-Game.git
cd Rose-Day-Wishing-Game
```

### 2. Environment Setup
It is highly recommended to use a virtual environment.

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
# OR
pip install -e .
```

### 4. Configuration
1. Locate `.env.example` in the root directory.
2. Rename or copy it to `.env`.
3. Open `.env` and customize the values.

### 5. Run the Game
```bash
python src/main.py
```

## Troubleshooting

### Music not playing
Ensure your `music.mp3` file is located in the `assets/` folder and that the `MUSIC_PATH` in your `.env` correctly points to it.

### Pygame installation errors
If you are on Linux, you may need to install development headers for SDL:
```bash
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
```

### Display errors in WSL
Pygame requires a GUI. If you are using WSL, ensure you have an X-Server installed and configured (like VcXsrv) or use WSLg.
