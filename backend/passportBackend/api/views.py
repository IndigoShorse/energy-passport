import os
import uuid

from django.http import FileResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EnergyPassportDetail
from .serializers import EnergyPassportDetailSerializer
from docxtpl import DocxTemplate
from io import BytesIO


@api_view(['POST'])
def post_energy_passport(request):
    if request.method == 'POST':
        serializer = EnergyPassportDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_energy_passports(request):
    if request.method == 'GET':
        passports = EnergyPassportDetail.objects.all()  # Получаем все записи
        serializer = EnergyPassportDetailSerializer(passports, many=True)  # Сериализуем данные
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def download_energy_passport(request):
    """Генерация и скачивание энергетического паспорта в формате DOCX"""
    passport_id = request.query_params.get('passport_id')

    if not passport_id:
        return Response(
            {'error': 'Не указан passport_id в query параметрах'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Пытаемся преобразовать в UUID
        passport_uuid = uuid.UUID(passport_id)
    except ValueError:
        return Response(
            {'error': 'Неверный формат passport_id (ожидается UUID)'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Получаем данные паспорта из БД по UUID
        passport = EnergyPassportDetail.objects.get(id=passport_uuid)

        # Загружаем шаблон документа
        template_path = os.path.join(os.path.dirname(__file__), 'templates/template.docx')
        doc = DocxTemplate(template_path)

        total_production_cost = []
        for i in range(len(passport.heating_and_ventilation)):
            total = passport.heating_and_ventilation[i] + passport.hot_water_supply[i]
            total_production_cost.append(total)
        # Подготавливаем контекст для шаблона из данных модели
        context = {
            "selfregulating_organization": passport.selfregulating_organization,
            "registration_number_date": passport.registration_number_date,
            "organization_conducted_survey": passport.organization_conducted_survey,
            "registration_number": passport.registration_number,
            "signature_person_conducted": passport.signature_person_conducted,
            "customers_signature": passport.customers_signature,
            "sro_signature": passport.sro_signature,
            "date_compilation": passport.date_compilation,
            "name_organization": passport.name_organization,
            "organization_legal_form": passport.organization_legal_form,
            "mailing_address": passport.mailing_address,
            "location": passport.location,
            "full_name": passport.full_name,
            "share_state_ownership": passport.share_state_ownership,
            "ogrn": passport.ogrn,
            "inn": passport.inn,
            "kpp": passport.kpp,
            "bank_details_inn": passport.bank_details_inn,
            "okved_code": passport.okved_code,
            "full_name_responsible_technical": passport.full_name_responsible_technical,
            "full_name_responsible_energy": passport.full_name_responsible_energy,

            "main_product_nomenclature": passport.main_product_nomenclature,
            "main_product_code": passport.main_product_code,
            "additional_product_nomenclature": passport.additional_product_nomenclature,
            "additional_product_code": passport.additional_product_code,
            "total_production_monetary": passport.total_production_monetary,
            "main_product_monetary": passport.main_product_monetary,
            "additional_product_monetary": passport.additional_product_monetary,
            "total_production_physical": passport.total_production_physical,
            "main_product_physical": passport.main_product_physical,
            "additional_product_physical": passport.additional_product_physical,
            "total_energy_monetary": passport.total_energy_monetary,
            "main_product_energy_monetary": passport.main_product_energy_monetary,
            "additional_product_energy_monetary": passport.additional_product_energy_monetary,
            "total_energy_physical": passport.total_energy_physical,
            "main_product_energy_physical": passport.main_product_energy_physical,
            "additional_product_energy_physical": passport.additional_product_energy_physical,
            "water_monetary": passport.water_monetary,
            "water_main_product_monetary": passport.water_main_product_monetary,
            "water_physical": passport.water_physical,
            "water_main_product_physical": passport.water_main_product_physical,
            "energy_intensity_main_product": passport.energy_intensity_main_product,
            "energy_intensity_additional_product": passport.energy_intensity_additional_product,
            "energy_and_water_payment_share": passport.energy_and_water_payment_share,
            "total_maximum_power": passport.total_maximum_power,
            "average_annual_declared_power": passport.average_annual_declared_power,
            "average_employee_headcount": passport.average_employee_headcount,
            "electricity_metered_points_count": passport.electricity_metered_points_count,
            "heat_metered_points_count": passport.heat_metered_points_count,
            "cold_water_metered_points_count": passport.cold_water_metered_points_count,
            "hot_water_metered_points_count": passport.hot_water_metered_points_count,
            "electricity_from_external_source": passport.electricity_from_external_source,
            "heat_from_external_source": passport.heat_from_external_source,
            "cold_water_from_external_source": passport.cold_water_from_external_source,
            "hot_water_from_external_source": passport.hot_water_from_external_source,
            "total_electricity_metering_nodes": passport.total_electricity_metering_nodes,
            "total_heat_metering_nodes": passport.total_heat_metering_nodes,
            "total_cold_water_metering_nodes": passport.total_cold_water_metering_nodes,
            "total_hot_water_metering_nodes": passport.total_hot_water_metering_nodes,

            # Приложение N 4
            "total_electricity_consumed": passport.total_electricity_consumed,
            "electricity_measured_by_meter": passport.electricity_measured_by_meter,
            "total_heat_consumed": passport.total_heat_consumed,
            "heat_measured_by_meters": passport.heat_measured_by_meters,
            "total_water_consumed": passport.total_water_consumed,
            "water_measured_by_meters": passport.water_measured_by_meters,

            # Приложение N 5
            "external_source": passport.external_source,
            "own_needs_consumption": passport.own_needs_consumption,
            "actual_reported_losses": passport.actual_reported_losses,
            "total_technological_losses": passport.total_technological_losses,
            "metering_tolerance_losses": passport.metering_tolerance_losses,
            "irrational_losses": passport.irrational_losses,

            # Приложение N 6
            "hot_external_source": passport.hot_external_source,
            "heating_and_ventilation": passport.heating_and_ventilation,
            "hot_water_supply": passport.hot_water_supply,
            "irrational_tech_losses_hot_water": passport.irrational_tech_losses_hot_water,
            "total_production_cost": total_production_cost,

            # Приложение №11
            'luminaires_below_35_lm_per_watt': passport.luminaires_below_35_lm_per_watt,
            'luminaires_from_35_to_100_lm_per_watt': passport.luminaires_from_35_to_100_lm_per_watt,
            'luminaires_above_100_lm_per_watt': passport.luminaires_above_100_lm_per_watt,
            'total_installed_lighting_power': passport.total_installed_lighting_power,
            'total_lighting_energy_consumption': passport.total_lighting_energy_consumption,

            # Приложение №13 - Здания и сооружения
            'building_name': passport.building_name,
            'year_of_commissioning': passport.year_of_commissioning,
            'wall_brief_description': passport.wall_brief_description,
            'window_brief_description': passport.window_brief_description,
            'roof_brief_description': passport.roof_brief_description,
            'total_building_area': passport.total_building_area,
            'heated_building_area': passport.heated_building_area,
            'heated_building_volume': passport.heated_building_volume,
            'building_wear': passport.building_wear,
            'actual_heat_specific_characteristic': passport.actual_heat_specific_characteristic,
            'calculated_normative_heat_specific_characteristic': passport.calculated_normative_heat_specific_characteristic,
            'total_specific_annual_heat_consumption': passport.total_specific_annual_heat_consumption,
        }

        # Заполняем шаблон
        doc.render(context)

        # Сохраняем во временный буфер
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        # Возвращаем файл как ответ
        response = FileResponse(
            buffer,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            as_attachment=True,
            filename=f'energy_passport_{passport_id}.docx'
        )

        return response

    except EnergyPassportDetail.DoesNotExist:
        return Response(
            {'error': 'Энергетический паспорт не найден'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        print(e)
        return Response(
            {'error': f'Ошибка генерации документа: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
