// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define(['./loginmain', './logoutmain', 'bidi/bidi'], function (login_main, logout_main, bidi) {
	if(bidi.isMirroringEnabled()){
		$("body").attr("dir","rtl");
	}
    return {
        login_main: login_main,
        logout_main: logout_main
    };
});
