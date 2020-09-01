---
layout: post
title: Meet our second cohort of project leads and their mentors
authors: 
- bebatut
- malvikasharan
- yochannah
image: https://images.unsplash.com/photo-1489533119213-66a5cd877091?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1051&q=80
photos:
  name: Danielle MacInnes
  license: CC-BY
  url: https://unsplash.com/photos/IuLgi9PWETU
---

*We are excited to welcome this fantastic set of mentees who are not only located in different parts of the world, but also represent different identities and backgrounds, aim to address a wide range of questions in their field, and are motivated to bring a culture change in their areas. Many of them are long-standing Open Scientists who aim to use this opportunity to apply “Open by Design” principle in their projects through this program.*

{% assign people = site.data.people %}
{% assign projects = site.data.ols-2-projects %}
{% assign experts = site.data.ols-2-metadata.experts %}
{% assign cohort = 'ols-2' %}

<!-- extract previous participants and mentors and count them later among mentors -->
{% assign ols-1-projects = site.data.ols-1-projects %}
{% assign prev-participants = '' %}
{% assign prev-mentors = '' %}
{% for project in ols-1-projects %}
    {% for p in project.participants %}
        {% capture prev-participants %}{{ prev-participants }}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture prev-mentors %}{{ prev-mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}

{% assign all-participants = '' %}
{% assign all-p-countries = '' %}
{% assign all-mentors = '' %}
{% assign all-m-countries = '' %}
{% assign prev-part-count = 0 %}
{% assign prev-mentor-count = 0 %}

{% for project in projects %}

<!-- parse participants of the project -->
    {% for p in project.participants %}
<!-- for name and link to them -->
        {% capture all-participants %}{{ all-participants }}, [{{ people[p].first-name }} {{ people[p].last-name }}](/{{ cohort }}/projects-participants#{{ p }}){% endcapture %}
<!-- for list of countries -->
        {% capture all-p-countries %}{{ all-p-countries }}, {{ people[p].country }}{% endcapture %}
    {% endfor %}

<!-- parse mentors of the project -->
    {% for m in project.mentors %}
<!-- for name and link to them -->
        {% capture all-mentors %}{{ all-mentors }}, [{{ people[m].first-name }} {{ people[m].last-name }}](/{{ cohort }}#{{ m }}){% endcapture %}
<!-- for list of countries -->
        {% capture all-m-countries %}{{ all-m-countries }}, {{ people[m].country }}{% endcapture %}
<!-- add +1 if participant in previous cohort -->
        {% if prev-participants contains m %}
            {% assign prev-part-count = prev-part-count | plus: 1 %}
        {% endif %}
<!-- add +1 if mentor in previous cohort -->
        {% if prev-mentors contains m %}
            {% assign prev-mentor-count = prev-mentor-count | plus: 1 %}
        {% endif %}
    {% endfor %}
{% endfor %}

<!-- transform into lists -->
{% assign p-participants = all-participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign p-countries = all-p-countries | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign p-mentors = all-mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign m-countries = all-m-countries | remove_first: ', ' | split: ", " | uniq | sort %}

We are thrilled to announce that [{{ p-participants | size }} members](/{{ cohort }}/projects-participants/#participants), who are the project leads of [{{ projects | size }} diverse projects](/{{ cohort }}/projects-participants/#projects), have joined the second cohort of the Open Life Science mentoring program - OLS-2!

### Meet our mentees!

The mentees joining this program are {{ p-participants | join: ', ' }}. These individuals are based in {{ p-countries | size }} countries ({{ p-countries | join: ', ' }}) where they will be leading their respective projects. 

Their projects range from TODO.

### Meet our mentors!

Our mentees will be supported in this program by our mentors' community who have been paired based on the compatibility of expertise and interests of mentors with the requests and requirements of our mentees. Our mentors are Open Science champions with previous experiences in training and mentoring. They are currently working in different professions in data science, publishing, community building, software development, clinical studies, industries, scientific training and IT services.

We welcome our {{ p-mentors | size }} mentors, {{ p-mentors | join: ', ' }}, based in {{ m-countries | size }} countries ({{ m-countries | join: ', ' }}). {{ prev-part-count }} of them were participants and {{ prev-mentor-count }} mentors in the [previous cohort (OLS-1)](/ols-1). They will be supported by [{{ experts | size }} experts](/{{ cohort }}#experts).

We are extremely grateful to them for their support and contributions to OLS and their impactful work in other open communities. They are committed to supporting their mentees in this program to help create a more open and fair-research, knowledge-sharing and inclusive culture within life science.

### The Program

We will begin our program this week with a mentoring training call, and mentor-mentee introductions. Check out the complete schedule and plans for OLS-2 here: [{{ site.url }}/{{ cohort }}](/{{ cohort }}).

You can keep track of our program, the progress of our second cohort and future announcements by following our twitter profile [@{{ site.twitter }}](https://twitter.com/{{ site.twitter }}) or subscribe to [our announcements list](site.announcement_list).

We invite new contributions to the program as a [new issue on the GitHub repo]({{ site.github.repository_url }}/issues) or by [email to the team](mailto:{{ site.email }}).

Once again, let's welcome our mentors and mentees to this program!

## Project details ([click here for full description](/{{ cohort }}/projects-participants/))

| Project | Project leaders | Mentors |
|----------|-----------------------|------------|
{%- for project in projects %}
| [{{ project.name }}](/{{ cohort }}/projects-participants/#{{ project.name | downcase | remove: "(" | remove: ")" | remove: "@" | remove: ":" | remove: "," | replace: " ", "-" }}) | {% capture p-participants %} {% for p in project.participants -%}, [{{ people[p].first-name }} {{ people[p].last-name }}](/{{ cohort }}/projects-participants#{{ p }}){% endfor %} {% endcapture %} {{ p-participants | remove_first: ', ' }} | {% capture p-mentors %} {% for p in project.mentors -%}with [{{ people[p].first-name }} {{ people[p].last-name }}](/{{ cohort }}#{{ p }}) {% endfor %} {% endcapture %} {{ p-mentors | remove_first: 'with ' }} |
{%- endfor %}

We wish our cohort members all the best as they begin this journey with us.


