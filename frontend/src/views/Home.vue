<script setup>
import SubmitButton from "@/components/buttons/SubmitButton.vue";
</script>

<template>
  <v-container class="welcome-screen">
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <div class="text-center">
          <h1 class="display-2 font-weight-bold mb-3">VoxPuzzle</h1>
          <p class="title font-weight-regular">
            Welcome to VoxPuzzle! Are you ready to test your puzzle solving
            skills?
          </p>
        </div>
        <router-link to="/game">
          <submit-button color="primary" button-text="Start Game" />
        </router-link>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.welcome-screen {
  padding: 50px;
}
</style>
