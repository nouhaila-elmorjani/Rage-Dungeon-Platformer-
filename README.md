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
```bash
# Clone the repository
git clone https://github.com/yourusername/rage-dungeon-platformer.git

# Navigate to project directory
cd rage-dungeon-platformer

# Install PyGame (if not already installed)
pip install pygame

# Run the game
python Python_Platformer.py
🕹️ Controls
Movement

Left/Right: Arrow Keys or A/D

Jump: Spacebar

Dash: Left Shift

Interface

Pause Menu: Escape

Level Selection (Demo): Tab

Quick Complete (Demo): C

Mouse

Menu Navigation: Click buttons

Level Selection: Click desired level

📁 Project Structure
text
rage-dungeon-platformer/
├── Python_Platformer.py     # Main game loop and state management
├── player.py               # Player physics and movement system
├── Levels.py               # Level loading and collision handling
├── Menu.py                 # UI interface and menu navigation  
├── Support.py              # File I/O and data persistence
├── Blocks_And_Objects.py   # Game objects and interactive elements
├── Sounds.py               # Audio management system
├── README.md               # Project documentation
├── Levels/                 # Level definition files (CSV format)
│   ├── Level 0/           # Tutorial introduction
│   ├── Level 1-8/         # Progressive challenge levels
│   └── Level 9/           # Final level challenge
├── Players/                # Player save data and high scores
├── MenuItems/              # UI assets and visual elements
├── SpriteSheets/          # Character and object animations
└── Sounds/                # Audio assets and music files
🔧 Technical Implementation
Physics Customization
The player movement system has been carefully calibrated:

Jump Strength: -22 (vertical impulse force)

Movement Speed: 10 (horizontal velocity)

Gravity: 0.7 (fall acceleration rate)

Dash Speed: 7 (horizontal boost velocity)

Level Design System
Levels use CSV files with numerical codes:

142: Standard ground platform

270-271: Hazardous spike traps

285: Player starting position

322: Level completion portal

Various IDs for enemies, collectibles, and mechanics

Data Persistence
Player progress is stored with tracking for:

Maximum level progression

Individual level completion times

Collectible item acquisition status

Ability unlock progression

📈 Development Process
Phase 1: Core Mechanics

Basic movement implementation

Gravity and collision systems

Player state management

Phase 2: Level Design

CSV-based level format creation

Progressive difficulty balancing

Checkpoint and respawn systems

Phase 3: Polish & Systems

Animated sprite integration

Audio system implementation

Menu and UI development

Phase 4: Presentation Features

Demo mode implementation

Level switching functionality

Save system optimization

🛠️ Customization Options
For Different Gameplay Styles:

Adjust physics parameters in player.py

Modify level designs in CSV files

Create new power-up abilities

Customize UI elements in MenuItems/

For Extended Development:

Add new enemy types with unique behaviors

Create additional level themes

Implement new collectible items

Expand the ability system

🤝 Contributing
This project serves as a final course submission, but the codebase is structured to allow for educational extensions and modifications for learning purposes.

📄 License
Educational project developed for Software Engineering & Game Development course. Code available for academic and learning purposes.

🙏 Acknowledgments
PyGame Community for the excellent game development framework

Course Instructors for guidance and educational framework

Game Design Principles from classic platformer titles

Open Source Tools that made development possible

Developer: Nouhaila
Course: Software Engineering & Game Development
Completion: December 2024
Technologies: Python, PyGame, CSV-based level design

