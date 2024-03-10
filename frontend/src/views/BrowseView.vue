<script setup lang="ts">
import CourseList from "../components/CourseList.vue";
import { useCourseList } from "../api/course";
import { useAuthStore } from "@/stores/auth";

const { data: courseList, isLoading,execute:refreshCourseList } = useCourseList();
const authStore = useAuthStore();
</script>
<template>
  <course-list
    :user-info="authStore.getUserInfo!"
    :courses="courseList!"
    :on-updated="refreshCourseList"
  ></course-list>
</template>
