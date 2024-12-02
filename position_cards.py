import string
import sys
from PIL import Image

def get_suit_name(c: str):
    match c:
        case 'C':
            return 'clubs'
        case 'D':
            return 'diamonds'
        case 'H':
            return 'hearts'
        case 'S':
            return 'spades'        

def get_value(a: str):
    if len(a) == 3:
        return '10'
    
    if a[0] >= '2' and a[0] <= '9':
        return '{}'.format(a[0])
    
    match a[0]:
        case 'J':
            return 'jack'
        case 'Q':
            return 'queen'
        case 'K':
            return 'king'
        case 'A':
            return 'ace'

def abbreviation_to_card_name(a: string):
    suit = a[-1]
    if a[-1] == '\n':
        suit = a[-2]
    return '{}_of_{}'.format(get_value(a), get_suit_name(suit))
    

f = open('input', 'r')
cards = list(map(abbreviation_to_card_name, f.readlines()))
print(cards)


CARDS_NUM = 6

values = ['{}'.format(i) for i in range(2, 11)] + ['jack', 'queen', 'king', 'ace']
suits = ['clubs', 'diamonds', 'hearts', 'spades']
names = ['cards/{}_of_{}.png'.format(value, suit) for value in values for suit in suits]
print(names[4])

images = [Image.open(name) for name in names]
print(images[4].size)
card_size = images[0].size
total_size = (card_size[0] * 10, card_size[1] * 10)
new_im = Image.new('RGB', total_size)

mid = total_size[0] // 2
offset = card_size[0] // 5

start = mid - CARDS_NUM * offset // 2 
o = 0
for i in range(CARDS_NUM):
    new_im.paste(images[i], (o, 0))
    o += offset
new_im.save('output.jpg')
# widths, heights = zip(*(i.size for i in images))

# total_width = sum(widths)
# max_height = max(heights)

# new_im = Image.new('RGB', (total_width, max_height))

# x_offset = 0
# for im in images:
#   new_im.paste(im, (x_offset,0))
#   x_offset += im.size[0]

# new_im.save('test.jpg')