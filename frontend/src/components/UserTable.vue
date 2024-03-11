<script setup lang="tsx">
import { useAuthStore } from "@/stores/auth";
import type { RawAxiosRequestConfig } from "axios";
import Button from "naive-ui/es/button/src/Button";
import { computed, reactive, ref, type Ref } from "vue";
import NewUserButton from "./NewUserButton.vue";
import UpdateUserButton from "./UpdateUserButton.vue";
import { NDataTable, useMessage, NDivider } from "naive-ui";
import type { User } from "@/interfaces/user.interface";
import { deleteUser } from "@/api/user";

const props = defineProps<{
  isLoading: boolean;
  users?: Array<User>;
  onUpdate: () => void;
}>();

const emit = defineEmits<{
  (e: "update", config: RawAxiosRequestConfig): void;
}>();

const message = useMessage();
const { hasPermission } = useAuthStore();

const onUserCreated = () => {
  props.onUpdate();
};

const handleUpdate = () => {
  props.onUpdate();
};

const handleDelete = async (user: User) => {
  const { username } = user;
  await deleteUser({ username });
  message.success("User deleted");
  props.onUpdate();
};

const columns = ref([
  {
    key: "id",
    title: "ID",
  },
  {
    key: "username",
    title: "Username",
  },
  {
    key: "display_name",
    title: "Display Name",
  },
  {
    key: "telephone",
    title: "Telephone",
  },
  {
    key: "campus.name",
    title: "Campus",
  },
  {
    key: "user_type",
    title: "User Type",
  },
  {
    key: "action",
    title: "Actions",
    render: (record: User) => {
      if (hasPermission("user_admin") || hasPermission("sys_owner"))
        return (
          <>
            <UpdateUserButton
              username={record.username}
              onCreated={handleUpdate}
            />
            <Button
              size="small"
              type="error"
              onClick={() => {
                handleDelete(record);
              }}
            >
              Delete
            </Button>
          </>
        );
    },
  },
]) as any;
</script>
<template>
  <n-data-table
    remote
    :columns="columns"
    :loading="isLoading"
    :data="users"
    striped
  />
  <n-divider v-if="hasPermission('user_admin') || hasPermission('sys_owner')">
    <new-user-button :on-created="onUserCreated"></new-user-button>
  </n-divider>
</template>
