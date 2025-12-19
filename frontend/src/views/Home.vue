<template>
  <LayoutCard>
    <template #header>
      Добро пожаловать в Task Manager
    </template>

    <div class="home-content">
      <p class="welcome-text">
        Эффективный менеджер задач для управления вашими делами
      </p>
      
      <div class="features">
        <div class="feature-item">
          <div class="feature-icon">📝</div>
          <h3>Управление задачами</h3>
          <p>Создавайте, редактируйте и удаляйте задачи</p>
        </div>
        <div class="feature-item">
          <div class="feature-icon">🔍</div>
          <h3>Фильтрация</h3>
          <p>Фильтруйте задачи по статусу</p>
        </div>
        <div class="feature-item">
          <div class="feature-icon">📊</div>
          <h3>Сортировка</h3>
          <p>Сортируйте по дате, приоритету или алфавиту</p>
        </div>
      </div>

      <div class="cta">
        <router-link to="/tasks" class="btn btn-primary btn-lg">
          Перейти к задачам
        </router-link>
      </div>
    </div>

    <template #footer>
      <div class="stats-section">
        <slot name="stats">
          <p>Начните управлять своими задачами эффективно!</p>
        </slot>
      </div>
    </template>
  </LayoutCard>
</template>

<script>
import LayoutCard from '../components/LayoutCard.vue'

export default {
  name: 'Home',
  components: {
    LayoutCard
  }
}
</script>

<style scoped>
.home-content {
  text-align: center;
}

.welcome-text {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 40px;
}

.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.feature-item {
  padding: 20px;
  border-radius: 8px;
  background: #f9f9f9;
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 15px;
}

.feature-item h3 {
  color: #333;
  margin-bottom: 10px;
}

.feature-item p {
  color: #777;
  font-size: 0.95rem;
}

.cta {
  margin: 40px 0;
}

.btn-lg {
  padding: 15px 40px;
  font-size: 1.1rem;
}

.stats-section {
  text-align: center;
  color: #666;
}

@media (max-width: 768px) {
  .features {
    grid-template-columns: 1fr;
  }
}
</style>
