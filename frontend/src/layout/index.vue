<script setup lang="ts">
import { NLayout } from "naive-ui";
import LayoutContent from "./LayoutContent.vue";
import LayoutSidebar from "./LayoutSidebar.vue";
import LayoutHeader from "./LayoutHeader.vue";
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
