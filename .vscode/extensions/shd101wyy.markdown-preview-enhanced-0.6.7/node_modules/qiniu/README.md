# Qiniu Cloud SDK for Node.js

[![@qiniu on weibo](http://img.shields.io/badge/weibo-%40qiniutek-blue.svg)](http://weibo.com/qiniutek)
[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE.md)
[![Build Status](https://api.travis-ci.org/qiniu/nodejs-sdk.svg?branch=master)](https://travis-ci.org/qiniu/nodejs-sdk)
[![Code Climate](https://codeclimate.com/github/qiniu/nodejs-sdk.svg)](https://codeclimate.com/github/qiniu/nodejs-sdk)
[![Latest Stable Version](https://img.shields.io/npm/v/qiniu.svg)](https://www.npmjs.com/package/qiniu)

## 下载

### 从 npm 安装

这是我们建议的方式

```bash
$ npm install qiniu
```

### 从 release 版本下载

下载地址：[https://github.com/qiniu/nodejs-sdk/releases](https://github.com/qiniu/nodejs-sdk/releases)

这里可以下载到旧版本的SDK，release 版本有版本号，有 [CHANGELOG](https://github.com/qiniu/nodejs-sdk/blob/master/CHANGELOG.md)，使用规格也会比较稳定。

### 从 git 库下载

你可以直接用 git clone 下载源代码来使用。但是请注意非 master 分支的代码可能会变更，应谨慎使用。

## 使用

参考文档：[七牛云存储 Node.js SDK 使用指南](http://developer.qiniu.com/kodo/sdk/nodejs)  

## 测试
```    
$ cd ./test/  
$ source test-env.sh  
$ mocha --grep 'bucketinfo'
```   

## 贡献代码

1. Fork
2. 创建您的特性分支 (`git checkout -b my-new-feature`)
3. 提交您的改动 (`git commit -am 'Added some feature'`)
4. 将您的修改记录提交到远程 `git` 仓库 (`git push origin my-new-feature`)
5. 然后到 github 网站的该 `git` 远程仓库的 `my-new-feature` 分支下发起 Pull Request

## 许可证

Copyright (c) 2015 qiniu.com

基于 MIT 协议发布:

* [www.opensource.org/licenses/MIT](http://www.opensource.org/licenses/MIT)
