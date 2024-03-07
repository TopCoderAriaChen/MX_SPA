<script lang="ts" setup>
import { useOrderList } from "@/api/order";
import OrderTable from "@/components/OrderTable.vue";
const { data: orders, isLoading, execute } = useOrderList();
</script>
<template>
  <order-table :orders="orders" :isLoading="isLoading" @update="execute" />
</template>
