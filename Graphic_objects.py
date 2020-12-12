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
    def __init__(self, width, height, left, top, text):
        "Cздание кнопки правил"

        self.width=width
        self.height=height

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

        self.text=text

    def draw(self,pause):
        self.image.fill(DIMGREY)
        if not pause:
            draw_text(self.image, self.text, int(self.height*0.7),0*self.width//2,0*self.height//2)

    def update(self, event=0):
        if not event:
            return False
        if event.type==pygame.MOUSEBUTTONUP:
            x=event.pos[0]
            y=event.pos[1]
            if x>=self.rect.left and x<=self.rect.left+self.width \
                and y>=self.rect.top and y<=self.rect.top+self.height:
                return True
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
        draw_pole(self.image, self.size, self.cell,CADETBLUE, DIMGREY, self.rect.left*0, self.rect.top*0, self.cell//2)
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
def draw_text(surf, text, size, x1, y1, midtop=False):
    #текст
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    if midtop:
        text_rect.midtop = (x1,y1)
    else:
        text_rect.left = x1
        text_rect.top = y1
    surf.blit(text_surface, text_rect)

def draw_background(surf, WIDTH, HEIGHT, size, CELL_SIZE,LEFT,TOP,pause=False):
    color1=DARKGREY
    color2=DIMGREY
    if WIDTH>HEIGHT:
        draw_pole(surf, WIDTH//CELL_SIZE*2, 2*CELL_SIZE, color1, color2, 0, HEIGHT - WIDTH, CELL_SIZE)
    else:
        draw_pole(surf, HEIGHT // CELL_SIZE*2, 2 * CELL_SIZE, color1, color2, 0, WIDTH-HEIGHT, 5*CELL_SIZE/6)
    if not pause:
        draw_pole(surf, size, CELL_SIZE, RED, DARKGREY, LEFT, TOP, CELL_SIZE//2)

def all_draw(all_sprites,screen,Play_window,bottons,pause,Clocks):
    #отрисовка
    all_sprites.update()
    for botton in bottons:
        botton.draw(pause)
    Play_window.draw_score(screen)
    Play_window.draw_field()
    Play_window.fall()
    all_sprites.draw(screen)
    Clocks.draw(screen)
    #pygame.display.flip()

def draw_rules(surf, WIDTH, HEIGHT):
    size=HEIGHT//20
    left=WIDTH//20
    draw_text(surf, "ПРАВИЛА", size, left*10, 0, True)
    draw_text(surf,"Передвигайте фишки, чтобы собрать линию",int(size*0.8),left,size)
    draw_text(surf, "из фишек одного цвета.(необязательно прямую)",int(size * 0.8), left,3 * size)
    beautiful_draw(surf, left * 11, size * 3, size * 2, GREEN, False)
    beautiful_draw(surf, left * 12, size * 3, size * 2, GREEN, True)
    beautiful_draw(surf, left * 12, size * 3-left, size * 2, GREEN, False)
    beautiful_draw(surf, left * 13, size * 3-left, size * 2, GREEN, True)
    beautiful_draw(surf, left * 14, size * 3 - left, size * 2, GREEN, True)
    draw_text(surf, "Очки даются только за фишки с кристаллом и звезды", int(size*0.8), left, 6*size)
    beautiful_draw(surf, left * 12, size * 5, size * 3, RED, False)
    beautiful_draw(surf, left * 14, size * 5, size * 3, RED, True)
    draw_text(surf, "Фишки с динамитом взрывают вокруг себя область 5 на 5 ", int(size*0.8), left, 9*size)
    beautiful_draw(surf, left * 13, size * 8, size * 3, ORANGE, False, False, 1)
    draw_text(surf, "Фишки с молниями уничтожают линии крестом.(свою строку и столбец)", int(size*0.8), left, 12*size)
    beautiful_draw(surf, left * 16, size * 11, size * 3, PURPLE, False, False, 2)
    draw_text(surf, "Звезда имеет одновременно все цвета", int(size*0.8), left, 15*size)
    beautiful_draw(surf, left * 9, size * 14, size * 3, RED, False, True)
    draw_text(surf, "Пpиятной игры!", int(size*0.8), left, 18*size)

def draw_pause(surf, WIDTH, HEIGHT):
    draw_text(surf, "PAUSE", HEIGHT // 2, WIDTH // 2, HEIGHT // 4, True)
    draw_text(surf, "Для продолжения кликните мышкой", HEIGHT//10,WIDTH//2, HEIGHT//4*3,True )

def draw_finish(surf, WIDTH, HEIGHT, victory):
    if victory:
        draw_text(surf, "VICTORY!!!", HEIGHT // 4, WIDTH // 2, HEIGHT // 4, True)
    else:
        draw_text(surf, "GAME OVER:(", HEIGHT // 4, WIDTH // 2, HEIGHT // 4, True)