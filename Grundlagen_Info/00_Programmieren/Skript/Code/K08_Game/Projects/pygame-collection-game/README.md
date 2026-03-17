# Pygame Collection Game

This project is a visually appealing collection game developed using Python and pygame-ce. The game features player movement, item collection with point counting, sound playback, a sunset background, and a 60-second time limit. The remaining time is displayed in the window title.

## Project Structure

```
pygame-collection-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game.py          # Main game logic and loop
│   ├── settings.py      # Configuration settings
│   ├── player.py        # Player class and movement
│   ├── item.py          # Item class for collectibles
│   ├── background.py     # Background rendering and animations
│   ├── ui.py            # User interface elements
│   ├── audio.py         # Audio management
│   └── __init__.py      # Marks src as a package
├── assets
│   ├── images           # Directory for image files
│   ├── sounds           # Directory for sound files
│   └── fonts            # Directory for font files
├── data                 # Directory for data files
├── requirements.txt     # Project dependencies
├── .gitignore           # Files to ignore in version control
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd pygame-collection-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, run the following command:
```
python src/main.py
```

## Gameplay

- Use the arrow keys to move the player character.
- Collect items to earn points.
- The game lasts for 60 seconds, and the remaining time is displayed in the window title.
- Enjoy the sunset background while playing!

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.