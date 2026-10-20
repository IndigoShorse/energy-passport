<script setup lang="ts">
import type {passportListItem} from "~/models/types/passportTypes";
import passportData from "~/composables/PassportData";

  const response = await PassportData().get_passports_list();
  const passports = ref<Array<passportListItem>>(response);
  console.log(response, passports.value);

  const handleClick = async (id: string) => {
    try {
      await passportData().download_passport(id);
      console.log('Download started');
    } catch (error) {
      console.error('Download failed:', error);
    }
  };
</script>

<template>
  <div class="container">
    <v-sheet class="tableSheet" elevation="0">
      <v-table theme="light" density="comfortable">
        <thead>
        <tr>
          <th class="text-left">
            Подписант
          </th>
          <th class="text-left">
            Организация
          </th>
        </tr>
        </thead>
        <tbody>
        <tr
            v-for="passport in passports"
            :key="passport.id"
            @click="handleClick(passport.id)"
            class="table-row"
        >
          <td>{{passport.customers_signature}}</td>
          <td>{{passport.name_organization}}</td>
        </tr>
        </tbody>
      </v-table>
    </v-sheet>
  </div>
</template>

<style scoped>
.container { width: 100%; max-width: 1240px; margin: 0 auto; padding: 40px 24px 56px; }
.tableSheet { overflow: hidden; border: 1px solid #e1e9eb; border-radius: 14px; box-shadow: 0 8px 24px rgba(31, 63, 79, .07); }
.tableSheet :deep(th) { background: #edf4f5; color: #31566b; font-size: 13px; font-weight: 700; letter-spacing: .02em; text-transform: uppercase; }
.tableSheet :deep(td), .tableSheet :deep(th) { padding: 16px 20px !important; }
.table-row:hover {
  background: #f3f8f7;
  color: #1f5d83;
  cursor: pointer;
}
@media (max-width: 520px) { .container { padding: 24px 16px 40px; } .tableSheet :deep(td), .tableSheet :deep(th) { padding: 13px 14px !important; } }
</style>
