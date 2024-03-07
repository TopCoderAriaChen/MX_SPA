<script setup lang="ts">
import CourseList from "../components/CourseList.vue";
import { useCourseList } from "../api/course";
import { useAuthStore } from "@/stores/auth";

const { data: courseList, isLoading } = useCourseList();
const authStore = useAuthStore();
</script>
<template>
  <course-list
    :user-info="authStore.getUserInfo!"
    :courses="courseList!"
  ></course-list>
</template>
