/***************************************************************************
* Copyright (c) 2018, Voilà contributors                                   *
*                                                                          *
* Distributed under the terms of the BSD 3-Clause License.                 *
*                                                                          *
* The full license is in the file LICENSE, distributed with this software. *
****************************************************************************/

// NOTE: this file is not transpiled, async/await is the only modern feature we use here
require([window.voila_js_url || 'static/voila'], function(voila) {
    // requirejs doesn't like to be passed an async function, so create one inside
    (async function() {
        var kernel = await voila.connectKernel()
        if (!kernel) {
            return;
        }

        const context = {
            sessionContext: {
                session: {
                    kernel,
                    kernelChanged: {
                        connect: () => {}
                    },
                },
                statusChanged: {
                    connect: () => {}
                },
                kernelChanged: {
                    connect: () => {}
                },
                connectionStatusChanged: {
                    connect: () => {}
                },
            },
            saveState: {
                connect: () => {}
            },
        };

        const settings = {
            saveState: false
        };

        const rendermime = new voila.RenderMimeRegistry({
            initialFactories: voila.extendedRendererFactories
        });

        var widgetManager = new voila.WidgetManager(context, rendermime, settings);

        async function init() {
            // it seems if we attach this to early, it will not be called
            const matches = document.cookie.match('\\b_xsrf=([^;]*)\\b');
            const xsrfToken = (matches && matches[1]) || '';
            const configData = JSON.parse(document.getElementById('jupyter-config-data').textContent);
            const baseUrl = configData.baseUrl;
            window.addEventListener('beforeunload', function (e) {
                const data = new FormData();
                data.append("_xsrf", xsrfToken);
                window.navigator.sendBeacon(`${baseUrl}voila/api/shutdown/${kernel.id}`, data);
                kernel.dispose();
            });
            await widgetManager.build_widgets();
            voila.renderMathJax();
        }

        if (document.readyState === 'complete') {
            init()
        } else {
            window.addEventListener('load', init);
        }
    })()
});

