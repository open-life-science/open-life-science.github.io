# OLS

***Sharing. Connecting. Empowering***

Find all the information about our community and projects at
[https://open-life-science.github.io](https://open-life-science.github.io).

## Welcome!

First and foremost, Welcome! 🎉 Willkommen! 🎊 Bienvenue! 🙏 सुस्वागत (Suswagat)🎈🎈🎈

This document (the `README` file) is a hub to give you some information about the
project. Jump straight to one of the sections below, or just scroll down to find
out more.

## What are we doing?

We are working to create a mentoring program for individuals interested in becoming
ambassadors for Open Science practice, training and education in their communities.

Our outcome is to support early stage researchers and young leaders by sharing
Open Science skills, connecting them to others in the community,
and empowering them to become ambassadors for Open Science practice,
training and education in their communities.

## Who are we?

We are currently a team of people who share a passion for Open Research and inclusiveness in Open Science. Please read more on [our website](https://openlifesci.org/community).

## What do we need?

**You!** In whatever way you can help.

We need expertise in open-science, training, mentoring, communication. We'd love your feedback along the way, of course.

## Get involved

If you think you can help in any of the areas listed above (and we bet you can)
or in any of the many areas that we haven't yet thought of (and here we're sure
you can), then please check out [our contributors' guidelines](CONTRIBUTING.md).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us,
we ask that you follow our [code of conduct](CODE_OF_CONDUCT.md) in all
interactions, both on and offline.


## How can I generate the website and contribute using GitHub Codespaces?

[GitHub Codespaces](https://github.com/features/codespaces) is a cloud development environment integrated with GitHub. You can use it to generate the website without installing anything on your computer.

1. Setting up a Codespace
   1. Create a fork of the OLS GitHub repository (to do only once)
      1. Go to the GitHub repository: [github.com/open-life-science/open-life-science.github.io](https://github.com/open-life-science/open-life-science.github.io)
      2. Click on the Fork button (top-right corner of the page)

      If you already have a fork, make sure to sync it first: go to your fork on GitHub and click "Sync fork" to get the latest changes from the main repository.

   2. Open your fork on GitHub
   3. Click the green "Code" button, then select the "Codespaces" tab
   4. Click "Create codespace on main" (or your preferred branch)

      GitHub will now configure your working space. This may take some time.

      Once the setup is finished, you should see a VS Code-like interface with:
      - On the Left: All the files in the OLS repository
      - Top: The main window where you can view and edit files
      - Bottom: Terminal window, where you can type commands (e.g. to build the website preview) and read output and error messages

2. Build and preview the OLS website
   1. Set up the conda environment: `make create-env`
   2. Install the project's dependencies: `make install-codespaces`
   3. Start the website: `make serve-codespaces`
   4. A popup will appear offering to open the preview in your browser. Click "Open in Browser"
      (Or click on the "Ports" tab and open the forwarded port 4000)

3. Make and view changes
   1. Open and/or create files via the file browser on the left
   2. Make and save the changes in the files
   3. Reload the preview page to view the changes

4. Saving changes back to GitHub
   1. Option 1: via the terminal
      1. Create a new branch with `git checkout -b your-branch-name` or `git switch -c your-branch-name`
      2. Commit your changes with `git add .` and `git commit -m "Your message"`
      3. Push changes with `git push origin your-branch-name`
   2. Option 2: via the web interface
      1. Create a new branch
         1. Click on the branch name at the bottom-left of the window
         2. Choose "+ Create new branch..." from the dropdown
         3. Give your new branch a name (at top of window)

      2. Commit changes
         1. Click on the "Source Control" tab (branch icon) on the left menu to show changed files
         2. Click on the "+" icon next to the edited files to stage changes
         3. Enter a commit message in the text box at the top
         4. Click the checkmark icon to commit the changes
         5. Click "Publish Branch" to push your changes

      Changes are now saved to your fork, and you can make a PR via the GitHub interface

**Note:** By default, Codespaces are automatically deleted after 30 days of inactivity. To prevent deletion, simply open the codespace again to reset the timer.
   
## How can I generate the website locally?

You need a `ruby` environment (version >= 3.0; last tested on 3.4). Either you have it installed and
you know how to install [Bundler](https://bundler.io/) and
[Jekyll](https://jekyllrb.com/) and then run Jekyll, or you use
(mini-)[conda](https://conda.io/docs/index.html), a package management system
that can install all these tools for you. You can install it by following the
instructions on this page: https://conda.io/docs/user-guide/install/index.html

**Windows users:** The setup commands use bash scripts and Unix tools like Make. We suggest you to use [WSL (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install) to run the commands below. Once WSL is installed, clone the repository inside the WSL filesystem (e.g., `~/open-life-science.github.io`) for best performance.

In the sequel, we assume you use miniconda.

1. Open a terminal
2. Clone this GitHub repository:

   ```
   $ git clone https://github.com/open-life-science/open-life-science.github.io.git
   ```

3. Navigate to the `open-life-science.github.io/` folder with the `cd` command
4. Set up the conda environment:

   ```
   $ make create-env
   ```

5. Install the project's dependencies:

   ```
   $ make install
   ```

6. Start the website:

   ```
   $ make serve
   ```

7. Open the website in your favorite browser at:
   [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

## Run the link checks

To avoid dead or wrong links, run the link checkers:

```
$ make check-html
```

## Add people or organization, update schedule, add post or event etc

Our knowledge about our different programs, our community, etc is managed via this repository, [CiviCRM](https://civicrm.org/), and documents stored in Google Drive. It is then added to the website as explained in our [Knowledge Management System documentation](https://we-are-ols.org/knowledge_management.html)

## **Deploy Preview for Pull Requests**  

This repository uses GitHub Actions to generate a **preview deployment** of pull requests from branches in this repository.
This allows contributors to see changes live before merging them into the `main` branch.  

### **How It Works**  
1. When a pull request is created against `main`, the GitHub Actions workflow (`.github/workflows/deploy-preview.yml`) runs automatically.  
2. The workflow:  
   - Checks out the repository code.  
   - Sets up Ruby and installs dependencies.  
   - Builds the Jekyll site.  
   - Deploys the built site to a separate repository (`ols-site-preview`) on the `gh-pages` branch.  
   - Comments on the pull request with a preview link in the format:  
     ```
     🎉 A preview of this PR is available at: https://we-are-ols.org/ols-site-preview
     ```  
3. Contributors can visit this link to view the changes live.  

### **Why This Setup?**  
- Allows easy previewing of pull request changes without merging.  
- Uses GitHub Pages for hosting, avoiding the need for third-party services.  
- Automates the process via GitHub Actions to ensure consistency.  
- The preview deploys to `ols-site-preview`, keeping the main repo clean.  

### **Usage Notes**  
- The preview is only available while the PR is open. Once merged or closed, the preview will be removed.  
- Ensure that the `PR_PREVIEW_TOKEN` secret is correctly set up in the repository settings for authentication.  

### 🚨 **Access Restrictions**  
This workflow uses a Personal Access Token (PAT) (`PR_PREVIEW_TOKEN`) to deploy previews. 
Due to GitHub security restrictions, contributors who are not part of the Open Life Science organisation may not have their PR previews generated automatically.

- PRs from organisation members working on branches **in this repository** will automatically receive a preview link.
- PRs from forks (even from organisation members) will not generate previews automatically.

## License

The content of this website are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0).

The code behind the infrastructure is licensed under the [MIT License](LICENSE.md)
