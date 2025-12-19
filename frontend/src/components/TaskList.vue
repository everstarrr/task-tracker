<template>
  <div class="task-list">
    <div class="filters-section">
      <div class="filter-group">
        <label>Статус:</label>
        <select v-model="filterStatus" class="filter-select">
          <option value="all">Все</option>
          <option value="active">Активные</option>
          <option value="completed">Выполненные</option>
        </select>
      </div>
      <div class="filter-group">
        <label>Сортировка:</label>
        <select v-model="sortBy" class="filter-select">
          <option value="date">По дате</option>
          <option value="title">По алфавиту</option>
          <option value="priority">По приоритету</option>
        </select>
      </div>
    </div>

    <div v-if="filteredAndSortedTasks.length === 0" class="empty-state">
      <p>📝 Задач пока нет</p>
      <router-link to="/tasks/new" class="btn btn-primary">
        Создать первую задачу
      </router-link>
    </div>

    <div v-else>
      <TaskItem
        v-for="task in filteredAndSortedTasks"
        :key="task.id"
        :task="task"
        @toggle-status="$emit('toggle-status', $event)"
        @edit="$emit('edit', $event)"
        @delete="$emit('delete', $event)"
      />
    </div>
  </div>
</template>

<script>
import TaskItem from './TaskItem.vue'

export default {
  name: 'TaskList',
  components: {
    TaskItem
  },
  props: {
    tasks: {
      type: Array,
      required: true
    }
  },
  emits: ['toggle-status', 'edit', 'delete'],
  data() {
    return {
      filterStatus: 'all',
      sortBy: 'date'
    }
  },
  computed: {
    filteredAndSortedTasks() {
      let result = [...this.tasks]

      // Фильтрация
      if (this.filterStatus === 'active') {
        result = result.filter(task => !task.completed)
      } else if (this.filterStatus === 'completed') {
        result = result.filter(task => task.completed)
      }

      // Сортировка
      if (this.sortBy === 'date') {
        result.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      } else if (this.sortBy === 'title') {
        result.sort((a, b) => a.title.localeCompare(b.title, 'ru'))
      } else if (this.sortBy === 'priority') {
        const priorityOrder = { high: 1, medium: 2, low: 3 }
        result.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority])
      }

      return result
    }
  }
}
</script>

<style scoped>
.task-list {
  width: 100%;
}

.filters-section {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  flex-wrap: wrap;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
  flex: 1;
  min-width: 200px;
}

.filter-group label {
  font-weight: 600;
  color: #333;
}

.filter-select {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
}

.filter-select:focus {
  outline: none;
  border-color: #667eea;
}

.empty-state {
  text-align: center;
  padding: 60px 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.empty-state p {
  font-size: 1.5rem;
  color: #999;
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  .filters-section {
    flex-direction: column;
  }
}
</style>
