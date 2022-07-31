<template>
  <div class="home mt-3">
    <div class="container">
      <h1>{{ category.title }}</h1>

      <div v-for="discussion in category.discussions" :key="discussion.slug">
        <div class="shadow p-3 mb-5 bg-body rounded">
          <div class="card-body">
            <p class="mb-0">
              Posted by:
              <span class="discussion-author">{{ discussion.user }}</span>
            </p>
            <router-link
              class="discussion-link"
              :to="{ name: 'discussion', params: { slug: discussion.slug } }"
              ><h2>{{ discussion.title }}</h2></router-link
            >
            <p class="mb-0">Answers: {{ discussion.answers_count }}</p>
          </div>
        </div>
      </div>
      <div class="my-4">
        <p v-show="loading">...loading...</p>
        <button
          v-show="next"
          @click="getCategories"
          class="btn btn-sm btn-outline-success"
        >
          Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";
export default {
  name: "Category",
  data() {
    return {
      category: {
        discussions: [],
      },
      next: null,
      loading: false,
    };
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.slug;
      let endpoint = `/api/v1/categories/${categorySlug}/`;
      try {
        const response = await axios.get(endpoint);
        this.category = response.data;
        console.log(response);
        console.log("test");
      } catch (error) {
        console.log("error");
      }
    },
  },
  created() {
    this.getCategory();
  },
  watch: {
    $route(to, from) {
      if (to.name === "category") {
        this.getCategory();
      }
    },
  },
};
</script>
