from Physical_objects import *
from Colors import *
from draw import *
from sounds import *
#from pravila import*

clock = pygame.time.Clock()

class Window_0(pygame.sprite.Sprite):
    def __init__(self):
        WIDTH = CELL_SIZE * Field_size
        HEIGHT = CELL_SIZE * Field_size

        self.width=WIDTH
        self.height=HEIGHT

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (700, 700))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

    def update(self):
        pass
        

class button(pygame.sprite.Sprite):
    def __init__(self, width, height, left, top):
        "Cздание кнопки правил"

        self.width=width
        self.height=height

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

    def update(self, event=0):
        if not event:
            return False




class Window(pygame.sprite.Sprite):
    def __init__(self, size, Field_size, CELL_SIZE, left, top):
        "Cздание игрового поля"
        WIDTH = CELL_SIZE * Field_size
        HEIGHT = CELL_SIZE * Field_size

        self.width=WIDTH
        self.height=HEIGHT

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

        self.touch_number=0
        self.touch_square=(-1,-1)

        self.size=Field_size
        self.cell=CELL_SIZE
        self.field=Field(size,CELL_SIZE,CELL_SIZE)

        self.draw_field()

        self.comatose=False


    def draw_field(self,):
        #Нарисовать поле
        draw_pole(self.image, self.size, self.cell,CADETBLUE, DIMGREY, self.rect.left*0, self.rect.top*0, 30)
        draw_pole_without_border(self.image, 1, self.cell, LIMEGREEN, DIMGREY, (self.touch_square[0]-1) * self.cell,
                                                                         (self.touch_square[1]-1) * self.cell, 30)
        for i in range(self.size+2):
            for j in range(self.size+2):
                self.draw_chip((i,j))


    def draw_chip(self, coords):
        #Нарисовать фишку

        self.field.massive[coords[0]][coords[1]].draw(self.image)


    def fill_square(self,coords,color):
        #Закрасить выбранный квадратик

        i=coords[0]
        j=coords[1]
        pygame.draw.rect(self.image, color,
                         ((i - 1) * self.cell, (j - 1) * self.cell, self.cell, self.cell))


    def search_the_square (self, event):
        #нахождеие области, куда попала мышка

        mp = event.pos
        x0=mp[0]-self.rect.left
        y0=mp[1]-self.rect.top

        for i in range(self.size + 1):
            if (i * self.cell - x0) // self.cell == 0:
                for j in range(self.size + 1):
                    if (j * self.cell - y0) // self.cell == 0:
                        return (i,j)


    def swap(self,coords1,coords2):
        #махнуть местами фишки

        self.field.swap(coords1,coords2)

        #move_sound.play()
        self.draw_chip(coords1)
        self.draw_chip(coords2)


    def draw_score(self,screen):
        # очки за выполнения действия
        draw_text(screen, str(self.field.score), 50, 50, 20)


    def fall(self):
        #падение фишек после уничтожения рядов
        if not self.comatose:
            return

        if self.field.update():
            self.draw_field()
            clock.tick(6)
        else:

            self.comatose=False
            self.field.create_balls()
            self.draw_field()
            if self.field.check():
                self.comatose=True


    def update (self, event=0):
        #Обработка тычка мыши

        if self.comatose or event==0:
            return
        self.touch_number+=1

        if self.touch_number==2:
            self.touch_number=0

            coords1=self.touch_square
            coords2=self.search_the_square(event)
            self.fill_square(coords1, WHITE)
            self.touch_square=(-1,-1)

            if abs(coords1[0]-coords2[0])+abs(coords1[1]-coords2[1])==1:
                self.swap(coords1, coords2)
                f1=f2=False
                if not self.field.walk_the_line(coords1):
                    f1=True
                if not self.field.walk_the_line(coords2):
                    f2=True
                if f1 and f2:
                    no_sound.play()
                    self.swap(coords1, coords2)
                else:
                    move_sound.play()
                    self.comatose=True
                    fall_sound.play()
            else:
                no_sound.play()
                self.draw_chip(coords1)

        else:

            self.touch_square=self.search_the_square(event)
            if self.touch_square==None:
                self.touch_square=(-1,-1)
                self.touch_number=0
                return
            self.color = WHITE
            flag=(event.type == pygame.MOUSEBUTTONUP)
            if flag:
                flag=False
                self.fill_square(self.touch_square,BLACK)



font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x1, y1):
    #текст
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x1, y1)
    surf.blit(text_surface, text_rect)

def draw_background(surf, WIDTH, HEIGHT, size, CELL_SIZE,LEFT,TOP):
    color1=DARKGREY
    color2=DIMGREY
    if WIDTH>HEIGHT:
        draw_pole(surf, WIDTH//CELL_SIZE, 2*CELL_SIZE, color1, color2, 0, HEIGHT - WIDTH, 60)
    else:
        draw_pole(surf, HEIGHT // CELL_SIZE, 2 * CELL_SIZE, color1, color2, 0, WIDTH-HEIGHT, 50)
    draw_pole(surf, size, CELL_SIZE, RED, DARKGREY, LEFT, TOP, 30)

def all_draw(all_sprites,screen,s):
    #отрисовка
    all_sprites.update()
    screen.fill(WHITE)
    s.draw_score(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
