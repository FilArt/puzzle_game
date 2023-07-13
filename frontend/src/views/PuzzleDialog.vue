<script setup>
import { ref, toRefs, watch } from "vue";
const props = defineProps(["puzzle", "answerResult"]);
const emit = defineEmits(["answer"]);
const { puzzle, answerResult } = toRefs(props);
const dialogVisible = ref(false);
const userAnswer = ref("");

watch(puzzle, (v) => {
  dialogVisible.value = !!v;
  userAnswer.value = "";
});
</script>

<template>
  <v-dialog v-model="dialogVisible" max-width="500px">
    <v-card>
      <v-img :src="puzzle?.image_urls" aspect-ratio="1"></v-img>
      <v-card-text>
        <v-text-field v-model="userAnswer" label="Your answer"></v-text-field>
      </v-card-text>
      <v-card-text>
        <v-alert v-if="answerResult.color" :type="answerResult.color">
          {{ answerResult.text }}
        </v-alert>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!userAnswer"
          color="primary"
          @click="emit('answer', userAnswer)"
          >Check Answer</v-btn
        >
        <v-btn text @click="dialogVisible = false">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
