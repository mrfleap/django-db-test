import django

from django.db import models
from guardian.shortcuts import get_objects_for_user

def user_stores(user):
    return (
        get_objects_for_user(user, "ormbug.owns_store")
        | Store.objects.filter(book__in=get_objects_for_user(user, "ormbug.owns_book"))
    )

def user_books(user):
    return (
        Book.objects.filter(store__in=get_objects_for_user(user, "ormbug.owns_store"))
        | get_objects_for_user(user, "ormbug.owns_book")
    )


class Store(models.Model):
    class Meta:
        permissions = (("owns_store", "Owns Store"),)


class Book(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        permissions = (("owns_book", "Owns Book"),)


# For more submodels to exaggerate the issue, use the following code:

# def user_stores(user):
#     return (
#         get_objects_for_user(user, "ormbug.owns_store")
#         | Store.objects.filter(book__in=get_objects_for_user(user, "ormbug.owns_book"))
#         | Store.objects.filter(book__in=Book.objects.filter(page__in=get_objects_for_user(user, "ormbug.owns_page")))
#         | Store.objects.filter(book__in=Book.objects.filter(page__in=Page.objects.filter(character__in=get_objects_for_user(user, "ormbug.owns_character"))))
#     )

# def user_books(user):
#     return (
#         Book.objects.filter(store__in=get_objects_for_user(user, "ormbug.owns_store"))
#         | get_objects_for_user(user, "ormbug.owns_book")
#         | Book.objects.filter(page__in=get_objects_for_user(user, "ormbug.owns_page"))
#         | Book.objects.filter(page__in=Page.objects.filter(character__in=get_objects_for_user(user, "ormbug.owns_character")))
#     )

# def user_pages(user):
#     return (
#         Page.objects.filter(book__in=Book.objects.filter(store__in=get_objects_for_user(user, "ormbug.owns_store")))
#         | Page.objects.filter(book__in=get_objects_for_user(user, "ormbug.owns_book"))
#         | get_objects_for_user(user, "ormbug.owns_page")
#         | Page.objects.filter(character__in=get_objects_for_user(user, "ormbug.owns_character"))
#     )

# def user_characters(user):
#     return (
#         Character.objects.filter(page__in=Page.objects.filter(book__in=Book.objects.filter(store__in=get_objects_for_user(user, "ormbug.owns_store"))))
#         | Character.objects.filter(page__in=Page.objects.filter(book__in=get_objects_for_user(user, "ormbug.owns_book")))
#         | Character.objects.filter(page__in=get_objects_for_user(user, "ormbug.owns_page"))
#         | get_objects_for_user(user, "ormbug.owns_character")
#     )

# class Page(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)

#     class Meta:
#         # Not a great example of a permission, but it gets the point across
#         permissions = (("owns_page", "Owns Page"),)
        

# class Character(models.Model):
#     page = models.ForeignKey(Page, on_delete=models.CASCADE)

#     class Meta:
#         # Not a great example of a permission, but it gets the point across
#         permissions = (("owns_character", "Owns Character"),)