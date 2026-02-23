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

.mainGrid {
  margin-top: 30px;
  display: grid;
  gap: 10px;
  grid-template-columns: repeat(2, 1fr);
}

.cardIcon {
  width: 50px;
  left: 0;
}

.cardTitle {
  height: 50px;
  position: relative;
  display: flex;
  font-size: 20px;
  align-items: center;
  gap: 5px;
  width: 100%;
  justify-content: start;
}

.cardText {
  text-align: start;
  font-size: 15px;
  padding: 20px;
}

.mainBody {
  width: 100%;
  background: #eee;
  flex-shrink: 0;
  flex-grow: 1;
}

.mainBody .mainContainer {
  width: 1280px;
  margin: 0 auto;
  padding: 0 30px;
}

.buttonsContainer {
  width: 1280px;
  margin: 0 auto;
  padding-left: 100px;
  display: flex;
  flex-direction: row;
  gap: 10px;
}

.mainImg {
  height: 300px;
  width: 100%;
  margin: 0 auto;
  padding: 40px 0 60px;
  background-size: cover;
  background-position: right bottom;
  object-fit: contain;
  object-position: center;
  background-image: url(assets/img/wide-angle-shot-many-electric-posts-dry-landscape-cloudy-sky.jpg);

  display: flex;
  flex-direction: column;
  justify-content: center;
}

.mainContainer {
  width: 1280px;
  gap: 10px;
  padding-left: 100px;
  margin: 0 auto;
}

.mainLabel {
  backdrop-filter: invert(30%);
  padding: 20px;
  width: 100%;
  color: #fff;
  font-size: 30px;
  font-weight: 600;
}

.mainBtn {
  width: fit-content;
  margin-top: 10px;
}
</style>