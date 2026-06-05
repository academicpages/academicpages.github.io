/**
 * Minified by jsDelivr using Terser v5.19.2.
 * Original file: /npm/@deepdub/ninja-keys@1.2.11/dist/ninja-action.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
var __decorate=this&&this.__decorate||function(t,e,i,n){var o,a=arguments.length,s=a<3?e:null===n?n=Object.getOwnPropertyDescriptor(e,i):n;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)s=Reflect.decorate(t,e,i,n);else for(var c=t.length-1;c>=0;c--)(o=t[c])&&(s=(a<3?o(s):a>3?o(e,i,s):o(e,i))||s);return a>3&&s&&Object.defineProperty(e,i,s),s};import{LitElement,html,css}from"./lit/index.min.js";import{customElement,property}from"./lit/decorators.min.js";import{classMap}from"./lit/directives/class-map.min.js";import{unsafeHTML}from"./lit/directives/unsafe-html.min.js";import{join}from"./lit/directives/join.min.js";let NinjaAction=class extends LitElement{constructor(){super(),this.selected=!1,this.hotKeysJoinedView=!0,this.addEventListener("click",this.click)}ensureInView(){this.scrollIntoView({block:"nearest"})}click(){this.dispatchEvent(new CustomEvent("actionsSelected",{detail:this.action,bubbles:!0,composed:!0}))}updated(t){t.has("selected")&&this.selected&&this.ensureInView()}highlightMatch(t,e){const tt=new DOMParser().parseFromString(t,'text/html').body.textContent||"";let i="",n=0,o=0;for(o=0;o<tt.length;o++)e[n]===o?(i+=`<span class="highlight">${t[o]}</span>`,n++):i+=t[o];if(o<t.length){i+=t.slice(o);}return unsafeHTML(i)}render(){let t,e;this.action.mdIcon?t=html`<div>${this.action.mdIcon}</div>`:this.action.icon&&(t=this.action.icon?unsafeHTML(`<div class="ninja-icon">${this.action.icon}</div>`):""),this.action.hotkey&&(e=this.hotKeysJoinedView?this.action.hotkey.split(",").map((t=>{const e=t.split("+"),i=html`${join(e.map((t=>html`<kbd>${t}</kbd>`)),"+")}`;return html`<div class="ninja-hotkey ninja-hotkeys">${i}</div>`})):this.action.hotkey.split(",").map((t=>{const e=t.split("+").map((t=>html`<kbd class="ninja-hotkey">${t}</kbd>`));return html`<kbd class="ninja-hotkeys">${e}</kbd>`})));const i={selected:this.selected,"ninja-action":!0};return html`
      <div class="ninja-action" part="ninja-action ${this.selected?"ninja-selected":""}" class=${classMap(i)}>
        ${t}
        ${this.action.type?html`<div class="ninja-action-type" style="background: ${n=this.action.type,"debug"===n?"#034900":"general"===n?"#193C79":"segments"===n?"#2F0A7D":"#000000"}">
              ${this.action.type}
            </div>`:html``}
        <div class="ninja-title">${this.highlightMatch(this.action.title,this.matchIndices)}</div>
        ${e}
      </div>
    `;var n}};NinjaAction.styles=css`
    :host {
      display: flex;
      width: 100%;
    }
    .ninja-action {
      padding: 0.75em 1em;
      display: flex;
      gap: 0.75rem;
      border-left: 2px solid transparent;
      align-items: center;
      justify-content: start;
      outline: none;
      transition: color 0s ease 0s;
      width: 100%;
    }
    .ninja-action .highlight {
      color: var(--ninja-accent-color);
      font-weight: bold;
    }
    .ninja-action.selected {
      cursor: pointer;
      color: var(--ninja-selected-text-color);
      background-color: var(--ninja-selected-background);
      border-left: 2px solid var(--ninja-accent-color);
      outline: none;
    }
    .ninja-action.selected .ninja-icon {
      color: var(--ninja-selected-text-color);
    }
    .ninja-icon {
      width: 20px;
      font-size: var(--ninja-icon-size);
      color: var(--ninja-icon-color);
      margin-right: 0.5625rem;
      position: relative;
      line-height: 0;
      flex-shrink: 0;
    }
    .ninja-icon img {
      width: 100%;
    }

    .ninja-title {
      flex-shrink: 0.01;
      margin-right: 0.5em;
      flex-grow: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .ninja-action-type {
      font-size: 11px;
      padding: 3px 5px;
      border-radius: 3px;
      color: #ffffff;
      text-transform: uppercase;
    }

    .ninja-hotkeys {
      flex-shrink: 0;
      width: min-content;
      display: flex;
    }

    .ninja-hotkeys kbd {
      font-family: inherit;
    }
    .ninja-hotkey {
      background: var(--ninja-secondary-background-color);
      padding: 0.06em 0.25em;
      border-radius: var(--ninja-key-border-radius);
      text-transform: capitalize;
      color: var(--ninja-secondary-text-color);
      font-size: 0.75em;
      font-family: inherit;
    }

    .ninja-hotkey + .ninja-hotkey {
      margin-left: 0.5em;
    }
    .ninja-hotkeys + .ninja-hotkeys {
      margin-left: 1em;
    }
  `,__decorate([property({type:Object})],NinjaAction.prototype,"action",void 0),__decorate([property({type:Array})],NinjaAction.prototype,"matchIndices",void 0),__decorate([property({type:Boolean})],NinjaAction.prototype,"selected",void 0),__decorate([property({type:Boolean})],NinjaAction.prototype,"hotKeysJoinedView",void 0),NinjaAction=__decorate([customElement("ninja-action")],NinjaAction);export{NinjaAction};