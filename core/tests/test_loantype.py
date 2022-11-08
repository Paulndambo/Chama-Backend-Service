import pytest
from rest_framework import status

@pytest.fixture
def create_loan_type(api_client):
    def create(loan_type):
        return api_client.post('/core/loan-types/', loan_type)
    return create

loan_type = {
            'name': 'string',
            'maximum_amount': 200.00,
            'minimum': 50.00,
            'repayment_days': 0,
            'number_of_guarators': 0,
            'minimum_savings': 150.00
        }
@pytest.mark.django_db
class TestCreateLoanType():
    def test_if_is_admin_return_201(self, authenticate_user, create_loan_type):
        authenticate_user()

        response = create_loan_type(loan_type)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_is_not_admin_return_403(self, create_loan_type, authenticate_user):
        authenticate_user(is_staff=False)

        response = create_loan_type(loan_type)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_201(self, create_loan_type):
        response = create_loan_type(loan_type)

        assert response.data['name'] is not None 
        assert response.data['maximum_amount'] is not None
        assert response.data['minimum'] is not None  
        assert response.data['repayment_days'] is not None 
        assert response.data['number_of_guarators'] is not None 
        assert response.data['minimum_savings'] is not None 

@pytest.mark.django_db
class TestGetLoanType():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/core/loan-types/')

        assert response.status_code == status.HTTP_200_OK
    
    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/core/loan-types/')

        assert response.status_code == status.HTTP_403_FORBIDDEN