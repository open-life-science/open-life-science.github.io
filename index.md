---
layout: default
title: OLS
description: A mentoring & training program for Open Science ambassadors
image: /images/index.jpg
photos:
  name: Bérénice Batut
  license: CC BY-SA 4.0
  url: https://flic.kr/p/2gHMJah
---

The **OLS** program is for people interested in **applying open principles** in their work and **becoming Open Science ambassadors** in their communities.

# About

This is a **16-week long personal mentorship and cohort-based training**, where participants (organisers, hosts, mentors and project leads/mentees) of this program will:
- **share** their expertise and gain knowledge essential to create, lead, and sustain an Open Science project
- **connect** with members across different projects, communities, backgrounds, and identities
- **empower** each other to become effective Open Science ambassadors in their communities

# Applications

<!--[Apply via Open Review](https://openreview.net/group?id=openlifesci.org/Open_Life_Science/2022/Cohort_6){:.button .is-link .is-fullwidth}

*Please register on Open Review before July 1, 2022 to allow activation of your Open Review profile as described in the [OLS-6 application guidelines and templates](https://github.com/open-life-science/application-forms).*-->

OLS-6 runs from September 2022 to January 2023. Applications for OLS-7 will open in end 2022. [Sign up to our low-traffic news list]({{ site.announcement_list }}) to hear when next cohort applications open.

## Timeline

{% assign schedule = site.data.ols-6-schedule %}
{% include _includes/timeline.md %}

Have a question or need any support to join this cohort?
We are here to help - feel free to email [{{ site.email|replace:'@','[at]' }}](mailto:{{ site.email }}), chat in real-time on [Gitter](https://gitter.im/{{ site.gitter }}) or connect on Twitter [@{{ site.twitter }}](https://twitter.com/{{ site.twitter }}).

## Projects

<!-- OLS-1 -->
{% assign ols-1-projects = site.data.ols-1-projects %}
{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in ols-1-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }} {% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture all-mentors %}{{ all-mentors }}, {{ m }} {% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-1-participants = all-participants | remove_first: ', ' | split: " , " | uniq | sort %}
{% assign ols-1-mentors = all-mentors | remove_first: ', ' | split: " , " | uniq | sort %}

<!-- OLS-2 -->
{% assign ols-2-projects = site.data.ols-2-projects %}
{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in ols-2-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }} {% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture all-mentors %}{{ all-mentors }}, {{ m }} {% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-2-participants = all-participants | remove_first: ', ' | split: " , " | uniq | sort %}
{% assign ols-2-mentors = all-mentors | remove_first: ', ' | split: " , " | uniq | sort %}

<!-- OLS-3 -->
{% assign ols-3-projects = site.data.ols-3-projects %}
{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in ols-3-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }} {% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture all-mentors %}{{ all-mentors }}, {{ m }} {% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-3-participants = all-participants | remove_first: ', ' | split: " , " | uniq | sort %}
{% assign ols-3-mentors = all-mentors | remove_first: ', ' | split: " , " | uniq | sort %}

<!-- OLS-4 -->
{% assign ols-4-projects = site.data.ols-4-projects %}
{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in ols-4-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }} {% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture all-mentors %}{{ all-mentors }}, {{ m }} {% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-4-participants = all-participants | remove_first: ', ' | split: " , " | uniq | sort %}
{% assign ols-4-mentors = all-mentors | remove_first: ', ' | split: " , " | uniq | sort %}

<!-- OLS-5 -->
{% assign ols-5-projects = site.data.ols-5-projects %}
{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in ols-5-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }} {% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture all-mentors %}{{ all-mentors }}, {{ m }} {% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-5-participants = all-participants | remove_first: ', ' | split: " , " | uniq | sort %}
{% assign ols-5-mentors = all-mentors | remove_first: ', ' | split: " , " | uniq | sort %}

Participants join this program with a project that they either are already working on or want to develop during this program individually or in teams.
Project ideas can range from solving technical questions to creating an open data project or report, developing an open source software project, writing an open publication, facilitating community/team culture movements, advancing open educational resources or contributing to other existing projects/communities.

**Check out the projects developed in the previous cohorts:**
- [OLS-1]({% link ols-1.md %}) from January to April 2020, [{{ ols-1-participants | size }} participants](/ols-1/projects-participants#participants) with [{{ ols-1-projects | size }} projects](/ols-1/projects-participants#projects)
- [OLS-2]({% link ols-2.md %}) from September to December 2020, [{{ ols-2-participants | size }} participants](/ols-2/projects-participants#participants) with [{{ ols-2-projects | size }} projects](/ols-2/projects-participants#projects)
- [OLS-3]({% link ols-3.md %}) from February to May 2021, [{{ ols-3-participants | size }} participants](/ols-3/projects-participants#participants) with [{{ ols-3-projects | size }} projects](/ols-3/projects-participants#projects)
- [OLS-4]({% link ols-4.md %}) from September 2021 to January 2022, [{{ ols-4-participants | size }} participants](/ols-4/projects-participants#participants) with [{{ ols-4-projects | size }} projects](/ols-4/projects-participants#projects)
- [OLS-5]({% link ols-5.md %}) from February 2022 to June 2022, [{{ ols-5-participants | size }} participants](/ols-5/projects-participants#participants) with [{{ ols-5-projects | size }} projects](/ols-5/projects-participants#projects)

All applications are welcome, whether the project is just an idea at this stage or something that is running for years, but, the projects must:

- promote one or several Open Science practices (i.e. Open Access, Open Source, Citizen Science, ) in science
- state a possible measurable outcome (i.e. feature, module, or minimum viable product) from this program
- create an inclusive space and welcome contributions from their community members

*You don't have a project but want to join the next OLS cohort? Please check our [dedicated issue]({{ site.github.repository_url }}/issues/297) and contact us at [{{ site.email }}](mailto:{{ site.email }}).*

## Does OLS only accept life science projects?

Modern science and scientific communities stand in the interface of computation and other research fields. Life science is one of them.
This interdisciplinary position provides an exciting opportunity for new scientists to understand and welcome open leadership practices -- skills that aren’t necessarily taught in the traditional education system.

OLS fills this gap by offering structured training and mentoring to help participants implement “open by design” principles in their projects systematically.

The founders of this program come from the life science backgrounds and have an extensive network of Open Science practitioners from this field who are experts and mentors in this program.
Therefore, OLS was initially designed with life science researchers and projects in mind.

However, with the growing interest from the community members and the transferable nature of lessons learned in this program, we have expanded the scope to other fields where these skills will be directly applicable.

## What's in it for you?

We want to make this program mutually beneficial for all the participants.
Here are a few values we think you will receive from participating in this project.

- Become a contributing member of this community
- Collaborate with others in Open Science projects
- Exchange skills with others and build your profiles
- Highlight and promote your resources
- Gain insights from other experts in the field
- Work on short-term projects and publish online
- Get recognition and acknowledgment for your work
- Co-develop this program by sharing feedback

