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
    <v-sheet elevation="4">
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
.container {
  width: 1280px;
  margin: 0 auto;
}
.table-row:hover {
  background: #eee;
  color: #333;
  font-weight: 600;
  cursor: pointer;
}
</style>