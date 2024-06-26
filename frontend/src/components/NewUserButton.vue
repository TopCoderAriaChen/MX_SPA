<script lang="ts" setup>
import { createUser, USER_TYPE, type CreateUserData } from "@/api/user";
import { getAllCourses } from "@/api/course";
import { getAllCampus } from "@/api/campus";
import {
  NButton,
  NModal,
  NCard,
  NForm,
  NFormItem,
  NDatePicker,
  NInput,
  NSpace,
  NInputNumber,
  NSelect,
  NRadioGroup,
  NRadioButton,
useMessage,
} from "naive-ui";
import { reactive, ref } from "vue";

const state = reactive({ courseOptions: [], campusOptions: [] });
const message = useMessage();
const newUserFormRef = ref(null);
const defaultData = {
  username: "",
  password: "",
  display_name: "",
  campus: "",
  user_type: USER_TYPE.STUDENT,
  wx: "",
  abn: "",
  uni: "",
  enrolled_courses: [],
  permissions: [],
  telephone: "",
};
const newUserForm = ref<CreateUserData>(defaultData);
const props = defineProps<{
  onCreated: () => void;
}>();

const handleOpenNewUserModal = async () => {
  const campuses = await getAllCampus();
  const courses = await getAllCourses();
  state.campusOptions = campuses.map((c: { name: string; id: string }) => ({
    label: c.name,
    value: c.id,
  }));
  state.courseOptions = courses.map((c: { name: string; id: string }) => ({
    label: c.name,
    value: c.id,
  }));
  showNewUserModal.value = true;
};

const createNewUser = async () => {
  await createUser(newUserForm.value.user_type, {
    ...newUserForm.value,
  });
  newUserForm.value = defaultData;
  message.success("User updated");
  showNewUserModal.value = false;
  props.onCreated();
};

const closeModal = () => {
  newUserForm.value = defaultData;
  showNewUserModal.value = false;
};

const showNewUserModal = ref(false);

const UserTypes = [
  { label: "Student", value: USER_TYPE.STUDENT },
  { label: "Teacher", value: USER_TYPE.TEACHER },
  { label: "Admin", value: USER_TYPE.ADMIN },
];

const Permission = [
  {
    label: "System Owner",
    value: "sys_owner",
  },
  {
    label: "Campus Admin",
    value: "campus_admin",
  },
  {
    label: "Course Admin",
    value: "course_admin",
  },
  {
    label: "User Admin",
    value: "user_admin",
  },
  {
    label: "Order Admin",
    value: "order_admin",
  },
];
</script>
<template>
  <n-button type="success" @click="handleOpenNewUserModal"
    >Add New User</n-button
  >
  <n-modal v-model:show="showNewUserModal">
    <n-card
      style="width: 400px; margin: 0 auto"
      title="Add New User"
      :bordered="false"
      size="huge"
    >
      <n-form
        ref="newUserFormRef"
        :model="newUserForm"
        label-placement="left"
        label-width="auto"
      >
        <n-form-item label="User Type" path="user_type">
          <n-radio-group v-model:value="newUserForm.user_type">
            <n-radio-button
              v-for="role in UserTypes"
              :key="role.value"
              :value="role.value"
              :label="role.label"
            />
          </n-radio-group>
        </n-form-item>
        <n-form-item label="User Name" path="username">
          <n-input v-model:value="newUserForm.username"></n-input>
        </n-form-item>
        <n-form-item label="Password" path="password">
          <n-input
            type="password"
            show-password-on="click"
            v-model:value="newUserForm.password"
          ></n-input>
        </n-form-item>
        <n-form-item label="Display Name" path="display_name">
          <n-input v-model:value="newUserForm.display_name"></n-input>
        </n-form-item>
        <n-form-item label="Telephone" path="telephone">
          <n-input v-model:value="newUserForm.telephone"></n-input>
        </n-form-item>
        <n-form-item label="Campus" path="campus">
          <n-select
            :options="state.campusOptions"
            v-model:value="newUserForm.campus"
          ></n-select>
        </n-form-item>
        <n-form-item
          v-show="newUserForm.user_type === USER_TYPE.STUDENT"
          label="University"
          path="uni"
        >
          <n-input v-model:value="newUserForm.uni"></n-input>
        </n-form-item>
        <n-form-item
          v-show="newUserForm.user_type === USER_TYPE.STUDENT"
          label="WeChat"
          path="wx"
        >
          <n-input v-model:value="newUserForm.wx"></n-input>
        </n-form-item>
        <n-form-item
          v-show="newUserForm.user_type === USER_TYPE.TEACHER"
          label="abn"
          path="abn"
        >
          <n-input v-model:value="newUserForm.abn"></n-input>
        </n-form-item>

        <!-- <n-form-item
          v-show="newUserForm.user_type === USER_TYPE.STUDENT"
          label="Enrolled Courses"
          path="enrolled_courses"
        >
          <n-select
            :options="state.courseOptions"
            multiple
            v-model:value="newUserForm.enrolled_courses"
          ></n-select>
        </n-form-item> -->
        <n-form-item
          v-show="newUserForm.user_type === USER_TYPE.ADMIN"
          label="Permission"
          path="permissions"
        >
          <n-select
            :options="Permission"
            multiple
            v-model:value="newUserForm.permissions"
          ></n-select>
        </n-form-item>
      </n-form>
      <template #footer>
        <n-space justify="end">
          <n-button type="primary" @click="createNewUser">Create</n-button>
          <n-button @click="closeModal">Cancel</n-button>
        </n-space>
      </template>
    </n-card>
  </n-modal>
</template>
