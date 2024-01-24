"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.createIdGenerator = void 0;
const ulid_1 = require("ulid");
function createIdGenerator() {
    return () => (0, ulid_1.ulid)();
}
exports.createIdGenerator = createIdGenerator;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiY3JlYXRlLWlkLWdlbmVyYXRvci5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbIi4uL3NyYy9jcmVhdGUtaWQtZ2VuZXJhdG9yLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiI7OztBQUFBLCtCQUE0QjtBQUU1QixTQUFnQixpQkFBaUI7SUFDL0IsT0FBTyxHQUFHLEVBQUUsQ0FBQyxJQUFBLFdBQUksR0FBRSxDQUFDO0FBQ3RCLENBQUM7QUFGRCw4Q0FFQyIsInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IHVsaWQgfSBmcm9tIFwidWxpZFwiO1xuXG5leHBvcnQgZnVuY3Rpb24gY3JlYXRlSWRHZW5lcmF0b3IoKTogKCkgPT4gc3RyaW5nIHtcbiAgcmV0dXJuICgpID0+IHVsaWQoKTtcbn1cbiJdfQ==