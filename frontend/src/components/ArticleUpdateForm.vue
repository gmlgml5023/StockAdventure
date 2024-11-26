<template>
  <div class="update-form">
    <h2 class="form-title">Edit Story</h2>
    <form @submit.prevent="handleSubmit" class="article-form">
      <div class="form-group">
        <label for="title">제목</label>
        <input 
          type="text" 
          id="title" 
          v-model="formData.title" 
          required
          class="form-input"
          placeholder="제목을 입력하세요"
        />
      </div>

      <div class="form-group">
        <label for="content">내용</label>
        <textarea
          id="content"
          v-model="formData.article_content"
          required
          class="form-textarea"
          placeholder="내용을 입력하세요"
        ></textarea>
      </div>

      <div class="button-group">
        <button type="submit" class="submit-button">
          <span class="button-text">수정완료</span>
          <span class="star-icon">💫</span>
        </button>
        <button type="button" @click="$emit('cancel')" class="cancel-button">
          <span class="button-text">취소</span>
          <span class="star-icon">✖</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useArticleStore } from "@/stores/article";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const props = defineProps({
  article: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["update-complete", "cancel"]);
const articleStore = useArticleStore();
const authStore = useAuthStore();
const router = useRouter();
const formData = ref({
  title: props.article.title,
  article_content: props.article.article_content,
});

const handleSubmit = async () => {
  // 작성자 확인
  if (!authStore.isAuthor(props.article.username)) {
    alert("게시글 수정 권한이 없습니다.");
    return;
  }

  if (confirm("게시글을 수정하시겠습니까?")) {
    try {
      await articleStore.updateArticle(props.article.id, formData.value);
      emit("update-complete");

      router
        .push({
          name: "ArticleDetailView",
          params: { article_id: props.article.id },
        })
        .then(() => {
          alert("게시글이 수정되었습니다.");
        });
    } catch (error) {
      console.error("수정 실패:", error);
      alert("게시글 수정에 실패했습니다.");
    }
  }
};
</script>

<style scoped>
.update-form {
  max-width: 800px;
  margin: auto;
  padding: 30px;
  border-radius: 15px;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(240, 219, 55, 0.2);
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 0 32px rgba(240, 219, 55, 0.05);
}

.form-title {
  color: #f0db37;
  text-align: center;
  margin-bottom: 30px;
  font-size: 28px;
  text-shadow: 0 0 15px rgba(240, 219, 55, 0.6);
}

.form-group {
  margin-bottom: 20px;
}

label {
  color: #f0db37;
  margin-bottom: 8px;
  display: block;
  font-weight: 500;
  text-shadow: 0 0 8px rgba(240, 219, 55, 0.4);
}

.form-input, .form-textarea {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: 1px solid rgba(240, 219, 55, 0.4);
  background: rgba(0, 0, 0, 0.2);
  color: #f0db37;
  font-size: 16px;
  transition: all 0.3s ease;
  backdrop-filter: blur(5px);
}

.form-textarea {
  min-height: 300px;
  resize: vertical;
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.form-input:focus,
.form-textarea:focus {
  outline: none;
  border-color: #f0db37;
  box-shadow: 0 0 15px rgba(240, 219, 55, 0.2);
  background: rgba(0, 0, 0, 0.3);
}

.button-group {
  display: flex;
  gap: 15px;
  margin-top: 30px;
}

.submit-button, .cancel-button {
  flex: 1;
  padding: 12px;
  border-radius: 8px;
  border: none;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.submit-button {
  background: linear-gradient(45deg, 
    rgba(240, 219, 55, 0.9), 
    rgba(255, 209, 4, 0.9)
  );
  color: #000;
}

.cancel-button {
  background: rgba(255, 255, 255, 0.1);
  color: #f0db37;
  border: 1px solid rgba(240, 219, 55, 0.4);
}

.submit-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(240, 219, 55, 0.3);
}

.cancel-button:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

.star-icon {
  font-size: 18px;
}
</style>