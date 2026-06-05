/**
 * Minified by jsDelivr using Terser v5.19.2.
 * Original file: /npm/@deepdub/ninja-keys@1.2.11/dist/base-styles.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
import{css}from"./lit/index.min.js";export const baseStyles=css`
  :host {
    --ninja-width: 640px;
    --ninja-backdrop-filter: none;
    --ninja-overflow-background: rgba(255, 255, 255, 0.5);
    --ninja-text-color: rgb(60, 65, 73);
    --ninja-font-size: 16px;
    --ninja-top: 20%;

    --ninja-key-border-radius: 0.25em;
    --ninja-accent-color: rgb(110, 94, 210);
    --ninja-secondary-background-color: rgb(239, 241, 244);
    --ninja-secondary-text-color: rgb(107, 111, 118);

    --ninja-selected-background: rgb(248, 249, 251);

    --ninja-icon-color: var(--ninja-secondary-text-color);
    --ninja-icon-size: 1.2em;
    --ninja-separate-border: 1px solid var(--ninja-secondary-background-color);

    --ninja-modal-background: #fff;
    --ninja-modal-shadow: rgb(0 0 0 / 50%) 0px 16px 70px;

    --ninja-actions-height: 300px;
    --ninja-group-text-color: rgb(144, 149, 157);

    --ninja-footer-background: rgba(242, 242, 242, 0.4);

    --ninja-placeholder-color: #8e8e8e;

    font-size: var(--ninja-font-size);

    --ninja-z-index: 1;
  }

  :host(.dark) {
    --ninja-backdrop-filter: none;
    --ninja-overflow-background: rgba(0, 0, 0, 0.7);
    --ninja-text-color: #7d7d7d;

    --ninja-modal-background: rgba(17, 17, 17, 0.85);
    --ninja-accent-color: rgb(110, 94, 210);
    --ninja-secondary-background-color: rgba(51, 51, 51, 0.44);
    --ninja-secondary-text-color: #888;

    --ninja-selected-text-color: #eaeaea;
    --ninja-selected-background: rgba(51, 51, 51, 0.44);

    --ninja-icon-color: var(--ninja-secondary-text-color);
    --ninja-separate-border: 1px solid var(--ninja-secondary-background-color);

    --ninja-modal-shadow: 0 16px 70px rgba(0, 0, 0, 0.2);

    --ninja-group-text-color: rgb(144, 149, 157);

    --ninja-footer-background: rgba(30, 30, 30, 85%);
  }

  .modal {
    display: none;
    position: fixed;
    z-index: var(--ninja-z-index);
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background: var(--ninja-overflow-background);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    -webkit-backdrop-filter: var(--ninja-backdrop-filter);
    backdrop-filter: var(--ninja-backdrop-filter);
    text-align: left;
    color: var(--ninja-text-color);
    font-family: var(--ninja-font-family);
  }
  .modal.visible {
    display: block;
  }

  .modal.isLoadingItems .loading-indicator {
    opacity: 1;
  }

  .modal-content {
    position: relative;
    top: var(--ninja-top);
    margin: auto;
    padding: 0;
    display: flex;
    flex-direction: column;
    flex-shrink: 1;
    -webkit-box-flex: 1;
    flex-grow: 1;
    min-width: 0px;
    will-change: transform;
    background: var(--global-bg-color);
    backdrop-filter: blur(20px);
    border-radius: 0.5em;
    box-shadow: var(--ninja-modal-shadow);
    max-width: var(--ninja-width);
    overflow: hidden;
  }

  .modal-body {
    background: var(--global-bg-color);
  }

  .loading-indicator {
    position: absolute;
    width: 100%;
    overflow: hidden;
    opacity: 0;
    height: 3px;
    z-index: 1;
    bottom: 34px;
  }

  .loading-indicator::before {
    content: '';
    position: absolute;
    inset: 0;
    background-color: var(--ninja-accent-color);
    opacity: 0.3;
  }

  @keyframes animation-bar1 {
    0% {
      left: -35%;
      right: 100%;
    }
    60% {
      left: 100%;
      right: -90%;
    }
    100% {
      left: 100%;
      right: -90%;
    }
  }

  .loading-indicator .bar1 {
    width: 100%;
    position: absolute;
    left: 0;
    bottom: 0;
    top: 0;
    -webkit-transition: -webkit-transform 0.2s linear;
    transition: transform 0.2s linear;
    transform-origin: left;
    background-color: var(--ninja-accent-color);
    width: auto;
    -webkit-animation: animation-bar1 2.1s cubic-bezier(0.65, 0.815, 0.735, 0.395) infinite;
    animation: animation-bar1 2.1s cubic-bezier(0.65, 0.815, 0.735, 0.395) infinite;
  }

  @keyframes animation-bar2 {
    0% {
      left: -200%;
      right: 100%;
    }
    60% {
      left: 107%;
      right: -8%;
    }
    100% {
      left: 107%;
      right: -8%;
    }
  }

  .loading-indicator .bar2 {
    width: 100%;
    position: absolute;
    left: 0;
    bottom: 0;
    top: 0;
    -webkit-transition: -webkit-transform 0.2s linear;
    transition: transform 0.2s linear;
    transform-origin: left;
    background-color: var(--ninja-accent-color);
    width: auto;
    -webkit-animation: animation-bar2 2.1s cubic-bezier(0.165, 0.84, 0.44, 1) 1.15s infinite;
    animation: animation-bar2 2.1s cubic-bezier(0.165, 0.84, 0.44, 1) 1.15s infinite;
  }

  .bump {
    animation: zoom-in-zoom-out 0.2s ease;
  }

  @keyframes zoom-in-zoom-out {
    0% {
      transform: scale(0.99);
    }
    50% {
      transform: scale(1.01, 1.01);
    }
    100% {
      transform: scale(1, 1);
    }
  }

  .title {
    font-size: 0.75rem;
    padding: 0.25rem 0.25rem;
    text-align: right;
    position: absolute;
    right: 0px;
    width: 100%;
  }

  .title.separator {
    border-top: 1px solid rgb(51, 51, 51);
  }

  .ninja-github {
    color: var(--ninja-keys-text-color);
    font-weight: normal;
    text-decoration: none;
  }

  .actions-list {
    max-height: var(--ninja-actions-height);
    overflow: auto;
    position: relative;
    margin: 0;
    padding: 0.5em 0;
    list-style: none;
    scroll-behavior: auto;
  }

  .group-header {
    height: 1.375em;
    line-height: 1.375em;
    padding-left: 1.25em;
    padding-top: 0.5em;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    font-size: 0.75em;
    line-height: 1em;
    color: var(--ninja-group-text-color);
    margin: 1px 0;
  }

  .modal-footer {
    padding: 0.5em 1em;
    display: flex;
    /* font-size: 0.75em; */
    border-top: var(--ninja-separate-border);
    color: var(--ninja-secondary-text-color);
  }

  .modal-footer .help {
    display: flex;
    margin-right: 1em;
    align-items: center;
    font-size: 0.75em;
  }

  .ninja-examplekey {
    background: var(--ninja-secondary-background-color);
    padding: 0.06em 0.25em;
    border-radius: var(--ninja-key-border-radius);
    color: var(--ninja-secondary-text-color);
    width: 1em;
    height: 1em;
    margin-right: 0.5em;
    font-size: 1.25em;
    fill: currentColor;
  }
  .ninja-examplekey.esc {
    width: auto;
    height: auto;
    font-size: 1.1em;
  }
  .ninja-examplekey.backspace {
    opacity: 0.7;
  }
`;