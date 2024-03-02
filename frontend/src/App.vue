<script setup lang="ts">
import { RouterView } from "vue-router";
import {
  NConfigProvider,
  darkTheme,
  NGlobalStyle,
  NMessageProvider,
} from "naive-ui";
import MessageContent from "./components/MessageContent.vue";
</script>

<template>
  <n-config-provider :theme="darkTheme">
    <n-message-provider>
      <n-global-style />
      <message-content />
      <RouterView />
    </n-message-provider>
  </n-config-provider>
</template>

<style scoped></style>
