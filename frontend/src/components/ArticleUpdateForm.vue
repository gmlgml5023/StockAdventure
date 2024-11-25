<template>
  <div class="update-form">
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="title">제목: </label>
        <input type="text" id="title" v-model="formData.title" required />
      </div>
      <div>
        <label for="content">내용: </label>
        <textarea
          id="content"
          v-model="formData.article_content"
          required
        ></textarea>
      </div>
      <div class="button-group">
        <button type="submit">제출</button>
        <button type="button" @click="$emit('cancel')">취소</button>
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