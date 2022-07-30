<template>
  <div class="container mt-3">
    <div v-if="discussion">
      <h1>{{ discussion.title }}</h1>
      <h2>{{ discussion.body }}</h2>
      <p class="mb-0">
        Posted by: <span class="user-name">{{ discussion.user }}</span>
      </p>
      <p>{{ discussion.created_at }}</p>
      <DiscussionActions :slug="discussion.slug" v-if="isDiscussionUser" />
      <hr />
      <div v-if="userHasAnswered">
        <p class="answer-added">You've already answered</p>
      </div>
      <div v-else-if="showForm">
        <p>Answer the question</p>
        <form @submit.prevent="onSubmit">
          <textarea
            v-model="newAnswerBody"
            class="form-control"
            placeholder="Share your knowledge"
            rows="10"
          ></textarea>
          <button type="submit" class="btn btn-success my-3">
            Submit answer
          </button>
        </form>
        <p v-if="error" class="error mt-2">{{ error }}</p>
      </div>
      <div v-else>
        <button class="btn btn-success" @click="showForm = true">
          Answer the question
        </button>
      </div>
    </div>
    <div v-else>
      <h1 class="error text-center">404 - Discussion not found</h1>
    </div>

    <div>
      <Answer
        v-for="answer in answers"
        :key="answer.uuid"
        :answer="answer"
        :requestUser="requestUser"
        :uuid="answer.uuid"
        @delete-answer="deleteAnswer"
      />
    </div>
    <div class="my-4">
      <p v-show="loading">...loading...</p>
      <button
        v-show="next"
        @click="getDiscussionsAnswers"
        class="btn btn-sm btn-outline-success"
      >
        Load More
      </button>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

import Answer from "@/components/Answer.vue";
import DiscussionActions from "@/components/DiscussionActions.vue";

export default {
  name: "Discussion",
  data() {
    return {
      discussion: {},
      answers: [],
      error: null,
      requestUser: null,
      loading: null,
      next: null,
      userHasAnswered: null,
      showForm: false,
      newAnswerBody: null,
    };
  },
  components: {
    Answer,
    DiscussionActions,
  },
  computed: {
    isDiscussionUser() {
      return this.discussion.user == this.requestUser;
    },
  },
  props: {
    slug: {
      type: String,
      required: true,
    },
  },

  methods: {
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    async getDiscussion() {
      let endpoint = `/api/v1/discussions/${this.slug}/`;
      try {
        const response = await axios.get(endpoint);
        this.discussion = response.data;
        this.userHasAnswered = response.data.user_has_answered;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async getDiscussionsAnswers() {
      let endpoint = `/api/v1/discussions/${this.slug}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loading = true;
      try {
        const response = await axios.get(endpoint);
        this.answers.push(...response.data.results);
        this.loading = false;
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
        // console.log(response);
      } catch (error) {
        console.log(error.response);
      }
    },
    async deleteAnswer(answer) {
      const endpoint = `/api/v1/answers/${answer.uuid}/`;
      try {
        await axios.delete(endpoint);
        this.answers.splice(this.answers.indexOf(answer), 1); //changes the contents of an array by removing or replacing existing elements and/or adding new elements in place
        this.userHasAnswered = false;
      } catch (error) {
        console.log(error.response);
      }
    },
    async onSubmit() {
      if (!this.newAnswerBody) {
        this.error = "You can't send an empty answer!";
        return;
      }
      const endpoint = `/api/v1/discussions/${this.slug}/answer/`;
      try {
        const response = await axios.post(endpoint, {
          body: this.newAnswerBody,
        });
        this.answers.unshift(response.data);
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
        }
      } catch (error) {
        console.log(error);
      }
    },
  },

  created() {
    this.getDiscussion(), this.getDiscussionsAnswers(), this.setRequestUser();
  },
};
</script>

<style>
.user-name {
  font-weight: bold;
  color: #dc3545;
}
.error {
  color: #dc3545;
}
.answer-added {
  font-weight: bold;
  color: green;
}
</style>
