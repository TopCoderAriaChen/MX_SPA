<script setup lang="tsx">
import { payOrder, type Order } from "@/api/order";
import type { PaginatedResponse } from "@/interfaces/api.interface";
import { useAuthStore } from "@/stores/auth";
import type { RawAxiosRequestConfig } from "axios";
import Button from "naive-ui/es/button/src/Button";
import { storeToRefs } from "pinia";
import { computed, reactive, ref, type Ref } from "vue";
import { dayjs } from "../utils/date";
import {
  NDataTable,
  NTag,
  NModal,
  NCard,
  NSpace,
  NH1,
  NForm,
  NFormItem,
  NInputNumber,
  NInput,
  NButton,
  type DataTableColumn,
  type PaginationInfo,
  useMessage,
} from "naive-ui";

const props = defineProps<{
  isLoading: boolean;
  orders?: PaginatedResponse<Order>;
}>();

const emit = defineEmits<{
  (e: "update", config: RawAxiosRequestConfig): void;
}>();

const authStore = useAuthStore();
const message = useMessage();

const showConfirmPayment = ref(false);
const clickedOrder = ref<Order | null>(null);
const params = reactive<{
  page: number;
  paid?: boolean;
}>({
  page: 1,
});

const paymentForm = ref({
  price: 0,
  comment: "",
});

const confirmPayment = async () => {
  await payOrder(
    clickedOrder.value?.id || "",
    paymentForm.value.comment,
    paymentForm.value.price
  );
  params.page = 1;
  delete params.paid;
  emit("update", {});
  showConfirmPayment.value = false;
  message.success("Payment confirmed");
};

const handleFilterChange = async (filters: Record<string, any>) => {
  params.page = 1;
  params.paid = filters.paid;
  emit("update", { params: params });
};

const paymentColumn = {
  key: "paid",
  title: "Payment",
  render: (record: Order) => {
    if (record.paid) {
      // @ts-ignore
      return <NTag type="success">Paid</NTag>;
    } else {
      return authStore.hasPermission("order_admin") ? (
        // @ts-ignore
        <Button type="primary" size="small" onClick={() => {
            showConfirmPayment.value = true;
            clickedOrder.value = record;
          }}
        >
          Pay
        </Button>
      ) : (
        // @ts-ignore
        <NTag type="warning">Unpaid</NTag>
      );
    }
  },
  filter: true,
  filterMultiple: false,
  filterOptionValue: null,
  filterOptions: [
    {
      label: "Paid",
      value: true,
    },
    {
      label: "Not paid",
      value: false,
    },
  ],
};

const columns = ref([
  {
    key: "id",
    title: "ID",
  },
  {
    key: "course.name",
    title: "Course",
  },
  {
    key: "student.display_name",
    title: "Student",
  },
  {
    key: "created_time",
    title: "Order Time",
    render(row: Order) {
      return dayjs(row.paid_time).toString();
    },
  },
  {
    key: "original_price",
    title: "Original Price",
    render(row: Order) {
      return "$" + row.original_price;
    },
  },
  paymentColumn,
]) as any;

const pagination = computed(() => ({
  page: props.orders?.page,
  pageSize: props.orders?.limit,
  pageCount: props.orders?.pages,
  itemCount: props.orders?.total,
  prefix: ({ itemCount }: PaginationInfo) => {
    return `Total Orders: ${itemCount}`;
  },
  onChange: (page: number) => {
    params.page = page;
    emit("update", {
      params: params,
    });
  },
}));
</script>
<template>
  <n-data-table
    remote
    :columns="columns"
    :loading="isLoading"
    :data="orders?.items"
    :pagination="pagination"
    @update:filters="handleFilterChange"
    striped
  />
  <n-modal v-model:show="showConfirmPayment">
    <n-card
      style="width: 500px"
      title="Confirm Payment"
      :bordered="false"
      size="huge"
    >
      <n-space vertical>
        <n-h1>Payment Details:</n-h1>
        <n-form ref="paymentFormRef" :label-width="80" :model="paymentForm">
          <n-form-item label="Actual Payment" path="price">
            <n-input-number
              v-model:value="paymentForm.price"
              :show-button="false"
            >
              <template #prefix> $ </template>
            </n-input-number>
          </n-form-item>
          <n-form-item label="Comment" path="comment">
            <n-input
              v-model:value="paymentForm.comment"
              type="textarea"
            ></n-input>
          </n-form-item>
        </n-form>
      </n-space>
      <template #footer>
        <n-space>
          <n-button type="primary" @click="confirmPayment">Confirm</n-button>
          <n-button @click="showConfirmPayment = false">Cancel</n-button>
        </n-space>
      </template>
    </n-card>
  </n-modal>
</template>
