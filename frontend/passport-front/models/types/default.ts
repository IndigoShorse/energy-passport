export interface DefaultResponse<T>{
    status: string
    detail: T
}

export interface DefaultListResult<T> {
    count: number
    next: string | null
    previous: string | null
    results: Array<T>
}

export interface MultipleAutoprefixerData {
    number: string
    volume: number
    period: string
}