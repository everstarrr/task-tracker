<template>
  <form @submit.prevent="handleSubmit" class="task-form">
    <div class="form-group">
      <label for="title">Заголовок *</label>
      <input
        id="title"
        v-model.trim="formData.title"
        type="text"
        placeholder="Введите название задачи"
        required
      />
      <span v-if="errors.title" class="error">{{ errors.title }}</span>
    </div>

    <div class="form-group">
      <label for="description">Описание *</label>
      <textarea
        id="description"
        v-model.trim="formData.description"
        placeholder="Опишите задачу подробнее"
        rows="4"
        required
      ></textarea>
      <span v-if="errors.description" class="error">{{ errors.description }}</span>
    </div>

    <div class="form-group">
      <label for="priority">Приоритет</label>
      <select id="priority" v-model="formData.priority">
        <option value="low">Низкий</option>
        <option value="medium">Средний</option>
        <option value="high">Высокий</option>
      </select>
    </div>

    <div class="form-group">
      <label>Категория</label>
      <div class="radio-group">
        <label class="radio-label">
          <input
            type="radio"
            v-model="formData.category"
            value="work"
          />
          Работа
        </label>
        <label class="radio-label">
          <input
            type="radio"
            v-model="formData.category"
            value="personal"
          />
          Личное
        </label>
        <label class="radio-label">
          <input
            type="radio"
            v-model="formData.category"
            value="study"
          />
          Учёба
        </label>
        <label class="radio-label">
          <input
            type="radio"
            v-model="formData.category"
            value="other"
          />
          Другое
        </label>
      </div>
    </div>

    <div class="form-group">
      <label class="checkbox-label">
        <input
          type="checkbox"
          v-model="formData.important"
        />
        Важная задача
      </label>
    </div>

    <div class="form-actions">
      <button type="submit" class="btn btn-primary" :disabled="submitting">
        {{ submitLabel }}
      </button>
      <button type="button" @click="handleCancel" class="btn btn-secondary">
        Отмена
      </button>
    </div>
  </form>
</template>

<script>
export default {
  name: 'TaskForm',
  props: {
    initialData: {
      type: Object,
      default: () => ({})
    },
    submitLabel: {
      type: String,
      default: 'Создать'
    }
  },
  emits: ['submit', 'cancel'],
  data() {
    return {
      formData: {
        title: this.initialData.title || '',
        description: this.initialData.description || '',
        priority: this.initialData.priority || 'medium',
        category: this.initialData.category || 'other',
        important: this.initialData.important || false,
        completed: this.initialData.completed || false
      },
      errors: {},
      submitting: false
    }
  },
  methods: {
    validate() {
      this.errors = {}
      
      if (!this.formData.title) {
        this.errors.title = 'Заголовок обязателен'
      } else if (this.formData.title.length < 3) {
        this.errors.title = 'Заголовок должен содержать минимум 3 символа'
      }

      if (!this.formData.description) {
        this.errors.description = 'Описание обязательно'
      } else if (this.formData.description.length < 10) {
        this.errors.description = 'Описание должно содержать минимум 10 символов'
      }

      return Object.keys(this.errors).length === 0
    },
    
    handleSubmit() {
      if (!this.validate()) {
        return
      }
      
      this.submitting = true
      this.$emit('submit', { ...this.formData })
    },
    
    handleCancel() {
      this.$emit('cancel')
    }
  },
  watch: {
    initialData: {
      handler(newData) {
        if (newData && Object.keys(newData).length > 0) {
          this.formData = {
            title: newData.title || '',
            description: newData.description || '',
            priority: newData.priority || 'medium',
            category: newData.category || 'other',
            important: newData.important || false,
            completed: newData.completed || false
          }
        }
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style scoped>
.task-form {
  background: white;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #333;
}

.form-group input[type="text"],
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 12px;
  border: 2px solid #e0e0e0;
  border-radius: 5px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  outline: none;
  border-color: #667eea;
}

.radio-group {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.radio-label {
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  font-weight: normal;
}

.radio-label input[type="radio"] {
  width: auto;
  cursor: pointer;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  font-weight: normal;
}

.checkbox-label input[type="checkbox"] {
  width: auto;
  cursor: pointer;
  transform: scale(1.2);
}

.error {
  display: block;
  color: #f44336;
  font-size: 0.875rem;
  margin-top: 5px;
}

.form-actions {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.form-actions button {
  flex: 1;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .task-form {
    padding: 20px;
  }

  .form-actions {
    flex-direction: column;
  }
}
</style>
