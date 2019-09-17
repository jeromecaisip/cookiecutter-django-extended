import pytest

from    django.urls    import    reverse

@pytest.fixture()
def users(django_user_model):
    user1  = django_user_model.objects.create(
               username      = 'user1',
               is_superuser  = True,
               is_staff      = True
             )
    user1.set_password('password'),
    user1.save()

    user2  = django_user_model.objects.create(
               username      = 'user2',
               is_superuser  = False,
               is_staff      = False
             )
    user2.set_password('password'),
    user2.save()

    user3  = django_user_model.objects.create(
               username      = 'user3',
               is_superuser  = False,
               is_staff      = False
             )
    user3.set_password('password'),
    user3.save()


class TestUserViewSet:
    def test_user_detail(self,
                         client,
                         django_user_model,
                         users):

        if not client.login(
                        username  = 'user1',
                        password  = 'password',
                      ):
            pytest.fail('failed to login')

        response  = client.get(
                             path  = reverse(
                                       viewname  = 'users:user-detail',
                                       kwargs    = {
                                                    'username':  'user1'
                                                   }
                                     )
                           )

        assert response.status_code == 200

    def test_user_list(self,
                       client,
                       django_user_model,
                       users):

        if not client.login(
                        username  = 'user1',
                        password  = 'password',
                      ):
            pytest.fail('failed to login')

        response  = client.get(
                             path  = reverse(
                                       viewname  = 'users:user-list'
                                     )
                           )

        assert response.status_code == 200
