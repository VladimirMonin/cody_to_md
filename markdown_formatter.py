from typing import Dict, List
from datetime import datetime


# Шаблоны для Markdown

OBSIDIAN_DATE_FORMAT = '%Y-%m-%d'
MD_TEMPLATE = """---
project: cody_chat
date: {date}
---

# Чат от {formatted_date}

{content}"""

MESSAGE_TEMPLATE = """### {role}
{text}
{context}
"""

DIALOG_SEPARATOR = "\n---\n\n"

def format_code_block(text: str) -> str:
    """
    Форматирование блоков кода:
    - Удаление двоеточия после языка
    - Добавление названия файла курсивом перед блоком
    """
    lines = text.split('\n')
    formatted_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('```'):
            if ':' in line:
                parts = line.split(':')
                language = parts[0].replace('```', '')
                if len(parts) > 1 and parts[1].strip():
                    # Есть имя файла
                    filename = parts[1].strip()
                    formatted_lines.append(f"*{filename}*\n")
                    formatted_lines.append(f"```{language}")
                else:
                    # Только язык
                    formatted_lines.append(f"```{language}")
            else:
                formatted_lines.append(line)
        else:
            formatted_lines.append(line)
        i += 1
    return '\n'.join(formatted_lines)

def get_obsidian_date(timestamp: str) -> str:
    """Получение даты в формате Obsidian"""
    dt = datetime.strptime(timestamp, '%a, %d %b %Y %H:%M:%S GMT')
    return dt.strftime(OBSIDIAN_DATE_FORMAT)

def format_markdown(messages: List[Dict], timestamp: str, formatted_date: str) -> str:
    """Форматирование сообщений в Markdown"""
    content = []
    
    for i in range(0, len(messages), 2):
        pair = []
        # Добавляем первое сообщение пары
        message = messages[i]
        context_text = ""
        if message['context']:
            context_text = "\nПрикрепленные файлы:\n" + "\n".join(f"- {path}" for path in message['context'])
        pair.append(MESSAGE_TEMPLATE.format(
            role=message['role'],
            text=message['text'],
            context=context_text
        ))
        
        # Добавляем второе сообщение пары, если оно есть
        if i + 1 < len(messages):
            message = messages[i + 1]
            context_text = ""
            if message['context']:
                context_text = "\nПрикрепленные файлы:\n" + "\n".join(f"- {path}" for path in message['context'])
            pair.append(MESSAGE_TEMPLATE.format(
                role=message['role'],
                text=message['text'],
                context=context_text
            ))
        
        content.append("".join(pair) + DIALOG_SEPARATOR)
    
    return MD_TEMPLATE.format(
        date=get_obsidian_date(timestamp),
        formatted_date=formatted_date,
        content="".join(content)
    )

def save_to_markdown(content: str, chat_date: str) -> str:
    """Сохранение чата в MD файл"""
    filename = f"chat_{chat_date.replace(':', '-').replace(' ', '_')}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return filename
