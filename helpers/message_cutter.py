from typing import Tuple


def split_message(message, max_length=4096):
    chunks = []
    current_chunk = ""
    open_tags = []

    i = 0
    while i < len(message):
        # Если текущий кусок достиг максимальной длины, добавляем его в список
        if len(current_chunk) >= max_length:
            # Закрываем все открытые теги
            for tag in reversed(open_tags):
                current_chunk += f"</{tag}>"
            chunks.append(current_chunk)
            current_chunk = ""
            open_tags = []

        # Обрабатываем открывающие теги
        if message[i] == '<' and i + 1 < len(message) and message[i + 1] != '/':
            tag_end = message.find('>', i)
            if tag_end != -1:
                tag = message[i + 1:tag_end].split()[0]  # Извлекаем имя тега
                open_tags.append(tag)
                current_chunk += message[i:tag_end + 1]
                i = tag_end + 1
                continue

        # Обрабатываем закрывающие теги
        if message[i] == '<' and i + 1 < len(message) and message[i + 1] == '/':
            tag_end = message.find('>', i)
            if tag_end != -1:
                tag = message[i + 2:tag_end]  # Извлекаем имя тега
                if tag in open_tags:
                    open_tags.remove(tag)
                current_chunk += message[i:tag_end + 1]
                i = tag_end + 1
                continue

        # Добавляем символ в текущий кусок
        current_chunk += message[i]
        i += 1

    # Добавляем последний кусок, если он не пустой
    if current_chunk:
        # Закрываем все открытые теги
        for tag in reversed(open_tags):
            current_chunk += f"</{tag}>"
        chunks.append(current_chunk)

    return tuple(chunks)
