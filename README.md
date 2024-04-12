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
you can), then please check out [our contributors' guidelines](CONTRIBUTING.md)
and our [roadmap](roadmap.md).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us,
we ask that you follow our [code of conduct](CODE_OF_CONDUCT.md) in all
interactions, both on and offline.


## How can I generate the website and contribute using GitPod?

[GitPod](https://www.gitpod.io/) is an open-source developer platform for remote development. You can use it to generate the website without installing anything on your computer.

1. Setting up GitPod
   1. Create a fork of the OLS GitHub repository (to do only 1 time)
      1. Go on the GitHub repository: [github.com/open-life-science/open-life-science.github.io](https://github.com/open-life-science/open-life-science.github.io)
      2. Click on the Fork button (top-right corner of the page)
   2. Open your browser and navigate to [gitpod.io](https://www.gitpod.io/)
   3. Log in with GitHub
   4. Copy the link to your fork of the GTN, e.g. https://github.com/bebatut/open-life-science.github.io

      Gitpod will now configure your environment. This may take some time.

      Once the setup is finished, you should see a page with:
      - On the Left: All the files in the OLS repository.
      - Top: The main window where you can view and edit files.
      - Bottom: Terminal window, where you can type commands (e.g. to build the website preview) and read output and error messages.

2. Build and preview the OLS website
   1. Type the following command `make serve-gitpod` in the terminal window (bottom)
   2. Click on the link in the terminal to see the OLS in full-screen: `Server address: http://127.0.0.1:4000`

3. Make and view changes
   1. Open and/or create files via the file browser on the left
   2. Make and save the changes in the files
   3. Reload the preview page to view the changes

4. Saving changes back to GitHub
   1. Option 1: via the terminal
      1. Create a new branch with `git checkout`
      2. Commit your changes with `git add` and `git commit`
      3. Push changes with `git push origin`
   2. Option 2: via the web interface
      1. Create a new branch
         1. Click on the bottom-left on the branch logo button on the bottom of the page with the current branch (probably "main")
         2. Give your new branch a name (at top of window)
         3. Choose "+ Create new branch..." from the dropdown
      2. Commit changes
         1. Click on the "Source Control" tab button (branch) on the left menu to show changed files.
         2. Click on the "+" icon next to the edited files to stage changes (stage changes button).
         3. Hit the checkmark icon at the top to commit the changes.
         4. Enter a commit message (top of window) - Publish changes.
         5. Click the cloud button at bottom left to publish your changes (publish changes button).

            Changes are now saved to your fork, and you can make a PR via the GitHub interface
   
## How can I generate the website locally?

You need a `ruby` environment (version >= 2.4). Either you have it installed and
you know how to install [Bundler](https://bundler.io/) and
[Jekyll](https://jekyllrb.com/) and then run Jekyll, or you use
(mini-)[conda](https://conda.io/docs/index.html), a package management system
that can install all these tools for you. You can install it by following the
instructions on this page: https://conda.io/docs/user-guide/install/index.html

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

## Add people or organization, update schedule, etc

Our knowledge about our different programs, our community, etc is managed via this repository, [CiviCRM](https://civicrm.org/), and documents stored in Google Drive. It is then added to the website as explained in our [Knowledge Management System documentation](https://we-are-ols.org/knowledge_management.html)

## Adding Events to the Website
This page is where we detail events, either organised by OLS or where we are invited to speak at.
To help you contribute events to this website, we would like to offer a step-by-step guide.
The process involves creating a new file and filling in some details. 

**What you'll need:**

- A text editor (like Notepad or VSCode).

**Steps to add an event:**

## License

The content of this website are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0).

The code behind the infrastructure is licensed under the [MIT License](LICENSE.md)