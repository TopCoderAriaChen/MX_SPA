<script lang="ts" setup>
import { NIcon, NLayoutSider, NMenu, NA } from "naive-ui";
import { ref, h, computed } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { Book, Home } from "@vicons/ionicons5";
import { useAuthStore } from "../stores/auth.ts"
import { storeToRefs } from "pinia";

interface MenuItem {
  label: string;
  key: string;
  path: string;
  icon?: any;
  children?: MenuItem[];
}

const route = useRoute();
const currentKey = ref(route.fullPath.slice(1));
const collapsed = ref(false);
const authStore = useAuthStore();
const auth = storeToRefs(authStore);

const menus = computed<MenuItem[]>(() => {
  return [
    {
      label: "Home",
      key: "home",
      path: "/",
      icon: Home
    },
    {
      label: "Courses",
      key: "courses",
      path: "/courses",
      icon: Book,
      children: auth.getUserInfo.value?.enrolled_courses?.map(
        ({ course_id, course_name }) => ({
          label: course_name,
          key: `courses/${course_id}`,
          path: `/courses/${course_id}`
        })
      )
    }
  ];
});

const renderMenu = (menus: MenuItem[]): any =>
  menus.map((item) => ({
    label: () =>
      h(RouterLink, { to: { path: item.path } }, { default: () => item.label }),
    key: item.key,
    icon:
      item.icon != null
        ? () => h(NIcon, null, { default: () => h(item.icon) })
        : undefined,
    children: item.children ? renderMenu(item.children) : undefined
  }));

const menuOptions = computed(() => renderMenu(menus.value));
</script>

<template>
  <n-layout-sider
    bordered
    :width="240"
    :native-scrollbar="false"
    show-trigger
    collapse-mode="width"
    v-model:collapsed="collapsed"
  >
    <router-link to="/" custom #="{ navigate, href }">
      <n-a class="logo" :href="href" @click="navigate">
        <img src="@/assets/logo.png" />
        <span>MoxueOnline</span>
      </n-a>
    </router-link>
    <n-menu
      :value="currentKey"
      :options="menuOptions"
      :collapsed="collapsed"
      @update:value="
        (k) => {
          currentKey = k;
        }
      "
    />
  </n-layout-sider>
</template>

<style lang="less" scoped>
.logo {
  position: sticky;
  top: 0;
  display: flex;
  align-items: center;
  font-size: 1.2em;
  font-weight: 300;
  text-decoration: none;
  padding: 20px;
  transition: padding 0.3s, font-size 0.3s;
  img {
    height: 32px;
    margin-right: 8px;
    transition: margin 0.3s;
  }
}

.n-layout-sider--collapsed .logo {
  font-size: 0;
  padding: 20px 12px;
  img {
    margin-right: 0px;
  }
}
</style>
