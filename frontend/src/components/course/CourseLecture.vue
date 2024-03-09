<script lang="ts" setup>
import {
  deleteLecture,
  uploadAttachment,
  deleteAttachment,
  type Lecture,
} from "@/api/course";
import { computed, defineProps, ref } from "vue";
import {
  NCard,
  NThing,
  NAvatar,
  NIcon,
  NDescriptions,
  NDescriptionsItem,
  NA,
  NDivider,
  NButton,
  NPopconfirm,
  NSpace,
  NTag,
  NModal,
  NUpload,
  NUploadDragger,
  type UploadCustomRequestOptions,
  useMessage,
} from "naive-ui";
import {
  Archive,
  CloudUpload,
  DocumentAttach,
  Videocam,
} from "@vicons/ionicons5";
import { Delete, CloseFilled } from "@vicons/carbon";

const props = defineProps<{
  lecture: Lecture;
  course_id: string;
  isAdmin: Boolean;
  onUpdate: () => void;
}>();

const message = useMessage();
const showUpload = ref(false);
const handleAddNewAttachment = () => {
  showUpload.value = true;
};

const uploadRequest = async ({
  file,
  onFinish,
  onError,
  onProgress,
}: UploadCustomRequestOptions) => {
  try {
    console.log("upload");
    await uploadAttachment(
      props.course_id,
      props.lecture.id,
      file.file!,
      file.name,
      "attachment",
      ({ progress }) => {
        onProgress({ percent: Math.ceil(progress || 0) });
      }
    );
    onFinish();
    message.success("File Uploaded.");
    setTimeout(() => window.location.reload(), 1500);
  } catch (e) {
    onError();
  }
};

const scheduled_at = computed(() => new Date(props.lecture.scheduled_at + "Z"));

const handleDelete = async () => {
  try {
    await deleteLecture(props.course_id, props.lecture.id);
    message.success("Lecture deleted successfully.");
    props.onUpdate();
  } catch (error) {
      message.error("Failed to delete attachment.");
  }
};

const handleDeleteAttachment = async (attachmentName: string) => {
  try {
    await deleteAttachment(props.course_id, props.lecture.id, attachmentName);
    message.success("Attachment deleted successfully.");
    props.onUpdate();
  } catch (error) {
    message.error("Failed to delete attachment.");
  }
};
</script>
<template>
  <n-card>
    <n-thing>
      <template #avatar>
        <n-avatar>
          <n-icon :component="Videocam"></n-icon>
        </n-avatar>
      </template>
      <template #header>
        {{ props.lecture.title }}
      </template>
      <template #header-extra>
        {{ scheduled_at.toLocaleDateString() }}
      </template>
      <template #description>
        <div class="text-xs text-slate-300">{{ props.lecture.id }}</div>
      </template>
      <n-descriptions :column="1" label-placement="left">
        <n-descriptions-item label="Time">
          {{ scheduled_at.toLocaleTimeString() }}
        </n-descriptions-item>
        <n-descriptions-item label="Streaming">
          <n-a :href="props.lecture.streaming_url">Jump to Zoom</n-a>
        </n-descriptions-item>
        <n-descriptions-item label="Recording">
          <n-a :href="props.lecture.recording_url">Jump to Zoom</n-a>
        </n-descriptions-item>
      </n-descriptions>
      <template #footer>
        <n-divider class="text-xs text-gray-400"> Attachments </n-divider>
        <n-space>
          <n-tag
            v-for="attachment in props.lecture.attachments"
            :key="attachment.name"
            size="small"
            round
            :bordered="false"
            type="success"
          >
            <template #icon>
              <n-icon :component="DocumentAttach"></n-icon>
              <n-a :href="attachment.signed_url">{{ attachment.name }}</n-a>
            </template>
            <n-popconfirm
              @positive-click="() => handleDeleteAttachment(attachment.name)"
            >
              <template #trigger>
                <n-button
                  quaternary
                  type="error"
                  style="padding: 5px; height: 20px"
                >
                  <template #icon>
                    <n-icon size="15"><CloseFilled /></n-icon>
                  </template>
                </n-button>
              </template>
              Are you sure you want to delete this attachment?
            </n-popconfirm>
          </n-tag>
          <n-tag
            v-if="isAdmin"
            round
            :bordered="false"
            size="small"
            type="success"
          >
            <template #icon>
              <n-icon :component="CloudUpload"></n-icon>
            </template>
            <n-a @click="handleAddNewAttachment">Upload +</n-a>
          </n-tag>
        </n-space>
        <n-space justify="end" v-if="isAdmin">
          <n-popconfirm @positive-click="handleDelete">
            <template #trigger>
              <n-button quaternary type="error">
                <template #icon>
                  <n-icon><delete /></n-icon>
                </template>
              </n-button>
            </template>
            Are you sure you want to delete this lecture?
          </n-popconfirm>
        </n-space>
      </template>
    </n-thing>
  </n-card>
  <n-modal v-model:show="showUpload">
    <n-card
      style="width: 400px"
      title="Upload new attachment"
      :bordered="false"
      size="huge"
    >
      <n-upload :directory-dnd="false" :custom-request="uploadRequest">
        <n-upload-dragger>
          <div><n-icon size="48" :depth="3" :component="Archive"></n-icon></div>
          Click or drag to here
        </n-upload-dragger>
      </n-upload>
    </n-card>
  </n-modal>
</template>
