<template>
  <v-container>
    <h1 class="text-center">Puzzles</h1>
    <v-progress-linear v-if="isLoading" indeterminate></v-progress-linear>
    <v-alert v-else-if="puzzles.length === 0" type="info">No puzzles available.</v-alert>
    <v-row v-else>
      <v-col v-for="puzzle in puzzles" :key="puzzle.id" cols="12" sm="6" md="4" lg="3">
        <v-card>
          <v-img :src="puzzle.image_urls" aspect-ratio="1"></v-img>
          <v-card-actions>
            <v-btn color="primary" text @click="getPuzzle(`/puzzles/${puzzle.id}`)">View Puzzle</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <puzzle-dialog :puzzle="currentPuzzle" :answer-result="answerResult"
      @answer="checkAnswer(`/puzzles/${currentPuzzle.id}/check_answer`, { data: $event })" />
  </v-container>
</template>

<script setup>
import { api } from '@/plugins/axios';
import PuzzleDialog from '@/views/PuzzleDialog.vue';
import { useAxios } from '@vueuse/integrations/useAxios';
import { ref, watch } from 'vue';

const { data: puzzles, isLoading } = useAxios('/puzzles', {}, api);
const { data: answerIsCorrect, execute: checkAnswer } = useAxios({ method: "POST" }, api)
const { data: currentPuzzle, execute: getPuzzle } = useAxios({}, api)
const answerResult = ref({
  color: '',
  text: '',
})
watch(currentPuzzle, () => {
  answerResult.value = { color: '', text: '' }
})
watch(answerIsCorrect, (v) => {
  if (v === true) {
    answerResult.value.color = 'success'
    answerResult.value.text = 'Correct answer!'
  } else if (v === false) {
    answerResult.value.color = 'error'
    answerResult.value.text = 'Incorrect answer.'
  }
})
</script>
