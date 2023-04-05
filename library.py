from pprint import pprint 

SIZE_BOOK_SHOW = 2
LAST_INDEX = 0

# LIST OF THE ID OF BOOKS BORROWED
BORROW_DB = []

BOOK_DB = [
    {
        "author": "Chinua Achebe",
        "country": "Nigeria",
        "imageLink": "images/things-fall-apart.jpg",
        "language": "English",
        "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
        "pages": 209,
        "title": "Things Fall Apart",
        "year": 1958
    },
    {
        "author": "Hans Christian Andersen",
        "country": "Denmark",
        "imageLink": "images/fairy-tales.jpg",
        "language": "Danish",
        "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
        "pages": 784,
        "title": "Fairy tales",
        "year": 1836
    },
    {
        "author": "Dante Alighieri",
        "country": "Italy",
        "imageLink": "images/the-divine-comedy.jpg",
        "language": "Italian",
        "link": "https://en.wikipedia.org/wiki/Divine_Comedy\n",
        "pages": 928,
        "title": "The Divine Comedy",
        "year": 1315
    },
    {
        "author": "Unknown",
        "country": "Sumer and Akkadian Empire",
        "imageLink": "images/the-epic-of-gilgamesh.jpg",
        "language": "Akkadian",
        "link": "https://en.wikipedia.org/wiki/Epic_of_Gilgamesh\n",
        "pages": 160,
        "title": "The Epic Of Gilgamesh",
        "year": -1700
    },
    {
        "author": "Unknown",
        "country": "Achaemenid Empire",
        "imageLink": "images/the-book-of-job.jpg",
        "language": "Hebrew",
        "link": "https://en.wikipedia.org/wiki/Book_of_Job\n",
        "pages": 176,
        "title": "The Book Of Job",
        "year": -600
    },
    {
        "author": "Unknown",
        "country": "India/Iran/Iraq/Egypt/Tajikistan",
        "imageLink": "images/one-thousand-and-one-nights.jpg",
        "language": "Arabic",
        "link": "https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights\n",
        "pages": 288,
        "title": "One Thousand and One Nights",
        "year": 1200
    },
    {
        "author": "Unknown",
        "country": "Iceland",
        "imageLink": "images/njals-saga.jpg",
        "language": "Old Norse",
        "link": "https://en.wikipedia.org/wiki/Nj%C3%A1ls_saga\n",
        "pages": 384,
        "title": "Njál's Saga",
        "year": 1350
    },
    {
        "author": "Jane Austen",
        "country": "United Kingdom",
        "imageLink": "images/pride-and-prejudice.jpg",
        "language": "English",
        "link": "https://en.wikipedia.org/wiki/Pride_and_Prejudice\n",
        "pages": 226,
        "title": "Pride and Prejudice",
        "year": 1813
    },
    {
        "author": "Honoré de Balzac",
        "country": "France",
        "imageLink": "images/le-pere-goriot.jpg",
        "language": "French",
        "link": "https://en.wikipedia.org/wiki/Le_P%C3%A8re_Goriot\n",
        "pages": 443,
        "title": "Le Père Goriot",
        "year": 1835
    },
    {
        "author": "Samuel Beckett",
        "country": "Republic of Ireland",
        "imageLink": "images/molloy-malone-dies-the-unnamable.jpg",
        "language": "French, English",
        "link": "https://en.wikipedia.org/wiki/Molloy_(novel)\n",
        "pages": 256,
        "title": "Molloy, Malone Dies, The Unnamable, the trilogy",
        "year": 1952
    },
    {
        "author": "Giovanni Boccaccio",
        "country": "Italy",
        "imageLink": "images/the-decameron.jpg",
        "language": "Italian",
        "link": "https://en.wikipedia.org/wiki/The_Decameron\n",
        "pages": 1024,
        "title": "The Decameron",
        "year": 1351
    },
    {
        "author": "Jorge Luis Borges",
        "country": "Argentina",
        "imageLink": "images/ficciones.jpg",
        "language": "Spanish",
        "link": "https://en.wikipedia.org/wiki/Ficciones\n",
        "pages": 224,
        "title": "Ficciones",
        "year": 1965
    },
    {
        "author": "Emily Brontë",
        "country": "United Kingdom",
        "imageLink": "images/wuthering-heights.jpg",
        "language": "English",
        "link": "https://en.wikipedia.org/wiki/Wuthering_Heights\n",
        "pages": 342,
        "title": "Wuthering Heights",
        "year": 1847
    },
    {
        "author": "Albert Camus",
        "country": "Algeria, French Empire",
        "imageLink": "images/l-etranger.jpg",
        "language": "French",
        "link": "https://en.wikipedia.org/wiki/The_Stranger_(novel)\n",
        "pages": 185,
        "title": "The Stranger",
        "year": 1942
    },
    {
        "author": "Paul Celan",
        "country": "Romania, France",
        "imageLink": "images/poems-paul-celan.jpg",
        "language": "German",
        "link": "\n",
        "pages": 320,
        "title": "Poems",
        "year": 1952
    },
    {
        "author": "Louis-Ferdinand Céline",
        "country": "France",
        "imageLink": "images/voyage-au-bout-de-la-nuit.jpg",
        "language": "French",
        "link": "https://en.wikipedia.org/wiki/Journey_to_the_End_of_the_Night\n",
        "pages": 505,
        "title": "Journey to the End of the Night",
        "year": 1932
    },   
]



def gen_id(books: list) -> None:
    """"Modify the books and genearte an id for them"""
    # Check if any book has an id already
    count = 1
    for book in BOOK_DB:
        book['id'] = count
        count += 1
    


def view_books(results: list) -> None:
    global LAST_INDEX
    next_index = LAST_INDEX + SIZE_BOOK_SHOW
    x = results[LAST_INDEX : next_index]
    LAST_INDEX = next_index
    return x



menu = """Welcome to the book club
1) View Books
2) Reset View
3) Search Books
(if desired book is found enter 'id <id of book>' >>>
"""
SEARCH_MENU = """1) Title    2)Year   3) Author  4) Exit Search"""

gen_id(BOOK_DB)

while True:
    choice = input(menu)
    if choice == "1":
        pprint(view_books(BOOK_DB), indent=4)
    elif choice == "2":
        LAST_INDEX = 0
    elif choice == "3":
        while True:
            result = []
            LAST_INDEX = 0 # Reset 
            print(SEARCH_MENU)
            search_field = input(">>> ")
            if search_field == "1":
                s_title = input("Enter title to search: ")
                result = [book['title'] for book in BOOK_DB if s_title in book['title']]
                if len(result) > 3:
                    print(result[:3])
                    LAST_INDEX = 3
                    while True:
                        view_nxt = input("next> ")
                        if view_nxt == "n":
                            split_result = view_books(result)
                            if len(split_result) > 0:
                                print(split_result)
                            else:
                                break
                else:
                    print(result)
    
    elif 'id' in choice:
        choice = choice.strip()
        id = int(choice[-1])
        book = list(filter(lambda book: book['id'] == id, BOOK_DB ))
        pprint(book, indent=8)
    else:
        print("Exiting library")
        break
