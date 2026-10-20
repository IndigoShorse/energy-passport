<script setup lang="ts">

</script>

<template>
  <header class="headerWrap">
    <div class="headerBar">
      <div class="logoBlock">
        <NuxtLink to="/">
          <img src="/mainLogo.svg" alt="Энергопаспорт" height="52" />
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
  </header>
</template>

<style scoped>
.headerWrap {
  position: sticky;
  top: 0;
  z-index: 10;
  width: 100%;
  background: rgba(255, 255, 255, .96);
  border-bottom: 1px solid #e4ebed;
  box-shadow: 0 2px 14px rgba(24, 54, 70, .04);
}

.headerBar {
  max-width: 1240px;
  min-height: 76px;
  margin: 0 auto;
  padding: 10px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 28px;
}

.logoBlock {
  display: flex;
  align-items: center;
}

.navBlock {
  display: flex;
  align-items: center;
  gap: 28px;
}

.navBlock a {
  width: max-content;
  padding: 9px 0;
  border-bottom: 2px solid transparent;
  color: #48606e;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  transition: color .2s ease, border-color .2s ease;
}

.navBlock a:visited {
  color: #48606e;
}

.navBlock a.router-link-active,
.navBlock a.router-link-exact-active {
  color: var(--ep-primary);
  border-color: #4a9a86;
  font-weight: 600;
}

.navBlock a:hover {
  color: var(--ep-primary);
}

.contactsBar {
  color: var(--ep-primary);
  font-size: 13px;
  font-weight: 500;
  white-space: nowrap;
}

.contactItem {
  text-decoration: none;
  color: var(--ep-primary);
}

.contactItem:hover {
  text-decoration: underline;
  color: color-mix(in oklab, var(--ep-primary), #000, 80%);
}

@media (max-width: 820px) {
  .headerBar {
    min-height: auto;
    flex-wrap: wrap;
    padding: 12px 20px;
    gap: 12px 20px;
  }

  .navBlock {
    order: 3;
    width: 100%;
    overflow-x: auto;
    gap: 22px;
    padding-bottom: 2px;
  }

  .contactsBar {
    margin-left: auto;
  }
}

@media (max-width: 520px) {
  .headerBar {
    padding: 10px 16px;
  }

  .logoBlock img {
    height: 42px;
  }

  .contactsBar {
    font-size: 12px;
  }
}
</style>
