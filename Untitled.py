#!/usr/bin/env python
# coding: utf-8

# In[10]:


class User:
    def _init_(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def display_info(self):
        print(f"Name: {self.name}")
        print("User ID: {self.user_id}")


class Librarian(User):
    def _init_(self, name, user_id, staff_id):
        super()._init_(name, user_id)
        self.staff_id = staff_id

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print("Role: Librarian")

    def add_book(self, book_title):
        print(f"Added '{book_title}' to the library collection.")


# In[ ]:




