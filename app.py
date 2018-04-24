import pygame
 
class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        self._VELOCITY = 10

        self._x = 30
        self._y = 30
        self._x_velocity = 0
        self._y_velocity = 0
 
    def init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._clock = pygame.time.Clock()
        self._running = True
 
    def process_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        self._x_velocity = 0
        self._y_velocity = 0

        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]: self._y_velocity = - self._VELOCITY
        if pressed[pygame.K_DOWN]: self._y_velocity = self._VELOCITY
        if pressed[pygame.K_LEFT]: self._x_velocity = - self._VELOCITY
        if pressed[pygame.K_RIGHT]: self._x_velocity = self._VELOCITY

    def do_actions(self):
        self._x += self._x_velocity
        self._y += self._y_velocity

    def draw(self):
        self._display_surf.fill((0, 0, 0))
        pygame.draw.ellipse(self._display_surf, (255, 200, 0), pygame.Rect(self._x, self._y, 60, 500))
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
 
    def run(self):
        if self.init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.process_event(event)

            self.do_actions()

            self.draw()

            self._clock.tick(60)
        self.cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.run()