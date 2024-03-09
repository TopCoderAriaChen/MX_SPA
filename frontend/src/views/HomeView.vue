<script setup lang="ts">
import UserInfoCard from "../components/UserInfoCard.vue";
import CoursesStatus from "../components/CoursesStatus.vue";
import CourseList from "@/components/CourseList.vue";
import { NGrid, NGridItem, NDivider } from "naive-ui";
import { useAuthStore } from "@/stores/auth";
const authStore = useAuthStore();
</script>

<template>
  <n-grid cols="1 m:2" :x-gap="12" :y-gap="8" responsive="screen">
    <n-grid-item v-if="authStore.userInfo">
      <user-info-card :user-info="authStore.getUserInfo!"></user-info-card>
    </n-grid-item>
    <n-grid-item>
      <courses-status :user-info="authStore.getUserInfo!"></courses-status>
    </n-grid-item>
  </n-grid>
  <n-divider />
  <course-list
    :user-info="authStore.getUserInfo!"
    :courses="authStore.getUserInfo?.enrolled_courses || []"
  ></course-list>
</template>
