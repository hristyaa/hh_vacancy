import re


def strip_tags(text):
    """Удаляет HTML-теги из строки"""
    if not text:
        return "Описание отсутствует"
    clean = re.sub(r"<.*?>", "", text)
    return clean.strip()
