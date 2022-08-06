[![GitHub Repo stars](https://img.shields.io/github/stars/mshuber1981/github-react-portfolio-template?color=%2361dbfb&style=for-the-badge&logo=github)](https://github.com/mshuber1981/github-react-portfolio-template/stargazers/) [![GitHub Repo Forks](https://img.shields.io/github/forks/mshuber1981/github-react-portfolio-template?color=%2361dbfb&style=for-the-badge&logo=github&label=Forks)](https://github.com/mshuber1981/github-react-portfolio-template/network/members)

# A React Portfolio Template for GitHub

A performant, accessible, progressive React portfolio template that uses the [GitHub REST API](https://docs.github.com/en/free-pro-team@latest/rest).

Add your GitHub username once and all of your info will automatically be updated. Deploy to GitHub pages in a few simple steps.

[Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)

![Page Speed](/README_images/speed.png)

### <a href="https://mshuber1981.github.io/github-react-portfolio-template/#/">LIVE DEMO</a>

![Project Preview](/README_images/preview.png)

## Getting Started

1. [Create a repository from this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
1. [Clone your repostiory](https://developers.google.com/speed/pagespeed/insights/)
1. Make sure [Node](https://nodejs.org/en/) is installed
1. Open your project and install the dependencies

   - ```bash
     npm install
     ```

1. Navigate to the src directory and open data.js
1. Add your GitHub username ([data.js](https://github.com/mshuber1981/github-react-portfolio-template/blob/0133fcc02ab048fefcf73825d02385ffe27c3721/src/data.js#L23) lines 23-27)

   - ```javascript
     /* START HERE
      ************************************************************** 
      Add your GitHub username (string - "YourUsername") below.
     */
     export const githubUsername = "Your GitHub username here";
     ```

1. Start the development server to view the results

   - ```bash
     npm start
     ```

## Updating the Projects section

![Projects Preview](/README_images/projects.png)

1. Follow the instructions to update the filteredProjects array ([data.js](https://github.com/mshuber1981/github-react-portfolio-template/blob/0133fcc02ab048fefcf73825d02385ffe27c3721/src/data.js#L94) lines 94-98)

   - ```javascript
     /* Projects
      ************************************************************** 
      List the repo names (string - "your-repo-name") you want to include (they will be sorted alphabetically). If empty, only the first 3 will be included.
     */
     export const filteredProjects = ["example-1", "example-2", "example-3"];
     ```

1. Import the projects images you want to use ([data.js](https://github.com/mshuber1981/github-react-portfolio-template/blob/0133fcc02ab048fefcf73825d02385ffe27c3721/src/data.js#L13) lines 13-14) or the default image will be applied

   - ```javascript
     // Projects Images (add your images to the images directory and import below)
     import Logo from "./images/logo.svg";
     ```

1. Follow the instructions to update the projectData array ([data.js](https://github.com/mshuber1981/github-react-portfolio-template/blob/0133fcc02ab048fefcf73825d02385ffe27c3721/src/data.js#L100) lines 100-106)

   - ```javascript
     // Replace the defualt GitHub image for matching repos below (images imported above - lines 13-14)
     export const projectCardImages = [
       {
         name: "example-1",
         image: Logo,
       },
     ];
     ```

## Updating the Contact section

![Contact Preview](/README_images/contact.png)

1. The contact form uses [Formspree](https://formspree.io/), create an account and add your endpoint URL ([data.js](https://github.com/mshuber1981/github-react-portfolio-template/blob/0133fcc02ab048fefcf73825d02385ffe27c3721/src/data.js#L108) lines 108-113)

   - ```javascript
     /* Contact Info
      ************************************************************** 
      Add your formspree endpoint below.
      https://formspree.io/
     */
     export const formspreeUrl = "https://formspree.io/f/YourEndpoint";
     ```

## Deploy

A helpful guide for Create React App deployments with GitHub Pages can be found [here](https://create-react-app.dev/docs/deployment#github-pages).

1. Update the homepage value ([package.json](https://github.com/mshuber1981/github-react-portfolio-template/blob/0133fcc02ab048fefcf73825d02385ffe27c3721/package.json#L3) line 3)

   - ```javascript
     "homepage": "https://YourUsername.github.io/your-app/",
     ```

1. Run the deploy command

   - ```bash
     npm run deploy
     ```

## Customization Options

Checkout the [Wiki](https://github.com/mshuber1981/github-react-portfolio-template/wiki) for additional customization options:

- [Updating the Hero images](https://github.com/mshuber1981/github-react-portfolio-template/wiki/Updating-the-Hero-images)
- [Add a custom Blog icon](https://github.com/mshuber1981/github-react-portfolio-template/wiki/Updating-the-Hero-images#add-a-custom-blog-icon)
- [Updating the About Me section](https://github.com/mshuber1981/github-react-portfolio-template/wiki/Updating-the-About-Me-section)
- [Updating the Skills section](https://github.com/mshuber1981/github-react-portfolio-template/wiki/Updating-the-Skills-section)
- [Add a link to your resume](https://github.com/mshuber1981/github-react-portfolio-template/wiki/Updating-the-Skills-section#add-a-link-to-your-resume)

<br />

[Back to top :top:](#a-react-portfolio-template-for-github)

## License

[MIT](https://choosealicense.com/licenses/mit/)
