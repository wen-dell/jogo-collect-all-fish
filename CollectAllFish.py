
import pygame, random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
DARK_BLUE = (32,154,249)
LIGHT_BLUE = (1,120,212)
RED = (255,0,0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.font.Font('LuckiestGuy.ttf', 10)
pygame.mixer.music.load("Ice-Cream-Truck.mp3")
som_ao_clicar = pygame.mixer.Sound("Quack.ogg")
background_image = pygame.image.load("CAF.jpg")
menu_image = pygame.image.load("menu_02.jpg")

def menu():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(menu_image,[0,0])
        botao("Iniciar", 515, 280, 245, 90, LIGHT_BLUE, DARK_BLUE,"iniciar")
        pygame.mixer.music.stop()
        pygame.display.update()
        clock.tick(20)

def botao(mensagem,x,y,l,a,ci,ca,acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+l> mouse[0] > x and y+a > mouse[1] > y:
        pygame.draw.rect(screen,ca,[x,y,l,a])
        if click[0] == 1 and acao != None:
            if acao == "iniciar":
                loop_do_jogo()
        
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()
        
    else:
        pygame.draw.rect(screen,ci,[x,y,l,a])
    fonte = pygame.font.SysFont("LuckiestGuy",60)
    texto = fonte.render(mensagem,True,WHITE)
    screen.blit(texto,[540,300])
    pygame.display.update()
    clock.tick(20)

class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super(Block, self).__init__()
        self.image = pygame.image.load("babelfish.png")
        self.rect = self.image.get_rect()

block_box_list = pygame.sprite.Group()
all_sprite_box_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLUE,20,15)
    block.rect.x = random.randrange(SCREEN_WIDTH-20)
    block.rect.y = random.randrange(SCREEN_HEIGHT-15)

    block_box_list.add(block)
    all_sprite_box_list.add(block)

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()

        self.image = pygame.image.load("pinguim.png").convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        self.rect.x += self.change_x
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):

        super(Wall, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption('Collect All Fish!')

all_sprite_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()
wall = Wall(-2, 0, 2, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(0, -2, 800, 2)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(0, 601, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(801,0,2,600)
wall_list.add(wall)
all_sprite_list.add(wall)
player = Player(50, 50)
player.walls = wall_list
 
all_sprite_list.add(player)
 
clock = pygame.time.Clock()

def loop_do_jogo():
    pygame.mixer.music.play(-1,0)
    done = False
    score = 0
    while not done:
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
                if len(block_box_list) == 0:
                    for i in range(50):
                        block = Block(BLUE,20,15)
                        block.rect.x = random.randrange(SCREEN_WIDTH-20)
                        block.rect.y = random.randrange(SCREEN_HEIGHT-15)

                        block_box_list.add(block)
                        all_sprite_box_list.add(block)
     
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, -3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, 3)
     
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player.changespeed(0, -3)
            if event.type == pygame.MOUSEBUTTONDOWN:
                som_ao_clicar.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                if event.key == pygame.K_t:
                    pygame.mixer.music.unpause()
     
            
            
     
        all_sprite_list.update()
     
        
        block_box_hit_list = pygame.sprite.spritecollide(player,block_box_list,True)
        for block in block_box_hit_list:
            score+= 1
        screen.blit(background_image,[0,0])    
        font = pygame.font.SysFont('LuckiestGuy',25,False,False)
        text = font.render("Placar: "+str(score),True,WHITE)
        screen.blit(text,[12,11])
     
        all_sprite_list.draw(screen)
        all_sprite_box_list.draw(screen)
        pygame.display.flip()
     
        clock.tick(60)
menu()
loop_do_jogo()
pygame.quit()
