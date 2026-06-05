/**
 * Bundled by jsDelivr using Rollup v2.79.1 and Terser v5.19.2.
 * Original file: /npm/@lit/reactive-element@2.0.4/decorators/query.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */
const e=(e,t,r)=>(r.configurable=!0,r.enumerable=!0,Reflect.decorate&&"object"!=typeof t&&Object.defineProperty(e,t,r),r)
/**
 * @license
 * Copyright 2017 Google LLC
 * SPDX-License-Identifier: BSD-3-Clause
 */;function t(t,r){return(n,o,l)=>{const u=e=>e.renderRoot?.querySelector(t)??null;if(r){const{get:t,set:r}="object"==typeof o?n:l??(()=>{const e=Symbol();return{get(){return this[e]},set(t){this[e]=t}}})();return e(n,o,{get(){let e=t.call(this);return void 0===e&&(e=u(this),(null!==e||this.hasUpdated)&&r.call(this,e)),e}})}return e(n,o,{get(){return u(this)}})}}export{t as query};export default null;