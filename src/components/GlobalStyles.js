import { createGlobalStyle } from "styled-components";

const GlobalStyles = createGlobalStyle`
/*
=============== 
Variables
===============
*/
:root {
  --primary-light: #b0edfd;
  /* Primary Color */
  --primary: #61DBFB;
  --primary-dark: #316e7e;
  --border: 1px solid #61DBFB;
  --transition: all 0.3s linear;
  --nav-height: 61px;
  --min-footer-height: 11vh;
}

/*
=============== 
Global Styles
===============
*/
body {
  background: ${({ theme }) => theme.background};
  color: ${({ theme }) => theme.color};
}

a:hover {
  cursor: pointer;
}

.navbar {
  border-bottom: var(--border);
}

.link-icons {
  line-height: 0;
  font-size: 2.25rem;
  transition: var(--transition);
  color: ${({ theme }) => theme.color};

  &:hover {
        color: var(--primary);
      }
}

img:not(.nav-logo) {
  width: 100%;
  height: auto;
  display: block;
}

.section {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: var(--nav-height) 0;

}

.title {
    font-family: "Permanent Marker";
}

.card {
  height: 30rem;
  border: var(--border);
  transition: all .2s ease-in-out;
  &:hover {
    transform: scale(1.03);
  }

  .card-img-top {
    height: 50%;
    object-fit: contain;
  }
}

@media screen and (min-width: 800px) {
  .link-icons {
    font-size: 3rem;
  }
  .form-group {
      max-width: 750px;
    }
}

 @media screen and (min-width: 1367px) {
  .link-icons:hover {
    color: var(--primary);
  }
  }
`;

export default GlobalStyles;
