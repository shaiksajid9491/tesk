from django.urls import path

from .views import home, town, table, user_table, create, edit, update, delete

urlpatterns = [
    path('home/',home),
    path('town/',town),
    path('table/',table),
    path('user/',user_table),
    path('create/',create),
    path('edit/<int:id>/',edit),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete)
]