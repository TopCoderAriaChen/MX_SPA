<script setup lang="ts">
import { RouterView } from "vue-router";
import { NConfigProvider, darkTheme, NGlobalStyle } from "naive-ui";
</script>

<template>
  <n-config-provider :theme="darkTheme"> 
    <n-global-style />
    <RouterView />
  </n-config-provider>

</template>

<style scoped></style>
