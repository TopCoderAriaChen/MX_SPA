<script lang="ts" setup>
import type { Course } from "@/api/courses";
import { useAuthStore } from "@/stores/auth";
import { storeToRefs } from "pinia";
import { computed } from "vue";
import {
  NCard,
  NSpace,
  NH3,
  NP,
  NImage,
  NTag,
  NIcon,
  NDivider
} from "naive-ui";
import { People } from "@vicons/ionicons5";

const props = defineProps<{
  course: Course;
}>();

const authStore = useAuthStore();
const auth = storeToRefs(authStore);
</script>

<template>
  <n-card>
    <div class="flex">
      <n-image :src="props.course.cover_image" class="w-1/3"></n-image>
      <n-space vertical class="course-info h-full pl-10">
        <n-h3>{{ props.course.name }}</n-h3>
        <n-space>
          <n-p>
            Price: <span>{{ props.course.original_price }}</span>
          </n-p>
          <n-p>
            Teacher: <span>{{ props.course.teacher.display_name }}</span>
          </n-p>
          <n-p>
            Campus: <span>{{ props.course.campus.name }}</span>
          </n-p>
        </n-space>
        <n-tag type="success" round :bordered="false" class="mt-2">
          Enrolled: {{ props.course.enrolled_students.length }}
          <template #icon>
            <n-icon :component="People" class="mr-1"></n-icon>
          </template>
        </n-tag>
        <n-divider></n-divider>
        <n-p class="text-base">{{ props.course.description }}</n-p>
      </n-space>
    </div>
  </n-card>
</template>

<style lang="less" scoped>
.course-info span {
  font-size: 16px;
  font-weight: 400;
  margin-left: 10px;
  margin-right: 16px;
}
</style>
