module.exports = {
    auth: {
        digest: require('./qiniu/auth/digest.js')
    },
    cdn: require('./qiniu/cdn.js'),
    form_up: require('./qiniu/storage/form.js'),
    resume_up: require('./qiniu/storage/resume.js'),
    rs: require('./qiniu/storage/rs.js'),
    fop: require('./qiniu/fop.js'),
    conf: require('./qiniu/conf.js'),
    rpc: require('./qiniu/rpc.js'),
    util: require('./qiniu/util.js'),
    zone: require('./qiniu/zone.js'),
    app: require('./qiniu/rtc/app.js'),
    room: require('./qiniu/rtc/room.js'),
    Credentials: require('./qiniu/rtc/credentials.js'),
    sms: {
        message: require('./qiniu/sms/message.js'),
    }
};
