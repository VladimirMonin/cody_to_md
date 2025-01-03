# Cody Chat Exporter 🤖📁

## Описание проекта

Инструмент для экспорта и форматирования чатов с ИИ-ассистентом Cody (Sourcegraph) с расширенными возможностями обработки и визуализации.

### 🌟 Основные возможности

- Импорт чатов из JSON-файла экспорта Cody
- Гибкий выбор чата для просмотра
- Два режима вывода:
  - Терминал
  - Markdown-файл
- Настройка отображения:
  - Включение/исключение контекстных файлов
  - Фильтрация сообщений пользователя
- Форматирование кода в блоках
- Поддержка часовых поясов

### 🛠 Технологический стек

- Python 3.13
- Библиотеки:
  - `pytz` для работы с временными зонами
  - Стандартные библиотеки: `json`, `datetime`

### 📦 Установка

1. Клонировать репозиторий
2. Установить зависимости:

```bash
git clone ...
pip install -r requirements.txt
```

## 🚀 Использование

### Экспорт чатов из Cody

- Зайдите в VSCode
- Откройте меню команд `ctrl + shift + p`
- Выберите `Cody: Export Chat as JSON`
- Выберите путь сохранения
- Укажите имя файла в `main.py` в константе `JSON_FILE_PATH`
- Выполните `main.py`

## 🔜 Планы развития

### Постобработка чатов через ИИ:
- Автоматическое реферирование
- Извлечение ключевых идей
- Генерация саммари

### Экспорт в HTML:
- Создание стильных отчетов
- Интерактивная навигация
- Подсветка кода
- Возможность скопировать код
- Автонаполняемые меню с заголовками

### Дополнительные форматы экспорта:
- PDF
- Docx


## 🤝 Вклад в проект
1. Форкните репозиторий
2. Создайте feature-branch
3. Commit изменений
4. Push и создайте Pull Request

## ⚖️ Лицензия
MIT License

---
### 📦 Installation

1. Clone the repository
2. Install dependencies:


git clone https://github.com/VladimirMonin/cody_to_md.git
pip install -r requirements.txt


## 🚀 Usage

### Export chats from Cody

- Open VSCode
- Open command palette `ctrl + shift + p`
- Select `Cody: Export Chat as JSON`
- Choose save location
- Specify filename in `main.py` in the `JSON_FILE_PATH` constant
- Run `main.py`

## 🔜 Development Plans

### AI Post-processing of Chats:
- Automatic summarization
- Key ideas extraction
- Summary generation

### HTML Export:
- Creating stylish reports
- Interactive navigation
- Code highlighting
- Code copy functionality
- Auto-populated headers menu

### Additional Export Formats:
- PDF
- Docx

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and create a Pull Request

## ⚖️ License
MIT License

---
