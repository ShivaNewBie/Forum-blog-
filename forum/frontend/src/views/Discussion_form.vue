<template>
  <div class="container">
    <h1 class="mb-3">Ask a question, share ideas, thoughts and projects!</h1>
    <form @submit.prevent="onSubmit">
      <select
        class="form-select mb-3"
        aria-label="Default select example"
        v-model="category_name"
      >
        <option
          v-for="(item, key) in categories"
          :key="item.title"
          :value="item.id"
        >
          {{ item.title }}
        </option>
      </select>

      <input type="text" class="form-control mb-3" v-model="title" />
      <textarea
        v-model="discussionBody"
        rows="4"
        placeholder="Ask a question, share ideas, thoughts and projects!"
        class="form-control"
      ></textarea>
      <button type="submit" class="btn btn-success mt-3">Publish</button>
    </form>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Discussion_form",
  props: {
    slug: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      discussionBody: null,
      title: null,
      category_name: null,
      categories: [],
    };
  },
  methods: {
    async getCategories() {
      let endpoint = "/api/v1/categories/";
      try {
        const response = await axios.get(endpoint);
        this.categories = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async onSubmit() {
      let endpoint = "/api/v1/discussions/";
      try {
        const response = await axios.post(endpoint, {
          category_name: this.category_name,
          title: this.title,
          body: this.discussionBody,
        });

        console.log(response);
      } catch (error) {
        console.log(error.response);
      }
    },
  },
  created() {
    this.getCategories();
  },
};
</script>
