from markdown_formatter import format_markdown, save_to_markdown, format_code_block
from typing import Dict, List
import json
from datetime import datetime
import pytz
import os

# Константы
JSON_FILE_PATH = "C:\\Users\\user\\Documents\\chat.json"
TIMEZONE = "Asia/Yekaterinburg"
DATE_FORMAT = "%d.%m.%Y %H:%M:%S"


def format_timestamp(timestamp: str) -> str:
    """Форматирование временной метки в удобочитаемый вид"""
    dt = datetime.strptime(timestamp, "%a, %d %b %Y %H:%M:%S GMT")
    local_dt = pytz.timezone(TIMEZONE).fromutc(dt)
    return local_dt.strftime(DATE_FORMAT)


def load_json_data(file_path: str) -> Dict:
    """Загрузка данных из JSON файла"""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_chat_timestamps(data: Dict) -> List[tuple]:
    """Получение списка всех временных меток чатов с форматированием"""
    timestamps = list(data["chat"].keys())
    return [(ts, format_timestamp(ts)) for ts in timestamps]


def format_messages(
    data: Dict, timestamp: str, include_context: bool = True
) -> List[Dict]:
    chat = data["chat"].get(timestamp)
    if not chat or not chat.get("interactions"):
        return []

    formatted_messages = []
    for interaction in chat["interactions"]:
        # Сообщение пользователя
        if "humanMessage" in interaction:
            message = {
                "role": "Пользователь",
                "text": interaction["humanMessage"]["text"],
                "context": [],
            }
            formatted_messages.append(message)

        # Сообщение ассистента
        if "assistantMessage" in interaction:
            message = {
                "role": "ИИ",
                "text": interaction["assistantMessage"]["text"],
                "context": [],
            }
            formatted_messages.append(message)

    return formatted_messages


def print_terminal_messages(messages: List[Dict]) -> None:
    """Вывод сообщений в терминал"""
    for message in messages:
        print(f"РОЛЬ: {message['role']}")
        print(f"ТЕКСТ: {message['text']}")
        if message["context"]:
            print("\nПРИКРЕПЛЕННЫЕ ФАЙЛЫ:")
            for file_path in message["context"]:
                print(f"- {file_path}")
        print("---\n")


def print_available_chats(timestamps: List[tuple]) -> None:
    """Вывод списка доступных чатов"""
    print("Доступные чаты:")
    for i, (original_ts, formatted_ts) in enumerate(timestamps, 1):
        print(f"{i}. {formatted_ts}")


def main():
    data = load_json_data(JSON_FILE_PATH)
    timestamps = get_all_chat_timestamps(data)
    print_available_chats(timestamps)

    try:
        choice = int(input("\nВыберите номер чата: ")) - 1
        include_context = (
            input("Показывать прикрепленные файлы? (да/нет): ").lower() == "да"
        )
        include_user = (
            input("Включать сообщения пользователя? (да/нет): ").lower() == "да"
        )
        output_choice = input(
            "Выберите формат вывода (1 - терминал, 2 - markdown файл): "
        )

        selected_timestamp = timestamps[choice][0]
        formatted_date = timestamps[choice][1]

        # Получаем все сообщения
        all_messages = format_messages(data, selected_timestamp, include_context)
        # Фильтруем сообщения если нужно
        messages = [msg for msg in all_messages if include_user or msg["role"] == "ИИ"]

        if output_choice == "1":
            print(f"\nСообщения чата от {formatted_date}:\n")
            print_terminal_messages(messages)
        elif output_choice == "2":
            content = format_markdown(messages, selected_timestamp, formatted_date)
            filename = save_to_markdown(content, formatted_date)
            print(f"\nЧат сохранен в файл: {filename}")
        else:
            print("Некорректный выбор формата вывода")

    except (ValueError, IndexError):
        print("Некорректный выбор чата")


if __name__ == "__main__":
    main()
