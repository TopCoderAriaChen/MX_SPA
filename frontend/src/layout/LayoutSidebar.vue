<script lang="ts" setup>
import { NIcon, NLayoutSider, NMenu } from 'naive-ui';
import { ref, h } from 'vue';
import { useRoute, RouterLink } from 'vue-router';
import { Book, Home } from '@vicons/ionicons5';

interface MenuItem {
  label: string;
  key: string;
  path: string;
  icon?: any;
  children?: MenuItem[];
}

const route = useRoute();
const currentKey = ref('home');
const collapsed = ref(false);

const menus: MenuItem[] = [
  {
    label: "Home",
    key: "home",
    path: "/",
    icon: Home,
  },
  {
    label: "Courses",
    key: "courses",
    path: "/courses",
    icon: Book,
    children: [
      {
        label: "Python - Basics",
        key: "courses/62c96de8d76bd4110d7b7464",
        path: "/courses/62c96de8d76bd4110d7b7464",
      },
    ],
  },
];


const renderMenu = (menus: MenuItem[]): any =>
  menus.map((item) => ({
    label: () =>
      h(RouterLink, { to: { path: item.path } }, { default: () => item.label }),
    key: item.key,
    icon:
      item.icon != null
        ? () => h(NIcon, null, { default: () => h(item.icon) })
        : undefined,
    children: item.children ? renderMenu(item.children) : undefined,
  }));

const menuOptions = renderMenu(menus);
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

