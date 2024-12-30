import os
import sys

if getattr(sys, 'frozen', False):
    PATH = os.path.join(sys._MEIPASS)
else:
    PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

icon_path = os.path.join(PATH, 'materials', 'icon.png')
background = os.path.join(PATH, 'materials', 'background.jpg')
kayamusic_path = os.path.join(PATH, 'materials', 'kayamusic.wav')
nom_sound_path = os.path.join(PATH, 'materials', 'nom.wav')
miau_sound_path = os.path.join(PATH, 'materials', 'miau.wav')
tbell_sound_path = os.path.join(PATH, 'materials', 'tbell.wav')
click_sound_path = os.path.join(PATH, 'materials', 'cuteclick.wav')
soundoff_path = os.path.join(PATH, 'materials', 'soundoff.wav')
tryagain_path = os.path.join(PATH, 'materials', 'wrongpong.wav')

kayacateye1_path = os.path.join(PATH, 'materials', 'kayacateye1.png')
kayacateye2_path = os.path.join(PATH, 'materials', 'kayacateye2.png')
kayacateye3_path = os.path.join(PATH, 'materials', 'kayacateye3.png')
kayacateye4_path = os.path.join(PATH, 'materials', 'kayacateye4.png')

kayacatopenmouth_path = os.path.join(PATH, 'materials', 'kayacatopenmouth.png')

kayacatshape1 = os.path.join(PATH, 'materials', 'kayacatshape1.png')
kayacatshape2 = os.path.join(PATH, 'materials', 'kayacatshape2.png')
kayacatshape3 = os.path.join(PATH, 'materials', 'kayacatshape3.png')

kayacatcolor1_1 = os.path.join(PATH, 'materials', 'kayacatcolor1_1.png')
kayacatcolor1_2 = os.path.join(PATH, 'materials', 'kayacatcolor1_2.png')
kayacatcolor1_3 = os.path.join(PATH, 'materials', 'kayacatcolor1_3.png')

kayacatcolor2_1 = os.path.join(PATH, 'materials', 'kayacatcolor2_1.png')
kayacatcolor2_2 = os.path.join(PATH, 'materials', 'kayacatcolor2_2.png')
kayacatcolor2_3 = os.path.join(PATH, 'materials', 'kayacatcolor2_3.png')

kayacatcolor3_1 = os.path.join(PATH, 'materials', 'kayacatcolor3_1.png')
kayacatcolor3_2 = os.path.join(PATH, 'materials', 'kayacatcolor3_2.png')
kayacatcolor3_3 = os.path.join(PATH, 'materials', 'kayacatcolor3_3.png')

title_image_path_1 = os.path.join(PATH, 'materials', 'title.png')
title_image_path_2 = os.path.join(PATH, 'materials', 'secret.png')

music_image_path_1 = os.path.join(PATH, 'materials', 'musicon.png')
music_image_path_2 = os.path.join(PATH, 'materials', 'nomusic.png')

fish_image_path = os.path.join(PATH, 'materials', 'fish.png')
fish_image_path2 = os.path.join(PATH, 'materials', 'fish2.png')
fish_image_path3 = os.path.join(PATH, 'materials', 'fish3.png')
eyes_gif_path = os.path.join(PATH, 'materials', 'kayacateye3.gif')

shopButton = os.path.join(PATH, 'materials', 'shopbutton.png')
shopButtonClicked = os.path.join(PATH, 'materials', 'shopbuttonclicked.png')
shopWindow = os.path.join(PATH, 'materials', 'shoppg1.png')
lockedImg = os.path.join(PATH, 'materials', 'locked2.png')
meownies = os.path.join(PATH, 'materials', 'meownies.png')