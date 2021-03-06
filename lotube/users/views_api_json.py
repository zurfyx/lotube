from django.core.urlresolvers import reverse

from core.mixins import JSONView, JSONListView
from .mixins import UserListMixin, UserDetailMixin


def get_item(db_user, request):
    href_relative_uri = reverse('api:users:user',
                                kwargs={'username': db_user.username,
                                        'format': '.json'})
    return {
        'type': 'user',
        'id': db_user.id,
        'href': request.build_absolute_uri(href_relative_uri),
        'username': db_user.username,
        'first_name': db_user.first_name,
        'last_name': db_user.last_name,
        'created_at': db_user.date_joined,
        'last_login': db_user.last_login,
        'is_staff': db_user.is_staff,
        'is_active': db_user.is_active,
    }


class UserListJSON(JSONListView, UserListMixin):
    """
    List of users
    """

    def __init__(self):
        self.type = 'user_list'
        self.items = []

    def craft_response(self, context, **response_kwargs):
        self.items = [get_item(db_user, self.request)
                      for db_user in context['user_list']]
        return super(UserListJSON, self)\
            .craft_response(context, **response_kwargs)


class UserDetailJSON(JSONView, UserDetailMixin):
    """
    User details
    """

    def craft_response(self, context, **response_kwargs):
        user = context['object']
        return get_item(user, self.request)
