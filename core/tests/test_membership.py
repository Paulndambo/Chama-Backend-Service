import pytest
from rest_framework import status

@pytest.fixture
def create_membership(api_client):
    def create(membership):
        return api_client.post('/core/memberships/', membership)
    return create

@pytest.mark.django_db
class TestCreateMembership():
    def test_if_is_admin_return_201(self, authenticate_user, create_membership):
        authenticate_user()

        response = create_membership({'name':'Gold', 'amount': 20})

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_is_not_admin_return_403(self, authenticate_user, create_membership):
        authenticate_user(False)

        response = create_membership({'name':'Gold', 'amount': 20})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_valid_return_201(self, create_membership):
        response = create_membership({'name':'Gold', 'amount': 20})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] is not None
        assert response.data['amount'] is not None

    def test_if_data_is_invalid_return_400(self, create_membership):
        response = create_membership({'name':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['name'] is not None
    

@pytest.mark.django_db
class TestGetMembership():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/core/memberships/')

        assert response.status_code == status.HTTP_200_OK


    def test_if_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/core/memberships/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


    