<template>
  <footer class="footer">
    <div class="footer-container">
      <p>&copy; 2025 Task Manager. Все права защищены.</p>
      <p class="footer-tech">Vue 3 + FastAPI + Docker</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
.footer {
  background-color: #333;
  color: white;
  margin-top: auto;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.footer-tech {
  margin-top: 5px;
  font-size: 0.9rem;
  color: #aaa;
}
</style>
