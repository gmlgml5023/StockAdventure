<!-- JournalListItem.vue -->
<template>
  <div class="journal-item">
    <p>매매일지 No: {{ journal.id }}</p>
    <p>거래일자: {{ journal.transaction_date }}</p>
    <p>거래유형: {{ journal.buysell }}</p>
    <RouterLink
      :to="{
        name: 'JournalDetailView',
        params: { journal_id: journal.id },
      }"
    >
      상세보기
    </RouterLink>
    <hr />
  </div>
</template>

<script setup>
defineProps({
  journal: {
    type: Object,
    required: true,
  },
});
</script>
