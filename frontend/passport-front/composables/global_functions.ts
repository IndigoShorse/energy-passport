import type {UseFetchOptions} from "#app";

export function default_headers() {
    return {
        'Content-Type': 'application/json',
        authorization: ''
    };
}
export function format_date_time(data: string): string {
    const message_datetime = new Date(data);
    const message_time = `${message_datetime.getHours() < 10 ? `0${message_datetime.getHours()}` : message_datetime.getHours()}:${message_datetime.getMinutes() > 9 ? message_datetime.getMinutes() : '0' + message_datetime.getMinutes().toString()}`;
    return `${message_datetime.getDate() < 10 ? `0${message_datetime.getDate()}` : message_datetime.getDate()}.${message_datetime.getMonth() < 9 ? `0${message_datetime.getMonth() + 1}` : `${message_datetime.getMonth() + 1}`}.${message_datetime.getFullYear()} ${message_time}`
}

export function format_date(date: string): string {
    const message_datetime = new Date(date);
    return `${message_datetime.getDate() < 10 ? `0${message_datetime.getDate()}` : message_datetime.getDate()}.${message_datetime.getMonth() < 9? `0${message_datetime.getMonth() + 1}` : `${message_datetime.getMonth() + 1}`}.${message_datetime.getFullYear()}`;
}

export function format_month_year(date: string): string {
    const message_datetime = new Date(date);
    return `${message_datetime.getMonth() < 9 ? `0${message_datetime.getMonth() + 1}` : `${message_datetime.getMonth() + 1}`}.${message_datetime.getFullYear()}`;
}
export function create_options(method: "get" | "post" | "put" | "patch" | "delete", auth: boolean, token?: string, body?: any, headers?: any, query?: any) {
    if (!headers)
        headers = default_headers();
    if (auth)
        headers.authorization = `Token ${token}`
    const options: UseFetchOptions<any> = {
        method: method,
        headers: headers
    }
    if (body)
        options.body = body;
    if (query)
        options.query = query;
    return options;
}

export function objectToFormData(obj: Record<string, any>): FormData {
    const formdata = new FormData();
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            const value = obj[key];
            if (!value)
                continue
            else {
                if (Array.isArray(value)) {
                    for (let i = 0; i < value.length; i++) {
                        formdata.append(`${key}`, value[i]);
                    }
                } else {
                    formdata.append(key, value);
                }
            }
        }
    }
    return formdata
}