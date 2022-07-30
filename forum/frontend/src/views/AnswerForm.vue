<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit your answer</h1>
    <form @submit.prevent="onSubmit">
      <textarea v-model="answerBody" class="form-control" rows="10"></textarea>
      <button type="submit" class="btn btn-success mt-3">Publish</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "AnswerEditor",
  props: {
    uuid: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      discussionSlug: null,
      answerBody: null,
      error: null,
    };
  },
  methods: {
    async onSubmit() {
      if (!this.answerBody) {
        this.error = "You can't submit an empty answer!";
        return;
      }
      const endpoint = `/api/v1/answers/${this.uuid}/`;
      try {
        await axios.put(endpoint, { body: this.answerBody });
        this.$router.push({
          name: "discussion",
          params: { slug: this.discussionSlug },
        });
      } catch (error) {
        console.log(error.response);
      }
    },
  },
  async beforeRouteEnter(to, from, next) {
    // get the answer's data from the REST API and set two data properties for the component
    const endpoint = `/api/v1/answers/${to.params.uuid}/`;
    try {
      const response = await axios.get(endpoint);
      return next(
        (vm) => (
          (vm.answerBody = response.data.body),
          (vm.discussionSlug = response.data.discussion_slug)
        )
      );
    } catch (error) {
      console.log(error);
    }
  },
};
</script>
