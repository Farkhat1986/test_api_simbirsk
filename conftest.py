import pytest
from endpoint.create_object import CreateObject
from endpoint.delete_object import DeleteObject
from generators.entity import EntityGenerator


@pytest.fixture()
def create_entity():
    """Фикстура для создания сущности (предусловие)."""
    create_endpoint = CreateObject()
    payload = EntityGenerator.random()
    create_endpoint.create_entity(payload)
    yield create_endpoint.response_txt, payload
    # Постусловие: удаление сущности
    delete_endpoint = DeleteObject()
    delete_endpoint.delete_entity_by_id(create_endpoint.response_txt)


@pytest.fixture()
def create_multiple_entities():
    """Фикстура для создания нескольких сущностей"""
    create_endpoint = CreateObject()
    entities = []
    for _ in range(3):  # Создаём 3 сущности
        payload = EntityGenerator.random()
        create_endpoint.create_entity(payload)
        entities.append((create_endpoint.response_txt, payload))
    yield entities  # Возвращаем список (ID, payload)
    # Постусловие: удаление всех созданных сущностей
    delete_endpoint = DeleteObject()
    for entity_id, _ in entities:
        delete_endpoint.delete_entity_by_id(entity_id)