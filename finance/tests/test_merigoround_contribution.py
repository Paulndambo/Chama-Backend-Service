import pytest
from rest_framework import status
from model_bakery import  baker


from users.models import Member
from finance.models import MeriGoRoundContribution

@pytest.fixture
def create_merigoround_contribution(api_client):
    def create(merigoround):
        return api_client.post('/finance/meri-go-round-contributions/', merigoround)
    return create

@pytest.fixture
def get_merigoround_by_id(api_client):
    def get():
        merigoround = baker.make(MeriGoRoundContribution)
        return api_client.get(f'/finance/meri-go-round-contributions/{merigoround.id}/')
    return get

@pytest.fixture
def update_merigoround(api_client):
    def update(merigoround):
        merigoround_ = baker.make(MeriGoRoundContribution)
        return api_client.patch(f'/finance/meri-go-round-contributions/{merigoround_.id}/', merigoround)
    return update


@pytest.fixture
def delete_merigoround(api_client):
    def delete(merigoround):
        merigoround_ = baker.make(MeriGoRoundContribution)
        return api_client.delete(f'/finance/meri-go-round-contributions/{merigoround_.id}/', merigoround)
    return delete

@pytest.mark.django_db
class TestCreateMeriGoRoundContribution():
    def test_if_is_admin_return_201(self, authenticate_user, create_merigoround_contribution):
        authenticate_user()

        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': 'pending',
            'member': member.id
        }

        response = create_merigoround_contribution(merigoround)

        assert response.status_code == status.HTTP_201_CREATED
    
    def test_if_not_admin_return_403(self, authenticate_user, create_merigoround_contribution):
        authenticate_user()

        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': 'pending',
            'member': member.id
        }

        response = create_merigoround_contribution(merigoround)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    
    def test_if_data_is_valid_return_201(self, authenticate_user, create_merigoround_contribution):
        authenticate_user()

        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': 'pending',
            'member': member.id
        }

        response = create_merigoround_contribution(merigoround)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['status'] is not None

    
    def test_if_data_is_invalid_return_400(self, authenticate_user, create_merigoround_contribution):
        authenticate_user()

        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': '',
            'member': member.id
        }

        response = create_merigoround_contribution(merigoround)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['status'] is not None


@pytest.mark.django_db
class TestGetMeriGoRoundContributions():
    def test_if_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/finance/meri-go-round-contributions/')

        assert response.status_code == status.HTTP_200_OK

    
    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/finance/meri-go-round-contributions/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
class TestGetMeriGoRoundContributionById():
    def test_if_merigoround_exists_return_200(self, api_client):
        merigoround = baker.make(MeriGoRoundContribution)

        response = api_client.get(f'/finance/meri-go-round-contributions/{merigoround.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': merigoround.id,
            'amount': merigoround.amount,
            'status': merigoround.status,
            'member': 1,
            'created': response.data['created'],
            'updated': response.data['updated']
        }

    def test_if_is_admin_return_200(self, api_client, authenticate_user, get_merigoround_by_id):
        authenticate_user()

        response = get_merigoround_by_id()

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_403(self, api_client, authenticate_user, get_merigoround_by_id):
        authenticate_user()
        
        response = get_merigoround_by_id()

        assert response.status_code == status.HTTP_403_FORBIDDEN

        

@pytest.mark.django_db
class TestUpdateMeriGoRoundContribution():
    def test_if_is_admin_return_200(self, authenticate_user, api_client, update_merigoround):
        authenticate_user()
        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': 'paid',
            'member': member.id
        }
        response = update_merigoround(merigoround)

        assert response.status_code == status.HTTP_200_OK

    def test_if_is_not_admin_return_200(self, authenticate_user, update_merigoround):
        authenticate_user(is_staff=False)
        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': 'paid',
            'member': member.id
        }
        response = update_merigoround(merigoround)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_200(self, authenticate_user,  update_merigoround):
        authenticate_user()
        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': 'paid',
            'member': member.id
        }
        response = update_merigoround(merigoround)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['status'] is not None

    def test_if_data_is_invalid_return_400(self, authenticate_user,  update_merigoround):
        authenticate_user()
        member = baker.make(Member)

        merigoround = {
            'amount': 10.00,
            'status': '',
            'member': member.id
        }
        response = update_merigoround(merigoround)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['status'] is not None

@pytest.mark.django_db
class TestDeleteMeriGoRound():
    def test_if_is_admin_return_200(self, authenticate_user, delete_merigoround):
        authenticate_user()
        member = baker.make(Member)
        merigoround = {
            'id': 1,
            'amount': 10.00,
            'status': '',
            'member': member.id
        }


        response = delete_merigoround(merigoround)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_if_is_not_admin_return_403(self, authenticate_user, delete_merigoround):
        authenticate_user()
        member = baker.make(Member)
        merigoround = {
            'id': 1,
            'amount': 10.00,
            'status': '',
            'member': member.id
        }


        response = delete_merigoround(merigoround)

        assert response.status_code == status.HTTP_403_FORBIDDEN