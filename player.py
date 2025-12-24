import pygame, time
from math import trunc
from pygame import K_SPACE
from Support import ImportFolder
from Sounds import *


class Player(pygame.sprite.Sprite):
    def __init__(self, SpawnPoint, ObtainedDoubleJump, ObtainedDash):
        super().__init__()
        self.ImportAssets()
        self.SpawnPoint = SpawnPoint
        self.RespawnPoint = SpawnPoint
        self.FrameIndex = 0
        self.AnimationSpeed = 0.15
        self.image = self.Animations['Idle'][self.FrameIndex]
        self.rect = self.image.get_rect(topleft = SpawnPoint)

        self.Direction = pygame.math.Vector2(0,0)

        self.SpacePressed = False
        self.ShiftPressed = False

        self.PlayerSpeed = 10
        self.NormalSpeed = self.PlayerSpeed
        self.JumpSpeed = -22
        self.Gravity = 0.7
        self.DashSpeed = 7

        self.OnPlatform = False
        self.IsJumping = False
        self.IsFalling = False
        self.Dashing = False
        self.Alive = True

        self.ObtainedDoubleJump = ObtainedDoubleJump
        self.DoubleJump = ObtainedDoubleJump
        self.ObtainedDash = ObtainedDash
        self.Dash = ObtainedDash
        self.DashStartTime = 0

        self.Status = 'Idle'
        self.PreviousStatus  = 'Idle'
        self.FacingRight = True

        self.OnCeiling = False
        self.OnGround = False
        self.OnRight = False
        self.OnLeft = False

    def ImportAssets(self):
        self.Animations = {'Idle':[], 'Run':[], 'Jump':[], 'Dash':[], 'Death':[], 'Fall':[]}

        for Animation in self.Animations.keys():
            FullPath = 'SpriteSheets/PlayerAnimation/' + Animation
            self.Animations[Animation] = ImportFolder(FullPath)
    
    def Animate(self):
        if self.Status != self.PreviousStatus:
            self.PreviousStatus = self.Status
            self.AnimationSpeed = 0.15
            self.FrameIndex = 0

        Animation = self.Animations[self.Status]
        self.Animation = Animation 
        
        self.FrameIndex += self.AnimationSpeed
        if self.FrameIndex >= len(Animation):
            self.FrameIndex = 0

        AnimFrame = Animation[int(self.FrameIndex)]
        if self.FacingRight:
            self.image = AnimFrame
        else:
            self.image = pygame.transform.flip(AnimFrame, True, False)

        if self.OnGround:
            if self.ObtainedDoubleJump and self.DoubleJump == False: 
                self.DoubleJump = True

            if self.OnRight:
                self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
            elif self.OnLeft:
                self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
            else:
                self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        
        elif self.OnCeiling and self.OnRight:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.OnCeiling and self.OnLeft:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.OnCeiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)  

    def GetInput(self):
        Key = pygame.key.get_pressed()

        if self.Dashing == False:
            if self.ShiftPressed:
                self.AnimationSpeed = 0.25
                self.TestDashing(self.FacingRight)
                self.ShiftPressed = False

            elif Key[pygame.K_RIGHT]:
                self.FacingRight = True
                self.Direction.x = 1

            elif Key[pygame.K_LEFT]:
                self.FacingRight = False
                self.Direction.x = -1

            else:
                self.Direction.x = 0

        if self.SpacePressed:
            self.SpacePressed = False
            if self.IsJumping == False and self.IsFalling == False:
                PlayerJumpSound()
                self.IsJumping = True
                self.Jump(self.JumpSpeed)
            elif self.DoubleJump and self.OnGround == False:
                self.DoubleJump = False
                PlayerJumpSound()
                self.IsJumping = True
                self.Jump(self.JumpSpeed + 5)

    def TestDashing(self, OnRight):
        if self.ObtainedDash:
            self.Dashing = True
            if OnRight: self.Direction.x = self.DashSpeed
            else: self.Direction.x = -self.DashSpeed
            return True
        return False

    def GetStatus(self):
        if self.Alive == False:
            self.Status = 'Death'
        else:
            if self.Direction.y < 0:
                self.Status = 'Jump'
                self.AnimationSpeed = 0.2
            elif self.Direction.y > self.Gravity:
                self.Status = 'Fall'
            else:
                if self.Direction.x != 0 and self.Status != 'Jump':
                    self.Status = 'Run'
                elif self.OnGround:
                    self.Status = 'Idle'

            if self.Dashing: 
                self.Status = 'Dash'
                self.ApplyDash()
            
    def ApplyDash(self):
        self.DashSlowSpeed = round(self.Direction.x / 14, 3)
        
        if (self.Direction.x > 1 and self.FacingRight) or (self.Direction.x < -1 and self.FacingRight == False):
            self.Direction.x -= self.DashSlowSpeed
        else:
            self.Dashing = False

    def ApplyGravity(self):
        self.Direction.y += self.Gravity
        self.rect.y += self.Direction.y

    def PlayerDeath(self):
        self.Direction.x = 0
        self.Alive = False
        self.Status = 'Death'

    def Jump(self, JumpSpeed):
        self.Direction.y = JumpSpeed

    def update(self):
        if self.Alive:
            self.GetInput()
            self.GetStatus()
        self.Animate()
