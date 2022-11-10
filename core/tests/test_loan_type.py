import pytest
from rest_framework import status

@pytest.fixture
def create_loantype(api_client):
    def create(loantype):
        return api_client.post('/core/loan-types/', loantype)
    return create

@pytest.mark.django_db
class TestCreateLoanType():
    def test_if_is_admin_return_201(self, authenticate_user, create_loantype):
        authenticate_user()

        loan_type = {
            'name': 'string',
            'maximum_amount': 20.00,
            'minimum': 20.00,
            'repayment_days': 3,
            'number_of_guarators': 4,
            'minimum_savings': 20.00
        }

        response = create_loantype(loan_type)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_is_not_admin_return_403(self, authenticate_user, create_loantype):
        authenticate_user(False)

        loan_type = {
            'name': 'string',
            'maximum_amount': 20.00,
            'minimum': 20.00,
            'repayment_days': 3,
            'number_of_guarators': 4,
            'minimum_savings': 20.00
        }

        response = create_loantype(loan_type)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_valid_return_201(self, create_loantype):
        loan_type = {
            'name': 'string',
            'maximum_amount': 20.00,
            'minimum': 20.00,
            'repayment_days': 3,
            'number_of_guarators': 4,
            'minimum_savings': 20.00
        }
        
        response = create_loantype(loan_type)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] is not None
        assert response.data['maximum_amount'] is not None
        assert response.data['minimum'] is not None
        assert response.data['repayment_days'] is not None
        assert response.data['number_of_guarators'] is not None
        assert response.data['minimum_savings'] is not None


    def test_if_data_is_invalid_return_400(self, create_loantype):
        loan_type = {
            'name': ''
        }

        response = create_loantype(loan_type)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['name'] is not None
    

@pytest.mark.django_db
class TestGetLoanType():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/core/loan-types/')

        assert response.status_code == status.HTTP_200_OK


    def test_if_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        response = api_client.get('/core/loan-types/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


    