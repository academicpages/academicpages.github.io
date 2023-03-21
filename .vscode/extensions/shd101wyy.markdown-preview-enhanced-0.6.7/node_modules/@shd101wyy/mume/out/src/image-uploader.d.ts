/**
 * Upload image
 * @param imageFilePath
 * @param method 'imgur' or 'sm.ms'
 * @param qiniu {AccessKey, SecretKey, Bucket, Domain}
 */
export declare function uploadImage(imageFilePath: string, { method, qiniu, }: {
    method?: string;
    qiniu?: {
        AccessKey: string;
        SecretKey: string;
        Bucket: string;
        Domain: string;
    };
}): Promise<string>;
