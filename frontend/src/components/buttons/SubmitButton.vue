<template>
  <v-btn :disabled="disabled" :color="color" submit block large>{{
    buttonText
  }}</v-btn>
</template>

<script>
export default {
  name: "SubmitButton",
  props: {
    color: {
      type: String,
      default: "primary",
    },
    buttonText: {
      type: String,
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
