import allure
from endpoint.create_object import CreateObject
from endpoint.delete_object import DeleteObject
from endpoint.get_all_object import GetAllObjects
from endpoint.get_object import GetObject
from endpoint.update_object import UpdateObject
from generators.entity import EntityGenerator
from schemas.entity import *


@allure.feature('API Тесты')
class TestEntityAPI:

    @allure.title('TC1: Создание и проверка сущности')
    def test_create_and_verify_entity(self):
        creator = CreateObject()
        getter = GetObject()
        payload = EntityCreateRequest.model_validate(EntityGenerator.entity_generator())

        created_entity = creator.create_entity(payload.model_dump())
        creator.check_status_code(201)

        retrieved_entity = getter.get_entity_by_id(created_entity.id)
        getter.check_status_code(200)
        assert retrieved_entity == created_entity

        DeleteObject().delete_entity_by_id(created_entity.id).check_status_code(204)

    @allure.title('TC2: Получение списка сущностей')
    def test_get_all_entities(self, create_multiple_entities):
        entities = create_multiple_entities  # Фикстура сама удалит сущности после теста
        getter = GetAllObjects()

        all_entities = getter.get_all_entities()
        getter.check_status_code(200)
        assert len(all_entities) >= len(entities)

    @allure.title('TC3: Обновление сущности')
    def test_update_entity(self):
        # Создаем сущность напрямую для этого теста
        creator = CreateObject()
        entity = creator.create_entity(
            EntityGenerator.entity_generator()
        )
        creator.check_status_code(201)

        # Тест обновления
        updater = UpdateObject()
        new_data = EntityUpdateRequest(title="New Title")
        updater.update_entity_by_id(entity.id, new_data.model_dump())
        updater.check_status_code(204)

        # Проверка
        updated = GetObject().get_entity_by_id(entity.id)
        assert updated.title == "New Title"

        # Очистка
        DeleteObject().delete_entity_by_id(entity.id).check_status_code(204)

    @allure.title('Удаление сущности')
    def test_delete_entity(self):
        # Создаем сущность для удаления
        entity = CreateObject().create_entity(
            EntityGenerator.entity_generator()
        )

        # Удаление
        DeleteObject().delete_entity_by_id(entity.id).check_status_code(204)

        # Проверка что удалилась
        response = GetObject().get_entity_by_id(entity.id)
        assert response.status_code == 404