<script lang="ts" setup>
import { NIcon, NLayoutSider, NMenu, NA } from "naive-ui";
import { ref, h } from "vue";
import { useRoute, RouterLink } from "vue-router";
import { Book, Home } from "@vicons/ionicons5";

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

const menus: MenuItem[] = [
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
    children: [
      {
        label: "Python - Basics",
        key: "courses/62c96de8d76bd4110d7b7464",
        path: "/courses/62c96de8d76bd4110d7b7464"
      }
    ]
  }
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
    children: item.children ? renderMenu(item.children) : undefined
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
