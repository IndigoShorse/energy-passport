from django.contrib import admin
from .models import EnergyPassportDetail


@admin.register(EnergyPassportDetail)
class EnergyPassportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_organization',
        'registration_number',
        'date_compilation',
        'selfregulating_organization',
        'inn'
    )  # Основные поля в таблице

    search_fields = (
        'name_organization',
        'registration_number',
        'inn',
        'ogrn',
        'full_name'
    )  # Поля по которым можно искать

    list_filter = (
        'selfregulating_organization',
        'date_compilation'
    )  # Фильтры

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'name_organization',
                'organization_legal_form',
                'location',
                'mailing_address',
                'full_name',
                'share_state_ownership'
            )
        }),
        ('Реквизиты', {
            'fields': (
                'ogrn',
                'inn',
                'kpp',
                'bank_details_inn',
                'okved_code'
            )
        }),
        ('Информация о паспорте', {
            'fields': (
                'selfregulating_organization',
                'registration_number',
                'registration_number_date',
                'organization_conducted_survey',
                'date_compilation'
            )
        }),
        ('Подписи', {
            'fields': (
                'signature_person_conducted',
                'customers_signature',
                'sro_signature',
                'full_name_responsible_technical',
                'full_name_responsible_energy'
            )
        }),
        ('Экономические показатели', {
            'fields': [
                'reporting_year',
                'main_product_nomenclature',
                'main_product_code',
                'additional_product_nomenclature',
                'additional_product_code',
                'total_production_monetary',
                'main_product_monetary',
                'additional_product_monetary',
                'total_production_physical',
                'main_product_physical',
                'additional_product_physical',
                'total_energy_monetary',
                'main_product_energy_monetary',
                'additional_product_energy_monetary',
                'total_energy_physical',
                'main_product_energy_physical',
                'additional_product_energy_physical',
                'water_monetary',
                'water_main_product_monetary',
                'water_physical',
                'water_main_product_physical',
                'energy_intensity_main_product',
                'energy_intensity_additional_product',
                'energy_and_water_payment_share',
                'total_maximum_power',
                'average_annual_declared_power',
                'average_employee_headcount',
            ]
        }),
    )