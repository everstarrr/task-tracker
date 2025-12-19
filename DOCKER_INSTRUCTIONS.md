# Инструкция по запуску через Docker

## Шаг 1: Подготовка

Убедитесь, что установлены:
- Docker Desktop (Windows/Mac) или Docker Engine (Linux)
- Docker Compose

## Шаг 2: Сборка и запуск

Из корневой директории проекта выполните:

```bash
docker-compose up --build
```

Первая сборка займёт несколько минут.

## Шаг 3: Проверка

После запуска должны быть доступны:

1. **Frontend:** http://localhost:3000
   - Главная страница с приветствием
   - Список задач
   - Создание/редактирование задач

2. **Backend API:** http://localhost:8000
   - Swagger документация: http://localhost:8000/docs

3. **Логи:**
   ```bash
   docker-compose logs -f frontend
   docker-compose logs -f backend
   ```

## Шаг 4: Остановка

```bash
# Остановить контейнеры
docker-compose down

# Остановить и удалить volumes (очистить БД)
docker-compose down -v
```

## Проверка работы

1. Откройте http://localhost:3000
2. Создайте несколько задач через форму
3. Проверьте фильтрацию и сортировку
4. Отредактируйте задачу
5. Удалите задачу
6. Перезапустите контейнеры - данные должны сохраниться

## Устранение проблем

### Порты заняты
```bash
# Проверить занятые порты
netstat -ano | findstr :3000
netstat -ano | findstr :8000

# Изменить порты в docker-compose.yml
```

### Ошибки сборки
```bash
# Очистить всё и пересобрать
docker-compose down -v
docker system prune -a
docker-compose up --build
```

### База данных
```bash
# Посмотреть содержимое volume
docker volume inspect vscode-projects_backend-data

# Зайти внутрь контейнера backend
docker exec -it task-manager-backend /bin/sh
ls -la /app
```
