<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">Forum</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link
              class="nav-link active"
              aria-current="page"
              :to="{ name: 'home' }"
              >Home</router-link
            >
          </li>
          <div class="dropdown">
            <button
              class="btn btn-secondary dropdown-toggle"
              type="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Categories
            </button>
            <ul class="dropdown-menu">
              <li>
                <router-link
                  v-for="category in categories"
                  class="dropdown-item"
                  :to="{ name: 'category', params: { slug: category.slug } }"
                  >{{ category.slug }}</router-link
                >
              </li>
            </ul>
          </div>
        </ul>

        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link
              class="btn btn-primary me-2"
              :to="{ name: 'discussion-form' }"
              >Ask Question</router-link
            >
          </li>
          <li class="nav-item">
            <a class="btn btn-outline-danger" href="/accounts/logout/"
              >Logout</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "Navbar",
  data() {
    return {
      categories: [],
    };
  },
  props: {
    category: {
      type: String,
    },
  },
  methods: {
    async getCategories() {
      let endpoint = "/api/v1/categories/";
      try {
        const response = await axios.get(endpoint);
        this.categories = response.data;
        console.log(response.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getCategories();
  },
};
</script>
