<script lang="ts" setup>
import {
  
  updateUser,
  getUser,
  USER_TYPE,
  type CreateUserData,
} from "@/api/user";
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
messageDark,
useMessage,
} from "naive-ui";
import { reactive, ref } from "vue";

const state = reactive({ courseOptions: [], campusOptions: [] });
const message = useMessage();
const updateUserFormRef = ref(null);
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
const updateUserForm = ref<CreateUserData>(defaultData);
const props = defineProps<{
  username: String;
  onCreated: () => void;
}>();

const handleOpenUpdateUserModal = async () => {
  const campuses = await getAllCampus();
  const courses = await getAllCourses();
  const data = await getUser(props.username);
  updateUserForm.value = data;
  updateUserForm.value.campus = data.campus.id;
  if (data.enrolled_courses) {
    updateUserForm.value.enrolled_courses = data.enrolled_courses.map(
      (c: { id: string }) => c.id
    );
  }
  state.campusOptions = campuses.map((c: { name: string; id: string }) => ({
    label: c.name,
    value: c.id,
  }));
  state.courseOptions = courses.map((c: { name: string; id: string }) => ({
    label: c.name,
    value: c.id,
  }));
  showUpdateUserModal.value = true;
};

const updateNewUser = async () => {
  await updateUser(updateUserForm.value.username, {
    ...updateUserForm.value,
  });
  updateUserForm.value = defaultData;
  showUpdateUserModal.value = false;
  message.success("User updated");
  props.onCreated();
};

const closeModal = () => {
  updateUserForm.value = defaultData;
  showUpdateUserModal.value = false;
};

const showUpdateUserModal = ref(false);

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
  <n-button
    size="small"
    style="margin-right: 8px"
    type="success"
    @click="handleOpenUpdateUserModal"
    >Check&Update</n-button
  >
  <n-modal v-model:show="showUpdateUserModal">
    <n-card
      style="width: 400px; margin: 0 auto"
      title="Update User"
      :bordered="false"
      size="huge"
    >
      <n-form
        ref="updateUserFormRef"
        :model="updateUserForm"
        label-placement="left"
        label-width="auto"
      >
        <n-form-item label="User Type" path="user_type">
          <n-radio-group :disabled="true" v-model:value="updateUserForm.user_type">
            <n-radio-button
              v-for="role in UserTypes"
              :key="role.value"
              :value="role.value"
              :label="role.label"
            />
          </n-radio-group>
        </n-form-item>
        <n-form-item label="User Name" path="username">
          <n-input :disabled="true" v-model:value="updateUserForm.username"></n-input>
        </n-form-item>
        <n-form-item label="Password" path="password">
          <n-input
            type="password"
            show-password-on="click"
            v-model:value="updateUserForm.password"
          ></n-input>
        </n-form-item>
        <n-form-item label="Display Name" path="display_name">
          <n-input v-model:value="updateUserForm.display_name"></n-input>
        </n-form-item>
        <n-form-item label="Telephone" path="telephone">
          <n-input v-model:value="updateUserForm.telephone"></n-input>
        </n-form-item>
        <n-form-item label="Campus" path="campus">
          <n-select
            :options="state.campusOptions"
            v-model:value="updateUserForm.campus"
          ></n-select>
        </n-form-item>
        <n-form-item
          v-show="updateUserForm.user_type === USER_TYPE.STUDENT"
          label="University"
          path="uni"
        >
          <n-input v-model:value="updateUserForm.uni"></n-input>
        </n-form-item>
        <n-form-item
          v-show="updateUserForm.user_type === USER_TYPE.STUDENT"
          label="WeChat"
          path="wx"
        >
          <n-input v-model:value="updateUserForm.wx"></n-input>
        </n-form-item>
        <n-form-item
          v-show="updateUserForm.user_type === USER_TYPE.TEACHER"
          label="abn"
          path="abn"
        >
          <n-input v-model:value="updateUserForm.abn"></n-input>
        </n-form-item>

        <n-form-item
          v-show="updateUserForm.user_type === USER_TYPE.STUDENT"
          label="Enrolled Courses"
          path="enrolled_courses"
        >
          <n-select
            :options="state.courseOptions"
            multiple
            :disabled="true"
            v-model:value="updateUserForm.enrolled_courses"
          ></n-select>
        </n-form-item>
        <n-form-item
          v-show="updateUserForm.user_type === USER_TYPE.ADMIN"
          label="Permission"
          path="permissions"
        >
          <n-select
            :options="Permission"
            multiple
            v-model:value="updateUserForm.permissions"
          ></n-select>
        </n-form-item>
      </n-form>
      <template #footer>
        <n-space justify="end">
          <n-button type="primary" @click="updateNewUser">Check&Update</n-button>
          <n-button @click="closeModal">Cancel</n-button>
        </n-space>
      </template>
    </n-card>
  </n-modal>
</template>
