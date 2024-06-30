import uuid
import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.repositories.group.groups_repository import GroupsRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="sensive test")
def test_add_group():
    mocked_id = str(uuid.uuid4())
    mocked_title = "TestGroup"

    groups_repository = GroupsRepository()
    groups_repository.add_group(id=mocked_id, title=mocked_title)

    sql = '''SELECT * FROM groups
    WHERE title = '{}' 
    '''.format(mocked_title)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.id == mocked_id
    assert registry.title == mocked_title

    connection.execute(text(f'''
        DELETE FROM groups WHERE title = '{registry.title}';                      
    '''))
    connection.commit()

@pytest.mark.skip(reason="sensive test")
def test_select_title():
    mocked_id = "550e8400-e29b-41d4-a716-446655440000"
    mocked_title = "TestGroup"

    sql = '''INSERT INTO
        groups (id, title) 
        VALUES ('{}', '{}')
    '''.format(mocked_id, mocked_title)
    connection.execute(text(sql))
    connection.commit()

    groups_repository = GroupsRepository()
    response = groups_repository.select_title(title=mocked_title)

    assert response.id == mocked_id
    assert response.title == mocked_title

    connection.execute(text(f'''
        DELETE FROM groups WHERE title = '{response.title}';                      
    '''))
    connection.commit()
