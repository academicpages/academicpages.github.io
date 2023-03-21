/**
 * typescript definition for qiniu 7.0.2
 * @date 2017-06-27
 * @author xialeistudio<xialeistudio@gmail.com>
 */
export declare type callback = (e?: Error, respBody?: any, respInfo?: any) => void;

export declare namespace auth {
    namespace digest {
        class Mac {
            accessKey: string;
            secretKey: string;

            constructor(accessKey?: string, secretKey?: string);
        }
    }
}

export declare namespace cdn {
    class CdnManager {
        mac: auth.digest.Mac;

        constructor(mac?: auth.digest.Mac);

        /**
         * 获取域名日志下载链接
         * @see http://developer.qiniu.com/article/fusion/api/log.html
         *
         * @param domains 域名列表  如：['obbid7qc6.qnssl.com','7xkh68.com1.z0.glb.clouddn.com']
         * @param logDay logDay 如 2016-07-01
         * @param callback  callbackFunc(err, respBody, respInfo)
         */
        getCdnLogList(domains: string[], logDay: string, callback: callback): void;

        /**
         * 获取域名访问流量数据
         * @see http://developer.qiniu.com/article/fusion/api/traffic-bandwidth.html#batch-flux
         *
         * @param startDate 开始日期，例如：2016-07-01
         * @param endDate 结束日期，例如：2016-07-03
         * @param granularity 粒度，取值：5min／hour／day
         * @param domains  域名列表 domain = ['obbid7qc6.qnssl.com','obbid7qc6.qnssl.com'];
         * @param callback callbackFunc(err, respBody, respInfo)
         */
        getFluxData(startDate: string, endDate: string, granularity: string, domains: string[], callback: callback): void;

        /**
         * 获取域名带宽数据
         * @see http://developer.qiniu.com/article/fusion/api/traffic-bandwidth.html#batch-flux
         * @param startDate 开始日期，例如：2016-07-01
         * @param endDate 结束日期，例如：2016-07-03
         * @param granularity 粒度，取值：5min／hour／day
         * @param domains  域名列表 domain = ['obbid7qc6.qnssl.com','obbid7qc6.qnssl.com'];
         * @param callback callbackFunc(err, respBody, respInfo)
         */
        getBandwidthData(startDate: string, endDate: string, granularity: string, domains: string[], callback: callback): void;

        /**
         * 预取文件链接
         * @see http://developer.qiniu.com/article/fusion/api/prefetch.html
         *
         * @param urls 预取urls  urls = ['http://obbid7qc6.qnssl.com/023','http://obbid7qc6.qnssl.com/025']
         * @param callback callbackFunc(err, respBody, respInfo)
         */
        prefetchUrls(urls: string[], callback: callback): void;

        /**
         * 刷新链接
         * @see http://developer.qiniu.com/article/fusion/api/refresh.html
         *
         * @param urls refreshUrls =  ['http://obbid7qc6.qnssl.com/023','http://obbid7qc6.qnssl.com/025']
         * @param callback callbackFunc(err, respBody, respInfo)
         */
        refreshUrls(urls: string[], callback: callback): void;

        /**
         * 刷新目录列表，每次最多不可以超过10个目录, 刷新目录需要额外开通权限，可以联系七牛技术支持处理
         * @see http://developer.qiniu.com/article/fusion/api/refresh.html
         *
         * @param dirs refreshDirs =  ['http://obbid7qc6.qnssl.com/wo/','http://obbid7qc6.qnssl.com/']
         * @param callback callbackFunc(err, respBody, respInfo)
         */
        refreshDirs(dirs: string[], callback: callback): void;

        /**
         * 刷新目录和链接
         * @param urls refreshUrls =  ['http://obbid7qc6.qnssl.com/023','http://obbid7qc6.qnssl.com/025']
         * @param dirs refreshDirs =  ['http://obbid7qc6.qnssl.com/wo/','http://obbid7qc6.qnssl.com/']
         * @param callback callbackFunc(err, respBody, respInfo)
         */
        refreshUrlsAndDirs(urls: string[], dirs: string[], callback: callback): void;

        /**
         * 构建标准的基于时间戳的防盗链
         * @param domain  自定义域名，例如 http://img.abc.com
         * @param fileName 待访问的原始文件名，必须是utf8编码，不需要进行urlencode
         * @param query  业务自身的查询参数，必须是utf8编码，不需要进行urlencode, 例如 {aa:"23", attname:"11111111111111"}
         * @param encryptKey 时间戳防盗链的签名密钥，从七牛后台获取
         * @param deadline 链接的有效期时间戳，是以秒为单位的Unix时间戳
         * @return signedUrl  最终的带时间戳防盗链的url
         */
        createTimestampAntiLeechUrl(domain: string, fileName: string, query: any, encryptKey: string, deadline: number): string;
    }
}

export declare namespace conf {
    let ACCESS_KEY: string;
    let SECRET_KEY: string;
    let USER_AGENT: string;
    let BLOCK_SIZE: number;
    let FormMimeUrl: string;
    let FormMimeJson: string;
    let FormMimeRaw: string;
    let RS_HOST: string;
    let RPC_TIMEOUT: number;

    interface ConfigOptions {
        /**
         * @default false
         */
        useHttpsDomain?: boolean;

        /**
         * @default true
         */
        useCdnDomain?: boolean;

        /**
         * @default null
         */
        zone?: Zone,

        /**
         * @default -1
         */
        zoneExpire?: number;
    }
    class Config implements ConfigOptions {
        constructor(options?: ConfigOptions);
    }

    class Zone {
        srcUpHosts: any;
        cdnUpHosts: any;
        ioHost: string;
        rsHost: string;
        rsfHost: string;
        apiHost: string;

        constructor(srcUpHosts?: any, cdnUpHosts?: any, ioHost?: string, rsHost?: string, rsfHost?: string, apiHost?: string);
    }
}

export declare namespace form_up {
    class FormUploader {
        conf: conf.Config;

        constructor(config?: conf.Config);

        /**
         *
         * @param uploadToken
         * @param key
         * @param rsStream
         * @param putExtra
         * @param callback
         */
        putStream(uploadToken: string, key: string | null, rsStream: NodeJS.ReadableStream, putExtra: PutExtra | null, callback: callback): void;

        /**
         *
         * @param uploadToken
         * @param key
         * @param body
         * @param putExtra
         * @param callback
         */
        put(uploadToken: string, key: string | null, body: any, putExtra: PutExtra | null, callback: callback): void;

        /**
         *
         * @param uploadToken
         * @param body
         * @param putExtra
         * @param callback
         */
        putWithoutKey(uploadToken: string, body: any, putExtra: PutExtra | null, callback: callback): void;

        /**
         * 上传本地文件
         * @param uploadToken 上传凭证
         * @param key 目标文件名
         * @param localFile 本地文件路径
         * @param putExtra 额外选项
         * @param callback
         */
        putFile(uploadToken: string, key: string | null, localFile: string, putExtra: PutExtra | null, callback: callback): void;

        /**
         *
         * @param uploadToken
         * @param localFile
         * @param putExtra
         * @param callback
         */
        putFileWithoutKey(uploadToken: string, localFile: string, putExtra: PutExtra | null, callback: callback): void;
    }

    class PutExtra {
        /**
         * @default ''
         */
        fname: string;

        /**
         * @default {}
         */
        params: any;

        /**
         * @default null
         */
        mimeType?: string;

        /**
         * @default null
         */
        crc32?: string;

        /**
         * @default 0|false
         */
        checkCrc?: number | boolean;

        /**
         * 上传可选参数
         * @param fname 请求体中的文件的名称
         * @param params 额外参数设置，参数名称必须以x:开头
         * @param mimeType 指定文件的mimeType
         * @param crc32 指定文件的crc32值
         * @param checkCrc 指定是否检测文件的crc32值
         */
        constructor(fname?: string, params?: any, mimeType?: string, crc32?: string, checkCrc?: number | boolean);
    }
}

export declare namespace resume_up {
    class ResumeUploader {
        config: conf.Config;

        constructor(config?: conf.Config);

        /**
         *
         * @param uploadToken
         * @param key
         * @param rsStream
         * @param rsStreamLen
         * @param putExtra
         * @param callback
         */
        putStream(uploadToken: string, key: string | null, rsStream: NodeJS.ReadableStream, rsStreamLen: number, putExtra: PutExtra | null, callback: callback): void;

        /**
         *
         * @param uploadToken
         * @param key
         * @param localFile
         * @param putExtra
         * @param callback
         */
        putFile(uploadToken: string, key: string | null, localFile: string, putExtra: PutExtra | null, callback: callback): void;

        /**
         *
         * @param uploadToken
         * @param localFile
         * @param putExtra
         * @param callback
         */
        putFileWithoutKey(uploadToken: string, localFile: string, putExtra: PutExtra | null, callback: callback): void;
    }

    class PutExtra {
        /**
         * @default ''
         */
        fname: string;

        /**
         * @default {}
         */
        params: any;

        /**
         * @default null
         */
        mimeType?: string;

        /**
         * 上传可选参数
         * @param fname 请求体中的文件的名称
         * @param params 额外参数设置，参数名称必须以x:开头
         * @param mimeType 指定文件的mimeType
         * @param resumeRecordFile
         * @param progressCallback
         */
        constructor(fname?: string, params?: any, mimeType?: string, resumeRecordFile?: string, progressCallback?: (data: any) => void);
    }
}

export declare namespace util {
    function isTimestampExpired(timestamp: number): boolean;

    function encodedEntry(bucket: string, key?: string): string;

    function getAKFromUptoken(uploadToken: string): string;

    function getBucketFromUptoken(uploadToken: string): string;

    function base64ToUrlSafe(v: string): string;

    function urlSafeToBase64(v: string): string;

    function urlsafeBase64Encode(jsonFlags: string): string;

    function urlSafeBase64Decode(fromStr: string): string;

    function hmacSha1(encodedFlags: string | Buffer, secretKey: string | Buffer): string;

    /**
     * 创建AccessToken凭证
     * @param mac AK&SK对象
     * @param requestURI 请求URL
     * @param reqBody  请求Body，仅当请求的ContentType为application/x-www-form-urlencoded 时才需要传入该参数
     */
    function generateAccessToken(mac: auth.digest.Mac, requestURI: string, reqBody?: string): string;


    /**
     * 创建AccessToken凭证
     * @param mac            AK&SK对象
     * @param requestURI     请求URL
     * @param reqMethod      请求方法，例如 GET，POST
     * @param reqContentType 请求类型，例如 application/json 或者  application/x-www-form-urlencoded
     * @param reqBody        请求Body，仅当请求的 ContentType 为 application/json 或者 application/x-www-form-urlencoded 时才需要传入该参数
     */
    function generateAccessTokenV2(mac: auth.digest.Mac, requestURI: string, reqMethod: string, reqContentType: string, reqBody?: string): string;

    /**
     * 校验七牛上传回调的Authorization
     * @param mac AK&SK对象
     * @param requestURI 回调的URL中的requestURI
     * @param reqBody 回调的URL中的requestURI 请求Body，仅当请求的ContentType为application/x-www-form-urlencoded时才需要传入该参数
     * @param callbackAuth 回调时请求的Authorization头部值
     */
    function isQiniuCallback(mac: auth.digest.Mac, requestURI: string, reqBody: string | null, callbackAuth: string): boolean;
}

export declare namespace rpc {
    interface Headers {
        'User-Agent'?: string;
        Connection?: string;
    }
    /**
     *
     * @param requestURI
     * @param requestForm
     * @param headers
     * @param callback
     */
    function post(requestURI: string, requestForm: Buffer | string | NodeJS.ReadableStream | null, headers: Headers | null, callback: callback): void;

    /**
     *
     * @param requestURI
     * @param requestForm
     * @param callback
     */
    function postMultipart(requestURI: string, requestForm: Buffer | string | NodeJS.ReadableStream | null, callback: callback): void;

    /**
     *
     * @param requestURI
     * @param requestForm
     * @param token
     * @param callback
     */
    function postWithForm(requestURI: string, requestForm: Buffer | string | NodeJS.ReadableStream | null, token: string | null, callback: callback): void;

    /**
     *
     * @param requestURI
     * @param token
     * @param callback
     */
    function postWithoutForm(requestURI: string, token: string | null, callback: callback): void;
}

export declare namespace zone {
    //huadong
    const Zone_z0: conf.Zone;
    //huabei
    const Zone_z1: conf.Zone;
    //huanan
    const Zone_z2: conf.Zone;
    //beimei
    const Zone_na0: conf.Zone;
    //Southeast Asia
    const Zone_as0: conf.Zone;
}

export declare namespace fop {
    interface PfopOptions {
        /**
         * 回调业务服务器，通知处理结果
         */
        notifyURL?: string;

        /**
         * 结果是否强制覆盖已有的同名文件
         */
        force?: boolean;
    }
    class OperationManager {
        mac: auth.digest.Mac;
        config: conf.Config;

        constructor(mac?: auth.digest.Mac, config?: conf.Config);

        /**
         * 发送持久化数据处理请求
         * @param bucket 空间名称
         * @param key 文件名称
         * @param fops 处理指令集合
         * @param pipeline 处理队列名称
         * @param options
         * @param callback
         */
        pfop(bucket: string, key: string, fops: string[], pipeline: string, options: PfopOptions | null, callback: callback): void;

        /**
         * 查询持久化数据处理进度
         * @param persistentId pfop操作返回的持久化处理ID
         * @param callback
         */
        prefop(persistentId: string, callback: callback): void;
    }
}

export declare namespace rs {
    interface ListPrefixOptions {
        /**
         * 列举的文件前缀
         */
        prefix?: string;

        /**
         * 上一次列举返回的位置标记
         */
        marker?: any;

        /**
         * 每次返回的最大列举文件数量
         */
        limit?: number;

        /**
         * 指定目录分隔符
         */
        delimiter?: string;
    }

    class BucketManager {
        mac: auth.digest.Mac;
        config: conf.Config;

        constructor(mac?: auth.digest.Mac, config?: conf.Config);

        /**
         * 获取资源信息
         * @see https://developer.qiniu.com/kodo/api/1308/stat
         *
         * @param bucket 空间名称
         * @param key 文件名称
         * @param callback
         */
        stat(bucket: string, key: string, callback: callback): void;

        /**
         * 修改文件的类型
         * @see https://developer.qiniu.com/kodo/api/1252/chgm
         *
         * @param bucket 空间名称
         * @param key 文件名称
         * @param newMime 新文件类型
         * @param callback
         */
        changeMime(bucket: string, key: string, newMime: string, callback: callback): void;

        /**
         * 修改文件的Headers
         * @see TODO
         *
         * @param bucket 空间名称
         * @param key 文件名称
         * @param headers Headers对象
         * @param callback
         */
        changeHeaders(bucket: string, key: string, headers: { [k: string]: string }, callback: callback): void;

        /**
         * 移动或重命名文件，当bucketSrc==bucketDest相同的时候，就是重命名文件操作
         * @see https://developer.qiniu.com/kodo/api/1288/move
         *
         * @param srcBucket 源空间名称
         * @param srcKey 源文件名称
         * @param destBucket 目标空间名称
         * @param destKey 目标文件名称
         * @param options
         * @param callback
         */
        move(srcBucket: string, srcKey: string, destBucket: string, destKey: string, options: { force?: boolean } | null, callback: callback): void;

        /**
         * 复制文件
         * @see https://developer.qiniu.com/kodo/api/1254/copy
         *
         * @param srcBucket 源空间名称
         * @param srcKey 源文件名称
         * @param destBucket 目标空间名称
         * @param destKey 目标文件名称
         * @param options
         * @param callback
         */
        copy(srcBucket: string, srcKey: string, destBucket: string, destKey: string, options: { force?: boolean } | null, callback: callback): void;

        /**
         * 删除资源
         * @see https://developer.qiniu.com/kodo/api/1257/delete
         *
         * @param bucket 空间名称
         * @param key 文件名称
         * @param callback
         */
        delete(bucket: string, key: string, callback: callback): void;

        /**
         * 更新文件的生命周期
         * @see https://developer.qiniu.com/kodo/api/1732/update-file-lifecycle
         *
         * @param bucket 空间名称
         * @param key 文件名称
         * @param days 有效期天数
         * @param callback
         */
        deleteAfterDays(bucket: string, key: string, days: number, callback: callback): void;

        /**
         * 抓取资源
         * @see https://developer.qiniu.com/kodo/api/1263/fetch
         *
         * @param resUrl 资源链接
         * @param bucket 空间名称
         * @param key 文件名称
         * @param callback
         */
        fetch(resUrl: string, bucket: string, key: string, callback: callback): void;

        /**
         * 更新镜像副本
         * @see https://developer.qiniu.com/kodo/api/1293/prefetch
         *
         * @param bucket 空间名称
         * @param key 文件名称
         * @param callback
         */
        prefetch(bucket: string, key: string, callback: callback): void;

        /**
         * 修改文件的存储类型
         * @see https://developer.qiniu.com/kodo/api/3710/modify-the-file-type
         *
         * @param bucket 空间名称
         * @param key 文件名称
         * @param newType 0 表示标准存储；1 表示低频存储。
         * @param callback
         */
        changeType(bucket: string, key: string, newType: number, callback: callback): void;

        /**
         * 设置空间镜像源
         * @see https://developer.qiniu.com/kodo/api/1370/mirror
         *
         * @param bucket 空间名称
         * @param srcSiteUrl 镜像源地址
         * @param srcHost 镜像Host
         * @param callback
         */
        image(bucket: string, srcSiteUrl: string, srcHost: string, callback: callback): void;

        /**
         * 取消设置空间镜像源
         * @see https://developer.qiniu.com/kodo/api/1370/mirror
         *
         * @param bucket 空间名称
         * @param callback
         */
        unimage(bucket: string, callback: callback): void;

        /**
         * 获取指定前缀的文件列表
         * @see https://developer.qiniu.com/kodo/api/1284/list
         *
         * @param bucket 空间名称
         * @param options 列举操作的可选参数
         * @param callback
         */
        listPrefix(bucket: string, options: ListPrefixOptions | null, callback: callback): void;

        /**
         * 批量文件管理请求，支持stat，chgm，chtype，delete，copy，move
         * @param operations
         * @param callback
         */
        batch(operations: any, callback: callback): void;

        /**
         * 获取私有空间的下载链接
         * @param domain 空间绑定的域名，比如以http或https开头
         * @param fileName 原始文件名
         * @param deadline 文件有效期时间戳（单位秒）
         */
        privateDownloadUrl(domain: string, fileName: string, deadline: number): string;

        /**
         * 获取公开空间的下载链接
         * @param domain 空间绑定的域名，比如以http或https开头
         * @param fileName 原始文件名
         */
        publicDownloadUrl(domain: string, fileName: string): string;
    }

    /**
     *
     * @param bucket
     * @param key
     */
    function statOp(bucket: string, key: string): string;

    /**
     *
     * @param bucket
     * @param key
     */
    function deleteOp(bucket: string, key: string): string;

    /**
     *
     * @param bucket
     * @param key
     * @param days
     */
    function deleteAfterDaysOp(bucket: string, key: string, days: number): string;

    /**
     *
     * @param bucket
     * @param key
     * @param newMime
     */
    function changeMimeOp(bucket: string, key: string, newMime: string): string;

    /**
     *
     * @param bucket
     * @param key
     * @param headers
     */
    function changeHeadersOp(bucket: string, key: string, headers: { [k: string]: string }): string;

    /**
     *
     * @param bucket
     * @param key
     * @param newType
     */
    function changeTypeOp(bucket: string, key: string, newType: number): string;

    /**
     *
     * @param srcBucket
     * @param srcKey
     * @param destBucket
     * @param destKey
     * @param options
     */
    function moveOp(srcBucket: string, srcKey: string, destBucket: string, destKey: string, options?: { force?: boolean }): string;

    /**
     *
     * @param srcBucket
     * @param srcKey
     * @param destBucket
     * @param destKey
     * @param options
     */
    function copyOp(srcBucket: string, srcKey: string, destBucket: string, destKey: string, options?: { force?: boolean }): string;

    interface PutPolicyOptions {
        scope?: string;
        isPrefixalScope?: number;
        expires?: number;
        insertOnly?: number;
        saveKey?: string;
        endUser?: string;
        returnUrl?: string;
        returnBody?: string;
        callbackUrl?: string;
        callbackHost?: string;
        callbackBody?: string;
        callbackBodyType?: string;
        callbackFetchKey?: number;

        persistentOps?: string;
        persistentNotifyUrl?: string;
        persistentPipeline?: string;

        fsizeLimit?: number;
        fsizeMin?: number;
        mimeLimit?: string;

        detectMime?: number;
        deleteAfterDays?: number;
        fileType?: number;
    }
    class PutPolicy {
        constructor(options?: PutPolicyOptions);

        getFlags(): any;

        uploadToken(mac?: auth.digest.Mac): string;
    }
}
