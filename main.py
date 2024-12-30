import pygame
import sys
import time

from scripts.constants import *
from scripts.sounds import *
from scripts.dictionary_path import *
from scripts.rendering import *
from scripts.dictionary_images import *
from scripts.scoreboard import *
from scripts.hitbox import *
from scripts.title import *
from scripts.secretsound import *
from scripts.kayacat import *
from scripts.food import *
from scripts.shop import *
from scripts.equipLogic import shop_items
from scripts.sprites_init import *
from scripts.var_classes import *

def main():
    shopWindowOpen = False
    musicBox = False
    clock = pygame.time.Clock()
    start_time = time.time()
    frame_meow_interval = 20
    numberOfPresses = 0
    hitboxx = pygame.Rect(200, 380, 150, 150)
    food_reset_position = (235, 135)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if food.rect.collidepoint(event.pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    food.dragging = True
                if gametitle.rect.collidepoint(event.pos):
                    numberOfPresses += 1
                    gametitle.updatetitle(numberOfPresses)
                    gametitle.play_sound()
                if shopButtonWindow.is_clicked(mouse_pos):
                    shopWindowOpen = not shopWindowOpen  
                    shopButtonWindow.image = shopButtonClicked
                    click.play()
                if musicNote.is_clicked(mouse_pos):
                    if musicNote.image == musicNoteImage[1]:
                        pygame.mixer.music.set_volume(0.8)
                        musicNote.image = musicNoteImage[0]
                    else:
                        musicNote.image = musicNoteImage[1]
                        soundoff.play()
                        pygame.mixer.music.set_volume(0.0)
                if shopWindowOpen:
                    for item in shop_items:
                        if item['shopitem'].is_clicked(mouse_pos):
                            item['shopitem'].trigger()
                            all_sprites.update()
                            all_sprites.draw(screen)
                            click.play()
                if musicBox:
                    pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEBUTTONUP:
                if food.dragging:
                    food.dragging = False
                    if hitboxx.colliderect(food.rect):
                        nomnom.play()
                        print('Is fed')
                        food.reset_position(food_reset_position)
                        scoreboard.update_score(gfd(fish_image[food.current_image]))
                    else:
                        food.reset_position(food_reset_position)
                if shopButtonWindow.is_clicked(mouse_pos):
                    shopButtonWindow.image = shopButton
            elif event.type == pygame.MOUSEMOTION:
                if food.dragging:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    food.rect.center = event.pos

        current_time = time.time()

        if current_time - start_time >= frame_meow_interval:
            miau.play()
            start_time = current_time

        screen.blit(background, (0, 0))
        #screen.blit(meownies, (4, 23))
        screen.blit(gametitle.image, gametitle.rect)
        all_sprites.update()
        kayaC.update(food.dragging)
        scoreboard.draw()
        all_sprites.draw(screen)
        
        if shopWindowOpen:
            screen.blit(shopClassWindow.image, shopClassWindow.rect.topleft)
            for item in shop_items:
                item['shopitem'].show_locked_status(screen)
            for item in shop_items:
                if item['shopitem'].rect.collidepoint(mouse_pos):
                    hover_text = font2.render(item['text'], True, (0, 0, 0))
                    screen.blit(hover_text, (mouse_pos[0] + 13, mouse_pos[1] + 10))
                    hover_text = font.render(item['text'], True, DARK_VIOLET)
                    screen.blit(hover_text, (mouse_pos[0] + 10, mouse_pos[1] + 10))
                    
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
