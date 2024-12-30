
from scripts.rendering import catColor, catShape, fish_image
from scripts.var_classes import kayaCColors, kayaShape, food, catColor, catShape, fish_image, scoreboard
from scripts.dictionary_images import *
from scripts.dictionary_path import *
from scripts.shop import *
from scripts.scoreboard import *
from scripts.sounds import *

#this is the worst code written in human history, but i don't have time to fix it

class eq_items:
    def equip_hat1():
        if kayaCColors.image in catColor[6:10]:
                kayaCColors.current_image = 6
                kayaCColors.image = catColor[kayaCColors.current_image]
        elif kayaCColors.image in catColor[3:6]:
                kayaCColors.current_image = 3
                kayaCColors.image = catColor[kayaCColors.current_image]
        elif kayaCColors.image in catColor[0:3]:
                kayaCColors.current_image = 0
                kayaCColors.image = catColor[kayaCColors.current_image]
        kayaShape.current_image = 0
        kayaShape.image = catShape[kayaShape.current_image]
        print("Equipped Hat 1!")

    def equip_hat2(scoreboard):
        if OwnedDictionary.get('hat2') == True or scoreboard.score >=250: 
            if kayaCColors.image in catColor[6:10]:
                kayaCColors.current_image = 7
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaCColors.image in catColor[3:6]:
                kayaCColors.current_image = 4
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaCColors.image in catColor[0:3]:
                kayaCColors.current_image = 1
                kayaCColors.image = catColor[kayaCColors.current_image]
            kayaShape.current_image = 1
            kayaShape.image = catShape[kayaShape.current_image]
            shop_items[1]['shopitem'].unlock_item()
            print("Equipped Hat 2!")
            if OwnedDictionary['hat2'] == False:
                scoreboard.score -= 250
                print("Purchased Hat 2!")
                scoreboard.render_score()
                kayaShape.current_image = 1
                kayaShape.image = catShape[kayaShape.current_image]
                OwnedDictionary['hat2'] = True
        else:
            tryagain.play()
            print('Not enough meowny!')
            print(scoreboard.score)

    def equip_hat3(scoreboard):
        if OwnedDictionary.get('hat3') == True or scoreboard.score >=1250:
            if kayaCColors.image in catColor[6:10]:
                kayaCColors.current_image = 8
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaCColors.image in catColor[3:6]:
                kayaCColors.current_image = 5
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaCColors.image in catColor[0:3]:
                kayaCColors.current_image = 2
                kayaCColors.image = catColor[kayaCColors.current_image]
            kayaShape.current_image = 2
            kayaShape.image = catShape[kayaShape.current_image]
            shop_items[2]['shopitem'].unlock_item()
            print("Equipped Hat 3!")
            if OwnedDictionary['hat2'] == False:
                scoreboard.score -= 1250
                print("Purchased Hat 3!")
                scoreboard.render_score()
                kayaShape.current_image = 2
                kayaShape.image = catShape[kayaShape.current_image]
                OwnedDictionary['hat3'] = True
        else:
            tryagain.play()
            print('Not enough meowny!')

    def equip_food1():
        food.current_image = 0
        food.image = fish_image[food.current_image]
        print("Equipped Food 1!")

    def equip_food2(scoreboard):
        if OwnedDictionary.get('food2') == True or scoreboard.score >= 500:
            food.current_image = 1
            food.image = fish_image[food.current_image]
            print("Equipped Food 2!")
            shop_items[4]['shopitem'].unlock_item()
            if OwnedDictionary['food2'] == False:
                scoreboard.score -= 500
                OwnedDictionary['food2'] = True
                scoreboard.render_score()
                print("Purchased Food 2!")
        else:
            tryagain.play()
            print("Not enough meowny!")

    def equip_food3(scoreboard):
        if OwnedDictionary.get('food3') == True or scoreboard.score >= 2500:
            food.current_image = 2
            food.image = fish_image[food.current_image]
            print("Equipped Food 3!")
            shop_items[5]['shopitem'].unlock_item()
            if OwnedDictionary['food3'] == False:
                scoreboard.score -= 2500
                OwnedDictionary['food3'] = True
                scoreboard.render_score()
                print("Purchased Food 3!")
        else:
            tryagain.play()
            print("Not enough meowny!")

    def change_color1():
        if kayaShape.current_image == 0:
            kayaCColors.current_image = 0
            kayaCColors.image = catColor[kayaCColors.current_image]
        elif kayaShape.current_image == 1:
            kayaCColors.current_image = 1
            kayaCColors.image = catColor[kayaCColors.current_image]
        elif kayaShape.current_image == 2:
            kayaCColors.current_image = 2
            kayaCColors.image = catColor[kayaCColors.current_image]

        print("Changed color!")

    def change_color2(scoreboard):
        if OwnedDictionary.get('color2') == True or scoreboard.score >= 1000:
            if kayaShape.current_image == 0:
                kayaCColors.current_image = 3
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaShape.current_image == 1:
                kayaCColors.current_image = 4
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaShape.current_image == 2:
                kayaCColors.current_image = 5
                kayaCColors.image = catColor[kayaCColors.current_image]
            shop_items[7]['shopitem'].unlock_item()
            print("Equipped Color 2!")
            if OwnedDictionary['color2'] == False:
                scoreboard.score -= 1000
                OwnedDictionary['color2'] = True
                scoreboard.render_score()
                print("Purchased Color 2!")
        else:
            tryagain.play()
            print("Not enough meowny!")

    def change_color3(scoreboard):
        if OwnedDictionary.get('color3') == True or scoreboard.score >= 5000:
            if kayaShape.current_image == 0:
                kayaCColors.current_image = 6
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaShape.current_image == 1:
                kayaCColors.current_image = 7
                kayaCColors.image = catColor[kayaCColors.current_image]
            elif kayaShape.current_image == 2:
                kayaCColors.current_image = 8
                kayaCColors.image = catColor[kayaCColors.current_image]
            shop_items[8]['shopitem'].unlock_item()
            print("Equipped Color 2!")
            if OwnedDictionary['color2'] == False:
                scoreboard.score -= 5000
                OwnedDictionary['color2'] = True
                scoreboard.render_score()
                print("Purchased Color 2!")
        else:
            tryagain.play()
            print("Not enough meowny!")
    

shop_items = [
    {'shopitem' : ShopItem(100, 220, 100, 100, eq_items.equip_hat1, unlocked=True), 'text' : """Cute and simple!"""},  # Hat 1
    {'shopitem' : ShopItem(250, 221, 100, 100, eq_items.equip_hat2, scoreboard, unlocked=False), 'text' : 'For the\nrainy days!'}, # Hat 2
    {'shopitem' : ShopItem(396, 221, 100, 100, eq_items.equip_hat3, scoreboard, unlocked=False), 'text' : 'Ready for\nautumn!'},  # Hat 3
    {'shopitem' : ShopItem(100, 350, 100, 100, eq_items.equip_food1, unlocked=True), 'text' : "A kitten's \nfavorite food!"}, # Food 1
    {'shopitem' : ShopItem(250, 351, 100, 100, eq_items.equip_food2, scoreboard, unlocked=False), 'text' : 'The taste of \nsummer!'}, # Food 2
    {'shopitem' : ShopItem(396, 351, 100, 100, eq_items.equip_food3, scoreboard, unlocked=False), 'text' : 'The cake\nis a lie!'}, # Food 3
    {'shopitem' : ShopItem(100, 480, 100, 100, eq_items.change_color1, unlocked=True), 'text' : 'Be gentle!'},# Color 1
    {'shopitem' : ShopItem(250, 481, 100, 100, eq_items.change_color2, scoreboard, unlocked=False), 'text' : 'Is that\na cow?'}, # Color 2
    {'shopitem' : ShopItem(396, 481, 100, 100, eq_items.change_color3, scoreboard, unlocked=False), 'text' : 'Chocolate\npattern!'}, # Color 3
]