from django.urls import path
from apps.user.views import *

urlpatterns = [
    path('users_list/', UsersList.as_view(), name='users_list'),
    path('users_table/', UsersTable.as_view(), name='users_table'),
    path('create_user/', CreateUser.as_view(), name='create_user'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name='delete_user')
]