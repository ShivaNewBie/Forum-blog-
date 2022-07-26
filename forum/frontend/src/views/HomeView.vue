<template>
  <div class="home mt-3">
    <div class="container">
      <div v-for="discussion in discussions" :key="discussion.uuid">
        <div class="shadow p-3 mb-5 bg-body rounded">
          <div class="card-body">
            <p class="mb-0">
              Posted by:
              <span class="discussion-author">{{ discussion.user }}</span>
            </p>
            <router-link
              class="discussion-link"
              :to="{ name: 'discussion', params: { slug: discussion.slug } }"
              ><h2>{{ discussion.body }}</h2></router-link
            >
            <p class="mb-0">Answers: {{ discussion.answers_count }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from "@/common/api.service.js";

export default {
  name: "HomeView",
  data() {
    return {
      discussions: [],
    };
  },
  components: {},
  methods: {
    async getDiscussions() {
      let endpoint = "/api/v1/discussions/";

      try {
        const response = await axios.get(endpoint);
        this.discussions = response.data;
        console.log(response);
      } catch (error) {
        console.log(error.response);
      }
    },
  },
  created() {
    this.getDiscussions();
  },
};
</script>

<style>
.discussion-author {
  font-weight: bold;
  color: #dc3545;
}

.discussion-link {
  font-weight: 400;
  color: black;
  text-decoration: none;
}

.discussion-link:hover {
  color: #343a40;
}
</style>
