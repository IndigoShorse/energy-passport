import type {passportDetail, passportListItem} from "~/models/types/passportTypes";
import {create_options} from "~/composables/global_functions";
import type {DefaultResponse, DefaultListResult} from "~/models/types/default";


export default () => {
    const config = useRuntimeConfig();
    const url = config.public.REQUEST_URL;

    async function post_passport_data(data: passportDetail) {
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