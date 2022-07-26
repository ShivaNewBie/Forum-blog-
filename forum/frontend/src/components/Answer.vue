<template>
  <strong>{{ answer.author }} &#8901; {{ answer.created_at }}</strong>
  <p style="white-space: pre-wrap">{{ answer.body }}</p>
</template>

<script>
export default {
  name: "Answer",
  props: {
    answer: {
      type: Object,
      required: true,
    },
  },
};
</script>
