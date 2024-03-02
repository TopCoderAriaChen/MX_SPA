<script setup lang="ts">
import { NLayout } from "naive-ui";
import LayoutContent from "./LayoutContent.vue";
import LayoutSidebar from "./LayoutSidebar.vue";
</script>

<template>
  <n-layout position="absolute" has-sider>
    <layout-sidebar></layout-sidebar>
    <n-layout>
      <layout-content></layout-content>
    </n-layout>
  </n-layout>
</template>
