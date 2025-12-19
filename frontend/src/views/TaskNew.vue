<template>
  <div class="task-new-page">
    <LayoutCard>
      <template #header>
        Создать новую задачу
      </template>

      <TaskForm
        submit-label="Создать задачу"
        @submit="createTask"
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
  name: 'TaskNew',
  components: {
    LayoutCard,
    TaskForm
  },
  methods: {
    async createTask(taskData) {
      try {
        await axios.post('/api/tasks', taskData)
        this.$router.push('/tasks')
      } catch (err) {
        alert('Ошибка при создании задачи: ' + (err.message || 'Неизвестная ошибка'))
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
.task-new-page {
  max-width: 700px;
  margin: 0 auto;
}
</style>
