from random import randint
from scripts.rendering import (kayacatshape1, kayacatshape2, kayacatshape3, kayacatColors, fish_image)

OwnedDictionary = {
    'hat1': True,
    'hat2': False,
    'hat3': False,
    'food1': True,
    'food2': False,
    'food3': False,
    'color1': True,
    'color2': False,
    'color3': False
}

def gfd(food_image):
    if food_image == fish_image[0]:
        return randint(1, 5)
    elif food_image == fish_image[1]:
        return randint(20, 50)
    elif food_image == fish_image[2]:
        return randint(30, 100)

ColorsAndImagesDictionary = {
    kayacatshape1[0] : kayacatColors[0:3],
    kayacatshape2[1] : kayacatColors[3:6],
    kayacatshape3[2] : kayacatColors[6:10]
 }
