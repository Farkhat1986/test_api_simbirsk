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
        # Подготовка
        creator = CreateObject()
        getter = GetObject()
        payload = EntityCreateRequest.model_validate(EntityGenerator.entity_generator())

        # Действие
        created_entity = creator.create_entity(payload.model_dump())
        creator.check_status_code(201)

        # Проверка
        retrieved_entity = getter.get_entity_by_id(created_entity.id)
        getter.check_status_code(200)

        assert retrieved_entity == created_entity, "Сущность не соответствует созданной"

        # Очистка
        DeleteObject().delete_entity_by_id(created_entity.id)

    @allure.title('TC2: Получение списка сущностей')
    def test_get_all_entities(self, create_multiple_entities):
        # Подготовка
        entities = create_multiple_entities
        getter = GetAllObjects()

        # Действие
        all_entities = getter.get_all_entities()
        getter.check_status_code(200)

        # Проверка
        assert len(all_entities) >= len(entities), "Не все созданные сущности получены"

    @allure.title('TC3: Обновление сущности')
    def test_update_entity(self, create_entity):
        # Подготовка
        entity_id, _ = create_entity
        updater = UpdateObject()
        getter = GetObject()
        new_data = EntityUpdateRequest.model_validate(EntityGenerator.entity_generator())

        # Действие
        updater.update_entity_by_id(entity_id, new_data.model_dump(exclude_unset=True))
        updater.check_status_code(204)

        # Проверка
        updated_entity = getter.get_entity_by_id(entity_id)
        assert updated_entity.title == new_data.title, "Название не обновилось"