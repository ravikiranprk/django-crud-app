from django.urls import path
from .views import get_users, create_user, update_user, delete_user

urlpatterns = [
    path("users", get_users, name="all_users"),
    path("users/create", create_user, name="create_user"),
    path("users/<int:id>/update", update_user, name="update_user"),
    path("users/<int:id>/delete", delete_user, name="delete_user"),
]