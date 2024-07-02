import datetime as dt
import uuid
import pytest
from sqlalchemy import text
from src.infra.db.repositories.relations.users_groups_repository import UsersGroupsRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.security.implementations.secure_email import SecureEmail

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

# @pytest.mark.skip(reason="sensive test")
def test_join_user():
    mocked_id = str(uuid.uuid4())
    mocked_email = 'test@outlook.com'

    mocked_group_id = str(uuid.uuid4())
    mocked_title = "TestTitleGroup"

    secure_email = SecureEmail()
    encrypt_email = secure_email.encrypt_email(email=mocked_email)

    users_groups_repository = UsersGroupsRepository()
    users_groups_repository.join_user(id=mocked_id,
                                      secure_email=encrypt_email,
                                      group_title=mocked_title,
                                      group_id=mocked_group_id,
                                      updated_at=dt.datetime.now())

    sql = '''SELECT * FROM users_groups
        WHERE secure_email = '{}' AND group_title = '{}' 
    '''.format(encrypt_email, mocked_title)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.secure_email == encrypt_email
    assert registry.group_title == mocked_title

    connection.execute(text(f'''
        DELETE FROM users_groups WHERE secure_email = '{registry.secure_email}' 
        AND group_title = '{registry.group_title}'                     
    '''))
    connection.commit()

@pytest.mark.skip(reason="sensive test")
def test_select_user_relations():
    mocked_id = str(uuid.uuid4())
    mocked_email = 'test@outlook.com'

    mocked_group_id = str(uuid.uuid4())
    mocked_title = "TestTitleGroup"
    mocked_updated_at = dt.datetime.now()

    secure_email = SecureEmail()
    encrypted_email = secure_email.encrypt_email(email=mocked_email)

    connection.execute(text('''INSERT INTO users_groups (id, secure_email,
    group_title, group_id, updated_at) VALUES ('{}', '{}', '{}', '{}', '{}')
    '''.format(mocked_id, encrypted_email, mocked_title, mocked_group_id, str(mocked_updated_at))))
    connection.commit()

    users_groups_repository = UsersGroupsRepository()
    response = users_groups_repository.select_user_relations(secure_email=encrypted_email)

    assert response[0].secure_email == encrypted_email
    assert response[0].group_title == mocked_title
    assert response[0].updated_at != dt.datetime.now()

    connection.execute(text(f'''
        DELETE FROM users_groups WHERE secure_email = '{response[0].secure_email}' 
        AND group_title = '{response[0].group_title}'                     
    '''))
    connection.commit()

@pytest.mark.skip(reason="sensive test")
def test_select_group_relations():
    mocked_id = str(uuid.uuid4())
    mocked_email = 'test@outlook.com'

    mocked_group_id = str(uuid.uuid4())
    mocked_title = "TestTitleGroup"
    mocked_updated_at = dt.datetime.now()

    secure_email = SecureEmail()
    encrypted_email = secure_email.encrypt_email(email=mocked_email)

    connection.execute(text('''INSERT INTO users_groups (id, secure_email,
    group_title, group_id, updated_at) VALUES ('{}', '{}', '{}', '{}', '{}')
    '''.format(mocked_id, encrypted_email, mocked_title, mocked_group_id, str(mocked_updated_at))))
    connection.commit()

    users_groups_repository = UsersGroupsRepository()
    response = users_groups_repository.select_group_relations(group_id=mocked_group_id)

    assert response[0].secure_email == encrypted_email
    assert response[0].group_title == mocked_title
    assert response[0].updated_at != dt.datetime.now()

    connection.execute(text(f'''
        DELETE FROM users_groups WHERE secure_email = '{response[0].secure_email}' 
        AND group_title = '{response[0].group_title}'                     
    '''))
    connection.commit()

@pytest.mark.skip(reason="sensive test")
def test_update_relation():
    mocked_id = "007b32fc-dd80-4147-add7-17213328bc2a"
    mocked_email = 'test@outlook.com'

    mocked_group_id = "a17b32fc-dd80-4147-add7-17213328bc2a"
    mocked_title = "TestTitleGroup"
    mocked_updated_at = dt.datetime(2024, 5, 30, 17, 56, 15, 766331)

    secure_email = SecureEmail()
    encrypted_email = secure_email.encrypt_email(email=mocked_email)

    connection.execute(text('''INSERT INTO users_groups (id, secure_email,
    group_title, group_id, updated_at) VALUES ('{}', '{}', '{}', '{}', '{}')
    '''.format(mocked_id, encrypted_email, mocked_title, mocked_group_id, str(mocked_updated_at))))
    connection.commit()

    mocked_updated_now = dt.datetime(2024, 6, 30, 17, 56, 15, 766331)

    users_groups_repository = UsersGroupsRepository()
    response = users_groups_repository.update_relation(secure_email=encrypted_email,
                                                       group_id=mocked_group_id,
                                                       updated_at=mocked_updated_now)

    assert response.secure_email == secure_email.encrypt_email("test@outlook.com")
    assert response.group_title == mocked_title
    assert response.updated_at != dt.datetime.now()

    connection.execute(text(f'''
        DELETE FROM users_groups WHERE secure_email = '{response.secure_email}' 
        AND group_title = '{response.group_title}'                     
    '''))
    connection.commit()
