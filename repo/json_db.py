import json
import os


class JsonDB:
    def __init__(self):
        self.path = "db.json"
        self.file_exist_or_make()

    def file_exist_or_make(self):
        if not os.path.exists(self.path):
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(
                    {
                        "checked": []
                    },
                    file,
                    ensure_ascii=False,
                    indent=4
                )

    def add_checked(self, item):
        """Добавляет новый элемент в список 'checked' в файле."""
        # Читаем данные из файла
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Добавляем элемент в список "checked"
        if item not in data["checked"]:
            data["checked"].append(item)

            # Перезаписываем файл с обновленными данными
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    def get_checked_list(self):
        """Возвращает список элементов из ключа 'checked'."""
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get("checked", [])
