# Task Manager - Менеджер задач

Мини-приложение с клиентской частью на Vue 3 и серверной частью на Python FastAPI.

## Возможности

- ✅ Отображение списка задач
- ✅ Создание новой задачи
- ✅ Редактирование задачи
- ✅ Удаление задачи
- ✅ Фильтрация и сортировка задач
- ✅ Роутинг с Vue Router
- ✅ Компоненты и слоты
- ✅ Хранение данных в SQLite
- ✅ Запуск через Docker

## Структура проекта

```
/
├── frontend/          # Vue 3 приложение
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   └── main.js
│   ├── Dockerfile
│   └── package.json
│
├── backend/           # FastAPI сервер
│   ├── main.py
│   ├── models.py
│   ├── tasks.db
│   ├── Dockerfile
│   └── requirements.txt
│
└── docker-compose.yml
```

## Запуск

### С Docker (рекомендуется)

1. Убедитесь, что Docker и Docker Compose установлены
2. Запустите проект:

```bash
docker-compose up --build
```

3. Откройте в браузере:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

4. Остановка:
```bash
docker-compose down
```

### Локально (для разработки)

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Backend запустится на http://localhost:8000

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```
Frontend запустится на http://localhost:3000

**Важно:** Для локальной разработки vite.config.js должен использовать `localhost:8000` для прокси.

## API Endpoints

- `GET /api/tasks` - Получить все задачи
- `GET /api/tasks/{id}` - Получить задачу по ID
- `POST /api/tasks` - Создать задачу
- `PUT /api/tasks/{id}` - Обновить задачу
- `DELETE /api/tasks/{id}` - Удалить задачу

## Технологии

- **Frontend:** Vue 3, Vue Router, Vite, Axios
- **Backend:** Python, FastAPI, SQLite
- **DevOps:** Docker, Docker Compose
