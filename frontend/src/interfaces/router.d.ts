import "vue-router";
declare module "vue-router" {
  interface RouteMeta extends Record<string, unknown> {
    requiresAuth: boolean;
    title: string;
  }
}
