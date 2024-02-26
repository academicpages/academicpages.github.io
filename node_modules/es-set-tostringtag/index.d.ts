declare function setToStringTag(
    object: object & { [Symbol.toStringTag]?: unknown },
    value: string | unknown,
    options?: { force?: boolean },
): void;

export = setToStringTag;