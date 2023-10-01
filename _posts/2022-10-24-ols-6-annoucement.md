---
layout: post
title: Meet our 6th cohort of project leads and their mentors
authors:
- bebatut
- malvikasharan
- yochannah
- emmyft
- pazbc
image: https://images.unsplash.com/photo-1562654501-9a587e8638d8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1631&q=80
photos:
  name: Arisa Chattasa
  license: CC-BY
  url: https://unsplash.com/photos/BoQ3FmPQgZI
---

*We are excited to kick-off the 6th round of Open Life Science with another incredible cohort of mentors, mentees, and experts. We are honored to bring together members of diverse identities and backgrounds who represent expertise from different domains of research, who are working to address a wide range of relevant questions in their field and are motivated to bring a culture change in their areas. Many of them are long-standing Open Scientists who aim to use this opportunity to apply open science and community-based principles in their projects through this program.*

{% include _includes/announcement-blog-metadata.html cohort='ols-6' %}

We are thrilled to announce that [{{ p-participants | size }} members]({% link openseeds/ols-6/projects-participants.md %}#participants), who are the project leads of [{{ projects | size }} diverse projects]({% link openseeds/ols-6/projects-participants.md %}#projects), have joined the fourth cohort of the Open Life Science mentoring program - OLS-6!

### Meet our mentees!

The mentees joining this program are {{ p-participants | join: ', ' }}. These individuals are based in {{ p-countries | size }} countries ({{ p-countries | join: ', ' }}) where they will be leading their respective projects.

Topics for their projects include {{ keywords | join: ', ' }}.

### Meet our mentors!

Our project leads (aka mentees) have been paired with 1 or 2 mentors based on their specific requirements of expertise and interests along with time zones and language preferences. Our mentors are Open Science champions with previous experiences in training, mentoring, computing, and community skills. They are currently working in different professions in data science, education, citizen science, publishing, community building, software development, clinical studies, industries, scientific training, policymaking, IT services, and so on.

Additionally, we have an incredible experts' community who will be delivering specialised talks during the cohort calls and will be available for our project leads for expert consultations upon request.

We welcome our {{ p-mentors | size }} mentors, {{ p-mentors | join: ', ' }}, based in {{ m-countries | size }} countries ({{ m-countries | join: ', ' }}). {{ prev-part-count }} of them were participants and {{ prev-mentor-count }} mentors in the [previous cohort (OLS-5)]({% link openseeds/ols-5/index.md %}). They will be supported by [{{ experts | size }} experts]({% link openseeds/{{ cohort }}/index.md %}#experts).

We are extremely grateful to them for their support and contributions to OLS and their impactful work in other open communities. They are committed to supporting their mentees in this program to help create a more open and fair-research, knowledge-sharing and inclusive culture within life science and beyond.

### The Program

We begin our program this week with a mentoring training call and mentor-mentee introductions. Check out the complete schedule and plans for OLS-6 here: [{{ site.url }}/{{ cohort }}]({% link openseeds/{{ cohort }}/index.md %}).

You can keep track of our program, the progress of our second cohort and future announcements by following our twitter profile [@{{ site.twitter }}](https://twitter.com/{{ site.twitter }}) or subscribe to [our announcements list]({{ site.announcement_list }}).

We invite new contributions to the program as a [new issue on the GitHub repo]({{ site.github.repository_url }}/issues) or by [email to the team](mailto:{{ site.email }}).

Once again, let's welcome our mentors, mentees and experts to this program!

## Project details ([click here for full description]({% link openseeds/ols-6/projects-participants.md %}#projects))

| Project | Project leaders | Mentors |
|----------|-----------------------|------------|
{%- for project in projects %}
| [{{ project.name }}]({% link openseeds/{{ cohort }}/projects-participants.md %}#{{ project.name | slugify }}) | {% capture p-participants %} {% for p in project.participants -%}, [{{ people[p].first-name }} {{ people[p].last-name }}]({% link openseeds/{{ cohort }}/projects-participants.md %}#{{ p }}){% endfor %} {% endcapture %} {{ p-participants | remove_first: ', ' }} | {% capture p-mentors %} {% for p in project.mentors -%}, [{{ people[p].first-name }} {{ people[p].last-name }}]({% link openseeds/{{ cohort }}/index.md %}#{{ p }}){% endfor %} {% endcapture %} {{ p-mentors | remove_first: ', ' }} |
{%- endfor %}

{{ project.name | slugify  }}

We wish our cohort members all the best as they begin this journey with us.
