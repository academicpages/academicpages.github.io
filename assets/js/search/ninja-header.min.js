/**
 * Minified by jsDelivr using Terser v5.19.2.
 * Original file: /npm/@deepdub/ninja-keys@1.2.11/dist/ninja-header.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
var __decorate=this&&this.__decorate||function(e,t,r,a){var n,o=arguments.length,i=o<3?t:null===a?a=Object.getOwnPropertyDescriptor(t,r):a;if("object"==typeof Reflect&&"function"==typeof Reflect.decorate)i=Reflect.decorate(e,t,r,a);else for(var s=e.length-1;s>=0;s--)(n=e[s])&&(i=(o<3?n(i):o>3?n(t,r,i):n(t,r))||i);return o>3&&i&&Object.defineProperty(t,r,i),i};import{LitElement,html,css}from"./lit/index.min.js";import{customElement,property}from"./lit/decorators.min.js";import{ref,createRef}from"./lit/directives/ref.min.js";let NinjaHeader=class extends LitElement{constructor(){super(...arguments),this.placeholder="",this.hideBreadcrumbs=!1,this.breadcrumbHome="Home",this.breadcrumbs=[],this._inputRef=createRef(),this._prevValue=""}render(){let e="";if(!this.hideBreadcrumbs){const t=[];for(const e of this.breadcrumbs)t.push(html`<button tabindex="-1" @click=${()=>this.selectParent(e)} class="breadcrumb">
            ${e}
          </button>`);e=html`<div class="breadcrumb-list">
        <button tabindex="-1" @click=${()=>this.selectParent()} class="breadcrumb">${this.breadcrumbHome}</button>
        ${t}
      </div>`}return html`
      ${e}
      <div part="ninja-input-wrapper" class="search-wrapper">
        <input
          part="ninja-input"
          type="text"
          id="search"
          spellcheck="false"
          autocomplete="off"
          @input="${this._handleInput}"
          @keyup="${this._handleKeyup}"
          ${ref(this._inputRef)}
          placeholder="${this.placeholder}"
          class="search"
        />
      </div>
    `}setSearch(e){this._inputRef.value&&(this._prevValue=e,this._inputRef.value.value=e)}focusSearch(){requestAnimationFrame((()=>this._inputRef.value.focus()))}_handleInput(e){const t=e.target;this.handleChange(t.value)}_handleKeyup(e){const t=e.target;t.value!==this._prevValue&&this.handleChange(t.value)}handleChange(e){this._prevValue=e,this.dispatchEvent(new CustomEvent("change",{detail:{search:e},bubbles:!1,composed:!1}))}selectParent(e){this.dispatchEvent(new CustomEvent("setParent",{detail:{parent:e},bubbles:!0,composed:!0}))}firstUpdated(){this.focusSearch()}_close(){this.dispatchEvent(new CustomEvent("close",{bubbles:!0,composed:!0}))}};NinjaHeader.styles=css`
    :host {
      flex: 1;
      position: relative;
    }
    .search {
      padding: 1.25em;
      flex-grow: 1;
      flex-shrink: 0;
      margin: 0px;
      border: none;
      appearance: none;
      font-size: 1.125em;
      background: transparent;
      caret-color: var(--ninja-accent-color);
      color: #ffffff;
      outline: none;
      font-family: var(--ninja-font-family);
    }
    .search::placeholder {
      color: var(--ninja-placeholder-color);
    }
    .breadcrumb-list {
      padding: 1em 4em 0 1em;
      display: flex;
      flex-direction: row;
      align-items: stretch;
      justify-content: flex-start;
      flex: initial;
    }

    .breadcrumb {
      background: var(--ninja-secondary-background-color);
      text-align: center;
      line-height: 1.2em;
      border-radius: var(--ninja-key-border-radius);
      border: 0;
      cursor: pointer;
      padding: 0.1em 0.5em;
      color: var(--ninja-secondary-text-color);
      margin-right: 0.5em;
      outline: none;
      font-family: var(--ninja-font-family);
    }

    .search-wrapper {
      display: flex;
      border-bottom: var(--ninja-separate-border);
      background: #000000;
    }
  `,__decorate([property()],NinjaHeader.prototype,"placeholder",void 0),__decorate([property({type:Boolean})],NinjaHeader.prototype,"hideBreadcrumbs",void 0),__decorate([property()],NinjaHeader.prototype,"breadcrumbHome",void 0),__decorate([property({type:Array})],NinjaHeader.prototype,"breadcrumbs",void 0),NinjaHeader=__decorate([customElement("ninja-header")],NinjaHeader);export{NinjaHeader};