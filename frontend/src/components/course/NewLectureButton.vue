<script lang="ts" setup>
import { createLecture, type CreateLectureData } from "@/api/course";
import {
  NButton,
  NModal,
  NCard,
  NForm,
  NFormItem,
  NDatePicker,
  NInput,
  NSpace,
} from "naive-ui";
import { ref } from "vue";
const newLectureFormRef = ref(null);
const newLectureForm = ref<CreateLectureData>({
  title: "",
  streaming_url: "",
  recording_url: "",
  scheduled_at: "",
  attachments: [],
});
const props = defineProps<{
  courseId: string;
  onCreated: () => void;
}>();

const handleDateUpdate = (value: number) => {
  newLectureForm.value.scheduled_at = new Date(value)
    .toISOString()
    .split(".")[0];
};
const createNewLecture = async () => {
  await createLecture(props.courseId, newLectureForm.value);
  showNewLectureModal.value = false;
  props.onCreated();
};
handleDateUpdate(Date.now());
const showNewLectureModal = ref(false);
</script>
<template>
  <n-button type="success" @click="showNewLectureModal = true"
    >Add New Lecture</n-button
  >
  <n-modal v-model:show="showNewLectureModal">
    <n-card
      style="width: 400px; margin: 0 auto"
      title="Add New Lecture"
      :bordered="false"
      size="huge"
    >
      <n-form
        ref="newLectureFormRef"
        :model="newLectureForm"
        label-placement="left"
        label-width="auto"
      >
        <n-form-item label="Title" path="title">
          <n-input v-model:value="newLectureForm.title"></n-input>
        </n-form-item>
        <n-form-item label="Streaming link" path="streaming_url">
          <n-input v-model:value="newLectureForm.streaming_url"></n-input>
        </n-form-item>
        <n-form-item label="Recording link" path="recording_url">
          <n-input v-model:value="newLectureForm.recording_url"></n-input>
        </n-form-item>
        <n-form-item label="Datetime" path="scheduled_at">
          <n-date-picker
            :on-update-value="handleDateUpdate"
            :default-value="Date.now()"
            type="datetime"
          ></n-date-picker>
        </n-form-item>
      </n-form>
      <template #footer>
        <n-space justify="end">
          <n-button type="primary" @click="createNewLecture">Create</n-button>
          <n-button @click="showNewLectureModal = false">Cancel</n-button>
        </n-space>
      </template>
    </n-card>
  </n-modal>
</template>
