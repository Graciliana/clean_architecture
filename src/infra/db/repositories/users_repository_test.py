from unittest import mock
from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.settings.users import Users as UsersEntity

def test_insert_user():
    mocked_first_name = 'first'
    mocked_last_name = 'last'
    mocked_age = 24
    
    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
    
