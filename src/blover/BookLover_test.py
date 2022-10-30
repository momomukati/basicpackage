import unittest
from BookLover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("book1", 3)

        self.assertIn("book1",set(test_object.book_list['book_name']))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("book1", 3)
        test_object.add_book("book1", 4)

        self.assertEqual(test_object.book_list['book_name'].count(),1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("book1", 3)
        test_object.add_book("book2", 4)

        answer = test_object.has_read('book1')
        self.assertEqual(answer,True)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("book1", 3)
        test_object.add_book("book2", 4)
        
        answer = test_object.has_read('book3')
        self.assertEqual(answer,False)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.

        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        test_object.add_book("book1", 3)
        test_object.add_book("book2", 4)
        test_object.add_book("book3", 5)

        self.assertEqual(test_object.num_books_read(),3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3

        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

        test_object.add_book("book1", 3)
        test_object.add_book("book2", 4)
        test_object.add_book("book3", 5)

        my_list1 = set(test_object.fav_books()['book_rating'])
        result = all(i > 3 for i in my_list1)
        self.assertEqual(result,True)
                
if __name__ == '__main__':
    unittest.main(verbosity=3)