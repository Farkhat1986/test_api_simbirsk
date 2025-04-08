from faker import Faker

fake = Faker('ru-RU')


class AdditionGenerator:
    @staticmethod
    def filling_entity():
        additional_info = fake.text()
        additional_number = fake.random_int(0, 100)
        return {
            "additional_info": additional_info,
            "additional_number": additional_number
        }


class EntityGenerator:
    @staticmethod
    def entity_generator():
        important_numbers = [fake.random_int(0, 100) for _ in range(fake.random_int(1, 5))]
        title = fake.word()
        verified = fake.boolean()
        addition = AdditionGenerator.filling_entity()
        return {
            "important_numbers": important_numbers,
            "title": title,
            "verified": verified,
            "addition": addition
        }