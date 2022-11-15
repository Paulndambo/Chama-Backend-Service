import pytest
from model_bakery import baker
from rest_framework import status


from core.models import LoanType
from users.models import Member
from loans.models import LoanApplication

@pytest.fixture
def create_loan_application(api_client):
    def create(loan_application):
        return api_client.post('/loans/loan-applications/', loan_application)
    return create

@pytest.fixture
def update_loan_application(api_client):
    def update(loan_application):
        loan_application_= baker.make(LoanApplication)
        return api_client.patch(f'/loans/loan-applications/{loan_application_.id}/', loan_application)
    return update


@pytest.fixture
def delete_loan_application(api_client):
    def delete():
        loan_application = baker.make(LoanApplication)
        return api_client.delete(f'/loans/loan-applications/{loan_application.id}/')
    return delete



@pytest.mark.django_db
class TestCreateLoanApplication():
    def test_if_is_admin_return_201(self, authenticate_user, create_loan_application):
        authenticate_user()

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan_application = {
            'member': member.id,
            'loan_type': loan_type.id,
            'amount_applying': 1000.00,
            'status': 'pending'
        }

        response = create_loan_application(loan_application)

        assert response.status_code == status.HTTP_201_CREATED

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_loan_application):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan_application = {
            'member': member.id,
            'loan_type': loan_type.id,
            'amount_applying': 1000.00,
            'status': 'pending'
        }

        response = create_loan_application(loan_application)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_user_is_authenticated_return_201(self, authenticate_user, create_loan_application):
        authenticate_user()

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan_application = {
            'amount_applying': 100.00,
            'status':  'pending',
            'member': member.id,
            'loan_type': loan_type.id
        }


        response = create_loan_application(loan_application)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_valid_return_201(self, create_loan_application, authenticate_user):
        authenticate_user()
        
        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan_application = {
            'amount_applying': 1000.00,
            'status': 'declined',
            'member': member.id,
            'loan_type': loan_type.id
        }


        response = create_loan_application(loan_application)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['amount_applying'] is not None
        assert response.data['status'] is not None


    def test_if_data_is_invalid_return_400(self, create_loan_application, authenticate_user):
        authenticate_user()

        loan_application = {
            'status': ' '
        }

        response = create_loan_application(loan_application)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['status'] is not None


@pytest.mark.django_db
class TestGetLoanApplication():
    def test_if_is_admin_return_200(self, api_client, authenticate_user):
        authenticate_user()

        response = api_client.get('/loans/loan-applications/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        response = api_client.get('/loans/loan-applications/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_is_not_authorized_return_401(self, api_client, authenticate_user):
        response = api_client.get('/loans/loan-applications/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestGetLoanApplicationById():
    def test_if_loan_application_exists_return_200(self, api_client, authenticate_user):
        authenticate_user()

        loan_application = baker.make(LoanApplication)

        response = api_client.get(f'/loans/loan-applications/{loan_application.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": loan_application.id,
            "member": 1,
            "loan_type": 1,
            "status": "pending",
            "amount_applying": response.data['amount_applying'],
            "created_at": response.data['created_at'],
            "updated_at": response.data['updated_at']
        }

    def test_if_user_is_authorized_return_200(self, authenticate_user, api_client):
        authenticate_user()

        loan_application = baker.make(LoanApplication)

        response = api_client.get(f'/loans/loan-applications/{loan_application.id}/')

        assert response.status_code == status.HTTP_200_OK
        
    def test_if_user_is_not_authorized_return_401(self, api_client):
        loan_application = baker.make(LoanApplication)

        response = api_client.get(f'/loans/loans/{loan_application.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED



@pytest.mark.django_db
class TestUpdateLoanApplication():
    def test_if_is_admin_return_200(self, authenticate_user, update_loan_application):
        authenticate_user()

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan_application = {
            "member": member.id,
            "loan_type": loan_type.id,
            "amount_applying": 20.00,
            "status": "pending"
        }


        response = update_loan_application(loan_application)

        assert response.status_code == status.HTTP_200_OK


    def test_if_not_admin_return_403(self, authenticate_user, update_loan_application):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan_application = {
            "member": member.id,
            "loan_type": loan_type.id,
            "amount_applying": 20.00,
            "status": "pending"
        }


        response = update_loan_application(loan_application)

        assert response.status_code == status.HTTP_403_FORBIDDEN



@pytest.mark.django_db
class TestDeleteLoanApplication():
    def test_if_is_admin_return_200(self, delete_loan_application, authenticate_user):
        authenticate_user()

        response = delete_loan_application()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_not_admin_return_403(self, delete_loan_application, authenticate_user):
        authenticate_user(is_staff=False)

        response = delete_loan_application()

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_authenticated_return_204(self, delete_loan_application, authenticate_user):
        authenticate_user()

        response = delete_loan_application()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_authenticated_return_401(self, delete_loan_application):

        response = delete_loan_application()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

