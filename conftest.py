import pytest
from endpoint.create_object import CreateObject
from endpoint.delete_object import DeleteObject
from generators.entity import EntityGenerator


@pytest.fixture()
def create_entity():

    create_endpoint = CreateObject()
    payload = EntityGenerator.random()
    create_endpoint.create_entity(payload)
    yield create_endpoint.response_txt, payload

    delete_endpoint = DeleteObject()
    delete_endpoint.delete_entity_by_id(create_endpoint.response_txt)


@pytest.fixture()
def create_multiple_entities():

    create_endpoint = CreateObject()
    entities = []
    for _ in range(3):
        payload = EntityGenerator.random()
        create_endpoint.create_entity(payload)
        entities.append((create_endpoint.response_txt, payload))
    yield entities

    delete_endpoint = DeleteObject()
    for entity_id, _ in entities:
        delete_endpoint.delete_entity_by_id(entity_id)