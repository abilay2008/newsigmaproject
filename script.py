from pyscript import Element

# Пример текста, который будет отображаться
sample_text = """
This is a Python project about text.
Another project written in python but has some error.
Random line with no keyword.
python project without error!
Welcome to the Python-based search app.
"""

# Отображаем sample_text при загрузке
Element("text-display").write(sample_text.strip())

# Функция поиска
def search_word(*args):
    keyword = Element("search-word").element.value.strip().lower()
    lines = sample_text.strip().splitlines()

    if not keyword:
        Element("output").write("Пожалуйста, введите слово для поиска.")
        return

    found = []
    for i, line in enumerate(lines, 1):
        if keyword in line.lower():
            found.append(f"Строка {i}: {line.strip()}")

    if found:
        result = f"Найдено {len(found)} вхождений слова «{keyword}»:\n\n" + "\n".join(found)
    else:
        result = f"Слово «{keyword}» не найдено."

    Element("output").write(result)
