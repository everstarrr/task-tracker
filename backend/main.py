from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Task, TaskCreate, TaskUpdate
import sqlite3
from datetime import datetime
from typing import List
import json

app = FastAPI(title="Task Manager API")

# CORS настройки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            priority TEXT DEFAULT 'medium',
            category TEXT DEFAULT 'other',
            important INTEGER DEFAULT 0,
            completed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()


def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/")
async def root():
    return {"message": "Task Manager API"}


@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """Получить все задачи"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    
    tasks = []
    for row in rows:
        tasks.append({
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "priority": row["priority"],
            "category": row["category"],
            "important": bool(row["important"]),
            "completed": bool(row["completed"]),
            "created_at": row["created_at"]
        })
    
    return tasks


@app.get("/api/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Получить задачу по ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "priority": row["priority"],
        "category": row["category"],
        "important": bool(row["important"]),
        "completed": bool(row["completed"]),
        "created_at": row["created_at"]
    }


@app.post("/api/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Создать новую задачу"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO tasks (title, description, priority, category, important, completed)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        task.title,
        task.description,
        task.priority,
        task.category,
        int(task.important),
        int(task.completed)
    ))
    
    conn.commit()
    task_id = cursor.lastrowid
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    conn.close()
    
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "priority": row["priority"],
        "category": row["category"],
        "important": bool(row["important"]),
        "completed": bool(row["completed"]),
        "created_at": row["created_at"]
    }


@app.put("/api/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskUpdate):
    """Обновить задачу"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    cursor.execute('''
        UPDATE tasks
        SET title = ?, description = ?, priority = ?, category = ?, important = ?, completed = ?
        WHERE id = ?
    ''', (
        task.title,
        task.description,
        task.priority,
        task.category,
        int(task.important),
        int(task.completed),
        task_id
    ))
    
    conn.commit()
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    conn.close()
    
    return {
        "id": row["id"],
        "title": row["title"],
        "description": row["description"],
        "priority": row["priority"],
        "category": row["category"],
        "important": bool(row["important"]),
        "completed": bool(row["completed"]),
        "created_at": row["created_at"]
    }


@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int):
    """Удалить задачу"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    
    return {"message": "Задача успешно удалена"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
