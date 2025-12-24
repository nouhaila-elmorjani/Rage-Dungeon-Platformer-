import pygame, sys
from Levels import *
from Support import *
from pygame import mixer

# Constants
ScreenWidth = 1280
ScreenHeight = 640

# Initialising pygame
pygame.init()

# Defining size of game window
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Rage Dungeon")

# Creating clock - to set max frame rate to 60
Clock = pygame.time.Clock()

# Set Level Variables
GameWon = False
StartedGame = False
CurrentLevelNum = -1
NumberOfLastLevel = 9
ProgrammerMode = False

# Player background game music
mixer.music.load('MenuItems/BackgroundMusic.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()  

# Routine to load and return the next level automatically after the prvious has been completed
def MoveToNextLevel(CurrentLevelNum, PlayerLivesAndAbilities, MaxLevelReached):
    CurrentLevelNum += 1
    if MaxLevelReached <= CurrentLevelNum:
        MaxLevelReached = CurrentLevelNum
    TempToDisableTimer = CurrentLevel.ToDisableTimer
    CSVPath = 'Levels/Level ' + str(CurrentLevelNum) + '/Level ' + str(CurrentLevelNum) + '.csv'
    return Level(ImportCSV(CSVPath), screen, CurrentLevelNum, ProgrammerMode, InGameMenu, TempToDisableTimer, PlayerLivesAndAbilities), CurrentLevelNum, MaxLevelReached

# --- Name Screen ---

Name = DisplayNameScreen(screen)
MaxLevelReached,PlayerInfo,PlayerID,PlayerLivesAndAbilities = LoadLevelsReached(Name)

# Demo mode - unlock all levels
MaxLevelReached = "9"
PlayerInfo[1] = "9"
PlayerLivesAndAbilities = [5, True, True]

# Create Menus (only needs to be created once each time the program is loaded)
TitleScreen = CreateTitleScreen(screen)
LevelSelectionScreen = CreateLevelSelectionScreen(screen)
InGameMenu = CreateInGameMenu((300,100), screen)

# --- Title Screen ---

while StartedGame == False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            TitleScreen.MouseDown = True

    screen.fill((11, 11, 11))
    TitleScreen.update()

    for button in TitleScreen.Buttons:
        if button.Name == 'Start' and button.Clicked:
            CurrentLevelNum = MaxLevelReached
            StartedGame = True
            break
        elif button.Name == 'Load Game' and button.Clicked:
            StartedGame = True
            break

    pygame.display.update()
    Clock.tick(60)

# The indefinite loop when the player has selected 'start' or 'load game'
while True:

    # --- Level selection screen ---
    
    CreateButtonsForLevelSelectionScreen(int(MaxLevelReached), LevelSelectionScreen)

    while CurrentLevelNum == -1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                SaveScores(MaxLevelReached, PlayerID, PlayerInfo)
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                LevelSelectionScreen.MouseDown = True

        screen.fill((11, 11, 11))
        LevelSelectionScreen.update()

        for button in LevelSelectionScreen.Buttons:
            if button.Clicked:
                if 'Level' in button.Name:
                    level_num = button.Name.replace(" Off", "").replace("Level ", "")
                    CurrentLevelNum = int(level_num)
                    break
                elif button.Name == 'See Stats':
                    DisplayStatsScreen(MaxLevelReached,PlayerID,PlayerInfo,screen)
                elif button.Name == 'See High Scores':
                    DisplayHighScoreScreen(MaxLevelReached,PlayerID,PlayerInfo,screen)
                button.Clicked = False

        pygame.display.update()
        Clock.tick(60)

    # Giving the main file acess to the class Level
    CSVPath = 'Levels/Level ' + str(CurrentLevelNum) + '/Level ' + str(CurrentLevelNum) + '.csv'
    CurrentLevel = Level(ImportCSV(CSVPath), screen, CurrentLevelNum, ProgrammerMode, InGameMenu, False, PlayerLivesAndAbilities)

    # --- In-game loop ---

    while InGameMenu.Return == False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                SaveScores(MaxLevelReached, PlayerID, PlayerInfo)
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                InGameMenu.MouseDown = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if CurrentLevel.MenuDisplayed == False:
                        CurrentLevel.MenuDisplayed = True
                    else:
                        CurrentLevel.MenuDisplayed = False
                elif event.key == pygame.K_SPACE:
                    CurrentLevel.SpacePressed = True
                elif event.key == pygame.K_LSHIFT:
                    CurrentLevel.ShiftPressed = True
                elif event.key == pygame.K_TAB:
                    InGameMenu.Return = True

        screen.fill((11, 11, 11))

        if CurrentLevel.FinishedLevel == False:
            CurrentLevel.run()
        else:
            if int(CurrentLevelNum) != 0:
                PreviousTime = float(PlayerInfo[(int(CurrentLevelNum)*2)])

                if CurrentLevel.ToDisableTimer == False and (float(CurrentLevel.ElapsedTime) < PreviousTime or str(PreviousTime) == "-1.0"):
                    PlayerInfo[(int(CurrentLevelNum)*2)] = str(CurrentLevel.ElapsedTime)
                if str(PlayerInfo[1+(int(CurrentLevelNum)*2)]) == 'False':
                    PlayerInfo[1+(int(CurrentLevelNum)*2)] = str(CurrentLevel.CollectedGoldenGear)

            if int(CurrentLevelNum) == NumberOfLastLevel:
                SaveScores(MaxLevelReached, PlayerID, PlayerInfo)
                InGameMenu.Return = True
            else:
                CurrentLevel, CurrentLevelNum, MaxLevelReached = MoveToNextLevel(int(CurrentLevelNum), PlayerLivesAndAbilities, int(MaxLevelReached))

        if CurrentLevel.SaveAndExit:
            SaveScores(MaxLevelReached, PlayerID, PlayerInfo)
            sys.exit()

        pygame.display.update()
        Clock.tick(60)

    CurrentLevelNum = -1
    InGameMenu.Return = False
    for button in LevelSelectionScreen.Buttons:
        button.Clicked = False
