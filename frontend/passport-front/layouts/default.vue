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
  }
</style>