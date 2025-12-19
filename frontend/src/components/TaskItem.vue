<template>
  <div class="task-item" :class="{ 'task-completed': task.completed }">
    <div class="task-content">
      <div class="task-header">
        <h3 class="task-title">{{ task.title }}</h3>
        <span class="task-priority" :class="`priority-${task.priority}`">
          {{ priorityLabel }}
        </span>
      </div>
      <p class="task-description">{{ task.description }}</p>
      <div class="task-meta">
        <span class="task-category">📁 {{ task.category }}</span>
        <span v-if="task.important" class="task-important">⭐ Важно</span>
        <span class="task-date">📅 {{ formatDate(task.created_at) }}</span>
      </div>
    </div>
    <div class="task-actions">
      <button 
        @click="$emit('toggle-status', task.id)" 
        class="btn btn-sm"
        :class="task.completed ? 'btn-warning' : 'btn-primary'"
      >
        {{ task.completed ? '↩ Вернуть' : '✓ Выполнено' }}
      </button>
      <button @click="$emit('edit', task.id)" class="btn btn-sm btn-secondary">
        ✏ Редактировать
      </button>
      <button @click="$emit('delete', task.id)" class="btn btn-sm btn-danger">
        🗑 Удалить
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TaskItem',
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  emits: ['toggle-status', 'edit', 'delete'],
  computed: {
    priorityLabel() {
      const labels = {
        high: 'Высокий',
        medium: 'Средний',
        low: 'Низкий'
      }
      return labels[this.task.priority] || this.task.priority
    }
  },
  methods: {
    formatDate(dateString) {
      if (!dateString) return ''
      const date = new Date(dateString)
      return date.toLocaleDateString('ru-RU', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  }
}
</script>

<style scoped>
.task-item {
  background: white;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.task-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.task-completed {
  opacity: 0.7;
  background: #f9f9f9;
}

.task-completed .task-title {
  text-decoration: line-through;
  color: #999;
}

.task-content {
  margin-bottom: 15px;
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  flex-wrap: wrap;
  gap: 10px;
}

.task-title {
  font-size: 1.3rem;
  color: #333;
}

.task-priority {
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
}

.priority-high {
  background-color: #ffebee;
  color: #c62828;
}

.priority-medium {
  background-color: #fff3e0;
  color: #e65100;
}

.priority-low {
  background-color: #e8f5e9;
  color: #2e7d32;
}

.task-description {
  color: #666;
  margin-bottom: 10px;
  line-height: 1.6;
}

.task-meta {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  font-size: 0.9rem;
  color: #777;
}

.task-important {
  color: #ff9800;
  font-weight: 600;
}

.task-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn-sm {
  padding: 8px 15px;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .task-actions {
    flex-direction: column;
  }
  
  .task-actions button {
    width: 100%;
  }
}
</style>
