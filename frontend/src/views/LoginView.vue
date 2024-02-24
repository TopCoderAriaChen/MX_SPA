<script setup lang="ts">
import { NSpace, NH1, NH5, NButton, NFormItem, NInput, NA } from "naive-ui";
import { ref } from "vue";

interface LoginForm {
  username: string;
  password: string;
}

const formRef = ref<LoginForm | null>(null);
const formValue = ref<LoginForm>({
  username: "admin",
  password: "password"
});

const handleClick = async () => {};
</script>

<template>
  <div class="login">
    <n-space vertical class="login-card">
      <n-h1>Welcome to Shangxue Online</n-h1>
      <n-h5>Please login to continue</n-h5>

      <n-form ref="formRef" :model="formValue">
        <n-form-item path="username" label="Username">
          <n-input
            type="text"
            placeholder="Please Input"
            :value="formValue.username"
          />
        </n-form-item>
        <n-form-item path="password" label="Password">
          <n-input
            type="password"
            placeholder="Please Input"
            :value="formValue.password"
          />
        </n-form-item>
      </n-form>

      <n-space align="center" justify="space-between">
        <n-a href="/forget"> Forget your password? </n-a>
        <n-space>
          <n-button tag="a" size="large" href="/register"> Register </n-button>
          <n-button type="primary" tag="a" size="large" @click="handleClick">Login</n-button>
        </n-space>
      </n-space>

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

.login-card {
  margin-right: 15vw;
}
</style>
