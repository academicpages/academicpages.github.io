## CHANGE LOG

## 7.3.1
新增归档存储解冻接口
支持上传时key值为空字符串

## v7.3.0
- 新增 19 个bucket及文件相关操作
- 新增文件列举 v2 接口功能
- 新增短信功能
- 更新上传加速域名策略
- 修复自动获取上传区域时的无效缓存
- 修复大文件上传异常
- 增加测试用例

## v7.2.2
- 一些log输出问题，travis增加eslint 检查

## v7.2.1
- 修复rtc获取回复存在的问题

## v7.2.0
- 修复node的stream读取的chunk大小比较随意的问题

## v7.1.9
- 修复新版node下resume up方式文件内容被缓存而导致的上传失败

## v7.1.8
- 修复 index.d.ts 文件中zone的设置

## v7.1.7
- 修复form上传在升级mime库后的错误

## v7.1.6
- 修复rs和rsf的https默认域名
- 升级修复mime库的安全风险

## v7.1.5
- 增加连麦功能

## v7.1.3
- 增加新加坡机房

## v7.1.2
- 增加自定义资源访问响应头部的功能
- 改进时间戳签名方法，支持复杂urlencode

### v7.1.1
- 修复 index.d.ts 中的函数声明错误

### v7.1.0
- 修复时间戳防盗链中存在特殊字符引发的签名错误
- 修复分片上传的时候最后一块小于2056字节引发的错误

### v7.0.9
- 增加Qiniu方式的管理凭证生成方法以支持新的产品鉴权

### v7.0.8
- 修复分片上传小文件的时候文件读取end的事件bug

### v7.0.7
- 给form upload添加默认的crc32校验以避免网络层面的字节反转导致上传内容不正确
- 修复resume upload在上传小文件的时候出现的上传失败情况

### v7.0.6
- 修复时间戳防盗链算法中对文件名的urlencode不兼容问题
- 发布index.d.ts文件

### v7.0.5
- 修复zone获取失败时callbackFunc不存在的问题
- 增加分片上传的时候的progressCallback

### v7.0.4
- 增加http&https代理功能

### v7.0.2
- 修复cdn刷新文件和目录中方法引用错误

### v7.0.1

- 重构文件表单上传和分片上传代码
- 重构CDN操作相关的代码
- 重构资源管理相关的代码
- 重构数据处理相关的代码
- 重构上传策略的相关代码

### v6.1.14

2017-01-16

- 增加CDN刷新、预取
- 增加获取带宽、流量数据
- 增加获取日志列表
- 增加时间戳防盗链签名

### v6.1.13

2016-10-13

- 修正从uptoken获取bucket

### v6.1.12

2016-10-10

- 增加多机房接口调用支持

### v6.1.11

2016-05-06

- npm 通过travis 自动发布

### v6.1.10

2016-04-25

- list 增加delimiter 支持
- 增加强制copy/move
- 底层使用putReadable 谢谢 @thesadabc
- 修正result 处理 谢谢 @loulin
- fix Unhandled stream error in pipe 谢谢@loulin
- putExtra 修正 paras 为 params

### v6.1.9

2015-12-03

- Make secure base url
- policy add fsizeMin
- 修正 getEncodedEntryUri(bucket, key)
- 文档修正

### v6.1.8

2015-05-13

- 上传增加putpolicy2

### v6.1.7

2015-05-09

- 上传putpolicy2增加 callbackHost、persistentPipeline, callbackFetchKey
- 增加fetch 函数
- imageview -> imageview2


### v6.1.6

2014-10-31

- 上传putpolicy2增加fsizelimit, insertonly


### v6.1.5

2014-7-23 issue [#111](https://github.com/qiniu/nodejs-sdk/pull/111)

- [#109] 统一user agent
- [#110] 更新put policy

### v6.1.4

2014-7-10 issue [#108](https://github.com/qiniu/nodejs-sdk/pull/108)

- [#107] 调整上传host


### v6.1.3

2014-4-03 issue [#102](https://github.com/qiniu/nodejs-sdk/pull/102)

- [#98] 增加pfop 功能
- [#99] 增加针对七牛callback的检查

### v6.1.2

2014-2-17 issue [#96](https://github.com/qiniu/nodejs-sdk/pull/96)

- Content-Length = 0 时的细节修复


### v6.1.1

2013-12-5 issue [#90](https://github.com/qiniu/nodejs-sdk/pull/90)

- 创建buffer前检测


### v6.1.0

2013-10-08 issues [#81](https://github.com/qiniu/nodejs-sdk/pull/81)

- 使用urllib
- 修复callbackUrl的bug
- 调整bucket的下载域名

### v6.0.0

2013-07-16 issue [#56](https://github.com/qiniu/nodejs-sdk/pull/56)

- 遵循 [sdkspec v6.0.4](https://github.com/qiniu/sdkspec/tree/v6.0.4)
