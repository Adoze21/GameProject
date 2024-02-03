
# an air hockey game for 2
# This game is made in a class Hockey, which has 7 methods:
# 1) constructor that describes items and launches main activities
# 2) main_loop that launches the game
# 3) move_items that helps the robot and the monster move (somehow the monster does not move, and I could'n figure out why yet)
# 4) check_events method, that checks which event is called
# 5) move_ball method that makes the coin-ball move and makes sure it bounces not only from the walls but from the sprites as well
# 6) points method that is supposed to count each time the ball enters the goal rectangle area (but it does not work properly yet)
# 7) draw_window that draws all the item on screen

#Several improvements are to be made by April 2024 (now I am more focused on ML courses)
# This game is supposed to work like a regular air hockey game. To make it work better I need to improve the following things:
# 1) fix the movements of the monster sprite
# 2) make the points counter work properly
# 3) make the ball stop each time the goal scored and start from scratch
# 4) ideally the ball should move only after the sprite touches it. I tried to make it work, but the ball was not moving enough this way
# 5) I need to think of how to make less of code for this game

# Thanks for reviewing my code! I hope you enjoy it
import pygame

class Hockey:
    def __init__(self):
        pygame.init()

        self.height = 480
        self.width = 640

        self.window = pygame.display.set_mode((self.width, self.height))
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.robot = pygame.image.load("robot.png")
        self.rect_robot = self.robot.get_rect()
        self.rect_robot.center = (50, 190)

        self.monster = pygame.image.load("monster.png")
        self.rect_monster = self.monster.get_rect()
        self.rect_monster.center = (590, 190)
        
        self.ball = pygame.image.load("coin.png")
        self.rect = self.ball.get_rect()
        self.rect.center = (100, 100)

        self.x1 = 50
        self.y1 = 240 - self.robot.get_height()
        self.x2 = 590 - self.monster.get_width()
        self.y2 = 240 - self.monster.get_height()

        self.to_left = False
        self.to_right = False
        self.up = False
        self.down = False

        self.to_left_m = False
        self.to_right_m = False
        self.up_m = False
        self.down_m = False

        pygame.display.set_caption("Air Hockey Game For 2")

        self.velocity = 4
        self.speed = [7, 4]

        self.clock = pygame.time.Clock()

        self.main_loop()
    
    def main_loop(self):
        self.monster_points = 0
        self.robot_points = 0
        while True:
            self.check_events()
            self.draw_window()
            self.move_items()
            self.move_ball()
            self.points()
    
    def move_items(self):
        if self.to_left:
            if self.rect_robot.left - self.velocity <= 0:
                self.to_left = False
            else:
                self.rect_robot.right -= self.velocity
        if self.to_right:
            if self.rect_robot.right + self.velocity >= 320 - self.robot.get_width():
                self.to_right = False
            else:
                self.rect_robot.right += self.velocity
        if self.up:
            if self.rect_robot.top - self.velocity <= 0:
                self.up = False
            else:
                self.rect_robot.top -= self.velocity
        if self.down:
            if self.rect_robot.bottom + self.velocity >= 480:
                self.down = False
            else:
                self.rect_robot.bottom += self.velocity

        #somehow the monster does not move, and I could'n figure out why yet
        if self.to_left_m:
            self.rect_monster.right -= self.velocity
        if self.to_right_m:
            self.rect_monster.right += self.velocity
        if self.up_m:
            self.rect_monster.top -= self.velocity
        if self.down_m:
            self.rect_monster.bottom += self.velocity
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.to_right = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
                if event.key == pygame.K_a:
                    self.to_left_m = True
                if event.key == pygame.K_d:
                    self.to_right_m = True
                if event.key == pygame.K_w:
                    self.up_m = True
                if event.key == pygame.K_s:
                    self.down_m = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.to_right = False
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False
                if event.key == pygame.K_a:
                    self.to_left_m = False
                if event.key == pygame.K_d:
                    self.to_right_m = False
                if event.key == pygame.K_w:
                    self.up_m = False
                if event.key == pygame.K_s:
                    self.down_m = False
                
                self.clock.tick(60)

            if event.type == pygame.QUIT:
                print(self.points())
                exit()

# move_ball method that makes the ball move and makes sure it bounces not only from the walls but from the sprites as well
    def move_ball(self):
        if pygame.Rect.colliderect(self.rect, self.rect_robot):
            self.speed[0] = -self.speed[0]
        if pygame.Rect.colliderect(self.rect, self.rect_monster):
            self.speed[0] = -self.speed[0]
        if self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        if self.rect.right >= 640:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 50:
            self.speed[1] = -self.speed[1]
        if self.rect.top >= 430:
            self.speed[1] = -self.speed[1]
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        pygame.display.update()
        self.clock.tick(60)
    
    def points(self):
        if pygame.Rect.colliderect(self.rect, self.rect_goal1):
            self.monster_points += 1
        if pygame.Rect.colliderect(self.rect, self.rect_goal2):
            self.robot_points += 1
        return f"Monster: {self.monster_points}, Robot: {self.robot_points}"

    
    def draw_window(self):
        self.window.fill((221, 229, 244))
        self.rect_goal1 = pygame.draw.rect(self.window, (102,142,171), (0, 150, 50, 180))
        self.rect_goal2 = pygame.draw.rect(self.window, (102,142,171), (590, 150, 50, 180))
        self.window.blit(self.robot, self.rect_robot)
        self.window.blit(self.monster, (self.x2, self.y2))
        self.window.blit(self.ball, self.rect)
    
        pygame.display.flip()

if __name__ == "__main__":
    Hockey()