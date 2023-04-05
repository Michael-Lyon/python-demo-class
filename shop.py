import utils
import climage
from pprint import pprint
last_index = 0
PRODUCTS_DB = utils.get_products()


def view_products():
    global last_index
    display_prods = []
    next_index = last_index + 2
    for prod in PRODUCTS_DB[last_index:next_index]:
        hold = []
        hold.append(prod['id'])
        hold.append(prod['title'])
        hold.append(prod['price'])
        display_prods.append(hold)
    last_index = next_index
    print(display_prods)

while  True:
    print("1) View Products")
    cmd = input("type here>> ")
    if cmd == "1":
        view_products()
    else:
        break
    
