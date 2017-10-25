#Gerson
import pygame, random
pygame.init()

#Cores:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
DARK_BLUE = (32,154,249)
LIGHT_BLUE = (1,120,212)
RED = (255,0,0)
 
#Dimensões da tela:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.font.Font('LuckiestGuy.ttf', 10)
pygame.mixer.music.load("Ice-Cream-Truck.mp3")
som_ao_clicar = pygame.mixer.Sound("Quack.ogg")
background_image = pygame.image.load("CAF.jpg")
menu_image = pygame.image.load("menu_02.jpg")
#FimGerson

#Roseane
#Essa é a função que exibe o menu
def menu():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(menu_image,[0,0])
        botão("Iniciar", 515, 280, 245, 90, LIGHT_BLUE, DARK_BLUE,"iniciar")
        pygame.mixer.music.stop()
        pygame.display.update()
        clock.tick(20)

#Essa função chama o loop do jogo.       
def botão(mensagem,x,y,l,a,ci,ca,ação=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+l> mouse[0] > x and y+a > mouse[1] > y:
        pygame.draw.rect(screen,ca,[x,y,l,a])
        if click[0] == 1 and ação != None:
            if ação == "iniciar":
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
#FimRoseane

#Wendell
class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.image.load("babelfish.png")
        self.rect = self.image.get_rect()

block_box_list = pygame.sprite.Group()
all_sprite_box_list = pygame.sprite.Group()

#Cria diversos "blocos" aleatórios que são objetos da classe Block."
for i in range(50):
    block = Block(BLUE,20,15)
    block.rect.x = random.randrange(SCREEN_WIDTH-20)
    block.rect.y = random.randrange(SCREEN_HEIGHT-15)

    block_box_list.add(block)
    all_sprite_box_list.add(block)

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Função construtora
    def __init__(self, x, y):
        # Chama o construtor da superclasse.
        super().__init__()
 
        # Define altura, largura
        self.image = pygame.image.load("pinguim.png").convert()
        self.image.set_colorkey(BLACK)
 
        # Faz nosso canto superior-esquerdo com a posição passada.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Define a velocidade:
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Altera a velocidade do the jogador. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Atualiza a posição do jogador. """
        # Mover esquerda/direita
        self.rect.x += self.change_x
 
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        # Mover para cima/para baixo:
        self.rect.y += self.change_y
 
        # Verificar e ver se colidimos com algo
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Resetar nossa posição baseado no topo/fundo do objeto:.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
#FimWendell

#Jobson 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Chama o construtor da superclasse
        super().__init__()
 
        # Fazer um muro azul, do tamanho especificado nos parâmetros
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        #Faz nosso canto superior-esquerdo com a posição passada.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 

 
# Cria uma tela de 800x600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Definir o titulo da janela
pygame.display.set_caption('Collect All Fish!')
 
# Lista que contem todos os sprites
all_sprite_list = pygame.sprite.Group()
 
# Criar os muros. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
#Cria instâncias para a classe Wall: 
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
 
#FimJobson
#Roseane,Jobson e Wendell
def loop_do_jogo():
    #Faz com que a música seja tocada:
    pygame.mixer.music.play(-1,0)
    done = False
    #Variável da pontuação:
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
        #Texto placar que é impresso na tela:
        screen.blit(background_image,[0,0])    
        font = pygame.font.SysFont('LuckiestGuy',25,False,False)
        text = font.render("Placar: "+str(score),True,WHITE)
        screen.blit(text,[12,11])
     
        all_sprite_list.draw(screen)
        all_sprite_box_list.draw(screen)
        #Atualiza a tela com o que desenhamos. 
        pygame.display.flip()
     
        clock.tick(60)
##Fim!
#Chamada das funções
menu()
loop_do_jogo()
pygame.quit()
