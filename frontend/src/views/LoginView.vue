<script setup lang="ts">
import { NSpace, NH1, NH5, NButton } from "naive-ui";
</script>

<template>
  <div class="login">
    <n-space vertical class="login-card mr-10">
      <n-h1>Welcome to Shangxue Online</n-h1>
      <n-h5>Please login to continue</n-h5>
      <n-button type="primary" tag="a">Hello</n-button>
    </n-space>
  </div>
</template>

<style lang="less">
.login {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.login-card{
  margin-right: 15vw;
}
</style>
