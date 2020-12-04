
from Physical_objects import *
from Colors import *
from draw import *

clock = pygame.time.Clock()

class Window(pygame.sprite.Sprite):
    def __init__(self, size, Field_size, CELL_SIZE, move_sound, left, top):
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

        self.move_sound=move_sound

        for i in range(Field_size):
            pygame.draw.line(self.image,BLACK, (i*CELL_SIZE,0) , (i*CELL_SIZE,HEIGHT))
            pygame.draw.line(self.image,BLACK, (0,i*CELL_SIZE) ,(WIDTH ,i*CELL_SIZE))

        self.draw_field()

        self.comatose=False

    def draw_field(self):
        #Нарисовать поле

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

        self.field.massive[coords1[0]][coords1[1]].color,self.field.massive[coords2[0]][coords2[1]].color = \
            self.field.massive[coords2[0]][coords2[1]].color,self.field.massive[coords1[0]][coords1[1]].color
        self.move_sound.play()
        self.draw_chip(coords1)
        self.draw_chip(coords2)


    def draw_score(self,screen):
        draw_text(screen, str(self.field.score), 50, 20, 20)


    def fall(self):
        if not self.comatose:
            return

        if self.field.update():
            self.draw_field()
            clock.tick(3)
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

            if abs(coords1[0]-coords2[0])+abs(coords1[1]-coords2[1])<=1:
                self.swap(coords1, coords2)
                if not self.field.walk_the_line(coords1) and not self.field.walk_the_line(coords2):
                    self.swap(coords1, coords2)

                self.comatose=True


            else:
                self.draw_chip(coords1)

        else:

            self.touch_square=self.search_the_square(event)
            self.color = WHITE
            flag=(event.type == pygame.MOUSEBUTTONUP)
            if flag:
                flag=False
                self.fill_square(self.touch_square,BLACK)

        for i in range(self.size):
            pygame.draw.line(self.image,BLACK, (i*self.cell,0) , (i*self.cell,self.height))
            pygame.draw.line(self.image,BLACK, (0,i*self.cell) ,(self.width ,i*self.cell))


font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x1, y1):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x1, y1)
    surf.blit(text_surface, text_rect)

def all_draw(all_sprites,screen,s):
    all_sprites.update()
    screen.fill(WHITE)
    s.draw_score(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
