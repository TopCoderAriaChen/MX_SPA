
import { progressProps } from 'naive-ui';
<script lang="ts" setup>
import { deleteLecture, type Lecture } from "@/api/courses";
import { computed, defineProps } from "vue";
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
  NSpace
} from "naive-ui";
import { Videocam } from "@vicons/ionicons5";
import { Delete } from "@vicons/carbon";

const props = defineProps<{
  lecture: Lecture;
  course_id: string;
  isAdmin: boolean;
  onUpdate: () => void;
}>();

const scheduled_at = computed(() => new Date(props.lecture.scheduled_at + "Z"));

const handleDelete = async () => {
  await deleteLecture(props.course_id, props.lecture.id);
  props.onUpdate();
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
</template>
