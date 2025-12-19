<template>
  <div class="tasks-page">
    <LayoutCard>
      <template #header>
        Список задач
      </template>

      <div v-if="loading" class="loading">
        Загрузка задач...
      </div>

      <div v-else-if="error" class="error-message">
        {{ error }}
      </div>

      <TaskList
        v-else
        :tasks="tasks"
        @toggle-status="toggleTaskStatus"
        @edit="editTask"
        @delete="deleteTask"
      />

      <template #footer>
        <div class="footer-actions">
          <router-link to="/tasks/new" class="btn btn-primary">
            ➕ Создать новую задачу
          </router-link>
        </div>
      </template>
    </LayoutCard>
  </div>
</template>

<script>
import axios from 'axios'
import LayoutCard from '../components/LayoutCard.vue'
import TaskList from '../components/TaskList.vue'

export default {
  name: 'TasksPage',
  components: {
    LayoutCard,
    TaskList
  },
  data() {
    return {
      tasks: [],
      loading: false,
      error: null
    }
  },
  mounted() {
    this.loadTasks()
  },
  methods: {
    async loadTasks() {
      this.loading = true
      this.error = null
      
      try {
        const response = await axios.get('/api/tasks')
        this.tasks = response.data
      } catch (err) {
        this.error = 'Ошибка при загрузке задач: ' + (err.message || 'Неизвестная ошибка')
        console.error(err)
      } finally {
        this.loading = false
      }
    },

    async toggleTaskStatus(taskId) {
      try {
        const task = this.tasks.find(t => t.id === taskId)
        if (!task) return

        const response = await axios.put(`/api/tasks/${taskId}`, {
          ...task,
          completed: !task.completed
        })
        
        const index = this.tasks.findIndex(t => t.id === taskId)
        if (index !== -1) {
          this.tasks[index] = response.data
        }
      } catch (err) {
        alert('Ошибка при обновлении статуса: ' + (err.message || 'Неизвестная ошибка'))
        console.error(err)
      }
    },

    editTask(taskId) {
      this.$router.push({ name: 'task-edit', params: { id: taskId } })
    },

    async deleteTask(taskId) {
      if (!confirm('Вы уверены, что хотите удалить эту задачу?')) {
        return
      }

      try {
        await axios.delete(`/api/tasks/${taskId}`)
        this.tasks = this.tasks.filter(t => t.id !== taskId)
      } catch (err) {
        alert('Ошибка при удалении задачи: ' + (err.message || 'Неизвестная ошибка'))
        console.error(err)
      }
    }
  }
}
</script>

<style scoped>
.tasks-page {
  max-width: 900px;
  margin: 0 auto;
}

.loading {
  text-align: center;
  padding: 40px;
  font-size: 1.2rem;
  color: #666;
}

.error-message {
  padding: 20px;
  background-color: #ffebee;
  color: #c62828;
  border-radius: 5px;
  text-align: center;
}

.footer-actions {
  display: flex;
  justify-content: center;
}
</style>
