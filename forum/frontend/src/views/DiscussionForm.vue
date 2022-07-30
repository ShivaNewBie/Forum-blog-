<template>
  <div class="container">
    <h1 class="mb-3">Ask a question, share ideas, thoughts and projects!</h1>
    <form @submit.prevent="onSubmit">
      <select
        class="form-select mb-3"
        aria-label="Default select example"
        v-model="category_name"
      >
        <option disabled value="">Select Category</option>

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
  name: "DiscussionForm",
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
      category_name: "",
      categories: [],
    };
  },
  methods: {
    async getCategories() {
      let endpoint = "/api/v1/categories/";
      try {
        const response = await axios.get(endpoint);
        this.categories = response.data.results;

        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async performNetworkRequest() {
      let endpoint = "/api/v1/discussions/";
      let method = "POST";
      if (this.slug !== undefined && this.slug !== "") {
        endpoint += `${this.slug}/`;
        method = "PUT";
      }
      try {
        const response = await axios({
          method: method,
          url: endpoint,
          data: {
            category_name: this.category_name,
            title: this.title,
            body: this.discussionBody,
          },
        });
        this.$router.push({
          name: "discussion",
          params: { slug: response.data.slug },
        });
      } catch (error) {
        this.error = error.response;
        console.log(error.response);
      }
    },
    onSubmit() {
      if (!this.discussionBody) {
        this.error = "You can't send an empty question!";
      } else {
        this.performNetworkRequest();
      }
    },
  },

  async beforeRouteEnter(to, from, next) {
    // if the component is used to update a question
    // get the question's data from the REST API
    if (to.params.slug !== undefined && to.params.slug !== "") {
      const endpoint = `/api/v1/discussions/${to.params.slug}/`;
      try {
        const response = await axios.get(endpoint);
        return next(
          (vm) => (
            (vm.discussionBody = response.data.body),
            (vm.title = response.data.title),
            (vm.category_name = response.data.category_name)
          )
        );
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    } else {
      return next();
    }
  },
  created() {
    this.getCategories(), (document.title = "Forum - Editor");
  },
};
</script>
