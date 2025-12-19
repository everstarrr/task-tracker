<template>
  <div class="task-edit-page">
    <LayoutCard>
      <template #header>
        Редактировать задачу
      </template>

      <div v-if="loading" class="loading">
        Загрузка задачи...
      </div>

      <div v-else-if="error" class="error-message">
        {{ error }}
      </div>

      <TaskForm
        v-else
        :initial-data="task"
        submit-label="Сохранить изменения"
        @submit="updateTask"
        @cancel="goBack"
      />
    </LayoutCard>
  </div>
</template>

<script>
import axios from 'axios'
import LayoutCard from '../components/LayoutCard.vue'
import TaskForm from '../components/TaskForm.vue'

export default {
  name: 'TaskEdit',
  components: {
    LayoutCard,
    TaskForm
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      task: null,
      loading: false,
      error: null
    }
  },
  mounted() {
    this.loadTask()
  },
  methods: {
    async loadTask() {
      this.loading = true
      this.error = null

      try {
        const response = await axios.get(`/api/tasks/${this.id}`)
        this.task = response.data
      } catch (err) {
        this.error = 'Ошибка при загрузке задачи: ' + (err.message || 'Неизвестная ошибка')
        console.error(err)
      } finally {
        this.loading = false
      }
    },

    async updateTask(taskData) {
      try {
        await axios.put(`/api/tasks/${this.id}`, taskData)
        this.$router.push('/tasks')
      } catch (err) {
        alert('Ошибка при обновлении задачи: ' + (err.message || 'Неизвестная ошибка'))
        console.error(err)
      }
    },

    goBack() {
      this.$router.push('/tasks')
    }
  }
}
</script>

<style scoped>
.task-edit-page {
  max-width: 700px;
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
</style>
