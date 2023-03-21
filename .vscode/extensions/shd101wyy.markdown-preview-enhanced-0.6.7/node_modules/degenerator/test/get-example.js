// get
function myFn () {
  var one = get('https://google.com');
  var two = get('http://nodejs.org');
  var three = JSON.parse(get('http://jsonip.org'));
  return [one, two, three];
}
