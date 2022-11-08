import pytest
from rest_framework import status
from model_bakery import baker

from users.models import Member


@pytest.fixture
def create_saving_contribution(api_client):
    def create(saving_contribution):
        return api_client.post('/finance/savings-contributions/', saving_contribution)
    return create


@pytest.mark.django_db
class TestCreateSavingContribution():
    def test_if_is_admin_return_201(self, authenticate_user, create_saving_contribution):
        authenticate_user()
        member = baker.make(Member)

        response = create_saving_contribution({'member': member.id, 'amount': 30.00})

        assert response.status_code == status.HTTP_201_CREATED

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_saving_contribution):
        authenticate_user(is_staff=False)
        member = baker.make(Member)

        response = create_saving_contribution({'member': member.id, 'amount': 30.00})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_201(self, create_saving_contribution):
        member = baker.make(Member)

        response = create_saving_contribution({'member': member.id, 'amount': 30.00})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['member'] is not None
        assert response.data['amount'] is not None

    def test_if_data_is_invalid_return_400(self, create_saving_contribution):

        response = create_saving_contribution({'member': 0})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['member'] is not None
        


@pytest.mark.django_db
class TestGetSavingContribution():
    def test_if_is_admin_return_200(self, api_client, authenticate_user):
        authenticate_user()
        member = baker.make(Member)
        
        response = api_client.get('/finance/savings-contributions/', {'member': member.id, 'amount':30.00})

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)
        member = baker.make(Member)
        
        response = api_client.get('/finance/savings-contributions/', {'member': member.id, 'amount':30.00})

        assert response.status_code == status.HTTP_403_FORBIDDEN

