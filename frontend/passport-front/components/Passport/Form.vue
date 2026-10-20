<script setup lang="ts">
import {ref} from 'vue';
import {useForm, useField} from 'vee-validate';
import * as yup from 'yup';
import type {passportDetail} from "~/models/types/passportTypes";

const max_step = 5;
const step = ref<number>(1);
const pending = ref<boolean>(false);
const submitted = ref<boolean>(false);

// Схема валидации для первого шага
const validationSchemas = [
  yup.object({
    selfregulating_organization: yup.string().required('Обязательное поле'),
    registration_number_date: yup.string().required('Обязательное поле'),
    organization_conducted_survey: yup.string().required('Обязательное поле'),
    registration_number: yup.string().required('Обязательное поле'),
    signature_person_conducted: yup.string().required('Обязательное поле'),
    customers_signature: yup.string().required('Обязательное поле'),
    sro_signature: yup.string().required('Обязательное поле'),
    date_compilation: yup.string().required('Обязательное поле'),
    name_organization: yup.string().required('Обязательное поле'),
    organization_legal_form: yup.string().required('Обязательное поле'),
    mailing_address: yup.number().required('Обязательное поле'),
    location: yup.string().required('Обязательное поле'),
    full_name: yup.string().required('Обязательное поле'),
    share_state_ownership: yup.number().required('Обязательное поле'),
    ogrn: yup.number().required('Обязательное поле'),
    inn: yup.number().required('Обязательное поле'),
    kpp: yup.number().required('Обязательное поле'),
    bank_details_inn: yup.number().required('Обязательное поле'),
    okved_code: yup.string().required('Обязательное поле'),
    full_name_responsible_technical: yup.string().required('Обязательное поле'),
    full_name_responsible_energy: yup.string().required('Обязательное поле'),
  }),
  // Поля для второго шага
  yup.object({
    reporting_year: yup.number().required('Обязательное поле'),
    main_product_nomenclature: yup.string().required('Обязательное поле'),
    main_product_code: yup.array().of(yup.string().required('Обязательное поле')).length(5).required('Обязательное поле'),
    additional_product_nomenclature: yup.array().of(yup.string().required('Обязательное поле')).length(5).required('Обязательное поле'),
    additional_product_code: yup.array().of(yup.string().required('Обязательное поле')).length(5).required('Обязательное поле'),
    main_product_monetary: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    additional_product_monetary: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    main_product_physical: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    additional_product_physical: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    main_product_energy_monetary: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    additional_product_energy_monetary: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    main_product_energy_physical: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    additional_product_energy_physical: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    water_monetary: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    water_main_product_monetary: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    water_physical: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    water_main_product_physical: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    energy_intensity_main_product: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    energy_intensity_additional_product: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    energy_and_water_payment_share: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    total_maximum_power: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    average_annual_declared_power: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    average_employee_headcount: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
  }),
  // Шаг 3 - Приложение №3
  yup.object({
    electricity_metered_points_count: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    heat_metered_points_count: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    cold_water_metered_points_count: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    hot_water_metered_points_count: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    electricity_from_external_source: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    heat_from_external_source: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    cold_water_from_external_source: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    hot_water_from_external_source: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    total_electricity_metering_nodes: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    total_heat_metering_nodes: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    total_cold_water_metering_nodes: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
    total_hot_water_metering_nodes: yup.number()
        .required('Обязательное поле')
        .min(0, 'Не может быть отрицательным'),
  }),

  // Шаг №4, приложения 4-6
  yup.object({
    // Приложение №4
    reporting_year: yup.number().required('Обязательное поле'),
    total_electricity_consumed: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    electricity_measured_by_meter: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    total_heat_consumed: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    heat_measured_by_meters: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    total_water_consumed: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    water_measured_by_meters: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    // Приложение №5
    external_source: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    own_needs_consumption: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    actual_reported_losses: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    total_technological_losses: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    metering_tolerance_losses: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    irrational_losses: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    // Приложение №6
    hot_external_source: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    heating_and_ventilation: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    hot_water_supply: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    irrational_tech_losses_hot_water: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
  }),
  // Шаг №5, приложения 11, 13
  yup.object({
    // Приложенеие №11
    luminaires_below_35_lm_per_watt: yup.number().required('Обязательное поле'),
    luminaires_from_35_to_100_lm_per_watt: yup.number().required('Обязательное поле'),
    luminaires_above_100_lm_per_watt: yup.number().required('Обязательное поле'),
    total_installed_lighting_power: yup.number().required('Обязательное поле'),
    total_lighting_energy_consumption: yup.array().of(yup.number().required('Обязательное поле')).length(5).required('Обязательное поле'),
    // Приложение №13
    building_name: yup.string().required('Обязательное поле'),
    year_of_commissioning: yup.number().required('Обязательное поле'),
    wall_brief_description: yup.string().required('Обязательное поле'),
    window_brief_description: yup.string().required('Обязательное поле'),
    roof_brief_description: yup.string().required('Обязательное поле'),
    total_building_area: yup.number().required('Обязательное поле'),
    heated_building_area: yup.number().required('Обязательное поле'),
    heated_building_volume: yup.number().required('Обязательное поле'),
    building_wear: yup.number().required('Обязательное поле'),
    actual_heat_specific_characteristic: yup.number().required('Обязательное поле'),
    calculated_normative_heat_specific_characteristic: yup.number().required('Обязательное поле'),
    total_specific_annual_heat_consumption: yup.number().required('Обязательное поле'),
  })
];

const {handleSubmit, errors, validate: validateStep, setErrors: setStepErrors} = useForm({
  validationSchema: computed(() => validationSchemas[step.value - 1])
});

// Поля первого шага
const {value: selfregulating_organization} = useField('selfregulating_organization');
const {value: registration_number_date} = useField('registration_number_date');
const {value: organization_conducted_survey} = useField('organization_conducted_survey');
const {value: registration_number} = useField('registration_number');
const {value: signature_person_conducted} = useField('signature_person_conducted');
const {value: customers_signature} = useField('customers_signature');
const {value: sro_signature} = useField('sro_signature');
const {value: date_compilation} = useField('date_compilation');
const {value: name_organization} = useField('name_organization');
const {value: organization_legal_form} = useField('organization_legal_form');
const {value: mailing_address} = useField('mailing_address');
const {value: location} = useField('location');
const {value: full_name} = useField('full_name');
const {value: share_state_ownership} = useField('share_state_ownership');
const {value: ogrn} = useField('ogrn');
const {value: inn} = useField('inn');
const {value: kpp} = useField('kpp');
const {value: bank_details_inn} = useField('bank_details_inn');
const {value: okved_code} = useField('okved_code');
const {value: full_name_responsible_technical} = useField('full_name_responsible_technical');
const {value: full_name_responsible_energy} = useField('full_name_responsible_energy');

// Поля второго шага
const {value: reporting_year} = useField('reporting_year', [], {initialValue: new Date().getFullYear()});
const {value: main_product_nomenclature} = useField('main_product_nomenclature');
const {value: main_product_code} = useField('main_product_code', [], {
  initialValue: Array(5).fill('-')
});
const {value: additional_product_nomenclature} = useField('additional_product_nomenclature', [], {
  initialValue: Array(5).fill('-')
});
const {value: additional_product_code} = useField('additional_product_code', [], {
  initialValue: Array(5).fill('-')
});
const {value: main_product_monetary} = useField('main_product_monetary', [], {
  initialValue: Array(5).fill(0)
});
const {value: additional_product_monetary} = useField('additional_product_monetary', [], {
  initialValue: Array(5).fill(0)
});
const {value: main_product_physical} = useField('main_product_physical', [], {
  initialValue: Array(5).fill(0)
});
const {value: additional_product_physical} = useField('additional_product_physical', [], {
  initialValue: Array(5).fill(0)
});
const {value: main_product_energy_monetary} = useField('main_product_energy_monetary', [], {
  initialValue: Array(5).fill(0)
});
const {value: additional_product_energy_monetary} = useField('additional_product_energy_monetary', [], {
  initialValue: Array(5).fill(0)
});
const {value: main_product_energy_physical} = useField('main_product_energy_physical', [], {
  initialValue: Array(5).fill(0)
});
const {value: additional_product_energy_physical} = useField('additional_product_energy_physical', [], {
  initialValue: Array(5).fill(0)
});
const {value: water_monetary} = useField('water_monetary', [], {
  initialValue: Array(5).fill(0)
});
const {value: water_main_product_monetary} = useField('water_main_product_monetary', [], {
  initialValue: Array(5).fill(0)
});
const {value: water_physical} = useField('water_physical', [], {
  initialValue: Array(5).fill(0)
});
const {value: water_main_product_physical} = useField('water_main_product_physical', [], {
  initialValue: Array(5).fill(0)
});
const {value: energy_intensity_main_product} = useField('energy_intensity_main_product', [], {
  initialValue: Array(5).fill(0)
});
const {value: energy_intensity_additional_product} = useField('energy_intensity_additional_product', [], {
  initialValue: Array(5).fill(0)
});
const {value: energy_and_water_payment_share} = useField('energy_and_water_payment_share', [], {
  initialValue: Array(5).fill(0)
});
const {value: total_maximum_power} = useField('total_maximum_power', [], {
  initialValue: Array(5).fill(0)
});
const {value: average_annual_declared_power} = useField('average_annual_declared_power', [], {
  initialValue: Array(5).fill(0)
});
const {value: average_employee_headcount} = useField('average_employee_headcount', [], {
  initialValue: Array(5).fill(0)
});

// Поля третьего шага
const {value: electricity_metered_points_count} = useField('electricity_metered_points_count', [], {initialValue: 0});
const {value: heat_metered_points_count} = useField('heat_metered_points_count', [], {initialValue: 0});
const {value: cold_water_metered_points_count} = useField('cold_water_metered_points_count', [], {initialValue: 0});
const {value: hot_water_metered_points_count} = useField('hot_water_metered_points_count', [], {initialValue: 0});
const {value: electricity_from_external_source} = useField('electricity_from_external_source', [], {initialValue: 0});
const {value: heat_from_external_source} = useField('heat_from_external_source', [], {initialValue: 0});
const {value: cold_water_from_external_source} = useField('cold_water_from_external_source', [], {initialValue: 0});
const {value: hot_water_from_external_source} = useField('hot_water_from_external_source', [], {initialValue: 0});
const {value: total_electricity_metering_nodes} = useField('total_electricity_metering_nodes', [], {initialValue: 0});
const {value: total_heat_metering_nodes} = useField('total_heat_metering_nodes', [], {initialValue: 0});
const {value: total_cold_water_metering_nodes} = useField('total_cold_water_metering_nodes', [], {initialValue: 0});
const {value: total_hot_water_metering_nodes} = useField('total_hot_water_metering_nodes', [], {initialValue: 0});

// Поля четвертого шага
const {value: total_electricity_consumed} = useField('total_electricity_consumed', [], {
  initialValue: Array(5).fill(0)
});
const {value: electricity_measured_by_meter} = useField('electricity_measured_by_meter', [], {
  initialValue: Array(5).fill(0)
});
const {value: total_heat_consumed} = useField('total_heat_consumed', [], {
  initialValue: Array(5).fill(0)
});
const {value: heat_measured_by_meters} = useField('heat_measured_by_meters', [], {
  initialValue: Array(5).fill(0)
});
const {value: total_water_consumed} = useField('total_water_consumed', [], {
  initialValue: Array(5).fill(0)
});
const {value: water_measured_by_meters} = useField('water_measured_by_meters', [], {
  initialValue: Array(5).fill(0)
});
// Приложение №5
const {value: external_source} = useField('external_source', [], {
  initialValue: Array(5).fill(0)
});
const {value: own_needs_consumption} = useField('own_needs_consumption', [], {
  initialValue: Array(5).fill(0)
});
const {value: actual_reported_losses} = useField('actual_reported_losses', [], {
  initialValue: Array(5).fill(0)
});
const {value: total_technological_losses} = useField('total_technological_losses', [], {
  initialValue: Array(5).fill(0)
});
const {value: metering_tolerance_losses} = useField('metering_tolerance_losses', [], {
  initialValue: Array(5).fill(0)
});
const {value: irrational_losses} = useField('irrational_losses', [], {
  initialValue: Array(5).fill(0)
});
// Приложение №6
const {value: hot_external_source} = useField('hot_external_source', [], {
  initialValue: Array(5).fill(0)
});
const {value: heating_and_ventilation} = useField('heating_and_ventilation', [], {
  initialValue: Array(5).fill(0)
});
const {value: hot_water_supply} = useField('hot_water_supply', [], {
  initialValue: Array(5).fill(0)
});
const {value: irrational_tech_losses_hot_water} = useField('irrational_tech_losses_hot_water', [], {
  initialValue: Array(5).fill(0)
});
// Поля пятого шага
// Приложение №11
const {value: luminaires_below_35_lm_per_watt} = useField('luminaires_below_35_lm_per_watt', [], {initialValue: 0});
const {value: luminaires_from_35_to_100_lm_per_watt} = useField('luminaires_from_35_to_100_lm_per_watt', [], {initialValue: 0});
const {value: luminaires_above_100_lm_per_watt} = useField('luminaires_above_100_lm_per_watt', [], {initialValue: 0});
const {value: total_installed_lighting_power} = useField('total_installed_lighting_power', [], {initialValue: 0});
const {value: total_lighting_energy_consumption} = useField('total_lighting_energy_consumption', [], {
  initialValue: Array(5).fill(0)
});

// Приложение №13
const {value: building_name} = useField('building_name');
const {value: year_of_commissioning} = useField('year_of_commissioning', [], {initialValue: 0});
const {value: wall_brief_description} = useField('wall_brief_description');
const {value: window_brief_description} = useField('window_brief_description');
const {value: roof_brief_description} = useField('roof_brief_description');
const {value: total_building_area} = useField('total_building_area', [], {initialValue: 0});
const {value: heated_building_area} = useField('heated_building_area', [], {initialValue: 0});
const {value: heated_building_volume} = useField('heated_building_volume', [], {initialValue: 0});
const {value: building_wear} = useField('building_wear', [], {initialValue: 0});
const {value: actual_heat_specific_characteristic} = useField('actual_heat_specific_characteristic', [], {initialValue: 0});
const {value: calculated_normative_heat_specific_characteristic} = useField('calculated_normative_heat_specific_characteristic', [], {initialValue: 0});
const {value: total_specific_annual_heat_consumption} = useField('total_specific_annual_heat_consumption', [], {initialValue: 0});

const results = ref<Array<Record<string, any>>>([]);

const onSubmit = handleSubmit(async (values) => {
  // Сохраняем данные текущего шага
  if (results.value.length <= step.value - 1) {
    // Новый шаг - добавляем в массив
    results.value.push({...values});
  } else {
    // Существующий шаг - обновляем данные
    results.value[step.value - 1] = {...values};
  }

  // Если не последний шаг - переходим дальше
  if (step.value < max_step) {
    await goToStep(step.value + 1);
    setTimeout(() => {
      setStepErrors({}); // Очищаем ошибки
    }, 10);
    return;
  }
  pending.value = true;
  // Если последний шаг - объединяем и отправляем
  try {
    const combinedData = results.value.reduce((acc, stepData) => ({
      ...acc,
      ...stepData
    }), {} as passportDetail);

    // Функция для расчета среднего и расширения массива
    const expandArrayWithAverages = (arr: number[], targetLength: number): number[] => {
      if (arr.length >= targetLength) return arr.slice(0, targetLength);

      const newArr = [...arr];
      while (newArr.length < targetLength) {
        const currentSum = newArr.reduce((sum, val) => sum + val, 0);
        const currentAvg = currentSum / newArr.length;
        newArr.push(currentAvg);
      }
      return newArr;
    };

    combinedData.total_production_monetary = combinedData.main_product_monetary.map(
        (val: number, index: number) => val + (combinedData.additional_product_monetary?.[index] || 0)
    );
    combinedData.total_production_physical = combinedData.main_product_physical.map(
        (val: number, index: number) => val + (combinedData.additional_product_physical?.[index] || 0)
    );
    combinedData.total_energy_monetary = combinedData.main_product_energy_monetary.map(
        (val: number, index: number) => val + (combinedData.additional_product_energy_monetary?.[index] || 0)
    );
    combinedData.total_energy_physical = combinedData.main_product_energy_physical.map(
        (val: number, index: number) => val + (combinedData.additional_product_energy_physical?.[index] || 0)
    );

    // Обрабатываем массивы Приложения №5
    combinedData.external_source = expandArrayWithAverages(combinedData.external_source || [], 10);
    combinedData.own_needs_consumption = expandArrayWithAverages(combinedData.own_needs_consumption || [], 10);
    combinedData.actual_reported_losses = expandArrayWithAverages(combinedData.actual_reported_losses || [], 10);
    combinedData.total_technological_losses = expandArrayWithAverages(combinedData.total_technological_losses || [], 10);
    combinedData.metering_tolerance_losses = expandArrayWithAverages(combinedData.metering_tolerance_losses || [], 10);
    combinedData.irrational_losses = expandArrayWithAverages(combinedData.irrational_losses || [], 10);

    // Массивы приложения №6
    combinedData.hot_external_source = expandArrayWithAverages(combinedData.external_source || [], 10);
    combinedData.heating_and_ventilation = expandArrayWithAverages(combinedData.own_needs_consumption || [], 10);
    combinedData.hot_water_supply = expandArrayWithAverages(combinedData.actual_reported_losses || [], 10);
    combinedData.irrational_tech_losses_hot_water = expandArrayWithAverages(combinedData.total_technological_losses || [], 10);

    const response = await PassportData().post_passport_data(combinedData as passportDetail);
    pending.value = false;
    submitted.value = true;

    // Переход на следующий шаг если нужно
    if (step.value < max_step) {
      step.value += 1;
    }
  } catch (error) {
    console.error('Ошибка при отправке данных:', error);
  }
});

const nextStep = () => {
  if (step.value < max_step) {
    step.value += 1;
  }
};
const prevStep = () => {
  if (step.value > 1) {
    step.value -= 1;
  }
};
const goToStep = async (newStep: number) => {
  const {valid} = await validateStep();

  if (valid || newStep < step.value) {
    step.value = newStep;
  }
};
</script>

<template>
  <div class="container">
    <v-alert v-if="submitted" class="successAlert" type="success" variant="tonal" closable @click:close="submitted = false">
      Паспорт сохранён в демонстрационном режиме. Он уже появился в таблице паспортов.
    </v-alert>
    <v-stepper v-model="step"
               :items="['Основная информация', 'Приложение №2', 'Приложение №3', 'Приложения №4, №5, №6', 'Приложения №11, №13']">
      <!-- Шаг 1 -->
      <template v-slot:item.1>
        <v-card class="stepCard" color="#fff" max-width="1200px" elevation="0">
          <v-card-title>
            <div class="stepLabel">Основная информация</div>
          </v-card-title>
          <v-card-text>
            <v-form class="form-grid" @submit.prevent="onSubmit">
              <div class="form-section-title">
                <div><strong>Сведения об обследовании</strong><small>Данные исполнителя и документа</small></div>
              </div>
              <v-text-field
                  v-model="selfregulating_organization"
                  label="Саморегулируемая организация"
                  :error-messages="errors.selfregulating_organization"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="registration_number_date"
                  label="Регистрационный номер и дата"
                  :error-messages="errors.registration_number_date"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="organization_conducted_survey"
                  label="Организация, проводившая обследование"
                  :error-messages="errors.organization_conducted_survey"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="registration_number"
                  label="Регистрационный номер"
                  :error-messages="errors.registration_number"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="signature_person_conducted"
                  label="Подпись лица, проводившего обследование"
                  :error-messages="errors.signature_person_conducted"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="customers_signature"
                  label="Подпись заказчика"
                  :error-messages="errors.customers_signature"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="sro_signature"
                  label="Подпись представителя СРО"
                  :error-messages="errors.sro_signature"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="date_compilation"
                  label="Дата составления"
                  type="date"
                  :error-messages="errors.date_compilation"
                  required
              ></v-text-field>

              <div class="form-section-title">
                <div><strong>Сведения об организации</strong><small>Наименование, адрес и форма собственности</small></div>
              </div>
              <v-text-field
                  v-model="name_organization"
                  label="Наименование организации"
                  :error-messages="errors.name_organization"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="organization_legal_form"
                  label="Организационно-правовая форма"
                  :error-messages="errors.organization_legal_form"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="mailing_address"
                  label="Почтовый адрес"
                  type="number"
                  :error-messages="errors.mailing_address"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="location"
                  label="Местонахождение"
                  :error-messages="errors.location"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="full_name"
                  label="Полное наименование"
                  :error-messages="errors.full_name"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="share_state_ownership"
                  label="Доля государственной собственности"
                  type="number"
                  :error-messages="errors.share_state_ownership"
                  required
              ></v-text-field>

              <div class="form-section-title">
                <div><strong>Реквизиты и классификаторы</strong><small>Регистрационные данные организации</small></div>
              </div>
              <v-text-field
                  v-model="ogrn"
                  label="ОГРН"
                  :error-messages="errors.ogrn"
                  required
                  @input="ogrn = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>

              <v-text-field
                  v-model="inn"
                  label="ИНН"
                  :error-messages="errors.inn"
                  required
                  @input="inn = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>

              <v-text-field
                  v-model="kpp"
                  label="КПП"
                  :error-messages="errors.kpp"
                  required
                  @input="kpp = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>

              <v-text-field
                  v-model="bank_details_inn"
                  label="ИНН банковских реквизитов"
                  :error-messages="errors.bank_details_inn"
                  required
                  @input="bank_details_inn = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>

              <v-text-field
                  v-model="okved_code"
                  label="Код ОКВЭД"
                  :error-messages="errors.okved_code"
                  required
              ></v-text-field>

              <div class="form-section-title">
                <div><strong>Ответственные лица</strong><small>Контакты по технической и энергетической части</small></div>
              </div>
              <v-text-field
                  v-model="full_name_responsible_technical"
                  label="ФИО ответственного за техническую политику"
                  :error-messages="errors.full_name_responsible_technical"
                  required
              ></v-text-field>

              <v-text-field
                  v-model="full_name_responsible_energy"
                  label="ФИО ответственного за энергетику"
                  :error-messages="errors.full_name_responsible_energy"
                  required
              ></v-text-field>
            </v-form>
          </v-card-text>

          <v-card-actions class="buttonsContainer">
            <div class="action-placeholder"></div>
            <v-btn class="mainBtn" type="button" color="#275c8c" size="large" variant="elevated" @click="onSubmit">
              Далее
            </v-btn>
          </v-card-actions>
        </v-card>

      </template>

      <!-- Шаг 2 -->
      <template v-slot:item.2>
        <v-card class="stepCard" color="#fff" max-width="1200px" elevation="0">
          <v-card-title>
            <div class="stepLabel">Приложение №2</div>
          </v-card-title>
          <v-card-text>
            <v-form class="form-grid" @submit.prevent="onSubmit">
              <div class="form-section-title">
                <div><strong>Производственная информация</strong><small>Отчётный год и сведения о выпускаемой продукции</small></div>
              </div>
              <!-- Поле для ввода отчетного года -->
              <v-text-field
                  v-model="reporting_year"
                  readonly
                  label="Отчетный год"
                  min="2020"
                  max="2099"
                  type="number"
                  :error-messages="errors.reporting_year"
              ></v-text-field>

              <!-- Основная продукция -->
              <v-text-field
                  v-model="main_product_nomenclature"
                  label="Номенклатура основной продукции"
                  :error-messages="errors.main_product_nomenclature"
              ></v-text-field>

              <!-- Компонент для ввода массива кодов основной продукции -->
              <div class="array-input-group">
                <h4>Код основной продукции</h4>
                <div v-for="(item, index) in main_product_code" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="main_product_code[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.main_product_code"
                  ></v-text-field>
                </div>
              </div>

              <!-- Дополнительная продукция -->
              <div class="array-input-group">
                <h4>Номенклатура дополнительной продукции</h4>
                <div v-for="(item, index) in additional_product_nomenclature" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="additional_product_nomenclature[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.additional_product_nomenclature"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Код дополнительной продукции</h4>
                <div v-for="(item, index) in additional_product_code" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="additional_product_code[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.additional_product_code"
                  ></v-text-field>
                </div>
              </div>

              <!-- Остальные поля с массивами (аналогично) -->
              <div class="array-input-group">
                <h4>Объем основной продукции (денежный), руб.</h4>
                <div v-for="(item, index) in main_product_monetary" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="main_product_monetary[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.main_product_monetary"
                      @input="main_product_monetary[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Объем дополнительной продукции (денежный), руб.</h4>
                <div v-for="(item, index) in additional_product_monetary" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="additional_product_monetary[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.additional_product_monetary"
                      @input="additional_product_monetary[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <!-- Физические объемы продукции -->
              <div class="array-input-group">
                <h4>Объем основной продукции (физический)</h4>
                <div v-for="(item, index) in main_product_physical" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="main_product_physical[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.main_product_physical"
                      @input="main_product_physical[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>

              <div class="array-input-group">
                <h4>Объем дополнительной продукции (физический)</h4>
                <div v-for="(item, index) in additional_product_physical" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="additional_product_physical[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.additional_product_physical"
                      @input="additional_product_physical[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>

              <!-- Энергетические показатели -->
              <div class="array-input-group">
                <h4>Энергозатраты на основную продукцию (денежный), руб.</h4>
                <div v-for="(item, index) in main_product_energy_monetary" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="main_product_energy_monetary[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.main_product_energy_monetary"
                      @input="main_product_energy_monetary[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Энергозатраты на дополнительную продукцию (денежный), руб.</h4>
                <div v-for="(item, index) in additional_product_energy_monetary" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="additional_product_energy_monetary[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.additional_product_energy_monetary"
                      @input="additional_product_energy_monetary[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Энергозатраты на основную продукцию в натуральном выражении</h4>
                <div v-for="(item, index) in main_product_energy_physical" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="main_product_energy_physical[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.main_product_energy_physical"
                      @input="main_product_energy_physical[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Энергозатраты на дополнительную продукцию в натуральном выражении</h4>
                <div v-for="(item, index) in additional_product_energy_physical" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="additional_product_energy_physical[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.additional_product_energy_physical"
                      @input="additional_product_energy_physical[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>

              <!-- Водопотребление -->
              <div class="array-input-group">
                <h4>Объем потребленной воды (денежный), руб.</h4>
                <div v-for="(item, index) in water_monetary" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="water_monetary[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.water_monetary"
                      @input="water_monetary[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Объем потребленной воды для основной продукции (денежный), руб.</h4>
                <div v-for="(item, index) in water_main_product_monetary" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="water_main_product_monetary[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.water_main_product_monetary"
                      @input="water_main_product_monetary[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Объем потребленной воды в натуральном выражении</h4>
                <div v-for="(item, index) in water_physical" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="water_physical[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.water_physical"
                      @input="water_physical[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Объем потребленной воды для основной продукции в натуральном выражении</h4>
                <div v-for="(item, index) in water_main_product_physical" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="water_main_product_physical[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.water_main_product_physical"
                      @input="water_main_product_physical[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>

              <!-- Энергоемкость -->
              <div class="array-input-group">
                <h4>Энергоемкость производства основной продукции</h4>
                <div v-for="(item, index) in energy_intensity_main_product" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="energy_intensity_main_product[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.energy_intensity_main_product"
                      @input="energy_intensity_main_product[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Энергоемкость производства дополнительной продукции</h4>
                <div v-for="(item, index) in energy_intensity_additional_product" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="energy_intensity_additional_product[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.energy_intensity_additional_product"
                      @input="energy_intensity_additional_product[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>

              <!-- Остальные показатели -->
              <div class="array-input-group">
                <h4>Доля платы за энергетические ресурсы и воду (%)</h4>
                <div v-for="(item, index) in energy_and_water_payment_share" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="energy_and_water_payment_share[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.energy_and_water_payment_share"
                      @input="energy_and_water_payment_share[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Суммарная максимальная мощность энергопринимающих устройств (тыс. кВт)</h4>
                <div v-for="(item, index) in total_maximum_power" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="total_maximum_power[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.total_maximum_power"
                      @input="total_maximum_power[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Суммарная среднегодовая заявленная мощность энергопринимающих устройств (тыс. кВт)</h4>
                <div v-for="(item, index) in average_annual_declared_power" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="average_annual_declared_power[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.average_annual_declared_power"
                      @input="average_annual_declared_power[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Среднесписочная численность работников</h4>
                <div v-for="(item, index) in average_employee_headcount" :key="index" class="array-input-item">
                  <v-text-field
                      v-model="average_employee_headcount[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      type="number"
                      :error-messages="errors.average_employee_headcount"
                      @input="average_employee_headcount[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
            </v-form>
          </v-card-text>
          <v-card-actions class="buttonsContainer">
            <v-btn class="mainBtn" color="#fff" size="large" variant="elevated" @click="prevStep">
              Назад
            </v-btn>
            <v-btn class="mainBtn" color="#275c8c" size="large" variant="elevated" @click="onSubmit">
              Далее
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
      <!-- Шаг 3 -->
      <template v-slot:item.3>
        <v-card class="stepCard" color="#fff" max-width="1200px" elevation="0">
          <v-card-title>
            <div class="stepLabel">Приложение №3</div>
          </v-card-title>
          <v-card-text>
            <v-form class="form-grid" @submit.prevent="onSubmit">
              <div class="array-input-group">
                <h4>Количество оборудованных узлами (приборами) учета точек приема (поставки), всего</h4>
                <div class="array-input-item">
                  <v-text-field
                      v-model="electricity_metered_points_count"
                      label="Электрической энергии"
                      :error-messages="errors.electricity_metered_points_count"
                      required
                      @input="electricity_metered_points_count = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="heat_metered_points_count"
                      label="Тепловой энергии"
                      :error-messages="errors.heat_metered_points_count"
                      required
                      @input="heat_metered_points_count = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="cold_water_metered_points_count"
                      label="Холодной воды"
                      :error-messages="errors.cold_water_metered_points_count"
                      required
                      @input="cold_water_metered_points_count = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="hot_water_metered_points_count"
                      label="Горячей воды"
                      :error-messages="errors.hot_water_metered_points_count"
                      required
                      @input="hot_water_metered_points_count = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4>Узлы(приборы) измерения полученной от стороннего источника</h4>
                <div class="array-input-item">
                  <v-text-field
                      v-model="electricity_from_external_source"
                      label="Электрической энергии"
                      :error-messages="errors.electricity_from_external_source"
                      required
                      @input="electricity_from_external_source = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="heat_from_external_source"
                      label="Тепловой энергии"
                      :error-messages="errors.heat_from_external_source"
                      required
                      @input="heat_from_external_source = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="cold_water_from_external_source"
                      label="Холодной воды"
                      :error-messages="errors.cold_water_from_external_source"
                      required
                      @input="cold_water_from_external_source = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="hot_water_from_external_source"
                      label="Горячей воды"
                      :error-messages="errors.hot_water_from_external_source"
                      required
                      @input="hot_water_from_external_source = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>

              <div class="array-input-group">
                <h4>Суммарное количество узлов (приборов) учета</h4>
                <div class="array-input-item">
                  <v-text-field
                      v-model="total_electricity_metering_nodes"
                      label="Электрической энергии"
                      :error-messages="errors.total_electricity_metering_nodes"
                      required
                      @input="total_electricity_metering_nodes = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="total_heat_metering_nodes"
                      label="Тепловой энергии"
                      :error-messages="errors.total_heat_metering_nodes"
                      required
                      @input="total_heat_metering_nodes = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="total_cold_water_metering_nodes"
                      label="Холодной воды"
                      :error-messages="errors.total_cold_water_metering_nodes"
                      required
                      @input="total_cold_water_metering_nodes = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
                <div class="array-input-item">
                  <v-text-field
                      v-model="total_hot_water_metering_nodes"
                      label="Горячей воды"
                      :error-messages="errors.total_hot_water_metering_nodes"
                      required
                      @input="total_hot_water_metering_nodes = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>
            </v-form>
          </v-card-text>
          <v-card-actions class="buttonsContainer">
            <v-btn class="mainBtn" color="#fff" size="large" variant="elevated" @click="prevStep">
              Назад
            </v-btn>
            <v-btn class="mainBtn" color="#275c8c" size="large" variant="elevated" @click="onSubmit">
              Далее
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
      <!-- Шаг 4 -->
      <template v-slot:item.4>
        <v-card class="stepCard" color="#fff" max-width="1200px" elevation="0">
          <v-card-title>
            <div class="stepLabel">Приложения №4, №5, №6</div>
          </v-card-title>
          <v-card-text>
            <v-form class="form-grid" @submit.prevent="onSubmit">
              <div class="form-section-title">
                <div><strong>Потребление ресурсов</strong><small>Показатели электроэнергии, тепла и воды за пять лет</small></div>
              </div>
              <!-- Поле для ввода отчетного года -->
              <v-text-field
                  v-model="reporting_year"
                  readonly
                  label="Отчетный год"
                  min="2020"
                  max="2099"
                  type="number"
                  :error-messages="errors.reporting_year"
              ></v-text-field>

              <div class="array-input-group">
                <h4> Потребление электроэнергии, всего </h4>
                <div v-for="(item, index) in total_electricity_consumed" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="total_electricity_consumed[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.total_electricity_consumed"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Потребление электроэнергии, по узлам учета </h4>
                <div v-for="(item, index) in electricity_measured_by_meter" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="electricity_measured_by_meter[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.electricity_measured_by_meter"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Потребление тепловой энергии, всего </h4>
                <div v-for="(item, index) in total_heat_consumed" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="total_heat_consumed[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.total_heat_consumed"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Потребление тепловой энергии, по узлам учета </h4>
                <div v-for="(item, index) in heat_measured_by_meters" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="heat_measured_by_meters[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.heat_measured_by_meters"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Потребление воды, всего </h4>
                <div v-for="(item, index) in total_water_consumed" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="total_water_consumed[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.total_water_consumed"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Потребление воды, по узлам учета </h4>
                <div v-for="(item, index) in water_measured_by_meters" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="water_measured_by_meters[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.water_measured_by_meters"
                  ></v-text-field>
                </div>
              </div>
              <!-- Приложение №5 -->
              <div class="array-input-group">
                <h4> Приход/расход электроэнергии, всего </h4>
                <div v-for="(item, index) in external_source" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="external_source[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.external_source"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Расход электроэнергии на собственные нужды </h4>
                <div v-for="(item, index) in own_needs_consumption" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="own_needs_consumption[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.own_needs_consumption"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Фактические(отчетные) потери электроэнергии </h4>
                <div v-for="(item, index) in actual_reported_losses" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="actual_reported_losses[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.actual_reported_losses"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Технические потери электроэнергии, всего </h4>
                <div v-for="(item, index) in total_technological_losses" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="total_technological_losses[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.total_technological_losses"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Потери электроэнергии, обусловленные допустимыми погрешностями </h4>
                <div v-for="(item, index) in metering_tolerance_losses" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="metering_tolerance_losses[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.metering_tolerance_losses"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Нерациональные потери электроэнергии </h4>
                <div v-for="(item, index) in irrational_losses" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="irrational_losses[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.irrational_losses"
                  ></v-text-field>
                </div>
              </div>
              <!-- Приложение №6 -->
              <div class="array-input-group">
                <h4> Приход/расход тепловой энергии, всего </h4>
                <div v-for="(item, index) in hot_external_source" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="hot_external_source[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.hot_external_source"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Расход тепловой энергии на отопление и вентиляцию </h4>
                <div v-for="(item, index) in heating_and_ventilation" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="heating_and_ventilation[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.heating_and_ventilation"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Расход тепловой энергии на воду </h4>
                <div v-for="(item, index) in hot_water_supply" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="hot_water_supply[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.hot_water_supply"
                  ></v-text-field>
                </div>
              </div>
              <div class="array-input-group">
                <h4> Нерациональные потери в системах отопления, вентиляции, горячего водоснабжения </h4>
                <div v-for="(item, index) in irrational_tech_losses_hot_water" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="irrational_tech_losses_hot_water[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.irrational_tech_losses_hot_water"
                  ></v-text-field>
                </div>
              </div>
            </v-form>
          </v-card-text>
          <v-card-actions class="buttonsContainer">
            <v-btn class="mainBtn" color="#fff" size="large" variant="elevated" @click="prevStep">
              Назад
            </v-btn>
            <v-btn class="mainBtn" color="#275c8c" size="large" variant="elevated" @click="onSubmit">
              Далее
            </v-btn>
          </v-card-actions>
        </v-card>
      </template>
      <!-- Шаг 5 -->
      <template v-slot:item.5>
        <v-card class="stepCard" color="#fff" max-width="1200px" elevation="0">
          <v-card-title>
            <div class="stepLabel">Приложения №11, №13</div>
          </v-card-title>
          <v-card-text>
            <v-form class="form-grid" @submit.prevent="onSubmit">
              <!-- Приложение №11 -->
              <h3 class="app-title">
                Приложение №11 - Показатели
                использования электрической энергии на цели освещения
              </h3>

              <v-text-field
                  v-model="luminaires_below_35_lm_per_watt"
                  label="Количество светильников с эффективностью ниже 35 лм/Вт"
                  type="number"
                  :error-messages="errors.luminaires_below_35_lm_per_watt"
                  required
                  @input="luminaires_below_35_lm_per_watt = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="luminaires_from_35_to_100_lm_per_watt"
                  label="Количество светильников с эффективностью 35-100 лм/Вт"
                  type="number"
                  :error-messages="errors.luminaires_from_35_to_100_lm_per_watt"
                  required
                  @input="luminaires_from_35_to_100_lm_per_watt = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="luminaires_above_100_lm_per_watt"
                  label="Количество светильников с эффективностью выше 100 лм/Вт"
                  type="number"
                  :error-messages="errors.luminaires_above_100_lm_per_watt"
                  required
                  @input="luminaires_above_100_lm_per_watt = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="total_installed_lighting_power"
                  label="Суммарная установленная мощность освещения, кВт"
                  type="number"
                  :error-messages="errors.total_installed_lighting_power"
                  required
                  @input="total_installed_lighting_power = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <div class="array-input-group">
                <h4>Годовое потребление электроэнергии на освещение, кВт·ч</h4>
                <div v-for="(item, index) in total_lighting_energy_consumption" :key="index" class="array-input-item">
                  <v-text-field
                      type="number"
                      v-model="total_lighting_energy_consumption[index]"
                      :label="`За ${reporting_year - (4 - index)} год`"
                      :error-messages="errors.total_lighting_energy_consumption"
                      @input="total_lighting_energy_consumption[index] = $event.target.value.replace(/\D/g, '')"
                  ></v-text-field>
                </div>
              </div>

              <!-- Приложение №13 -->
              <h3 class="app-title">
                Приложение №13 - Краткая характеристика
                объекта (зданий, строений и сооружений)
              </h3>

              <v-text-field
                  v-model="building_name"
                  label="Наименование здания/сооружения"
                  :error-messages="errors.building_name"
                  required
              ></v-text-field>
              <v-text-field
                  v-model="year_of_commissioning"
                  label="Год ввода в эксплуатацию"
                  type="number"
                  :error-messages="errors.year_of_commissioning"
                  required
                  @input="year_of_commissioning = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="wall_brief_description"
                  label="Краткое описание стен (материал, толщина)"
                  :error-messages="errors.wall_brief_description"
                  required
              ></v-text-field>
              <v-text-field
                  v-model="window_brief_description"
                  label="Краткое описание окон (материал, количество камер)"
                  :error-messages="errors.window_brief_description"
                  required
              ></v-text-field>
              <v-text-field
                  v-model="roof_brief_description"
                  label="Краткое описание крыши (материал, утепление)"
                  :error-messages="errors.roof_brief_description"
                  required
              ></v-text-field>
              <v-text-field
                  v-model="total_building_area"
                  label="Общая площадь здания, м²"
                  type="number"
                  :error-messages="errors.total_building_area"
                  required
                  @input="total_building_area = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="heated_building_area"
                  label="Отапливаемая площадь здания, м²"
                  type="number"
                  :error-messages="errors.heated_building_area"
                  required
                  @input="heated_building_area = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="heated_building_volume"
                  label="Отапливаемый объем здания, м³"
                  type="number"
                  :error-messages="errors.heated_building_volume"
                  required
                  @input="heated_building_volume = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="building_wear"
                  label="Износ здания, %"
                  type="number"
                  :error-messages="errors.building_wear"
                  required
                  @input="building_wear = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="actual_heat_specific_characteristic"
                  label="Фактическая удельная тепловая характеристика, Вт/(м³·°С)"
                  type="number"
                  :error-messages="errors.actual_heat_specific_characteristic"
                  required
                  @input="actual_heat_specific_characteristic = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="calculated_normative_heat_specific_characteristic"
                  label="Расчетная нормативная удельная тепловая характеристика, Вт/(м³·°С)"
                  type="number"
                  :error-messages="errors.calculated_normative_heat_specific_characteristic"
                  required
                  @input="calculated_normative_heat_specific_characteristic = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
              <v-text-field
                  v-model="total_specific_annual_heat_consumption"
                  label="Суммарное удельное годовое потребление тепла, кВт·ч/м²"
                  type="number"
                  :error-messages="errors.total_specific_annual_heat_consumption"
                  required
                  @input="total_specific_annual_heat_consumption = $event.target.value.replace(/\D/g, '')"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions class="buttonsContainer" v-if="!pending">
            <v-btn class="mainBtn" color="#fff" size="large" variant="elevated" @click="prevStep">
              Назад
            </v-btn>
            <v-btn class="mainBtn" color="#275c8c" size="large" variant="elevated" @click="onSubmit">
              Создать паспорт
            </v-btn>
          </v-card-actions>
          <v-card-actions v-else class="buttonsIconContainer">
            <Icon name="svg-spinners:bars-scale-fade" size="30" style="color: #275c8c"/>
          </v-card-actions>
        </v-card>
      </template>
      <template v-slot:actions>
      </template>
    </v-stepper>
  </div>
</template>

<style scoped>
.array-input-group {
  margin: 24px 0;
  padding: 20px;
  border: 1px solid #dfe8ea;
  border-radius: 10px;
  background: #f9fbfb;
  display: grid;
  grid-template-columns: repeat(5, minmax(120px, 1fr));
  gap: 0 12px;
}

.array-input-group h4 {
  grid-column: 1 / -1;
  margin-bottom: 18px;
  color: #1f5d83;
  font-size: 15px;
  line-height: 1.35;
}

.array-input-item {
  margin-bottom: 0;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  column-gap: 20px;
}

.form-grid > .form-section-title,
.form-grid > .array-input-group,
.form-grid > .app-title {
  grid-column: 1 / -1;
}

.form-section-title {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 20px 0 4px;
  padding: 14px 16px;
  border-left: 3px solid #4a9a86;
  border-radius: 0 8px 8px 0;
  background: #f1f7f6;
}

.form-section-title strong,
.form-section-title small { display: block; }
.form-section-title strong { color: #24495f; font-size: 15px; }
.form-section-title small { margin-top: 2px; color: #697b84; font-size: 12px; }

.container {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 36px 24px 56px;
}

.successAlert { margin-bottom: 18px; border-radius: 10px; }

.stepCard {
  padding: 8px 40px 24px;
}

.stepCard .stepLabel {
  color: #1f5d83;
  font-size: 22px;
  margin-bottom: 12px;
  text-align: center;
  font-weight: 600;
}

.stepCard .v-input {
  margin-top: 12px;
}

.form-grid > :deep(.v-input) { min-width: 0; }
.array-input-group :deep(.v-input) { margin-top: 0; }

@keyframes fill-step {
  0% {
    transform-origin: left;
    transform: scaleX(0%);
  }
  50% {
    transform-origin: left;
    transform: scaleX(50%);
  }
  100% {
    transform-origin: left;
    transform: scaleX(100%);
  }
}

@keyframes empty-step {
  0% {
    transform-origin: left;
    transform: scaleX(100%);
  }
  50% {
    transform-origin: left;
    transform: scaleX(50%);
  }
  100% {
    transform-origin: left;
    transform: scaleX(0%);
  }
}

.buttonsContainer {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.buttonsIconContainer {
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.mainBtn {
  margin: 10px;
  padding: 10px 30px;
  border-radius: 8px;
  font-weight: 600;
  letter-spacing: 0;
  text-transform: none;
}

/* Стили для stepper */
:deep(.v-stepper-item--selected .v-avatar) {
  background-color: #275c8c !important;
  color: white !important;
}

:deep(.v-stepper-item--selected .v-stepper-item__title) {
  color: #275c8c !important;
  font-weight: bold;
}

/* Для hover эффекта */
:deep(.v-stepper-item--selected:hover .v-avatar) {
  background-color: #3275b2 !important;
}

:deep(.v-stepper) {
  overflow: hidden;
  border: 1px solid #e1e9eb;
  border-radius: 14px;
  box-shadow: 0 8px 24px rgba(31, 63, 79, .07);
}

:deep(.v-stepper-header) { padding: 8px 16px; border-bottom: 1px solid #e5edef; }
:deep(.v-field) { border-radius: 8px; }

@media (max-width: 720px) {
  .container { padding: 24px 16px 40px; }
  .stepCard { padding: 4px 16px 20px; }
  .stepCard .stepLabel { font-size: 19px; }
  :deep(.v-stepper-header) { overflow-x: auto; justify-content: flex-start; }
  :deep(.v-stepper-item) { min-width: max-content; }
  .buttonsContainer { gap: 4px; }
  .mainBtn { flex: 1; margin: 8px 0; }
  .form-grid { grid-template-columns: 1fr; }
  .array-input-group { grid-template-columns: repeat(2, minmax(0, 1fr)); padding: 16px; }
}

@media (max-width: 420px) {
  .array-input-group { grid-template-columns: 1fr; }
}
</style>
