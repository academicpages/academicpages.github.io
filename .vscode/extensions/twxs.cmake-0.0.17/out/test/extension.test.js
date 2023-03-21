"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator.throw(value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : new P(function (resolve) { resolve(result.value); }).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments)).next());
    });
};
suite("Utility tests", () => {
    test("Reloads only when needed", function () {
        return __awaiter(this, void 0, void 0, function* () {
            //  let cm = new cmake.CMakeHelpers();
            // let cmd = await cm.cmake_help_command('set');        
            // assert.strictEqual(await reader.needsReloading(), true);
            // assert.strictEqual(await reader.needsReloading(), true);
            // await reader.get("CMAKE_GENERATOR");
            // assert.notStrictEqual(cmd.length, 0);
        });
    });
});
//# sourceMappingURL=extension.test.js.map