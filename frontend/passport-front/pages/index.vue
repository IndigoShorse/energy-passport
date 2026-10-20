<script setup lang="ts">

</script>

<template>
  <div class="mainImg">
    <div class="mainLabel">
      <div class="mainContainer">
        Цифровой энергопаспорт
      </div>
    </div>
    <div class="buttonsContainer">
      <v-btn class="mainBtn" color="#fff" size="large" variant="elevated" @click="navigateTo('/passports/downloads')">
        Скачать паспорт
      </v-btn>
      <v-btn class="mainBtn" color="#275c8c" size="large" variant="elevated" @click="navigateTo('/passports/create')">
        Создать паспорт
      </v-btn>
    </div>
  </div>
  <div class="mainBody">
    <div class="mainContainer">
      <div class="mainGrid">
        <v-card
            elevation="5"
            class="mx-auto"
            width="fit-content"
        >
          <template v-slot:title>
          <span class="cardTitle">
            <img src="/public/icons/card-image-1.png" class="cardIcon"/>
            <span class="font-weight-black">Кто мы?</span>
          </span>
          </template>

          <div class="cardText">
            Мы – команда профессионалов, работающих в сфере цифровизации энергетики. Наша деятельность направлена на
            внедрение отечественных IT-решений, соответствующих актуальным национальным целям развития и требованиям
            импортозамещения.
          </div>
        </v-card>
        <v-card
            elevation="5"
            class="mx-auto"
            width="fit-content"
        >
          <template v-slot:title>
          <span class="cardTitle">
            <img src="/public/icons/card-image-4.png" class="cardIcon"/>
            <span class="font-weight-black">Наши преимущества</span>
          </span>
          </template>

          <div class="cardText">
            ✔️ Работаем в соответствии с актуальными нормативными требованиями.<br/>
            ✔️ Предлагаем только проверенные и надежные цифровые решения.<br/>
            ✔️ Помогаем организациям снижать затраты и оптимизировать энергопотребление.<br/>
          </div>
        </v-card>
        <v-card
            elevation="5"
            class="mx-auto"
            width="fit-content"
        >
          <template v-slot:title>
          <span class="cardTitle">
            <img src="/public/icons/card-image-3.png" class="cardIcon"/>
            <span class="font-weight-black">Что мы делаем?</span>
          </span>
          </template>

          <div class="cardText">
            Мы занимаемся разработкой и внедрением цифровых решений в области энергосбережения и повышения
            энергоэффективности. Одним из ключевых направлений нашей работы является цифровизация системы энергетических
            паспортов, что позволяет:<br/>
            1) Повысить прозрачность учета энергоресурсов.<br/>
            2) Упростить контроль за потреблением энергии.<br/>
            3) Обеспечить эффективное планирование энергосбережения.
          </div>
        </v-card>
        <v-card
            elevation="5"
            class="mx-auto"
            width="fit-content"
        >
          <template v-slot:title>
          <span class="cardTitle">
            <img src="/public/icons/card-image-2.png" class="cardIcon"/>
            <span class="font-weight-black">Почему это важно?</span>
          </span>
          </template>

          <div class="cardText">
            С принятием Указа Президента РФ №309 от 7 мая 2024 года цифровизация энергетики стала приоритетным
            направлением развития страны. В 2024 году интерес к оформлению энергетических паспортов значительно вырос —
            на
            20% по сравнению с 2023 годом. Это говорит о возрастающей роли энергоэффективности и усилении
            государственного
            контроля в данной сфере.
          </div>
        </v-card>
      </div>
    </div>
  </div>
</template>

<style scoped>
.mainImg { display: flex; flex-direction: column; justify-content: center; min-height: 330px; width: 100%; padding: 56px 0; background: linear-gradient(90deg, rgba(17, 55, 78, .86), rgba(17, 55, 78, .45)), url('~/assets/img/wide-angle-shot-many-electric-posts-dry-landscape-cloudy-sky.jpg') right bottom / cover; }
.mainContainer, .buttonsContainer, .mainBody .mainContainer { width: 100%; max-width: 1240px; margin: 0 auto; padding: 0 24px; }
.mainLabel { width: 100%; padding: 0; color: #fff; font-size: clamp(30px, 4vw, 44px); font-weight: 700; letter-spacing: -.02em; }
.buttonsContainer { display: flex; gap: 12px; }
.mainBtn { margin-top: 18px; padding: 0 20px; border-radius: 8px; font-weight: 600; letter-spacing: 0; text-transform: none; }
.mainBody { flex-grow: 1; width: 100%; background: #f4f7f7; }
.mainGrid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; padding: 40px 0 56px; }
.mainGrid :deep(.v-card) { width: 100% !important; overflow: hidden; border: 1px solid #e1e9eb; border-radius: 14px; box-shadow: 0 8px 24px rgba(31, 63, 79, .07) !important; }
.mainGrid :deep(.v-card-item) { padding: 20px 22px 4px; }
.cardIcon { width: 42px; }
.cardTitle { display: flex; align-items: center; gap: 10px; min-height: 42px; width: 100%; font-size: 19px; }
.cardText { padding: 16px 22px 24px; color: #52636c; font-size: 15px; line-height: 1.6; text-align: start; }
@media (max-width: 720px) { .mainImg { min-height: 290px; padding: 42px 0; } .mainGrid { grid-template-columns: 1fr; padding: 28px 0 40px; } .buttonsContainer { flex-wrap: wrap; } }
@media (max-width: 520px) { .mainContainer, .buttonsContainer, .mainBody .mainContainer { padding-right: 16px; padding-left: 16px; } .mainBtn { width: 100%; } }
</style>
