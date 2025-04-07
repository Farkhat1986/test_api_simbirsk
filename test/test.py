from endpoint.create_object import CreateObject
from endpoint.delete_object import DeleteObject
from endpoint.get_all_object import GetAllObjects
from endpoint.get_object import GetObject
from endpoint.update_object import UpdateObject
from generators.entity import EntityGenerator
from schemas.entity import Entity
import allure


@allure.feature('ServiceTest')
@allure.title('Получение создание сущности')
@allure.description("""
    Цель: Проверить создание сущности

    Шаги:
    1. Сделать запрос на создание сущности
    2. Проверить статус ответа""")
def test_create_entity():
    with allure.step("Запрос на создание сущности"):
        payload = EntityGenerator.random()
        new_object_endpoint = CreateObject()
        new_object_endpoint.create_entity(payload)
        temp_entity_id = new_object_endpoint.response_txt

    with allure.step("Проверка статуса ответа сервиса"):
        new_object_endpoint.check_status_code(200)
        new_object_endpoint.check_type_response()

    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_entity_by_id(temp_entity_id)


@allure.feature('ServiceTest')
@allure.title('Удаление сущности')
@allure.description("""
    Цель: Проверить удаление сущности

    Шаги:
    1. Сделать запрос на удаление сущности
    2. Проверить статус ответа""")
def test_delete_entity(obj_id):
    with allure.step("Запрос на удаление сущности"):
        delete_obj_endpoint = DeleteObject()
        delete_obj_endpoint.delete_entity_by_id(obj_id)

    with allure.step("Проверка статуса ответа сервиса"):
        delete_obj_endpoint.check_status_code(204)


@allure.feature('ServiceTest')
@allure.title('Получение сущности')
@allure.description("""
    Цель: Проверить получение сущности

    Шаги:
    1. Сделать запрос на получение сущности
    2. Проверить статус ответа
    3. Валидировать полученные данные""")
def test_get_entity(obj_id):
    with allure.step("Запрос на получение сущности"):
        get_obj_endpoint = GetObject()
        get_obj_endpoint.get_entity_by_id(obj_id)

    with allure.step("Проверка статуса ответа сервиса"):
        get_obj_endpoint.check_status_code(200)

    with allure.step("Проверка валидности полученных данных"):
        get_obj_endpoint.check_validate_response(Entity)


@allure.feature('ServiceTest')
@allure.title('Получение всех сущностей')
@allure.description("""
    Цель: Проверить получение всех сущностей

    Шаги:
    1. Сделать запрос на получение всех сущностей
    2. Проверить статус ответа
    3. Валидировать полученные данные""")
def test_get_all_entities():
    with allure.step("Запрос на получение всех сущностей"):
        get_all_objs_endpoint = GetAllObjects()
        get_all_objs_endpoint.get_all_entities()

    with allure.step("Проверка статуса ответа сервиса"):
        get_all_objs_endpoint.check_status_code(200)
    with allure.step("Проверка валидности полученных данных"):
        get_all_objs_endpoint.check_validate_response(Entity)


@allure.feature('ServiceTest')
@allure.title('Обновление сущности')
@allure.description("""
    Цель: Проверить обновление сущности

    Шаги:
    1. Сделать запрос на обновление сущности
    2. Проверить статус ответа""")
def test_update_entity(obj_id):
    with allure.step("Запрос на обновление сущности"):
        payload = EntityGenerator.random()
        update_obj_endpoint = UpdateObject()
        update_obj_endpoint.update_entity_by_id(obj_id, payload)

    with allure.step("Проверка статуса ответа сервиса"):
        update_obj_endpoint.check_status_code(204)