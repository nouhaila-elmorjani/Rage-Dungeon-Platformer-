# Rage Dungeon - PyGame Platformer

**A challenging 2D platformer with enhanced physics and progressive level design**  
*Final Project - Software Engineering & Game Development Course*

![Platformer Game](https://img.shields.io/badge/Game-Platformer-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-red)

## 📋 Project Overview

Rage Dungeon is a feature-complete 2D platformer developed with PyGame, demonstrating professional game development practices and software engineering principles. The game features custom physics, progressive difficulty, and a complete player progression system.

**Key Highlights:**
- **Enhanced Physics Engine** - Custom-tuned movement mechanics for responsive gameplay
- **10 Challenging Levels** - Progressive difficulty with unique obstacles in each stage
- **Complete Save System** - Persistent player data and high score tracking
- **Demo Features** - Presentation-ready tools for showcasing project capabilities

## 🎮 Core Features

### Gameplay Mechanics
- **Precision Platforming** - Smooth character control with momentum-based movement
- **Ability System** - Collectible power-ups (Double Jump & Dash) that persist through levels
- **Health Management** - 5-heart health system with checkpoint-based respawning
- **Environmental Challenges** - Spikes, moving platforms, enemy AI, and interactive objects

### Technical Systems
- **Custom Physics Engine** - Fine-tuned parameters for optimal player experience
- **Modular Level Design** - CSV-based level format for easy content creation
- **State Management** - Comprehensive game state handling for menus and gameplay
- **Asset Pipeline** - Organized sprite sheets and audio management

### Presentation & Polish
- **Animated Sprites** - Fluid character animations for all actions
- **Complete UI Suite** - Title screen, level selection, pause menu, and settings
- **Audio Feedback** - Background music and contextual sound effects
- **Visual Effects** - Particle systems and transition animations

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- PyGame 2.0+

### Installation

# Clone the repository
git clone https://github.com/yourusername/rage-dungeon-platformer.git

# Navigate to project directory
cd rage-dungeon-platformer

# Install PyGame (if not already installed)
pip install pygame

# Run the game
python Python_Platformer.py
🕹️ Controls
Action	Primary Control	Alternative
Move Left	Left Arrow	A
Move Right	Right Arrow	D
Jump	Spacebar	
Dash	Left Shift	
Pause Menu	Escape	
Level Selection (Demo)	Tab	
Quick Complete (Demo)	C	
🏗️ Project Architecture
File Structure
text
rage-dungeon-platformer/
├── Python_Platformer.py     # Main game loop and state management
├── player.py               # Player character with physics implementation
├── Levels.py               # Level loading and collision systems
├── Menu.py                 # UI interface and menu navigation
├── Support.py              # File I/O and data persistence
├── Blocks_And_Objects.py   # Game objects and interactive elements
├── Sounds.py               # Audio management system
├── README.md               # Project documentation
├── .gitignore              # Version control exclusions
├── Levels/                 # Level definition files (CSV format)
│   ├── Level 0/           # Tutorial level
│   ├── Level 1-8/         # Progressive challenge levels
│   └── Level 9/           # Final boss level
├── Players/                # Player data and high scores
├── MenuItems/              # UI assets and interface elements
├── SpriteSheets/          # Character and object animations
└── Sounds/                # Audio assets and music files
Physics Parameters (Customized)
The player movement has been carefully calibrated for optimal gameplay feel:

Jump Strength: -22 (vertical impulse)

Movement Speed: 10 (horizontal velocity)

Gravity: 0.7 (fall acceleration)

Dash Speed: 7 (horizontal boost)

Level Design System
Levels are defined using CSV files where numerical values represent different game elements:

142: Solid ground tiles

270-271: Hazardous spike traps

285: Player spawn point

322: Level completion portal

Various IDs for enemies, collectibles, and interactive objects

🔧 Development Features
For Presentation & Demonstration
Demo Mode: All levels unlocked by default for seamless showcasing

Level Navigation: Instant level switching with Tab key during gameplay

Quick Completion: C key for rapid level progression during demonstrations

Save System Architecture
Player progress is stored in a structured text format tracking:

Maximum level reached

Completion time for each level

Golden gear collection status

Ability unlock progression

Extensibility
The modular design allows for easy expansion:

Add new levels by creating CSV files in the Levels/ directory

Modify physics parameters in player.py for different gameplay feels

Extend the ability system with new power-ups

Customize UI elements in the MenuItems/ folder

📈 Learning Outcomes
This project demonstrates comprehensive understanding of:

Software Engineering Principles
Object-oriented design patterns

Modular code organization

State management and game loops

File I/O and data persistence

Game Development Techniques
2D physics and collision detection

Sprite animation and rendering

Audio integration and management

User interface design

Progressive difficulty balancing

Project Management
Iterative development process

Version control with Git

Professional documentation

Presentation preparation

🤝 Contributing
While this is a final project submission, the codebase is structured to allow for:

Level design contributions via CSV files

Physics parameter adjustments for different gameplay styles

UI/UX improvements through asset modifications

📄 License
This project is developed as a final course submission. All code is available for educational purposes.

🙏 Acknowledgments
Built with PyGame

Developed as a final project for Software Engineering & Game Development course

Inspired by classic 2D platformer mechanics

Special thanks to course instructors for guidance and feedback

Developer: Nouhaila
Course: Software Engineering & Game Development
Completion Date: December 2024
