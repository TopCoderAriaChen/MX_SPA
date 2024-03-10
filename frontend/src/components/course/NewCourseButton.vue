<script lang="ts" setup>
import { createCource, type CreateCourceData } from "@/api/course";
import { getAllCampus } from "@/api/campus";
import { getAllTeachers } from "@/api/user";
import type { User } from "@/interfaces/user.interface";
import {
  NButton,
  NModal,
  NCard,
  NForm,
  NFormItem,
  NDatePicker,
  NInput,
  NSpace,
  NInputNumber,
  NSelect,
} from "naive-ui";
import { reactive, ref } from "vue";

const state = reactive({ teacherOptions: [], campusOptions: [] });

const newCourseFormRef = ref(null);
const newCourseForm = ref<CreateCourceData>({
  name: "",
  uni_course_code: "",
  description: "",
  teacher: "",
  campus: "",
  original_price: 0,
  cover_image: "",
  publish_time: "",
});
const props = defineProps<{
  onCreated: () => void;
}>();

const handleOpenNewCourseModal = async () => {
  const teachers = await getAllTeachers();
  const campuses = await getAllCampus();
  state.teacherOptions = teachers.map(
    (t: { username: string; id: string }) => ({
      label: t.username,
      value: t.id,
    })
  );
  state.campusOptions = campuses.map((c: { name: string; id: string }) => ({
    label: c.name,
    value: c.id,
  }));
  showNewCourseModal.value = true;
};

const handleDateUpdate = (value: number) => {
  newCourseForm.value.publish_time = new Date(value)
    .toISOString()
    .split(".")[0];
};
const createNewCourse = async () => {
  await createCource({
    ...newCourseForm.value,
  });
  showNewCourseModal.value = false;
  props.onCreated();
};
const createNewCource = async () => {
  showNewCourceModal.value = false;
  props.onCreated();
};

handleDateUpdate(Date.now());
const showNewCourseModal = ref(false);
const showNewCourceModal = ref(false);
</script>
<template>
  <n-button type="success" @click="handleOpenNewCourseModal"
    >Add New Course</n-button
  >
  <n-modal v-model:show="showNewCourseModal">
    <n-card
      style="width: 400px; margin: 0 auto"
      title="Add New Course"
      :bordered="false"
      size="huge"
    >
      <n-form
        ref="newCourseFormRef"
        :model="newCourseForm"
        label-placement="left"
        label-width="auto"
      >
        <n-form-item label="Name" path="name">
          <n-input v-model:value="newCourseForm.name"></n-input>
        </n-form-item>
        <n-form-item label="Course Code" path="uni_course_code">
          <n-input v-model:value="newCourseForm.uni_course_code"></n-input>
        </n-form-item>
        <n-form-item label="Description" path="description">
          <n-input v-model:value="newCourseForm.description"></n-input>
        </n-form-item>
        <n-form-item label="Teacher" path="teacher">
          <n-select
            :options="state.teacherOptions"
            v-model:value="newCourseForm.teacher"
          ></n-select>
        </n-form-item>
        <n-form-item label="Campus" path="campus">
            <n-select
            :options="state.campusOptions"
            v-model:value="newCourseForm.campus"
          ></n-select>
     
        </n-form-item>
        <n-form-item label="Original Price" path="original_price">
          <n-input-number v-model:value="newCourseForm.original_price">
          </n-input-number>
        </n-form-item>
        <n-form-item label="Cover Image" path="cover_image">
          <n-input v-model:value="newCourseForm.cover_image"></n-input>
        </n-form-item>
        <n-form-item label="Publish_time" path="publish_time">
          <n-date-picker
            :on-update-value="handleDateUpdate"
            :default-value="Date.now()"
            type="datetime"
          ></n-date-picker>
        </n-form-item>
      </n-form>
      <template #footer>
        <n-space justify="end">
          <n-button type="primary" @click="createNewCourse">Create</n-button>
          <n-button @click="showNewCourseModal = false">Cancel</n-button>
        </n-space>
      </template>
    </n-card>
  </n-modal>
</template>
