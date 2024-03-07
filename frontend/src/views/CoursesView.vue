<script setup lang="ts">
import { useCourseList } from "@/api/course";
import CourseList from "@/components/CourseList.vue";
import { useAuthStore } from "@/stores/auth";
const authStore = useAuthStore();
const { data: courseList, isLoading } = useCourseList();
</script>

<template>
  <course-list
    :user-info="authStore.getUserInfo!"
    :courses="courseList!"
    v-if="!isLoading"
  ></course-list>
</template>
