import pytest
from rest_framework import status
from model_bakery import baker

from users.models import Member


@pytest.fixture
def create_saving(api_client):
    def create(saving):
        return api_client.post('/finance/savings/', saving)
    return create


@pytest.mark.django_db
class TestCreateSaving():
    def test_if_is_admin_return_201(self, authenticate_user, create_saving):
        authenticate_user()
        member = baker.make(Member)
        saving = {
            'year': '2022',
            'amount_saved': 20.00,
            'interest_earned': 20.00,
            'total_savings': 20.00,
            'member': member.id
        }

        response = create_saving(saving)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_is_not_admin_return_403(self, authenticate_user, create_saving):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        saving = {
            'year': '2022',
            'amount_saved': 20.00,
            'interest_earned': 20.00,
            'total_savings': 20.00,
            'member': member.id
        }

        response = create_saving(saving)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_valid_return_201(self, create_saving):
        member = baker.make(Member)
        saving = {
            'year': '2022',
            'amount_saved': 20.00,
            'interest_earned': 20.00,
            'total_savings': 20.00,
            'member': member.id
        }

        response = create_saving(saving)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['year'] is not None
        


    def test_if_data_is_invalid_return_400(self, create_saving):
        member = baker.make(Member)
        saving = {
            'year': '',
            'amount_saved': 20.00,
            'interest_earned': 20.00,
            'total_savings': 20.00,
            'member': member.id
        }

        response = create_saving(saving)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['year'] is not None


@pytest.mark.django_db
class TestGetSaving():
    def test_if_is_admin_return_200(self, api_client, authenticate_user):
        authenticate_user()

        response = api_client.get('/finance/savings/')

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user()

        response = api_client.get('/finance/savings/')

        assert response.status_code == status.HTTP_403_FORBIDDEN