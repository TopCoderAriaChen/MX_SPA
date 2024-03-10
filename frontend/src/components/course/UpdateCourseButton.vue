<script lang="ts" setup>
import {
  updateCourse,
  type UpdateCourceData,
  type CreateCourceData,
  useCourse,
} from "@/api/course";
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
const updateCourseForm = ref<CreateCourceData>({
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
  course_id: string;
  onUpdated: () => void;
}>();

const handleOpenUpdateCourseModal = async () => {
  const teachers = await getAllTeachers();
  const campuses = await getAllCampus();
  const { data: course } = await useCourse(props.course_id);
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

  if (course) {
    const {
      name,
      uni_course_code,
      description,
      teacher,
      campus,
      original_price,
      cover_image,
      publish_time,
      // @ts-ignore
    } = course._value;

    updateCourseForm.value = {
      ...updateCourseForm.value,
      name,
      uni_course_code,
      description,
      teacher: teacher.id,
      campus: campus.id,
      original_price,
      cover_image,
      publish_time,
    };
  }
  showUpdateCourseModal.value = true;
};

const handleDateUpdate = (value: number) => {
  updateCourseForm.value.publish_time = new Date(value)
    .toISOString()
    .split(".")[0];
};
const updateNewCourse = async () => {
  const { name, uni_course_code, description, original_price } =
    updateCourseForm.value;
  await updateCourse({
    course_id: props.course_id,
    name,
    uni_course_code,
    description,
    original_price: String(original_price),
  });
  showUpdateCourseModal.value = false;
  props.onUpdated();
};
const createNewCource = async () => {
  showUpdateCourceModal.value = false;
  props.onUpdated();
};

handleDateUpdate(Date.now());
const showUpdateCourseModal = ref(false);
const showUpdateCourceModal = ref(false);
</script>
<template>
  <n-button size="small" @click="handleOpenUpdateCourseModal">Update</n-button>
  <n-modal v-model:show="showUpdateCourseModal">
    <n-card
      style="width: 400px; margin: 0 auto"
      title="Update Course"
      :bordered="false"
      size="huge"
    >
      <n-form
        ref="newCourseFormRef"
        :model="updateCourseForm"
        label-placement="left"
        label-width="auto"
      >
        <n-form-item label="Name" path="name">
          <n-input v-model:value="updateCourseForm.name"></n-input>
        </n-form-item>
        <n-form-item label="Course Code" path="uni_course_code">
          <n-input v-model:value="updateCourseForm.uni_course_code"></n-input>
        </n-form-item>
        <n-form-item label="Description" path="description">
          <n-input v-model:value="updateCourseForm.description"></n-input>
        </n-form-item>
        <n-form-item label="Teacher" path="teacher">
          <n-select
            :disabled="true"
            :options="state.teacherOptions"
            v-model:value="updateCourseForm.teacher"
          ></n-select>
        </n-form-item>
        <n-form-item label="Campus" path="campus">
          <n-select
            :disabled="true"
            :options="state.campusOptions"
            v-model:value="updateCourseForm.campus"
          ></n-select>
        </n-form-item>
        <n-form-item label="Original Price" path="original_price">
          <n-input-number v-model:value="updateCourseForm.original_price">
          </n-input-number>
        </n-form-item>
        <n-form-item label="Cover Image" path="cover_image">
          <n-input
            :disabled="true"
            v-model:value="updateCourseForm.cover_image"
          ></n-input>
        </n-form-item>
        <n-form-item label="Publish_time" path="publish_time">
          <n-date-picker
            :disabled="true"
            :on-update-value="handleDateUpdate"
            :default-value="Date.now()"
            type="datetime"
          ></n-date-picker>
        </n-form-item>
      </n-form>
      <template #footer>
        <n-space justify="end">
          <n-button type="primary" @click="updateNewCourse">Update</n-button>
          <n-button @click="showUpdateCourseModal = false">Cancel</n-button>
        </n-space>
      </template>
    </n-card>
  </n-modal>
</template>
