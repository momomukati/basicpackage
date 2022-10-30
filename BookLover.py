# CODE HERE

import pandas as pd
import numpy as np

class BookLover():
    name = email = fav_genre = ""
    num_books = 0
    book_list = []

    def __init__(self,name,email,fav_genre,num_books=0,book_list=[]):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def add_book(self, book_name, book_rating):
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]
        })
        if book_name not in set(self.book_list['book_name']):
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

    def has_read(self,book_name):
        if book_name in set(self.book_list['book_name']):
            return True 
        else:
            return False

    def num_books_read(self):
        return self.book_list['book_name'].count()

    def fav_books(self):
        return self.book_list.loc[self.book_list['book_rating'] > 3] 


