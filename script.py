from pyscript import Element

# Содержимое sample.txt — вставим прямо сюда, чтобы всё было в одном
sample_text = """
This is a Python project about text.
Another project written in python but has some error.
Random line with no keyword.
python project without error!
Welcome to the Python-based search app.
"""

# Показываем текст в поле
Element("input-text").write(sample_text.strip())

def search_word(*args):
    text = sample_text.strip().splitlines()
    keyword = Element("search-word").element.value.strip().lower()

    if not keyword:
        Element("output").write("Пожалуйста, введите слово для поиска.")
        return

    found_lines = []
    for i, line in enumerate(text, 1):
        if keyword in line.lower():
            found_lines.append(f"Строка {i}: {line.strip()}")

    if found_lines:
        result = f"Найдено {len(found_lines)} вхождений слова «{keyword}»:\n\n" + "\n".join(found_lines)
    else:
        result = f"Слово «{keyword}» не найдено."

    Element("output").write(result)
