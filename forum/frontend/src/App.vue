<template>
  <div id="nav">
    <Navbar />
  </div>
  <router-view />
</template>

<script>
import { axios } from "@/common/api.service.js";

import Navbar from "@/components/Navbar.vue";

export default {
  name: "App",
  data() {
    return {
      categories: [],
    };
  },
  components: {
    Navbar,
  },

  methods: {
    async setUserInfo() {
      try {
        const response = await axios.get("/auth/users/me/");
        const requestUser = response.data["username"];
        window.localStorage.setItem("username", requestUser); //key and value pair
        console.log(response.data);
      } catch (error) {
        this.error = error.response.statusText;
      }
    },
  },
  created() {
    this.setUserInfo();
  },
};
</script>

<style></style>
