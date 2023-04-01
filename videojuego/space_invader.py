import pygame
import random
import math

# Inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))


# Titulo e ícono
pygame.display.set_caption("Space Invader")
# Aqui va el icono de Flaticon
icono = pygame.image.load("imagen en carpeta")
pygame.display.set_icon(icono)
fondo = pygame.image.load("imagen de fondo")


# jugador
img_jugador = pygame.image.load("imagen del cohete")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("imagen del enemigo"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# bala
img_bala = pygame.image.load("imagen de la bala")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

# puntaje
puntaje = 0


# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# funcion disparar 
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Funcion para detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False



# Loop del juego
se_ejecuta = True

while se_ejecuta:

    # img
    pantalla.blit(fondo, (0,0))

    # iterar eventos
    for evento in pygame.event.get():

        # Cerrar el programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                if not bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # ubicacion del jugador
    jugador_x += jugador_x_cambio

    # mantener dentro de los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x <= 736:
        jugador_x = 736

     # ubicacion del enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

    # mantener dentro de los bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] <= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]

          # colision
        colicion = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colicion:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        
        enemigo(enemigo_x[e], enemigo_y[e], e)


    # movimiento bala
    if bala_y <= -64:
        bala_y == 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

  


    jugador(jugador_x, jugador_y)

    # actualizar
    pygame.display.update()