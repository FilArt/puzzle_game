<script setup>
import SubmitButton from "@/components/buttons/SubmitButton.vue";
import { ref } from "vue";

const images = ref([]);
const correctAnswer = "";
const userInput = ref("");
const checkAnswer = () => {
  if (userInput?.value.toLowerCase() === correctAnswer.toLowerCase()) {
    alert("Right answer!");
  } else {
    userInput.value = "";
    alert("Sorry, please try again.");
  }
};
</script>

<style scoped>
.game-screen {
  text-align: center;
  padding: 50px;
}
</style>

<template>
  <v-card>
    <v-card-title>Game</v-card-title>

    <v-card-text>
      <v-container class="game-screen">
        <v-row justify="center">
          <v-col cols="12" sm="8" md="6">
            <v-card>
              <v-img
                v-for="(image, index) in images"
                :key="index"
                :src="image"
                aspect-ratio="1"
              ></v-img>
              <v-text-field
                v-model="userInput"
                label="Your answer"
                @keyup.enter="checkAnswer"
              ></v-text-field>
              <submit-button
                color="primary"
                button-text="Submit Answer"
                @click="checkAnswer"
              />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
  </v-card>
</template>
