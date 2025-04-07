import allure
from endpoint.delete_object import DeleteObject
from endpoint.get_all_object import GetAllObjects
from endpoint.get_object import GetObject
from endpoint.update_object import UpdateObject
from generators.entity import EntityGenerator



@allure.feature('ServiceTest')
@allure.title('Получить данные сущности и сравнить с созданными')
def test_get_entity_and_compare(create_entity):
    entity_id, payload = create_entity
    get_obj_endpoint = GetObject()

    with allure.step("Получить сущность по ID"):
        get_obj_endpoint.get_entity_by_id(entity_id)
        get_obj_endpoint.check_status_code(200)
        response_data = get_obj_endpoint.response_json

    with allure.step("Сравнить данные с payload"):
        assert response_data["title"] == payload["title"], "Название не совпадает"
        assert response_data["verified"] == payload["verified"], "Статус verified не совпадает"
        assert response_data["addition"]["additional_info"] == payload["addition"]["additional_info"], "Доп. информация не совпадает"


@allure.feature('ServiceTest')
@allure.title('Получить список сущностей и проверить количество')
def test_get_all_entities_and_check_count(create_multiple_entities):
    entities = create_multiple_entities
    get_all_endpoint = GetAllObjects()

    with allure.step("Получить все сущности"):
        get_all_endpoint.get_all_entities()
        get_all_endpoint.check_status_code(200)
        all_entities = get_all_endpoint.response_json

    with allure.step("Проверить количество сущностей"):
        assert len(all_entities) == len(entities), "Количество сущностей не совпадает"


@allure.feature('ServiceTest')
@allure.title('Проверить, что сущность появилась в списке после создания')
def test_check_entity_in_list_after_creation(create_entity):
    entity_id, payload = create_entity
    get_all_endpoint = GetAllObjects()

    with allure.step("Получить все сущности"):
        get_all_endpoint.get_all_entities()
        all_entities = get_all_endpoint.response_json

    with allure.step("Найти созданную сущность в списке"):
        found = False
        for entity in all_entities:
            if entity["id"] == int(entity_id):
                assert entity["title"] == payload["title"], "Название не совпадает"
                found = True
        assert found, "Сущность не найдена в списке"


@allure.feature('ServiceTest')
@allure.title('Обновить сущность и проверить изменения')
def test_update_entity_and_verify(create_entity):
    entity_id, _ = create_entity
    update_endpoint = UpdateObject()
    new_payload = EntityGenerator.random()

    with allure.step("Обновить сущность"):
        update_endpoint.update_entity_by_id(entity_id, new_payload)
        update_endpoint.check_status_code(204)

    with allure.step("Проверить обновленные данные"):
        get_endpoint = GetObject()
        get_endpoint.get_entity_by_id(entity_id)
        updated_data = get_endpoint.response_json
        assert updated_data["title"] == new_payload["title"], "Название не обновилось"
        assert updated_data["addition"]["additional_info"] == new_payload["addition"]["additional_info"], "Доп. информация не обновилась"


@allure.feature('ServiceTest')
@allure.title('Удалить сущность и проверить её отсутствие в списке')
def test_delete_entity_and_check_absence(create_multiple_entities):
    entities = create_multiple_entities
    entity_to_delete = entities[0][0]  # Берём первую сущность
    delete_endpoint = DeleteObject()

    with allure.step("Удалить сущность"):
        delete_endpoint.delete_entity_by_id(entity_to_delete)
        delete_endpoint.check_status_code(204)

    with allure.step("Проверить, что сущности нет в списке"):
        get_all_endpoint = GetAllObjects()
        get_all_endpoint.get_all_entities()
        remaining_entities = get_all_endpoint.response_json
        remaining_ids = [entity["id"] for entity in remaining_entities]
        assert int(entity_to_delete) not in remaining_ids, "Сущность не удалилась"