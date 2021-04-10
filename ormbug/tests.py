from django.test import TestCase
from django.contrib.auth.models import User

from ormbug.models import user_stores, user_books, Store, Book
# from ormbug.models import user_stores, user_books, user_pages, user_characters, Store, Book, Page, Character

import django
import time

# Create your tests here.
class OrmBugTest(TestCase):
    def setUp(self):
        user = User.objects.create_user("test", "test@test.com", "testpasswordhere")
        user.save()

        self.user = user

        for i in range(10):
            store = Store.objects.create()

            for i in range(15):
                book = Book.objects.create(store=store)

    def test_orm_speed(self):
        """"""
        print("Running on Django " + str(django.get_version()))

        proc_start_time = time.process_time()
        start_time = time.time()

        for i in range(100):
            stores = user_stores(self.user)
            user_books(self.user).filter(store__in=stores).query
        
        print(f"Process time taken: {time.process_time() - proc_start_time}s")
        print(f"Real time taken: {time.time() - start_time}s")
        
        