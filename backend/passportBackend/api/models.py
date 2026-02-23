# models.py
import uuid
from django.db import models

class EnergyPassportDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    selfregulating_organization = models.CharField(max_length=255, verbose_name='Саморегулируемая организация')
    registration_number_date = models.CharField(max_length=255, verbose_name='Дата регистрационного номера')
    organization_conducted_survey = models.CharField(max_length=255, verbose_name='Организация, проводившая обследование')
    registration_number = models.CharField(max_length=255, verbose_name='Регистрационный номер')
    signature_person_conducted = models.CharField(max_length=255, verbose_name='Подпись лица, проводившего обследование')
    customers_signature = models.CharField(max_length=255, verbose_name='Подпись заказчика')
    sro_signature = models.CharField(max_length=255, verbose_name='Подпись СРО')
    date_compilation = models.CharField(verbose_name='Дата составления')
    name_organization = models.CharField(max_length=255, verbose_name='Наименование организации')
    organization_legal_form = models.CharField(max_length=255, verbose_name='Организационно-правовая форма')
    mailing_address = models.IntegerField(verbose_name='Почтовый адрес')
    location = models.CharField(max_length=255, verbose_name='Местонахождение')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    share_state_ownership = models.IntegerField(verbose_name='Доля государственной собственности')
    ogrn = models.BigIntegerField(verbose_name='ОГРН')
    inn = models.BigIntegerField(verbose_name='ИНН')
    kpp = models.BigIntegerField(verbose_name='КПП', )
    bank_details_inn = models.BigIntegerField(verbose_name='Банковские реквизиты ИНН')
    okved_code = models.CharField(max_length=12,verbose_name='Код ОКВЭД')
    full_name_responsible_technical = models.CharField(max_length=255, verbose_name='ФИО ответственного за техническое состояние')
    full_name_responsible_energy = models.CharField(max_length=255, verbose_name='ФИО ответственного за энергетику')

    # Новые поля для экономических показателей
    reporting_year = models.IntegerField(verbose_name="Отчетный год")
    main_product_nomenclature = models.CharField(max_length=255, verbose_name="Основная номенклатура продукции")
    main_product_code = models.JSONField(verbose_name="Коды основной продукции")
    additional_product_nomenclature = models.JSONField(verbose_name="Номенклатура дополнительной продукции")
    additional_product_code = models.JSONField(verbose_name="Коды дополнительной продукции")

    total_production_monetary = models.JSONField(verbose_name="Суммарный объем продукции (руб)")
    main_product_monetary = models.JSONField(verbose_name="Объем основной продукции (руб)")
    additional_product_monetary = models.JSONField(verbose_name="Объем дополнительной продукции (руб)")

    total_production_physical = models.JSONField(verbose_name="Суммарный объем продукции (физический)")
    main_product_physical = models.JSONField(verbose_name="Объем основной продукции (физический)")
    additional_product_physical = models.JSONField(verbose_name="Объем дополнительной продукции (физический)")

    total_energy_monetary = models.JSONField(verbose_name="Суммарные энергозатраты на продукцию (руб)")
    main_product_energy_monetary = models.JSONField(verbose_name="Энергозатраты на основную продукцию (руб)")
    additional_product_energy_monetary = models.JSONField(verbose_name="Энергозатраты на доп. продукцию (руб)")

    total_energy_physical = models.JSONField(verbose_name="Энергозатраты на основную продукцию (физический)")
    main_product_energy_physical = models.JSONField(verbose_name="Энергозатраты на основную продукцию (физический)")
    additional_product_energy_physical = models.JSONField(verbose_name="Энергозатраты на доп. продукцию (физический)")

    water_monetary = models.JSONField(verbose_name="Затраты на воду (руб)")
    water_main_product_monetary = models.JSONField(verbose_name="Затраты на воду для основной продукции (руб)")
    water_physical = models.JSONField(verbose_name="Объем водопотребления")
    water_main_product_physical = models.JSONField(verbose_name="Объем водопотребления для основной продукции")

    energy_intensity_main_product = models.JSONField(verbose_name="Энергоемкость основной продукции")
    energy_intensity_additional_product = models.JSONField(verbose_name="Энергоемкость дополнительной продукции")
    energy_and_water_payment_share = models.JSONField(verbose_name="Доля платежей за энергию и воду")

    total_maximum_power = models.JSONField(verbose_name="Суммарная максимальная мощность")
    average_annual_declared_power = models.JSONField(verbose_name="Среднегодовая заявленная мощность")
    average_employee_headcount = models.JSONField(verbose_name="Среднесписочная численность работников")
    electricity_metered_points_count = models.IntegerField(
        verbose_name="Количество узлов учета электроэнергии",
        default=0
    )
    heat_metered_points_count = models.IntegerField(
        verbose_name="Количество узлов учета тепловой энергии",
        default=0
    )
    cold_water_metered_points_count = models.IntegerField(
        verbose_name="Количество узлов учета холодной воды",
        default=0
    )
    hot_water_metered_points_count = models.IntegerField(
        verbose_name="Количество узлов учета горячей воды",
        default=0
    )
    electricity_from_external_source = models.IntegerField(
        verbose_name="Электроэнергия из внешних источников (кВт·ч)",
        default=0
    )
    heat_from_external_source = models.IntegerField(
        verbose_name="Тепловая энергия из внешних источников (Гкал)",
        default=0
    )
    cold_water_from_external_source = models.IntegerField(
        verbose_name="Холодная вода из внешних источников (м³)",
        default=0
    )
    hot_water_from_external_source = models.IntegerField(
        verbose_name="Горячая вода из внешних источников (м³)",
        default=0
    )
    total_electricity_metering_nodes = models.IntegerField(
        verbose_name="Всего узлов учета электроэнергии",
        default=0
    )
    total_heat_metering_nodes = models.IntegerField(
        verbose_name="Всего узлов учета тепловой энергии",
        default=0
    )
    total_cold_water_metering_nodes = models.IntegerField(
        verbose_name="Всего узлов учета холодной воды",
        default=0
    )
    total_hot_water_metering_nodes = models.IntegerField(
        verbose_name="Всего узлов учета горячей воды",
        default=0
    )
    # Приложение №4
    total_electricity_consumed = models.JSONField(verbose_name="Потребление электроэнергии, всего")
    electricity_measured_by_meter = models.JSONField(verbose_name="Потребление электроэнергии, по узлам учета")
    total_heat_consumed = models.JSONField(verbose_name="Потребление тепловой энергии, всего")
    heat_measured_by_meters = models.JSONField(verbose_name="Потребление тепловой энергии, по узлам учета")
    total_water_consumed = models.JSONField(verbose_name="Потребление воды, всего")
    water_measured_by_meters = models.JSONField(verbose_name="Потребление воды, по узлам учета")

    # Приложение №5
    external_source = models.JSONField(verbose_name="Приход/расход электроэнергии, всего")
    own_needs_consumption = models.JSONField(verbose_name="Расход электроэнергии на собственные нужды")
    actual_reported_losses = models.JSONField(verbose_name="Фактические(отчетные) потери электроэнергии")
    total_technological_losses = models.JSONField(verbose_name="Технические потери электроэнергии, всего")
    metering_tolerance_losses = models.JSONField(verbose_name="Потери электроэнергии, обусловленные допустимыми погрешностями")
    irrational_losses = models.JSONField(verbose_name="Нерациональные потери электроэнергии")

    # Приложение №6
    hot_external_source = models.JSONField(verbose_name="Приход/расход тепловой энергии, всего")
    heating_and_ventilation = models.JSONField(verbose_name="Расход тепловой энергии на отопление и вентиляцию")
    hot_water_supply = models.JSONField(verbose_name="Расход тепловой энергии на воду")
    irrational_tech_losses_hot_water = models.JSONField(verbose_name="Нерациональные потери в системах отопления, вентиляции, горячего водоснабжения")

    # Приложение №11 - Осветительные установки
    luminaires_below_35_lm_per_watt = models.IntegerField(
        verbose_name="Количество светильников с эффективностью ниже 35 лм/Вт",
        default=0
    )
    luminaires_from_35_to_100_lm_per_watt = models.IntegerField(
        verbose_name="Количество светильников с эффективностью 35-100 лм/Вт",
        default=0
    )
    luminaires_above_100_lm_per_watt = models.IntegerField(
        verbose_name="Количество светильников с эффективностью выше 100 лм/Вт",
        default=0
    )
    total_installed_lighting_power = models.FloatField(
        verbose_name="Суммарная установленная мощность освещения, кВт",
        default=0
    )
    total_lighting_energy_consumption = models.JSONField(
        verbose_name="Годовое потребление электроэнергии на освещение, кВт·ч",
        default=list
    )

    # Приложение №13 - Здания и сооружения
    building_name = models.CharField(
        max_length=255,
        verbose_name="Наименование здания/сооружения",
        blank=True,
        null=True
    )
    year_of_commissioning = models.IntegerField(
        verbose_name="Год ввода в эксплуатацию",
        null=True,
        blank=True
    )
    wall_brief_description = models.TextField(
        verbose_name="Краткое описание стен (материал, толщина)",
        blank=True,
        null=True
    )
    window_brief_description = models.TextField(
        verbose_name="Краткое описание окон (материал, количество камер)",
        blank=True,
        null=True
    )
    roof_brief_description = models.TextField(
        verbose_name="Краткое описание крыши (материал, утепление)",
        blank=True,
        null=True
    )
    total_building_area = models.FloatField(
        verbose_name="Общая площадь здания, м²",
        null=True,
        blank=True
    )
    heated_building_area = models.FloatField(
        verbose_name="Отапливаемая площадь здания, м²",
        null=True,
        blank=True
    )
    heated_building_volume = models.FloatField(
        verbose_name="Отапливаемый объем здания, м³",
        null=True,
        blank=True
    )
    building_wear = models.FloatField(
        verbose_name="Износ здания, %",
        null=True,
        blank=True
    )
    actual_heat_specific_characteristic = models.FloatField(
        verbose_name="Фактическая удельная тепловая характеристика, Вт/(м³·°С)",
        null=True,
        blank=True
    )
    calculated_normative_heat_specific_characteristic = models.FloatField(
        verbose_name="Расчетная нормативная удельная тепловая характеристика, Вт/(м³·°С)",
        null=True,
        blank=True
    )
    total_specific_annual_heat_consumption = models.FloatField(
        verbose_name="Суммарное удельное годовое потребление тепла, кВт·ч/м²",
        null=True,
        blank=True
    )
    def __str__(self):
        return f"{self.name_organization} ({self.registration_number})"

    class Meta:
        verbose_name = 'Основная информация(паспорт)'
        verbose_name_plural = 'Основная информация(паспорт)'
        db_table = 'energy_passports_detail'
