<script setup lang="ts">

</script>

<template>
  <Header />
  <div class="pageBody">
    <slot />
  </div>
</template>

<style scoped>
  .pageBody {
    display: flex;
    flex-direction: column;
    min-height: calc(100vh - 77px);
  }
</style>
