<script setup lang="ts">
import type { CourseBasicInfo } from "@/api/course";
import NewCourseButton from "@/components/course/NewCourseButton.vue";
import { createOrder } from "@/api/order";
import { deleteCource } from "@/api/course";
import type { User } from "@/interfaces/user.interface";
import { useAuthStore } from "@/stores/auth";
import {
  NGrid,
  NGridItem,
  NCard,
  NA,
  NP,
  NSpace,
  NButton,
  NModal,
  useMessage,
  NDivider,
  NPopconfirm,
} from "naive-ui";
import { ref } from "vue";
import { useRouter } from "vue-router";

const props = defineProps<{
  userInfo: User;
  courses: CourseBasicInfo[];
}>();
const router = useRouter();
const authStore = useAuthStore();

const { hasPermission } = useAuthStore();

const message = useMessage();

const showPurchaseModal = ref(false);
const clickedCourse = ref<string>("");

const isEnrolledCourse = (course_id: string) => {
  if (props.userInfo?.permissions?.includes("course_admin")) {
    return true;
  } else {
    return props.userInfo?.enrolled_courses
      ?.map((c) => c.course_id)
      .includes(course_id);
  }
};

const handleCourseClick = (course_id: string) => {
  if (isEnrolledCourse(course_id)) {
    router.replace(`/courses/${course_id}`);
  } else {
    clickPurchase(course_id);
  }
};

const clickPurchase = (course_id: string) => {
  clickedCourse.value = course_id;
  showPurchaseModal.value = true;
};

const purchase = async () => {
  const orderId = await createOrder(
    clickedCourse.value,
    authStore.getUserInfo?.id!
  );
  message.success(`Course ordered. Order ID: ${orderId}`);
};

const handleDeleteCourse = async (course_id: string) => {
  const response = await deleteCource(course_id);
  message.success(`Course deleted.`);
};

const onCourseCreated = () => {
  console.log("created");
};
</script>

<template>
  <n-grid :cols="3" :x-gap="12" :y-gap="8">
    <n-grid-item v-for="course in courses" :key="course.id">
      <n-card :title="course.name">
        <template #cover>
          <n-a @click="handleCourseClick(course.id)">
            <img :src="course.cover_image" alt="" style="height: 100%" />
          </n-a>
        </template>
        <template #footer>
          <n-space
            justify="space-between"
            align="center"
            class="h-8"
            v-if="!isEnrolledCourse(course.id)"
          >
            <span class="text-orange-400 py-2">
              ${{ course.original_price }}
            </span>
            <n-button
              size="small"
              type="success"
              @click="() => clickPurchase(course.id)"
              >Puchase now</n-button
            >
          </n-space>
          <n-space class="h-8" align="center" v-else>
            <span
              class="text-green-500"
              v-if="
                !authStore.getUserInfo?.permissions?.includes('course_admin')
              "
            >
              Enrolled
            </span>
          </n-space>
          <n-space class="h-8" v-if="hasPermission('course_admin')">
            <n-popconfirm @positive-click="() => handleDeleteCourse(course.id)">
              <template #trigger>
                <n-button size="small" type="error">Delete</n-button>
              </template>
              Do you want to confirm the deletion?
            </n-popconfirm>
          </n-space>
        </template>
        <n-p class="mt-1"> Teacher: {{ course.teacher.display_name }} </n-p>
        <n-p> Description: {{ course.description }} </n-p>
      </n-card>
    </n-grid-item>
  </n-grid>
  <n-divider v-if="hasPermission('course_admin')">
    <new-course-button :on-created="onCourseCreated"></new-course-button>
  </n-divider>

  <n-modal
    v-model:show="showPurchaseModal"
    preset="dialog"
    title="Purchase Course"
    content="Do you want to purchase this course?"
    positive-text="Place Order"
    negative-text="Cancel"
    @positive-click="purchase"
  ></n-modal>
</template>
