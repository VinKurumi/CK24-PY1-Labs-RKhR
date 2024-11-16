import json


def task(file_path: str) -> float:
    with open(file_path, 'r') as file:  # Открывает файл в режиме чтения
        data = json.load(file)  # Читает содержимое файла как список словарей

    # Вычисляет сумму произведений значений по ключам в словарях с проверкой наличия этих ключей
    total = sum(value["score"] * value["weight"] for value in data if "score" in value and "weight" in value)

    return round(total, 3)  # Округляет результат до 3 знаков после запятой


print(task('input.json'))  # Вызывает функцию с указанием пути к файлу
