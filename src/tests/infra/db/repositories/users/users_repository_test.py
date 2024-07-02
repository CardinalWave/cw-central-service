import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositories.users.users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="sensive test")
def test_insert_user():
    mocked_token = '39721cd4-6f50-46c5-9d2a-10f9159b09ee'
    mocked_email = 'lua@outlook.com'
    mocked_username = 'Lua'

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_token, mocked_email, mocked_username)

    sql = '''SELECT * FROM users
        WHERE email = '{}' 
    '''.format(mocked_email)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.token == mocked_token
    assert registry.email == mocked_email
    assert registry.username == mocked_username

    connection.execute(text(f'''
        DELETE FROM users WHERE token = '{registry.token}';                      
    '''))
    connection.commit()

@pytest.mark.skip(reason="sensive test")
def test_select_email():
    mocked_token = '39721cd4-6f50-46c5-9d2a-10f9159b09aa'
    mocked_email = 'lua2@outlook.com'
    mocked_username = 'lua2'

    sql = '''INSERT INTO
        users (token, email, username) 
        VALUES ('{}', '{}', '{}')
    '''.format(mocked_token, mocked_email, mocked_username)
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_email(email=mocked_email)

    assert response.token == mocked_token
    assert response.email == mocked_email
    assert response.username == mocked_username

    connection.execute(text(f'''
        DELETE FROM users WHERE token = '{response.token}'                     
    '''))
    connection.commit()


@pytest.mark.skip(reason="sensive test")
def test_select_username():
    mocked_token = '39721cd4-6f50-46c5-9d2a-10f9159b09aa'
    mocked_email = 'lua2@outlook.com'
    mocked_username = 'lua2'

    sql = '''INSERT INTO
        users (token, email, username) 
        VALUES ('{}', '{}', '{}')
    '''.format(mocked_token, mocked_email, mocked_username)
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_username(username=mocked_username)

    assert response.token == mocked_token
    assert response.email == mocked_email
    assert response.username == mocked_username

    connection.execute(text(f'''
        DELETE FROM users WHERE token = '{response.token}'                     
    '''))
    connection.commit()

@pytest.mark.skip(reason="sensive test")
def test_remove_user():
    mocked_token = '39721cd4-6f50-46c5-9d2a-10f9159b09aa'
    mocked_email = 'lua2@outlook.com'
    mocked_username = 'lua2'

    sql = '''INSERT INTO
        users (token, email, username) 
        VALUES ('{}', '{}', '{}')
    '''.format(mocked_token, mocked_email, mocked_username)
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    users_repository.remove_user(token=mocked_token)

    # Verificar se o usuário foi removido
    result = connection.execute(text(f'''
        SELECT * FROM users WHERE token = '{mocked_token}'
    ''')).fetchone()

    assert result is None
