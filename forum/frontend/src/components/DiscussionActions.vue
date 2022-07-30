<template>
  <div class="mt-3">
    <router-link
      class="btn btn-sm btn-warning me-1"
      :to="{ name: 'discussion-form', params: { slug: slug } }"
    >
      Update
    </router-link>
    <button
      class="btn btn-sm btn-danger mx-1"
      @click="deleteConfirmation = !deleteConfirmation"
    >
      Delete
    </button>
    <button
      class="btn btn-sm btn-outline-danger"
      v-show="deleteConfirmation"
      @click="deleteDiscussion"
    >
      Yes, delete my post
    </button>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "DiscussionActions",
  data() {
    return {
      deleteConfirmation: false,
    };
  },
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  methods: {
    async deleteDiscussion() {
      const endpoint = `/api/v1/discussions/${this.slug}/`;
      try {
        await axios.delete(endpoint);
        this.$router.push({ name: "home" });
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
