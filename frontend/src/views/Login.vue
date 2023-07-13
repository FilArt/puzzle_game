<script setup>
import SubmitButton from "@/components/buttons/SubmitButton.vue";
import { useAppStore } from "@/store/app";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useAppStore();

const username = ref(store.username);

const submit = () => {
  store.setUsername(username);
  router.push("/game");
};
</script>

<template>
  <v-container class="login">
    <h2>Enter your username:</h2>

    <v-form @submit.prevent="submit">
      <v-text-field label="Username" v-model="username" />

      <submit-button :disabled="!username" button-text="Save" />
    </v-form>
  </v-container>
</template>

<style scoped>
.login {
  text-align: center;
  padding: 50px;
  max-width: 750px;
}
</style>
