import pytest
from model_bakery import baker
from rest_framework import status


from users.models import Member
from loans.models import Loan, LoanPayment

@pytest.fixture
def create_loan_payment(api_client):
    def create(loan_payment):
        loan = baker.make(Loan)
        return api_client.post(f'/loans/loans/{loan.id}/payments/', loan_payment)
    return create

@pytest.fixture
def update_loan_payment(api_client):
    def update(loan_payment):
        loan_payment_= baker.make(LoanPayment)
        return api_client.patch(f'/loans/loans/{loan_payment_.loan.id}/payments/{loan_payment_.id}/', loan_payment)
    return update


@pytest.fixture
def delete_loan_payment(api_client):
    def delete():
        loan_payment = baker.make(LoanPayment)
        return api_client.delete(f'/loans/loans/{loan_payment.loan.id}/payments/{loan_payment.id}/')
    return delete



@pytest.mark.django_db
class TestCreateLoanPayment():
    def test_if_is_admin_return_201(self, authenticate_user, create_loan_payment):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'string',
        }

        response = create_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_201_CREATED

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_loan_payment):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'mpesa',
        }

        response = create_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_user_is_authenticated_return_201(self, authenticate_user, create_loan_payment):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'mpesa',
        }

        response = create_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_201_CREATED


    def test_if_user_is_not_authenticated_return_401(self, create_loan_payment):
        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'mpesa',
        }

        response = create_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_data_is_valid_return_201(self, create_loan_payment, authenticate_user):
        authenticate_user()
        
        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'string'
        }

        response = create_loan_payment(loan_payment)
        

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['amount'] is not None
        assert response.data['payment_method'] is not None
        


    def test_if_data_is_invalid_return_400(self, create_loan_payment, authenticate_user):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': '',
            'payment_method': '',
        }

        response = create_loan_payment(loan_payment)
        

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['amount'] is not None
    
    


@pytest.mark.django_db
class TestGetLoanPayment():
    def test_if_is_admin_return_200(self, api_client, authenticate_user):
        authenticate_user()

        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/payments/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/payments/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_is_not_authorized_return_401(self, api_client, authenticate_user):
        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/payments/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestGetLoanGuarantorById():
    def test_if_loan_guarantor_exists_return_200(self, api_client, authenticate_user):
        authenticate_user()

        payment = baker.make(LoanPayment)

        response = api_client.get(f'/loans/loans/{payment.loan.id}/payments/{payment.id}/')

        assert response.status_code == status.HTTP_200_OK
        

    def test_if_user_is_authorized_return_200(self, authenticate_user, api_client):
        authenticate_user()

        payment = baker.make(LoanPayment)

        response = api_client.get(f'/loans/loans/{payment.loan.id}/payments/{payment.id}/')

        assert response.status_code == status.HTTP_200_OK
        
    def test_if_user_is_not_authorized_return_401(self, api_client):
        payment = baker.make(LoanPayment)

        response = api_client.get(f'/loans/loans/{payment.loan.id}/payments/{payment.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED



@pytest.mark.django_db
class TestUpdateLoanPayment():
    def test_if_is_admin_return_200(self, authenticate_user, update_loan_payment):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'mpesa',
        }


        response = update_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_200_OK


    def test_if_not_admin_return_403(self, authenticate_user, update_loan_payment):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'mpesa',
        }


        response = update_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_user_is_authorized_return_200(self, authenticate_user, update_loan_payment):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'mpesa',
        }


        response = update_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_user_is_not_authorized_return_401(self, update_loan_payment):
        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_payment = {
            'member': member.id,
            'loan': loan.id,
            'amount': 100.00,
            'payment_method': 'mpesa',
        }


        response = update_loan_payment(loan_payment)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED



@pytest.mark.django_db
class TestDeleteLoanPayment():
    def test_if_is_admin_return_200(self, delete_loan_payment, authenticate_user):
        authenticate_user()

        response = delete_loan_payment()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_not_admin_return_403(self, delete_loan_payment, authenticate_user):
        authenticate_user(is_staff=False)

        response = delete_loan_payment()

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_authenticated_return_204(self, delete_loan_payment, authenticate_user):
        authenticate_user()

        response = delete_loan_payment()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_authenticated_return_401(self, delete_loan_payment):

        response = delete_loan_payment()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

