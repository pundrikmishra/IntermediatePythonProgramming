import pygame
import random
from blob import Blob
import numpy as np

STARTING_BLUE_BLOBS =20
STARTING_RED_BLOBS = 20
STARTING_GREEN_BLOBS = 10
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

class BlueBlob(Blob):
    # pass
    # def __init__(self, color, x_boundary, y_boundary, size_range=(4,8), movement_range=( -1,2)):
    #     super().__init__(color, x_boundary, y_boundary, size_range=size_range, movement_range=movement_range)
    def __init__(self, color, x_boundary, y_boundary):
        # super().__init__(color, x_boundary, y_boundary)
        Blob.__init__(self,(0,0,255),x_boundary, y_boundary)
        # self.color = BLUE

    # def move_fast(self):
    #     self.x +=random.randrange(-10,10)
    #     self.y +=random.randrange(-10,10)


# class RedBlob(Blob):
#         def __init__(self, color, x_boundary, y_boundary):
#             # super().__init__(color, x_boundary, y_boundary)
#             Blob.__init__(self,(255,0,0),x_boundary, y_boundary)

class RedBlob(Blob):
        def __init__(self,x_boundary, y_boundary):
            # super().__init__(color, x_boundary, y_boundary)
            Blob.__init__(self,(255,0,0),x_boundary, y_boundary)


class GreenBlob(Blob):
        def __init__(self, color, x_boundary, y_boundary):
            # super().__init__(color, x_boundary, y_boundary)
            Blob.__init__(self,(0,255,0),x_boundary, y_boundary)

        def __add__(self, other_blob):
            if other_blob.color == (255,0,0):
                self.size -= other_blob.size
                other_blob.size -= self.size
            elif other_blob.color == (0,0,255):
                self.size += other_blob.size
                other_blob.size = 0
            elif other_blob.color == (0,255,0):
                pass
            else:
                raise Exception('Tried to one or multiple blobs of unsupported colors.')

def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y]) - np.array([b2.x, b2.y])) < (b1.size + b2.size)
  
def handle_collisions(blob_list):
    blues, reds, greens = blob_list
    for green_id, green_blob, in greens.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id , other_blob in other_blobs.copy().items():
                if green_blob == other_blob:
                    pass
                else:
                    if is_touching(green_blob, other_blob):
                        green_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if green_blob.size <= 0:
                            del blues[green_id]
    return blues, reds, greens

def draw_environment(blob_list):
    blues, reds, greens  = handle_collisions(blob_list)
    game_display.fill(WHITE)
    blues, reds, greens  = handle_collisions(blob_list)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            # blob.move_fast()
            blob.move()
            blob.check_bounds()
    pygame.display.update()
    return blues, reds, greens
    # blob.move()

def main():
    # red_blob = Blob(RED)
    # blue_blobs = [Blob(BLUE) for i in range(STARTING_BLUE_BLOBS)]
    blue_blobs = dict(enumerate([BlueBlob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    # red_blobs = dict(enumerate([RedBlob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(GREEN,WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    # print(blue_blobs)


    # print('Blue blob size: {} red blob size: {}'.format(green_blobs[0].size), red_blobs[0].size)
    # green_blobs[0] + red_blobs[0]
    # print('Blue blob size: {} red blob size: {}'.format(green_blobs[0].size), red_blobs[0].size)




    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT():
        #         pygame.quit()
        #         quit()
        # draw_environment(red_blob)
        blue_blobs,red_blobs,green_blobs =draw_environment([blue_blobs,red_blobs,green_blobs])
        clock.tick(60)
        # print(red_blob.x, red_blob.y)

if __name__ == '__main__':
    main()