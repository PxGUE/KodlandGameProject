Kodland Game Project

Es un juego topdown del tipo árcade, el cual consiste en controlar una nave y disparar a los asteroides que aparecerán desde los bordes sin dejar que los mismos destruyan la nave.

Los controles son W, A, S, D para maniobrar la nave y se usa el cursor del mouse para apuntar. La nave rotará en la posición del cursor y haciendo clic izquierdo se dispara. Le juego finaliza si un asteroide impacta la nave.

-Estructura:

El juego consta de:

-Menú principal:

![image_2025-01-06_100930246](https://github.com/user-attachments/assets/4916aae5-3e79-4c4c-8cc6-8e3a6f1e3d45)

Desde el menú principal se podrá iniciar el juego o salir del mismo y cerra la ventana. (El botón opciones funciona, pero queda pendiente la creación de dicho menú).

-Juego:

![image_2025-01-06_101112391](https://github.com/user-attachments/assets/374f9f9f-63d5-43b1-9d21-020ad09c50d2)

La ventana de juego cuenta con la nave, el fondo, los asteroides y el puntaje en la parte superior derecha.

-Pausa:

![image_2025-01-06_101205408](https://github.com/user-attachments/assets/4d4e9f78-a59f-44b1-a23f-ef109b408e0f)

El juego se puede pausar haciendo oprimiendo la tecla ESCAPE y se podrá retornar el juego dando clic sobre el botón REINICIAR. Adicional se podrá regresar al menú principal o salir del juego y se cierre la ventana.

-Game over

![image_2025-01-06_101418391](https://github.com/user-attachments/assets/83b0b49e-47cd-4551-8b31-23c9d7552893)

Una vez el jugador sea golpeado por un asteroide, el  juego termina y aparecerá un menú con el cual se podrá regresar al menú principal, reiniciar el juego o salir y cerrar la venta.

Estructura interna:

El juego se ejecuta desde el archivo main.py en dicho archivo se agregó la siguiente línea de código para asegurarnos de que no se ejecute otro archivo por error:

    if __name__ == '__main__':
        pygame.init()
        main_menu()

Con esto nos aseguramos del que se inicie correctamente pygame y se ejecute el menú principal.

El archivo main.py se encargará de llamar los loops para el menú principal, el juego y los demás menús.

-Clases:

El juego tiene las siguientes clases principales:

-Player:

Desde esta clase se llaman los atributos necesarios para dibujar la nave, así como sus colisiones, sistema de disparo, movimiento y rotación. La clase recibe como parámetros la posición inicial para que aparezca en pantalla.

-Asteroid:

Al igual que Player, asteroide tiene los atributos para dibujar los sprites en pantalla, además desde el constructor se define la posición aleatoria del cual es asteroide aparecerá. Dicha posición corresponde a cualquier punto del borde la pantalla y se moverá en una dirección aleatoria en línea recta hacia el interior, destruyéndose si llega al otro extremo de la pantalla sin que el jugador le haya dado.

    side : str = random.choice(['top', 'bottom', 'left', 'right'])

-Bullet:

Es la munición de la nave, recibe como parámetros la poción del centro del sprite de la nave y el ángulo al que la nave está apuntando, así cuando la bala spawnee se moverá en dicha dirección.

    self.velocity_x = math.cos(self.angle * (2*math.pi/360)) * self.speed
    self.velocity_y = math.sin(self.angle * (2*math.pi/360)) * self.speed

Además, se comprueba si el cursor toca el botón haciendo uso de la siguiente función:

     def check_input(self, position)->bool

-Game

Es la clase encargada de spawnear el jugador, los asteroides y llevar el puntaje. Además de manejar el sistema de colisiones, el cual se logra distribuyendo en grupos los sprites que aparecen en pantalla:

    self.bullet_group = pygame.sprite.Group()
    self.asteroid_group = pygame.sprite.Group()
    self.player_group = pygame.sprite.GroupSingle()

Estos grupos se usan para determinar si un sprite está colisionando con otro grupo, de esa forma, se determina, por ejemplo, si una bala golpea un asteroide:


    for bullet in self.bullet_group:
        bullet_hit = pygame.sprite.spritecollide(bullet, self.asteroid_group, False, pygame.sprite.collide_mask)
        for hit in bullet_hit:
            pygame.mixer.Sound.play(self.a_sound)
            self.score += 1
            bullet_hit.remove(hit)
            hit.kill()
            bullet.kill()

Adicionalmente, los sprites se ponen en un grupo global, el cual se usa para llamar las funciones draw y update para dibujar en pantalla los elementos sin tener que hacerlo manualmente a cada uno:

    self.global_sprites.draw(self.screen)
    self.global_sprites.update()
  
Por ultimo hay dos archivos importantes que se usan para facilitar el llamado de assets y configurar algunas propiedades:

-lib.py

![image_2025-01-06_103152366](https://github.com/user-attachments/assets/18b3da87-e029-4135-8b92-ff33fd305a5a)

Desde este archivo se llaman las rutas a los archivos usados en el juego, sprites, sonidos y fuentes.

-settings.py

![image_2025-01-06_103246225](https://github.com/user-attachments/assets/b8b53906-2a78-482f-83eb-2882af5588a0)

Desde acá se pueden configurar diferentes aspectos del juego como el tamaño de pantalla, la velocidad de las balas, la escala de la nave, su velocidad, entre otros.

ASSETS:

Todos los assets usados para este proyecto son de uso libre.




