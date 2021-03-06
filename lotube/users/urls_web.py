from django.conf.urls import url

from .views_web import UserList, UserDetail, LoginView, RegisterView, LogoutView, \
    UserDelete, UserUpdate

urlpatterns = [
    # List of users
    url(
        r'^$',
        UserList.as_view(),
        name='users'
    ),

    # Login
    url(
        r'^\/login$',
        LoginView.as_view(),
        name='login'
    ),

    # Sign up
    url(
        r'^\/signup',
        RegisterView.as_view(),
        name='signup'
    ),

    # Logout
    url(
        r'^\/logout',
        LogoutView.as_view(),
        name='logout'
    ),

    # Retrieve a specific user
    url(
        r'^\/(?P<username>[\w\d]+)$',
        UserDetail.as_view(),
        name='user'
    ),

    # Update a specific user
    url(
        r'\/(?P<username>[\w\d]+)/edit$',
        UserUpdate.as_view(),
        name='update'
    ),

    # Delete a specific user
    url(
        r'\/(?P<username>[\w\d]+)/delete$',
        UserDelete.as_view(),
        name='delete'
    ),
]
