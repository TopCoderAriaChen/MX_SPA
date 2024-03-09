<script setup lang="ts">
import { NCard, NSpace, NH2, NP, NAvatar, NTag, NIcon } from "naive-ui";
import { Person } from "@vicons/ionicons5";
import type { User } from "@/interfaces/user.interface";
const props = defineProps<{
  userInfo: User;
}>();
</script>
<template>
  <n-card
    :segmented="{
      content: true,
      footer: 'soft',
    }"
  >
    <template #default>
      <n-space justify="space-between" align="center">
        <n-space vertical>
          <n-h2> Welcome {{ props.userInfo?.display_name }}</n-h2>
          <n-p> Telehpone: {{ props.userInfo?.telephone }}</n-p>
          <n-p> Current campus: {{ props.userInfo?.campus.name }}</n-p>
        </n-space>
        <n-avatar :size="96" round>
          <img src="~@/assets/logo.jpg" alt="" />
        </n-avatar>
      </n-space>
    </template>
    <template #footer>
      <n-space>
        <n-tag type="success" round :bordered="false"
          >{{ props.userInfo?.user_type }}
          <template #icon>
            <n-icon :component="Person"></n-icon>
          </template>
        </n-tag>
        <n-tag
          v-for="permission in props.userInfo?.permissions"
          round
          :key="permission.toString()"
          :bordered="false"
        >
          {{ permission }}
        </n-tag>
      </n-space>
    </template>
  </n-card>
</template>
