import * as yup from "yup";
import {useField} from "vee-validate";

export interface passportDetail {
    // Поля первого шага
    selfregulating_organization: string;
    registration_number_date: string;
    organization_conducted_survey: string;
    registration_number: string;
    signature_person_conducted: string;
    customers_signature: string;
    sro_signature: string;
    date_compilation: string;
    name_organization: string;
    organization_legal_form: string;
    mailing_address: string;
    location: string;
    full_name: string;
    share_state_ownership: number;
    ogrn: number;
    inn: number;
    kpp: number;
    bank_details_inn: number;
    okved_code: string;  // Изменил на string, так как может содержать точки
    full_name_responsible_technical: string;  // Исправил тип
    full_name_responsible_energy: string;     // Исправил тип

    // Поля второго шага
    reporting_year: number;
    main_product_nomenclature: string;
    main_product_code: string[]; // Массив из 5 элементов
    additional_product_nomenclature: string[];
    additional_product_code: string[];
    total_production_monetary: number[];
    main_product_monetary: number[];
    additional_product_monetary: number[];
    total_production_physical: number[];
    main_product_physical: number[];
    additional_product_physical: number[];
    total_energy_monetary: number[];
    main_product_energy_monetary: number[];
    additional_product_energy_monetary: number[];
    total_energy_physical: number[];
    main_product_energy_physical: number[];
    additional_product_energy_physical: number[];
    water_monetary: number[];
    water_main_product_monetary: number[];
    water_physical: number[];
    water_main_product_physical: number[];
    energy_intensity_main_product: number[];
    energy_intensity_additional_product: number[];
    energy_and_water_payment_share: number[];
    total_maximum_power: number[];
    average_annual_declared_power: number[];
    average_employee_headcount: number[];
    // Поля третьего джага-джага
    electricity_metered_points_count: number;
    heat_metered_points_count: number;
    cold_water_metered_points_count: number;
    hot_water_metered_points_count: number;
    electricity_from_external_source: number;
    heat_from_external_source: number;
    cold_water_from_external_source: number;
    hot_water_from_external_source: number;
    total_electricity_metering_nodes: number;
    total_heat_metering_nodes: number;
    total_cold_water_metering_nodes: number;
    total_hot_water_metering_nodes: number;
}

export interface passportListItem extends passportDetail {
    id: string;
}