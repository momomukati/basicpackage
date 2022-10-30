# CODE HERE
from BookLover import BookLover

if __name__ == '__main__':
    
    ##testing BookLover class
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("book1", 3)
    test_object.add_book("book2", 4)
    test_object.add_book("book3", 5)
    test_object.add_book("book4", 2)

    print(test_object.fav_books())

