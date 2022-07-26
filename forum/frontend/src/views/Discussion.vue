<template>
  <div class="container mt-3">
    <h1>{{ discussion.body }}</h1>
    <p class="mb-0">
      Posted by: <span class="user-name">{{ discussion.user }}</span>
    </p>
    <p>{{ discussion.created_at }}</p>
    <hr />
    <div>
      <Answer v-for="answer in answers" :key="answer.uuid" :answer="answer" />
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

import Answer from "@/components/Answer.vue";

export default {
  name: "Discussion",
  data() {
    return {
      discussion: {},
      answers: [],
    };
  },
  components: {
    Answer,
  },
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  methods: {
    async getDiscussion() {
      let endpoint = `/api/v1/discussions/${this.slug}/`;
      try {
        const response = await axios.get(endpoint);
        this.discussion = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async getDiscussionsAnswers() {
      let endpoint = `/api/v1/discussions/${this.slug}/answers/`;
      try {
        const response = await axios.get(endpoint);
        this.answers = response.data;
        console.log(response);
      } catch (error) {
        console.log(error.response);
      }
    },
  },

  created() {
    this.getDiscussion(), this.getDiscussionsAnswers();
  },
};
</script>

<style>
.user-name {
  font-weight: bold;
  color: #dc3545;
}
</style>
