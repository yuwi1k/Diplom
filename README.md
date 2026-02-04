# 📊 Brand Analytics Dashboard

Дипломный проект: система анализа тональности отзывов о брендах  
(Flask + RuBERT Sentiment + SQLite + Dashboard)

---

## 🚀 Возможности

- Ручной ввод отзывов и анализ тональности
- Генерация тестовых отзывов
- Хранение истории в SQLite
- Диаграмма распределения тональности
- Пагинация отзывов ("Загрузить ещё")

---

## 🛠 Стек

- Flask
- SQLAlchemy (SQLite)
- HuggingFace Transformers (RuBERT)
- Chart.js

---

## 📂 Структура проекта

project/
├── client/
│ ├── index.html
│ ├── script.js
│ └── style.css
│
├── server/
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── db_init.py
│ └── services/
│ ├── nlp_service.py
│ └── generator.py
│
├── requirements.txt
└── README.md

yaml
Копировать код

---

## ⚙️ Установка и запуск

### 1) Клонировать репозиторий

```bash
git clone https://github.com/USERNAME/brand-analytics.git
cd brand-analytics
2) Создать виртуальное окружение
bash
Копировать код
python -m venv venv
Активировать:

Windows:

bash
Копировать код
venv\Scripts\activate
Linux/Mac:

bash
Копировать код
source venv/bin/activate
3) Установить зависимости
bash
Копировать код
pip install -r requirements.txt
4) Создать базу данных
bash
Копировать код
cd server
python db_init.py
5) Запустить сервер
bash
Копировать код
python app.py
🌐 Интерфейс
Открыть в браузере:

cpp
Копировать код
http://127.0.0.1:5000/
📌 API Endpoints
Метод	URL	Описание
POST	/api/analyze	анализ введённого текста
GET	/api/generate	генерация тестового отзыва
GET	/api/stats	статистика тональности
GET	/api/reviews?page=1	отзывы с пагинацией

