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

Participants join this program with a **project** that they either are already working on or want to develop during this program **individually or in teams**.


# Applications

<!--[Apply via Open Review](https://openreview.net/group?id=openlifesci.org/Open_Life_Science/2022/Cohort_6){:.button .is-link .is-fullwidth}

*Please register on Open Review before July 1, 2022 to allow activation of your Open Review profile as described in the [OLS-6 application guidelines and templates](https://github.com/open-life-science/application-forms).*-->

OLS-6 runs from September 2022 to January 2023. Applications for OLS-7 will open in end 2022. [Sign up to our low-traffic news list]({{ site.announcement_list }}) to hear when next cohort applications open.

## Timeline

{% assign schedule = site.data.ols-6-schedule %}
{% include _includes/timeline.md %}

Have a question or need any support to join this cohort?
We are here to help - feel free to email [{{ site.email|replace:'@','[at]' }}](mailto:{{ site.email }}), chat in real-time on [Gitter](https://gitter.im/{{ site.gitter }}) or connect on Twitter [@{{ site.twitter }}](https://twitter.com/{{ site.twitter }}).

# Cohorts

<!-- OLS-1 -->
{% assign ols-1-projects = site.data.ols-1-projects %}
{% assign ols-1-experts = site.data.ols-1-metadata.experts %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-1-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-1-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-1-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-1-schedule = site.data.ols-1-schedule %}
{% assign ols-1-end = '' %}
{% for w in ols-1-schedule.weeks %}
    {% assign ols-1-end = w[1].start %}
{% endfor %}
<!-- OLS-2 -->
{% assign ols-2-projects = site.data.ols-2-projects %}
{% assign ols-2-experts = site.data.ols-2-metadata.experts %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-2-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-2-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-2-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-2-schedule = site.data.ols-2-schedule %}
{% assign ols-2-end = '' %}
{% for w in ols-2-schedule.weeks %}
    {% assign ols-2-end = w[1].start %}
{% endfor %}
<!-- OLS-3 -->
{% assign ols-3-projects = site.data.ols-3-projects %}
{% assign ols-3-experts = site.data.ols-3-metadata.experts %}
{% assign ols-3-facilitators = site.data.ols-3-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-3-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-3-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-3-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-3-schedule = site.data.ols-3-schedule %}
{% assign ols-3-end = '' %}
{% for w in ols-3-schedule.weeks %}
    {% assign ols-3-end = w[1].start %}
{% endfor %}
<!-- OLS-4-->
{% assign ols-4-projects = site.data.ols-4-projects %}
{% assign ols-4-experts = site.data.ols-4-metadata.experts %}
{% assign ols-4-facilitators = site.data.ols-4-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-4-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-4-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-4-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-4-schedule = site.data.ols-4-schedule %}
{% assign ols-4-end = '' %}
{% for w in ols-4-schedule.weeks %}
    {% assign ols-4-end = w[1].start %}
{% endfor %}
<!-- OLS-5-->
{% assign ols-5-projects = site.data.ols-5-projects %}
{% assign ols-5-experts = site.data.ols-5-metadata.experts %}
{% assign ols-5-facilitators = site.data.ols-5-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-5-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-5-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-5-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-5-schedule = site.data.ols-5-schedule %}
{% assign ols-5-end = '' %}
{% for w in ols-5-schedule.weeks %}
    {% assign ols-5-end = w[1].start %}
{% endfor %}
<!-- OLS-6-->
{% assign ols-6-projects = site.data.ols-6-projects %}
{% assign ols-6-experts = site.data.ols-6-metadata.experts %}
{% assign ols-6-facilitators = site.data.ols-6-metadata.facilitators %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-6-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-6-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-6-participants = participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign ols-6-schedule = site.data.ols-6-schedule %}
{% assign ols-6-end = '' %}
{% for w in ols-6-schedule.weeks %}
    {% assign ols-6-end = w[1].start %}
{% endfor %}

Cohort | Schedule | Projects | Mentors | Experts | Facilitators
--- | --- | --- | --- | --- | ---
[OLS-1]({% link ols-1.md %}) | [{{ ols-1-schedule.weeks['01'].start }} - {{ ols-1-end }}]({% link _ols-1/schedule.md %}) | [{{ ols-1-participants | size }} mentees](/ols-1/projects-participants#participants) working on [{{ ols-1-projects | size }} projects](/ols-1/projects-participants#projects) | [{{ ols-1-mentors | size }} mentors](/ols-1#mentors) | [{{ ols-1-experts | uniq | size }} experts](/ols-1#experts) | 
[OLS-2]({% link ols-2.md %}) | [{{ ols-2-schedule.weeks['01'].start }} - {{ ols-2-end }}]({% link _ols-2/schedule.md %}) | [{{ ols-2-participants | size }} mentees](/ols-2/projects-participants#participants) working on [{{ ols-1-projects | size }} projects](/ols-2/projects-participants#projects) | [{{ ols-2-mentors | size }} mentors](/ols-2#mentors) | [{{ ols-2-experts | uniq | size }} experts](/ols-2#experts) | 
[OLS-3]({% link ols-3.md %}) | [{{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }}]({% link _ols-3/schedule.md %}) | [{{ ols-3-participants | size }} mentees](/ols-3/projects-participants#participants) working on [{{ ols-3-projects | size }} projects](/ols-3/projects-participants#projects) | [{{ ols-3-mentors | size }} mentors](/ols-3#mentors) | [{{ ols-3-experts | uniq | size }} experts](/ols-3#experts) | [{{ ols-3-facilitators | uniq | size }} facilitator](/ols-3#facilitators)
[OLS-4]({% link ols-4.md %}) | [{{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }}]({% link _ols-4/schedule.md %}) | [{{ ols-4-participants | size }} mentees](/ols-4/projects-participants#participants) working on [{{ ols-4-projects | size }} projects](/ols-4/projects-participants#projects) | [{{ ols-4-mentors | size }} mentors](/ols-4#mentors) | [{{ ols-4-experts | uniq | size }} experts](/ols-4#experts) | [{{ ols-4-facilitators | uniq | size }} facilitators](/ols-4#facilitators)
[OLS-5]({% link ols-5.md %}) | [{{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }}]({% link _ols-5/schedule.md %}) | [{{ ols-5-participants | size }} mentees](/ols-5/projects-participants#participants) working on [{{ ols-5-projects | size }} projects](/ols-5/projects-participants#projects) | [{{ ols-5-mentors | size }} mentors](/ols-5#mentors) | [{{ ols-5-experts | uniq | size }} experts](/ols-5#experts) | [{{ ols-5-facilitators | uniq | size }} facilitators](/ols5#facilitators)
[OLS-6]({% link ols-6.md %}) | [{{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }}]({% link _ols-6/schedule.md %}) | [{{ ols-6-participants | size }} mentees](/ols-6/projects-participants#participants) working on [{{ ols-6-projects | size }} projects](/ols-6/projects-participants#projects) | [{{ ols-6-mentors | size }} mentors](/ols-6#mentors) | [{{ ols-6-experts | uniq | size }} experts](/ols-6#experts) | [{{ ols-6-facilitators | uniq | size }} facilitators](/ols-6#facilitators)