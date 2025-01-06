Kodland Game Project

Es un juego topdown del tipo arcade el cual consiste en controlar una nave y disparar a los asterides que apareceran desde los bordes sin dejar que los mismos destrullan la nave.

Los controles son W, A, S, D para maniobrar la nave y se usa el cursor del mouse para apuntar. La nave rotara en la posicion del cursor y haciendo clic izquierdo se dispara. Le juego finaliza si un asteroide impacta la nave

-Estructura:

El juego consta de:

-Menu principal:

![image_2025-01-06_100930246](https://github.com/user-attachments/assets/4916aae5-3e79-4c4c-8cc6-8e3a6f1e3d45)

Desde el menu principal se podra iniciar el juego o salir del mismo y cerra la ventana. (El boton opciones funciona, pero queda pendiente la creacion de dicho menu)

-Juego:

![image_2025-01-06_101112391](https://github.com/user-attachments/assets/374f9f9f-63d5-43b1-9d21-020ad09c50d2)

La ventana de juego cuenta con la nave, el fondo los asteroides y el puntaje en la parte superoir derecha.

-Pausa:

![image_2025-01-06_101205408](https://github.com/user-attachments/assets/4d4e9f78-a59f-44b1-a23f-ef109b408e0f)

El juego se puede pausar haciendo oprimiendo la tecla ESCAPE y se podra retornar el juego dando clic sobre el boton REINICIAR. Adicional se podra regresar al menu principal o salir del juego y se cierre la ventana.

-Game over

![image_2025-01-06_101418391](https://github.com/user-attachments/assets/83b0b49e-47cd-4551-8b31-23c9d7552893)

Una vez el jugador sea golpeado por un asteroide el  juego termina y aparecera un menu con el cual se podra regresar al menu principal, reiniciar el juego o salir y cerrar la venta.

Estructura interna:

El juego se ejecuta desde el archivo main.py en dicho archivo se agrego la siguiente linea de codigo para asegurarnos de que no se ejecute otro archivo por error:

    if __name__ == '__main__':
        pygame.init()
        main_menu()

Con esto nos aseguramos del que se inicie correctamente pygame y se ejecute el menu principal.

El archivo main.py se encargar de llamar los loops para el menu principal, el juego y los demas menus.

-Clases:

El juego tiene las siguientes clases principales:

-Player:

Desde esta clase se llamen los atributos necesarios para dibujar la nave, asi como sus colisiones, sistema de disparo, movimiento y rotacion. La clase recive como parametros la pocision inicial para que aparezca en pantalla.

-Asteroid:

Al igual que Player, asteroide tiene los atributos para dibujar los sprites en pantalla, ademas desde el constructor se define la posicion aleatorea del cual es asteroide aparecera. Dicha posicion corresponde a cualquier punto del borde la pantalla y se movera en una direccion aleatorea en linea recta hacia el interori, destruyendose si llega al otro extremo de la pantalla sin que el jugador le alla dado.

    side : str = random.choice(['top', 'bottom', 'left', 'right'])

-Bullet:

Es la muncion de la nave, recibe como parametros la pocion del centro del sprite de la nave y el angulo al que la nave esta apuntando, asi cuando la bala spawnee se movera en dicha direccion.

    self.velocity_x = math.cos(self.angle * (2*math.pi/360)) * self.speed
    self.velocity_y = math.sin(self.angle * (2*math.pi/360)) * self.speed

-Button

Esta clase dibuja el fondo y el texto de los botones de la interfaz y se hace uso de la siguiente funcion para determinar que el cursos esta sobre el:

     def check_input(self, position)->bool

-Game

Es la clase encarda de spawnear el jugadro, los asteroides y llevar el puntaje. Ademas de manejar el sistema de colisiones el cual se logra distribuyendo en grupos los sprites que aparecen en pantalla:

    self.bullet_group = pygame.sprite.Group()
    self.asteroid_group = pygame.sprite.Group()
    self.player_group = pygame.sprite.GroupSingle()

Estos grupos se usan para determinar si un sprite esta colisionando con otro grupo de esa forma se determina, por ejemplo, si una bala golpea un asteroide:


    for bullet in self.bullet_group:
        bullet_hit = pygame.sprite.spritecollide(bullet, self.asteroid_group, False, pygame.sprite.collide_mask)
        for hit in bullet_hit:
            pygame.mixer.Sound.play(self.a_sound)
            self.score += 1
            bullet_hit.remove(hit)
            hit.kill()
            bullet.kill()

Adicionalmente los sprites se ponen un un grupo global el cual se usa para llamar las funciones draw y updte para dibujar en pantalla los elementos sin tener que hacerlo manualemnte a cada uno:

    self.global_sprites.draw(self.screen)
    self.global_sprites.update()
  



