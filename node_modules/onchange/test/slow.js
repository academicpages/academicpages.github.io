require('net').createServer().listen()

console.log(process.argv[2], process.argv[3])

process.on('SIGTERM', function () {
  setTimeout(function () {
    process.exit(0)
  }, 2000)
})