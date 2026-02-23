<script setup lang="ts">

</script>

<template>
  <div class="headerWrap">
    <div class="headerBar">
      <div class="logoBlock">
        <NuxtLink to="/">
          <img src="/public/mainLogo.svg" alt="Main Logo" height="60" />
        </NuxtLink>
      </div>
      <div class="navBlock">
        <NuxtLink to="/"> Главная </NuxtLink>
        <NuxtLink to="/passports/create"> Создать паспорт </NuxtLink>
        <NuxtLink to="/passports/downloads"> Таблица паспортов </NuxtLink>
      </div>
      <div class="contactsBar">
        <a class="contactItem" href="mailto:energypassport42@mail.ru">
          energypassport42@mail.ru
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.headerWrap {
  position: relative;
  background: #fff;
  width: 100%;
}
.navBlock {
  display: flex;
  flex-direction: row;
  gap: 50px;
}
.navBlock a {
  width: max-content;
  font-size: 16px;
  text-decoration: none;
  color: #275c8c;
}
.navBlock a:visited {
  color: #275c8c;
}
.navBlock a.router-link-active,
.navBlock a.router-link-exact-active {
  color: #508ad5;
  font-weight: 600;
}
.navBlock a:hover {
  color: #508ad5;
}
.logoBlock {
  padding-bottom: 5px;
  padding-top: 10px;
}
.headerBar {
  width: 1280px;
  margin: 0 auto;
  padding: 5px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.contactsBar {
  padding-top: 3px;
}
</style>