function* foo() {
    return yield baz();
}
function* bar() {
    return yield foo(baz);
}
function* baz() {
    return yield bar();
}
