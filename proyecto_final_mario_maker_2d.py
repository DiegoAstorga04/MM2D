import pygame
from pygame.locals import *
import sys
import os

#///////////////////////PROPIEDADES DE LA PANTALLA///////////////////////
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
IMG_DIR = "sprites"

#////////////////////////////CREAR LA VENTANA/////////////////////////
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Maker 2D")

lvl = 1
#///////////////////VARIABLES PARA EL SPRITE DE MARIO/////////////////
x = 585
y= 640
vel = 6
volando = False
vida = 5
#////////////COMPROBACIÓN DE DIRECCIONES PARA MARIO//////////////
left = False
right = False
up = False
down = False
walkcount = 0 

#//////////FUNCION PARA CARGAR IMAGENES////////////////
def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image       

#////////////MARIO SPAWNEA EN ESTA PLATAFORMA/////////////////
class inicio(pygame.sprite.Sprite):
    "la plataforma de inicio"

    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("inicio.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

#/////////////INDICA EL CAMINO HACIA LA SIGUIENTE ZONA////////////////
class nextzone(pygame.sprite.Sprite):
    "camino hacia la siguiente zona"

    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("next.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

class camino(pygame.sprite.Sprite):

    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("camino.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

class pared(pygame.sprite.Sprite):
    
    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("roca.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

class catapulta(pygame.sprite.Sprite):

    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("cannonxd.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

class meta(pygame.sprite.Sprite):

    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("bandera.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

class goomba(pygame.sprite.Sprite):
    
    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("goombaL2.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

class planta(pygame.sprite.Sprite):
    def __init__(self):    
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("planta2.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

#////////////////EL SPRITE DE MARIO ////////////////7
class spritemario(pygame.sprite.Sprite):
    "mario"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("mario.png", IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()

 #/////////////////////IMÁGENES PARA LAS ANIMACIONES DE MARIO///////////////////
 #R = RIGHT, L = LEFT, U = UP, D = DOWN
walkright = [load_image("MarioR1.png", IMG_DIR, alpha=True), load_image("MarioR2.png", IMG_DIR, alpha=True)]
walkleft = [load_image("MarioL1.png", IMG_DIR, alpha=True), load_image("MarioL2.png", IMG_DIR, alpha=True)]
walkfw = [load_image("MarioU1.png", IMG_DIR, alpha=True), load_image("MarioU2.png", IMG_DIR, alpha=True)]
walkbw = [load_image("MarioD1.png", IMG_DIR, alpha=True), load_image("MarioD2.png", IMG_DIR, alpha=True)]
mario = spritemario()

class vidas(pygame.sprite.Sprite):
    "contador de vidas"

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("lives.png", IMG_DIR, alpha=True)


vida1 =  load_image("n1.png", IMG_DIR, alpha=True)
vida2 = load_image("n2.png", IMG_DIR, alpha=True)
vida3 = load_image("n3.png", IMG_DIR, alpha=True)
vida4 = load_image("n4.png", IMG_DIR, alpha=True)
vida5 = load_image("n5.png", IMG_DIR, alpha=True)

#////////////////////////CARGAR LA IMAGEN DE FONDO //////////////////
lvl_bg = load_image("background.png", IMG_DIR, alpha=False)
lvl_bg2 = load_image("background2.png", IMG_DIR, alpha=False)
#////////////////////// CONFIGURACIÓN DE LOS FPS (ver linea 133)///////////////
clock = pygame.time.Clock()

#/////////////////FUNCION PARA ANIMAR A MARIO//////////////////////
def redrawGameWindow():
    global walkcount
    global lvl
    global vida
    global x
    global y

    lvl_bg = load_image("background.png", IMG_DIR, alpha=False)
    lvl_bg2 = load_image("background2.png", IMG_DIR, alpha=False)
    gameover = load_image("gameover.png", IMG_DIR, alpha=False)
    victory = load_image("victory.png", IMG_DIR, alpha=True)
    p_inicio = inicio() 
    next_z = nextzone()
    path = camino()
    lives = vidas()
    roca = pared()
    cannon = catapulta()
    bandera = meta()
    goombaL = goomba()
    plantapiraña = planta()
    #CARGAR EL FONDO DEL NIVEL, LA PLATAFORMA DE INICIO Y EL CAMINO A LA SIGUIENTE ZONA
    

    if lvl == 1:
        screen.blit(lvl_bg,(0,0))
        screen.blit(p_inicio.image,(580,640))
        screen.blit(next_z.image,(580,0))
        screen.blit(roca.image,(540,0))
        screen.blit(roca.image,(540,40))
        screen.blit(roca.image,(620,0))
        screen.blit(roca.image,(620,40))
        
        screen.blit(roca.image,(100,600))
        screen.blit(roca.image,(100,560))
        screen.blit(roca.image,(100,520))
        screen.blit(roca.image,(140,480))
        screen.blit(roca.image,(140,440))
        screen.blit(roca.image,(180,400))
        screen.blit(roca.image,(180,360))
        screen.blit(roca.image,(220,320))
        screen.blit(roca.image,(220,280))
        screen.blit(roca.image,(220,240))
        screen.blit(roca.image,(240,200))
        screen.blit(roca.image,(240,160))
        screen.blit(roca.image,(220,120))
        screen.blit(roca.image,(260,80))
        screen.blit(roca.image,(300,80))
        screen.blit(roca.image,(340,80))
        screen.blit(roca.image,(380,80))
        screen.blit(roca.image,(380,40))
        screen.blit(roca.image,(420,40))
        screen.blit(roca.image,(460,40))
        screen.blit(roca.image,(500,40))

        screen.blit(roca.image,(1100,600))
        screen.blit(roca.image,(1100,560))
        screen.blit(roca.image,(1100,520))
        screen.blit(roca.image,(1060,480))
        screen.blit(roca.image,(1060,440))
        screen.blit(roca.image,(1020,400))
        screen.blit(roca.image,(1020,360))
        screen.blit(roca.image,(980,320))
        screen.blit(roca.image,(980,280))
        screen.blit(roca.image,(980,240))
        screen.blit(roca.image,(940,200))
        screen.blit(roca.image,(940,160))
        screen.blit(roca.image,(980,120))
        screen.blit(roca.image,(940,80))
        screen.blit(roca.image,(900,80))
        screen.blit(roca.image,(860,80))
        screen.blit(roca.image,(820,80))
        screen.blit(roca.image,(820,40))
        screen.blit(roca.image,(780,40))
        screen.blit(roca.image,(740,40))
        screen.blit(roca.image,(700,40))
        screen.blit(roca.image,(660,40))

        screen.blit(plantapiraña.image,(500,500))
        screen.blit(plantapiraña.image,(650,500))
        screen.blit(plantapiraña.image,(940,280))
        screen.blit(plantapiraña.image,(270,280))
        screen.blit(plantapiraña.image,(440,80))
        screen.blit(plantapiraña.image,(760,80))
        screen.blit(goombaL.image,(440,400))

    elif lvl == 2:
        screen.blit(lvl_bg2,(0,0))
        screen.blit(cannon.image, (800,620))
        screen.blit(cannon.image, (70,380))
        screen.blit(bandera.image, (1000,0))
        screen.blit(goombaL.image, (200, 650))
        screen.blit(goombaL.image, (900, 400))
        screen.blit(goombaL.image, (400, 350))
        screen.blit(goombaL.image, (200, 120))
        screen.blit(goombaL.image, (900, 50))
        screen.blit(goombaL.image, (1000, 600))

        screen.blit(plantapiraña.image,(440,80))
        screen.blit(plantapiraña.image,(600,400))

        screen.blit(path.image, (790, 480))
        screen.blit(path.image, (790, 520))
        screen.blit(path.image, (790, 560))

        screen.blit(path.image, (69, 170))
        screen.blit(path.image, (69, 210))
        screen.blit(path.image, (69, 250))
        screen.blit(path.image, (69, 290))


        #detección del precipicio 1
        if volando is False:
            if x >= 0 and x <= 770:
                if y >= 460 and y <= 560:
                    x = 585
                    y = 640
                    vida -= 1
        if volando is False:
            if x >= 820 and x <= 1200:
                if y >= 460 and y <= 560:
                    x = 585
                    y = 640
                    vida -= 1

        #detección del precipicio 2
        if volando is False:
            if x >= 0 and x <= 46:
                if y >= 160 and y <= 296:
                    x = 585
                    y = 640
                    vida -= 1
        if volando is False:
            if x >= 104 and x <= 1200:
                if y >= 160 and y <= 296:
                    x = 585
                    y = 640
                    vida -= 1

        

        #mensaje de victoria
        if lvl == 2:
            if x >= 1005 and x <= 1200:
                if y >= 110 and y <= 140:
                    screen.blit(victory, (0,0))

        if vida == 0:
            screen.blit(gameover, (0,0))
            if vida == -1:
                vida = 5
        
        
    screen.blit(lives.image, (0,0))
    

    if vida == 5:
        screen.blit(vida5, (120,42))
    elif vida == 4:
        screen.blit(vida4, (120,42))
    elif vida == 3:
        screen.blit(vida3, (120,42))
    elif vida ==2:
        screen.blit(vida2, (120,42))
    elif vida == 1:
        screen.blit(vida1, (120,42))

    if walkcount + 1 >= 2:
        walkcount = 0
    #/////////////DIRECCIONES/////////////////
    if left:  
        screen.blit(walkleft[walkcount//100], (x,y))
        walkcount += 1                          
    elif right:
        screen.blit(walkright[walkcount//100], (x,y))
        walkcount += 1
    elif up:
        screen.blit(walkfw[walkcount//100], (x,y))
        walkcount += 1   
    elif down:
        screen.blit(walkbw[walkcount//100], (x,y))
        walkcount += 1   
    else:
        screen.blit(mario.image, (x, y))
        walkcount = 0
    
    if vida == 0:
            screen.blit(gameover, (0,0))
            if vida == -1:
                vida = 5

    #/////////////ACTUALIZAR PANTALLA//////////////
    pygame.display.update() 





#/////////////FUNCION PRINCIPAL DEL JUEGO////////////////
def main():
    global x
    global y 
    global vel
    global left
    global right
    global up
    global down
    global walkcount
    global lvl
    global vida
    
   ##############LINEA 133, FPS///////////////
    clock.tick(60)

    while True:
        
        #///////////////////BUCLE QUE COMPRUEBA LA SALIDA/////////////
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #/////////////////////COMANDOS DE LAS TECLAS/////////////////
        keys = pygame.key.get_pressed()

        #/////////FLECHA A LA IZQUIERDA//////////////
        if keys[pygame.K_LEFT]: 
            x -= vel
            left = True
            right = False
        
        #//////////////FLECHA A LA DERECHA//////////////
        elif keys[pygame.K_RIGHT]: 
            x += vel
            left = False
            right = True
        
        #/////////////ARRIBA//////////////////
        elif keys[pygame.K_UP]: 
            y -= vel
            up = True
            down = False

        #////////////ABAJO///////////////
        elif keys[pygame.K_DOWN]: 
            y += vel
            up = False
            down = True

        #///////////EN CASO DE QUE MARIO SE QUEDE QUIETO/////////
        else: 
            left = False
            right = False
            walkcount = 0

        #para pasar al 2do nivel
        if x >= 580 and x <= 590:
            if y >= 0 and y <= 10:
                lvl = 2
                x = 585
                y= 640
        
        print(x,y)
        #//////////LA FUNCIÓN PARA ANIMAR A MARIO////////////
        redrawGameWindow()

#/////////////////LLAMAR A LA FUNCIÓN PRINCIPAL////////////////
if __name__ == "__main__":
    main()