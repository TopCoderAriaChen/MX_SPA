<script lang="ts" setup>
import { useUserList} from "@/api/user";
import UserTable from "@/components/UserTable.vue";
const { data: users, isLoading, execute } = useUserList();
</script>
<template>
  <user-table :users="users" :isLoading="isLoading" @update="execute" />
</template>