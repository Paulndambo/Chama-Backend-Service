import pytest
from model_bakery import baker
from rest_framework import status


from users.models import Member
from loans.models import Loan, LoanGuarantor

@pytest.fixture
def create_loan_guarantor(api_client):
    def create(loan_guatantor):
        loan = baker.make(Loan)
        return api_client.post(f'/loans/loans/{loan.id}/guarantors/', loan_guatantor)
    return create

@pytest.fixture
def update_loan_guarantor(api_client):
    def update(loan_guarantor):
        loan_guarantor_= baker.make(LoanGuarantor)
        return api_client.patch(f'/loans/loans/{loan_guarantor_.loan.id}/guarantors/{loan_guarantor_.id}/', loan_guarantor)
    return update


@pytest.fixture
def delete_loan_guarantor(api_client):
    def delete():
        loan_guarantor = baker.make(LoanGuarantor)
        return api_client.delete(f'/loans/loans/{loan_guarantor.loan.id}/guarantors/{loan_guarantor.id}/')
    return delete



@pytest.mark.django_db
class TestCreateLoanGuarantor():
    def test_if_is_admin_return_201(self, authenticate_user, create_loan_guarantor):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }

        response = create_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_201_CREATED

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_loan_guarantor):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }

        response = create_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_user_is_authenticated_return_201(self, authenticate_user, create_loan_guarantor):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }

        response = create_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_201_CREATED


    def test_if_user_is_not_authenticated_return_401(self, create_loan_guarantor):
        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }

        response = create_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_data_is_valid_return_201(self, create_loan_guarantor, authenticate_user):
        authenticate_user()
        
        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }

        response = create_loan_guarantor(loan_guarantor)
        

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] is not None
        assert response.data['id_number'] is not None
        
        assert response.data['relationship'] is not None
        assert response.data['birth_date'] is not None
        assert response.data['gender'] is not None
        assert response.data['marital_status'] is not None
        assert response.data['postal_code'] is not None
        assert response.data['town'] is not None
        assert response.data['country'] is not None


    def test_if_data_is_invalid_return_400(self, create_loan_guarantor, authenticate_user):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': ' ',
            'id_number': ' ',
            'phone_number': ' ',
            'email': 'guarantor@gmail.com',
            'relationship': ' ',
            'birth_date': '2000-01-01',
            'gender': ' ',
            'marital_status': ' ',
            'postal_code': ' ',
            'town': ' ',
            'country': ' '
        }

        response = create_loan_guarantor(loan_guarantor)
        

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['name'] is not None
        assert response.data['id_number'] is not None
        assert response.data['relationship'] is not None
        assert response.data['gender'] is not None
        assert response.data['marital_status'] is not None
        assert response.data['postal_code'] is not None
        assert response.data['town'] is not None
        assert response.data['country'] is not None



@pytest.mark.django_db
class TestGetLoanGuarantor():
    def test_if_is_admin_return_200(self, api_client, authenticate_user):
        authenticate_user()

        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/guarantors/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user(is_staff=False)

        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/guarantors/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_is_not_authorized_return_401(self, api_client, authenticate_user):
        loan = baker.make(Loan)

        response = api_client.get(f'/loans/loans/{loan.id}/guarantors/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
class TestGetLoanGuarantorById():
    def test_if_loan_guarantor_exists_return_200(self, api_client, authenticate_user):
        authenticate_user()

        guarantor = baker.make(LoanGuarantor)

        response = api_client.get(f'/loans/loans/{guarantor.loan.id}/guarantors/{guarantor.id}/')

        assert response.status_code == status.HTTP_200_OK
        

    def test_if_user_is_authorized_return_200(self, authenticate_user, api_client):
        authenticate_user()

        guarantor = baker.make(LoanGuarantor)

        response = api_client.get(f'/loans/loans/{guarantor.loan.id}/guarantors/{guarantor.id}/')

        assert response.status_code == status.HTTP_200_OK
        
    def test_if_user_is_not_authorized_return_401(self, api_client):
        guarantor = baker.make(LoanGuarantor)

        response = api_client.get(f'/loans/loans/2/guarantors/{guarantor.id}/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED



@pytest.mark.django_db
class TestUpdateLoanGuarantor():
    def test_if_is_admin_return_200(self, authenticate_user, update_loan_guarantor):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }


        response = update_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_200_OK


    def test_if_not_admin_return_403(self, authenticate_user, update_loan_guarantor):
        authenticate_user(is_staff=False)

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }


        response = update_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_user_is_authorized_return_200(self, authenticate_user, update_loan_guarantor):
        authenticate_user()

        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }


        response = update_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_user_is_not_authorized_return_401(self, update_loan_guarantor):
        member = baker.make(Member)
        loan = baker.make(Loan)

        loan_guarantor = {
            'member': member.id,
            'loan': loan.id,
            'name': 'Hellen',
            'id_number': '000004',
            'phone_number': '099876544',
            'email': 'guarantor@gmail.com',
            'relationship': 'single',
            'birth_date': '2000-01-01',
            'gender': 'male',
            'marital_status': 'single',
            'postal_code': '2233',
            'town': 'Nairobi',
            'country': 'Kenya'
        }


        response = update_loan_guarantor(loan_guarantor)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED



@pytest.mark.django_db
class TestDeleteLoanGuarantor():
    def test_if_is_admin_return_200(self, delete_loan_guarantor, authenticate_user):
        authenticate_user()

        response = delete_loan_guarantor()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_not_admin_return_403(self, delete_loan_guarantor, authenticate_user):
        authenticate_user(is_staff=False)

        response = delete_loan_guarantor()

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_authenticated_return_204(self, delete_loan_guarantor, authenticate_user):
        authenticate_user()

        response = delete_loan_guarantor()

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_user_is_not_authenticated_return_401(self, delete_loan_guarantor):

        response = delete_loan_guarantor()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

