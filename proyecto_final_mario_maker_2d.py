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
vel = 4
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
    lvl_bg = load_image("background.png", IMG_DIR, alpha=False)
    lvl_bg2 = load_image("background2.png", IMG_DIR, alpha=False)
    p_inicio = inicio() 
    next_z = nextzone()
    lives = vidas()
    #CARGAR EL FONDO DEL NIVEL, LA PLATAFORMA DE INICIO Y EL CAMINO A LA SIGUIENTE ZONA
    
    #si la variable lvl es 1 se muestra el nivel 1, si es 2 se muestra el nivel 2
    #ver linea 204
    if lvl == 1:
        screen.blit(lvl_bg,(0,0))
        screen.blit(p_inicio.image,(580,640))
        screen.blit(next_z.image,(580,0))
    elif lvl == 2:
        screen.blit(lvl_bg2,(0,0))
    
    
    screen.blit(lives.image, (0,0))
    screen.blit(vida5, (120,42))

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
        
        #esto es una idea que tuve, cuando la posición de mario sea la posición de la wea que indica el camino a la nueva zona
        #la variable lvl cambia a 2 y pasa al segundo nivel
        #eso es en teoría, en la practica no se por qué no funciona
        #ver linea 110

        #para pasar al 2do nivel
        if x >= 580 and x <= 590:
            if y >= 42 and y <= 46:
                lvl = 2
        print(x,y)
        #//////////LA FUNCIÓN PARA ANIMAR A MARIO////////////
        redrawGameWindow()

#/////////////////LLAMAR A LA FUNCIÓN PRINCIPAL////////////////
if __name__ == "__main__":
    main()