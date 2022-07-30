<template>
  <strong>{{ answer.author }} &#8901; {{ answer.created_at }}</strong>
  <p style="white-space: pre-wrap">{{ answer.body }}</p>
  <div v-if="isAnswerAuthor">
    <router-link
      :to="{ name: 'answer-editor', params: { uuid: uuid } }"
      class="btn btn-sm btn-warning"
      >Edit</router-link
    >
    <button
      class="btn btn-sm btn-danger mx-1"
      @click="showDeleteConfirmation = !showDeleteConfirmation"
    >
      Delete
    </button>
    <button
      class="btn btn-sm btn-danger mx-1"
      @click="triggerDeleteAnswer"
      v-show="showDeleteConfirmation"
    >
      Yes, delete my answer
    </button>
  </div>
  <div v-else>
    <button
      @click="toggleLike"
      class="btn"
      :class="{
        'btn-warning': userLikedAnswer,
        'btn-outline-danger': !userLikedAnswer,
      }"
    >
      Like answer&nbsp;
      <span class="badge bg-danger">{{ likesCounter }}</span>
    </button>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Answer",
  data() {
    return {
      showDeleteConfirmation: false,
      userLikedAnswer: this.answer.user_has_liked,
      likesCounter: this.answer.likes_count,
    };
  },
  props: {
    uuid: {
      type: String,
      required: true,
    },
    answer: {
      type: Object,
      required: true,
    },
    requestUser: {
      type: String,
      required: true,
    },
  },
  methods: {
    toggleLike() {
      this.userLikedAnswer === false ? this.likeAnswer() : this.unLikeAnswer(); //condition ? ifTrue : ifFalse. if user has not like answer like it
    },
    async likeAnswer() {
      this.userLikedAnswer = true;
      this.likesCounter += 1;
      const endpoint = `/api/v1/answers/${this.answer.uuid}/like/`;
      try {
        await axios.post(endpoint);
      } catch (error) {
        console.log(error.response);
      }
    },
    async unLikeAnswer() {
      this.userLikedAnswer = false;
      this.likesCounter -= 1;
      const endpoint = `/api/v1/answers/${this.answer.uuid}/like/`;
      try {
        await axios.delete(endpoint);
      } catch (error) {
        console.log(error.response);
      }
    },
    triggerDeleteAnswer() {
      this.$emit("delete-answer", this.answer);
    },
  },
  computed: {
    isAnswerAuthor() {
      return this.answer.author == this.requestUser;
    },
  },
};
</script>
