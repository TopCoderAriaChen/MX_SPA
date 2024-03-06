<script setup lang="ts">
import { NLayout } from "naive-ui";
import LayoutContent from "./LayoutContent.vue";
import LayoutSidebar from "./LayoutSidebar.vue";
import LayoutHeader from "./LayoutHeader.vue";
import { useAuthStore } from "@/stores/auth";
import { onMounted } from "vue";

const authStore = useAuthStore();

onMounted(() => {
  authStore.reload();
});
</script>

<template>
  <n-layout position="absolute" has-sider>
    <layout-sidebar />
    <n-layout>
      <layout-header></layout-header>
      <layout-content></layout-content>
    </n-layout>
  </n-layout>
</template>
