function* foo() {
    return (yield a('bar')) || (yield b());
}
