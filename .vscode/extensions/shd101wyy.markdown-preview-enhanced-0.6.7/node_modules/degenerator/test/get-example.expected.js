function* myFn() {
    var one = yield get('https://google.com');
    var two = yield get('http://nodejs.org');
    var three = JSON.parse(yield get('http://jsonip.org'));
    return [
        one,
        two,
        three
    ];
}
