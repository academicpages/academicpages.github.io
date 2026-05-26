# Deployment Guide

This guide is designed for beginners. You don't need complex configurations to deploy your website.

## Option 1: GitHub Pages

1.  **Build your project**
    
    First, ensure you have the correct Node.js version installed.
    *   **Download & Install**: Go to [https://nodejs.org/en/download](https://nodejs.org/en/download) and install Node.js manually.
    *   Better not to use the system's default Node.js as it might be outdated.

    Open your terminal in the project folder and run:
    
    ```bash
    npm install
    npm run build
    ```
    This will create a folder named `out` in your project directory. This folder contains your generated website.
    
2.  **Create a GitHub Repository**
    *   Log in to GitHub.
    *   Create a new **Public** repository.
    *   Name it `username.github.io` (replace `username` with your actual GitHub username).

3.  **Upload Files**
  
    *   Upload **all the files inside the `out` folder** to your new repository.
    *   You can do this by clicking "Upload files" on the GitHub repository page and dragging everything from the `out` folder.
    *   *Alternatively, if you know Git, you can push the contents of `out` to the repository.*
    
4.  **Add .nojekyll file**
  
    *   In your GitHub repository, click "Add file" -> "Create new file".
    *   Name the file `.nojekyll` (start with a dot, all lowercase).
    *   Leave the content empty and click "Commit changes".
    *   *This is important! It tells GitHub to allow folders starting with `_` (like `_next`).*
    
5.  **Configure Pages**
    *   Go to your repository **Settings**.
    *   Click on **Pages** in the left sidebar.
    *   Under **Build and deployment**, ensure "Deploy from a branch" is selected.
    *   Select your branch (usually `main`) and click **Save**.

6.  **Done!**
    Visit `https://username.github.io` to see your website.

### (Optional) Deploy Automatically with GitHub Actions

PRISM also supports **automatic deployment to GitHub Pages** using GitHub Actions.  
This method is recommended if you want your site to update automatically whenever you push changes.

#### How to enable

This repository includes an optional workflow located at:

```
.github/workflows/deploy.yml
```

For template users, GitHub disables workflows by default.  
To enable deployment:

1. Go to **Settings > Pages**, and under **Build and deployment > Source**, choose **GitHub Actions**.
2. Go to **Actions** Tab, and select **"Deploy PRISM to GitHub Pages"**.
3. Click **"Enable workflow"**.
4. Run manually using **Run workflow**.
5. (Optional) To enable automatic deployment on push:  
   Edit `.github/workflows/deploy.yml` and uncomment:

   ```yaml
   on:
     push:
       branches:
         - main
         - ci
   ```

Once enabled, GitHub Actions will:

- Build your site (`npm install && npm run build`)
- Export static files into `out/`
- Deploy automatically to GitHub Pages

Your site will be available at `https://<username>.github.io`

If you are using a repository other than `username.github.io`, your site will be at `https://<username>.github.io/<repository>/`.

In this case, make sure to set the `basePath` and `assetPrefix` in `next.config.ts` accordingly to add path prefixes to your assets:

```
// next.config.ts
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'export',
  trailingSlash: true,

  // Add these two lines
  basePath: "/my-repo",
  assetPrefix: "/my-repo",

  images: {
    unoptimized: true,
  },
  /* config options here */
  webpack: (config) => {
    config.module.rules.push({
      test: /\.bib$/,
      type: 'asset/source',
    });
    return config;
  },
};

export default nextConfig;
```



---

## Option 2: Cloudflare Pages

1.  **Build your project**
    Run `npm run build` to generate the `out` folder.

2.  **Create Application**
    *   Log in to the [Cloudflare Dashboard](https://dash.cloudflare.com/).
    *   Go to **Workers & Pages** -> **Create Application**.
    *   Select the **Pages** tab.
    *   Click **Drag and drop your files**.

3.  **Upload**
    *   Enter a **Project name** (this will be your subdomain, e.g., `my-site`).
    *   Click **Create project**.
    *   Drag and drop your `out` folder (or a zip archive of it) into the upload area.
    *   Click **Deploy**.

4.  **Done!**
    You will see your site live at `https://<project-name>.pages.dev`.
