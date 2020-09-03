# Open Life Science

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

We are currently a team of 3 members who share a passion for Open Research and inclusiveness in Open Science.

As the graduates, mentors, and hosts of various Mozilla Open Leaders cohorts, we have gained expertise in the technical and culture track. Furthermore, we participate in a wide range of activities in different international communities of practice in the life sciences: ELIXIR (European bioinformatics network), Galaxy, The Carpentries, Software Sustainability Institute (SSI), Open Bioinformatics Foundation (OBF), and Mozilla.

## What do we need?

**You!** In whatever way you can help.

We need expertise in open-science, training, mentoring, communication. We'd love your feedback along the way, and of course.

## Get involved

If you think you can help in any of the areas listed above (and we bet you can)
or in any of the many areas that we haven't yet thought of (and here we're sure
you can) then please check out [our contributors' guidelines](CONTRIBUTING.md)
and our [roadmap](roadmap.md).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us
we ask that you follow our [code of conduct](CODE_OF_CONDUCT.md) in all
interactions both on and offline.

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
   git clone https://github.com/open-life-science/open-life-science.github.io.git
   ```

3. Navigate to the `open-life-science.github.io/` folder with `cd`
4. Set up the conda environment:

   ```
   make create-env
   ```

5. Install the project's dependencies:

   ```
   make install
   ```

6. Start the website:

   ```
   make serve
   ```

7. Open the website in your favorite browser at:
   [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

## Run the link checks

To avoid dead or wrong links, run the link checkers:

```
make check-html
```

## Create a new blog post

To create a new blog post:

1. Create a file in the folder `_posts` with a file named following the pattern `yyyy-mm-dd-name.md`
2. Add some metadata on the top of the file

    ```
    ---
    layout: post
    title: <title of the post>
    author: <github id of the author>
    image: images/yyyy-mm-dd-name.jpg
    ---
    ```

4. Add content of the post in the file in Markdown
3. Add images in `images/posts/`

## Add someone as mentor, expert or organizer

1. Open the `_data/people.yaml` file
2. Create a new entry there (using the GitHub id) following the alphabetical order
3. Fill in information using the tags:
    - `name`
    - `email`
    - `website`
    - `twitter`
    - `gitter`
    - `orcid`
    - `description`
4. Add if the person should be listed as mentor by adding `mentor: true`
5. Add if the person should be listed as expert by adding `expert: true`
6. Add if the person should be listed as organizer by adding `organizer: true`
    
## Add a partner/sponsor

1. Open the `_data/partners.yaml` file
2. Create a new entry there (using the name in lowercase, with spaces replaced by `-`) following an alphabetical order
3. Fill in information using the tags:
    - `name`
    - `website`
    - `description`
4. Add a logo (if possible) named as the entry in `images/partners` folder
5. Add the path to the logo in `_data/partners.yaml` using `logo` tag

## Update schedule for a cohort

The schedule displayed in a cohort page is automatically generated from a file `_data/ols-n-schedule.yaml`.

In this file, for each week, it is listed the timeframe and the different calls planned. For each call, several information are given:
- `type`: `Mentor-Mentee`, `Cohort`, `Mentors` or `Coworking`
- `duration` in min
- `title` 
- `date` in the format `Month Day, Year`
- `time` in the format '14:00' and for Berlin time
- `calendar-event`: link to calendar event
- `agenda`: tldr
- `notes`: link to notes
- `recording`: link to recording
- `content` with details of the content written in Markdown
- `before` with tasks to do before as a list written in Markdown
- `after` with tasks to do after as a list written in Markdown
- `resources`: list of useful resources with for each of them:
   - `type`: `slides`, `document`, or `external-link`
   - `title`
   - `speaker`: username in `_data/people.yaml`, if slides
   - `link`
