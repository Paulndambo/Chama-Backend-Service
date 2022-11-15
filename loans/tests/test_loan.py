from decimal import Decimal
import pytest
from model_bakery import baker
from rest_framework import status

from core.models import LoanType
from users.models import Member
from loans.models import Loan

@pytest.fixture
def create_loan(api_client):
    def create(loan):
        return api_client.post('/loans/loans/', loan)
    return create

@pytest.fixture
def update_loan(api_client):
    def update(loan):
        loan_= baker.make(Loan)
        return api_client.patch(f'/loans/loans/{loan_.id}/', loan)
    return update


@pytest.fixture
def delete_loan(api_client):
    def delete():
        loan = baker.make(Loan)
        return api_client.delete(f'/loans/loans/{loan.id}/')
    return delete

@pytest.mark.django_db
class TestCreateLoan():
    def test_if_is_admin_return_201(self, authenticate_user, create_loan):
        authenticate_user()

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan = {
            "member": member.id,
            "loan_type": loan_type.id,
            "amount_awared": 20.00,
            "amount_to_repay": 20.00,
            "total_interest": 20.00,
            "amount_repaid": 20.00,
            "balance": 0.00,
            "status": "still_paying",
            "expected_last_pay_date": "2022-11-10",
            "date_applied": "2022-11-10",
            "date_awared": "2022-11-10",
        }

        response = create_loan(loan)

        assert response.status_code == status.HTTP_201_CREATED


    def test_if_user_is_not_authorized_return_401(self, authenticate_user, create_loan):

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan = {
            "member": member.id,
            "loan_type": loan_type.id,
            "amount_awared": 20.00,
            "amount_to_repay": 20.00,
            "total_interest": 20.00,
            "amount_repaid": 20.00,
            "balance": 0.00,
            "status": "still_paying",
            "expected_last_pay_date": "2022-11-10",
            "date_applied": "2022-11-10",
            "date_awared": "2022-11-10",
        }

        response = create_loan(loan)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_data_is_valid_return_201(self, authenticate_user, create_loan):
        authenticate_user()
        
        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan = {
            "member": member.id,
            "loan_type": loan_type.id,
            "amount_awared": 20.00,
            "amount_to_repay": 20.00,
            "total_interest": 20.00,
            "amount_repaid": 20.00,
            "balance": 0.00,
            "status": "still_paying",
            "expected_last_pay_date": "2022-11-10",
            "date_applied": "2022-11-10",
            "date_awared": "2022-11-10",
        }

        response = create_loan(loan)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['expected_last_pay_date'] is not None
        assert response.data['date_applied'] is not None
        assert response.data['date_awared'] is not None


    def test_if_data_is_invalid_return_400(self, authenticate_user, create_loan):
        authenticate_user()

        loan = {
            "date_applied": "",
            "date_awared": "",
        }

        response = create_loan(loan)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['date_applied'] is not None
        assert response.data['date_awared'] is not None

@pytest.mark.django_db
class TestGetLoan():
    def test_if_is_admin_return_200(self, api_client, authenticate_user):
        authenticate_user()

        response = api_client.get('/loans/loans/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        response = api_client.get('/loans/loans/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
class TestGetLoanById():
    def test_if_loan_exists_return_200(self, api_client, authenticate_user):
        authenticate_user()
        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": loan.id,
            "member": 1,
            "loan_type": 1,
            "amount_awared": str(loan.amount_awared),
            "amount_to_repay": Decimal(loan.amount_to_repay),
            "total_interest": Decimal(loan.total_interest),
            "amount_repaid": Decimal(loan.amount_repaid),
            "balance": Decimal(loan.balance),
            "status": loan.status,
            "expected_last_pay_date": loan.expected_last_pay_date,
            "date_applied": str(loan.date_applied),
            "date_awared": loan.date_awared,
        }

    def test_if_user_is_authorized_return_200(self, authenticate_user, api_client):
        authenticate_user()

        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/')

        assert response.status_code == status.HTTP_200_OK
        
    def test_if_user_is_not_authorized_return_401(self, api_client):
        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestUpdateLoan():
    def test_if_is_admin_return_200(self, authenticate_user, update_loan):
        authenticate_user()

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan = {
            "member": member.id,
            "loan_type": loan_type.id,
            "amount_awared": 20.00,
            "amount_to_repay": 20.00,
            "total_interest": 20.00,
            "amount_repaid": 20.00,
            "balance": 0.00,
            "status": "still_paying",
            "expected_last_pay_date": "2022-11-10",
            "date_applied": "2022-11-10",
            "date_awared": "2022-11-10",
        }


        response = update_loan(loan)

        assert response.status_code == status.HTTP_200_OK


    def test_if_not_admin_return_403(self, authenticate_user, update_loan):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        loan_type = baker.make(LoanType)

        loan = {
            "member": member.id,
            "loan_type": loan_type.id,
            "amount_awared": 20.00,
            "amount_to_repay": 20.00,
            "total_interest": 20.00,
            "amount_repaid": 20.00,
            "balance": 0.00,
            "status": "still_paying",
            "expected_last_pay_date": "2022-11-10",
            "date_applied": "2022-11-10",
            "date_awared": "2022-11-10",
        }


        response = update_loan(loan)

        assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
class TestDeleteLoan():
    def test_if_is_admin_return_200(self, delete_loan, authenticate_user):
        authenticate_user(is_staff=True)

        response = delete_loan()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_not_admin_return_403(self, delete_loan, authenticate_user):
        authenticate_user(is_staff=False)

        response = delete_loan()

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_user_is_authenticated_return_204(self, delete_loan, authenticate_user):
        authenticate_user()

        response = delete_loan()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_authenticated_return_401(self, delete_loan):

        response = delete_loan()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


