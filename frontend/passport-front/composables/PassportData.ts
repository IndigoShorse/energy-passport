import type {passportDetail, passportListItem} from "~/models/types/passportTypes";
import {create_options} from "~/composables/global_functions";
import type {DefaultResponse, DefaultListResult} from "~/models/types/default";

const mockStorageKey = 'energy-passport-mock-passports';
const mockPassports = [
    {id: 'mock-001', customers_signature: 'Алексей Морозов', name_organization: 'ООО «ЭнергоТех»'},
    {id: 'mock-002', customers_signature: 'Марина Волкова', name_organization: 'АО «Северная генерация»'},
    {id: 'mock-003', customers_signature: 'Илья Соколов', name_organization: 'Промышленная группа «Вектор»'},
] as unknown as passportListItem[];

function getStoredMockPassports(): passportListItem[] {
    if (!import.meta.client) return [];

    try {
        return JSON.parse(localStorage.getItem(mockStorageKey) || '[]') as passportListItem[];
    } catch {
        return [];
    }
}

function saveMockPassport(data: passportDetail): passportListItem {
    const passport = {
        ...data,
        id: `mock-${Date.now()}`,
        customers_signature: data.customers_signature || 'Новый паспорт',
        name_organization: data.name_organization || 'Новая организация',
    } as passportListItem;

    if (import.meta.client) {
        const stored = getStoredMockPassports();
        localStorage.setItem(mockStorageKey, JSON.stringify([passport, ...stored]));
    }

    return passport;
}

export default () => {
    const config = useRuntimeConfig();
    const url = config.public.REQUEST_URL;
    const isMockMode = !url;

    async function post_passport_data(data: passportDetail) {
        if (isMockMode) {
            await new Promise(resolve => setTimeout(resolve, 350));
            return {status: 'ok', detail: saveMockPassport(data)} as DefaultResponse<passportDetail>;
        }

        const options = create_options("post", false, '', data)
        try {
            // @ts-ignore
            const response = await $fetch<DefaultResponse<passportDetail>>(`${url}/passport/create`, options)
            return response;
        } catch(e: any){
            console.log(e.statusCode, e.statusMessage);
            throw createError(e)
        }
    }

    async function get_passports_list() {
        if (isMockMode) {
            return [...getStoredMockPassports(), ...mockPassports];
        }

        const options = create_options("get", false)
        try {
            //@ts-ignore
            const response = await $fetch<Array<passportListItem>>(`${url}/passport/list/`, options)
            return response;
        } catch(e: any){
            console.log(e.statusCode, e.statusMessage);
            throw createError(e)
        }
    }

    async function download_passport(id: string) {
        if (isMockMode) {
            if (!import.meta.client) return true;
            const passport = [...getStoredMockPassports(), ...mockPassports].find(item => item.id === id);
            const blob = new Blob([
                `Энергетический паспорт\\n\\nОрганизация: ${passport?.name_organization || ''}\\nПодписант: ${passport?.customers_signature || ''}\\n\\nДемонстрационный файл.`
            ], {type: 'text/plain;charset=utf-8'});
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = `energy_passport_${id}.txt`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(link.href);
            return true;
        }

        try {
            const response = await $fetch<Blob>(
                `${url}/passport/download/`,
                {
                    query: {passport_id: id},
                    method: "GET",
                    responseType: 'blob'
                }
            );

            // Создаем ссылку для скачивания
            const blob = new Blob([response], {
                type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = `energy_passport_${id}.docx`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);

            return true;
        } catch (e: any) {
            console.error('Download error:', e);
            throw createError({
                statusCode: e.statusCode || 500,
                statusMessage: e.statusMessage || 'Failed to download passport'
            });
        }
    }

    return {
        post_passport_data,
        get_passports_list,
        download_passport
    };
}
