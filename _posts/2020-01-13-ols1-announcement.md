---
layout: post
title: Meet our first cohort of project leads and their mentors
authors: 
- bebatut
- malvikasharan
- yochannah
image: https://images.unsplash.com/photo-1533745848184-3db07256e163?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2389&q=80
---

{% assign mentors = site.data.people %}
{% assign participants = site.data.ols-1-participants %}
{% assign projects = site.data.ols-1-projects %}

We are thrilled to announce that [{{ participants | size }} members](/ols-1/projects-participants/#participants), who are the project leads of [{{ projects | size }} diverse projects](/ols-1/projects-participants/#projects), have joined the first cohort of the Open Life Science mentoring program - OLS-1!

### Meet our mentees!

{% capture p-participants %}
{% for p in participants %}, [{{ p[1].name }}](/ols-1/projects-participants/#{{ p[0] }}){% endfor %}
{% endcapture %} 

The mentees joining this program are {{ p-participants | split: " , " | uniq | sort | join: ", " | remove_first: ", " }}. These individuals are based in different African, Asian, European, Latin American, North American, and Russian countries where they will be leading their respective projects. 

We are excited to welcome this fantastic set of mentees who are not only located in different parts of the world, but also represent different identities and backgrounds, aim to address a wide range of questions in their field, and are motivated to bring a culture change in their areas. Many of them are long-standing Open Scientists who aim to use this opportunity to apply “Open by Design” principle in their projects through this program.

Their project range from the ideas of creating new local communities, promoting best practices in open science in their existing communities, developing open software, enhancing and promoting science communication, learning community skills, improving documentation for sustainability, building open education resources, or providing support to open practitioners in their network. One member, Renato Alves, is a mentee of a project but is also mentoring one of the other projects. The project of Lena Karvovskaya was transferred from the eLife Innovation Program as it fits better with the goal and scope of the OLS program. 

### Meet our mentors!

{% capture p-mentors %}
{% for p in projects %} {% for m in p.mentors %}, [{{ mentors[m].name }}](/about#{{ m }}){% endfor %} {%- endfor %}
{% endcapture %}

Our mentees will be supported in this program by our mentors' community who have been paired based on the compatibility of expertise and interests of mentors with the requests and requirements of our mentees. Our mentors are Open Science champions with previous experiences in training and mentoring. They are currently working in different professions in data science, publishing, community building, software development, clinical studies, industries, scientific training and IT services.

We welcome our mentors, {{ p-mentors | split: " , " | uniq | sort | join: ", " | remove_first: ", " }}. Yo and Malvika will also mentor one project each in this cohort. We are extremely grateful to them for their support and contributions to OLS and their impactful work in other open communities. They are committed to supporting their mentees in this program to help create a more open and fair-research and knowledge-sharing culture within life science.

### The Program

We will begin our program this week with a mentoring training call, and mentor-mentee introductions. Check out the complete schedule and plans for OLS-1 here: [{{ site.url }}/ols-1](/ols-1).

You can keep track of our program, the progress of our first cohort and future announcements by following our twitter profile [@{{ site.twitter }}](https://twitter.com/{{ site.twitter }}) or joining our [community Gitter channel](https://gitter.im/{{ site.gitter }}).

We invite new contributions to the program as a [new issue on the GitHub repo]({{ site.github.repository_url }}/issues) or by [email to the team](mailto:{{ site.email }}).

Once again, let's welcome our mentors and mentees to this program!

## Project details ([click here for full description](/ols-1/projects-participants/))

| Project | Project leaders | Mentor (with secondary mentors if any) |
|----------|-----------------------|------------|
{%- for project in projects %}
| [{{ project.name }}](/ols-1/projects-participants/#{{ project.name | downcase | remove: "(" | remove: ")" | remove: "@" | remove: ":" | remove: "," | replace: " ", "-" }}) | {% capture p-participants %} {% for p in project.participants -%}, [{{ participants[p].name }}](/ols-1/projects-participants/#{{ p }}){% endfor %} {% endcapture %} {{ p-participants | remove_first: ', ' }} | {% capture p-mentors %} {% for p in project.mentors -%}with [{{ mentors[p].name }}](/about#{{ p }}) {% endfor %} {% endcapture %} {{ p-mentors | remove_first: 'with ' }} |
{%- endfor %}

We wish our cohort members all the best as they begin this journey with us.


