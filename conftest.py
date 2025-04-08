import pytest
from endpoint.create_object import CreateObject
from endpoint.delete_object import DeleteObject
from generators.entity import EntityGenerator
from schemas.entity import EntityCreateRequest


@pytest.fixture
def create_entity():
    creator = CreateObject()
    deleter = DeleteObject()

    # Создаем сущность с валидацией
    payload = EntityCreateRequest.model_validate(EntityGenerator.entity_generator())
    entity = creator.create_entity(payload.model_dump())

    yield entity

    # Очистка
    deleter.delete_entity_by_id(entity.id)


@pytest.fixture
def create_multiple_entities():
    creator = CreateObject()
    deleter = DeleteObject()
    entities = []

    for _ in range(3):
        payload = EntityCreateRequest.model_validate(EntityGenerator.entity_generator())
        entity = creator.create_entity(payload.model_dump())
        entities.append(entity)

    yield entities

    # Очистка
    for entity in entities:
        deleter.delete_entity_by_id(entity.id)