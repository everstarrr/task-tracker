<template>
  <div class="not-found">
    <h1>404</h1>
    <p>Страница не найдена</p>
    <router-link to="/" class="btn btn-primary">
      Вернуться на главную
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'NotFound'
}
</script>

<style scoped>
.not-found {
  text-align: center;
  padding: 100px 20px;
}

.not-found h1 {
  font-size: 6rem;
  color: #667eea;
  margin-bottom: 20px;
}

.not-found p {
  font-size: 1.5rem;
  color: #666;
  margin-bottom: 30px;
}
</style>
