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

![OLS schedule overview. In the middle, the timeline represents the 16 weeks. On the top, boxes in green represent the 8 different cohort calls pointing to the corresponding weeks (even week numbers). Below the week timeline, blue boxes represent the mentor-mentee meetings pointing to the uneven number weeks. Below the blue boxes, are red boxes corresponding to 3 skill-up calls: "GitHub tutorial for beginners" (week 5), "Open Leadership: Academia, industry, and beyond" (week 9), "Self-care & social call" (week 1s)](/images/schedule.png){: .schedule-overview}

# Applications

<!--[Apply via Open Review](https://openreview.net/group?id=openlifesci.org/Open_Life_Science/2023/Cohort_7){:.button .is-link .is-fullwidth}

*Please register on Open Review before January 13, 2023 to allow activation of your Open Review profile as described in the [OLS-7 application guidelines and templates](https://github.com/open-life-science/application-forms).*-->

OLS-7 runs from February to June 2023. Applications for OLS-8 will open at mid 2023. [Sign up to our low-traffic news list]({{ site.announcement_list }}) to get updates on the next cohort application.

## Timeline

{% assign schedule = site.data.cohorts.ols-7.schedule %}
{% include _includes/timeline.md %}

Have a question or need any support to join this cohort?
We are here to help - feel free to email [{{ site.email|replace:'@','[at]' }}](mailto:{{ site.email }}), chat in real-time on [Gitter](https://gitter.im/{{ site.gitter }}) or connect on Twitter [@{{ site.twitter }}](https://twitter.com/{{ site.twitter }}).

# Cohorts
{% assign cohorts_path = '_data/cohorts' %}

{% for cohort_folder in site.data.cohorts %}
    
    {% assign cohort_folder_path = cohorts_path | append: '/' | append: cohort_folder %}
    {% for subfolder in site.static_files %}
    {% if subfolder.path contains cohort_folder_path %}
        <!--Store path of matching subfolder-->
        {% assign subfolder_path = subfolder.path %}
        {% break %}
    {% endif %}
    {% endfor %}

    {% assign metadata_path = subfolder_path | append: '/metadata.yaml' %}
    {% assign projects_path = subfolder_path | append: '/projects.yaml' %}
    {% assign schedule_path = subfolder_path | append: '/schedule.yaml' %}

<!--Parse yaml files and store extracted data in extracted files-->
    {% assign cohort_metadata = site.data | yaml_parse: metadata_path %}
    {% assign cohort_projects = site.data | yaml_parse: projects_path %}
    {% assign cohort_schedule = site.data | yaml_parse: schedule_path %}

  <!-- Test: Access the extracted data -->
  <p>{{ cohort_metadata }}</p>
  <p>{{ cohort_metadata[0] }}</p>
  
  <!-- test -->
  {% if cohort_folder == ols-1 %}
    {% assign ols-1_metadata = cohort_metadata %}
    {% assign ols-1_projects = cohort_projects %}
    {% assign ols-1_schedule = cohort_schedule %}
  {% endif %}
{% endfor %}

{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% assign all-experts = '' %}
{% assign all-facilitators = '' %}
<!-- OLS-1 -->
{% assign ols-1-projects = site.data.cohorts.ols-1.projects %}
{% assign ols-1-experts = site.data.cohorts.ols-1.metadata.experts | uniq | size %}
{% capture all-experts %}{{ all-experts}}, {{ site.data.cohorts.ols-1.metadata.experts | join: ', ' }}{% endcapture %}
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
{% assign ols-1-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-mentors %}{{ all-mentors}}, {{ mentors }}{% endcapture %}
{% assign ols-1-participants = participants | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-participants %}{{ all-participants}}, {{ participants }}{% endcapture %}
{% assign ols-1-projects = ols-1-projects | size %}
{% assign ols-1-schedule = site.data.cohorts.ols-1.schedule %}
{% assign ols-1-end = '' %}
{% for w in ols-1-schedule.weeks %}
    {% assign ols-1-end = w[1].start %}
{% endfor %}
<!-- OLS-2 -->
{% assign ols-2-projects = site.data.cohorts.ols-2.projects %}
{% assign ols-2-experts = site.data.cohorts.ols-2.metadata.experts | uniq | size %}
{% capture all-experts %}{{ all-experts}}, {{ site.data.ols-2-metadata.experts | join: ', ' }}{% endcapture %}
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
{% assign ols-2-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort  | size %}
{% capture all-mentors %}{{ all-mentors}}, {{ mentors }}{% endcapture %}
{% assign ols-2-participants = participants | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-participants %}{{ all-participants}}, {{ participants }}{% endcapture %}
{% assign ols-2-projects = ols-2-projects | size %}
{% assign ols-2-schedule = site.data.cohorts.ols-2.schedule %}
{% assign ols-2-end = '' %}
{% for w in ols-2-schedule.weeks %}
    {% assign ols-2-end = w[1].start %}
{% endfor %}
<!-- OLS-3 -->
{% assign ols-3-projects = site.data.cohorts.ols-3.projects %}
{% assign ols-3-experts = site.data.cohorts.ols-3.metadata.experts | uniq | size %}
{% capture all-experts %}{{ all-experts}}, {{ site.data.cohorts.ols-3.metadata.experts | join: ', ' }}{% endcapture %}
{% assign ols-3-facilitators = site.data.cohorts.ols-3.metadata.facilitators | uniq | size %}
{% capture all-facilitators %}{{ all-facilitators}}, {{ site.data.cohorts.ols-3.metadata.facilitators | join: ', ' }}{% endcapture %}
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
{% assign ols-3-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-mentors %}{{ all-mentors}}, {{ mentors }}{% endcapture %}
{% assign ols-3-participants = participants | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-participants %}{{ all-participants}}, {{ participants }}{% endcapture %}
{% assign ols-3-projects = ols-3-projects | size %}
{% assign ols-3-schedule = site.data.cohorts.ols-3.schedule %}
{% assign ols-3-end = '' %}
{% for w in ols-3-schedule.weeks %}
    {% assign ols-3-end = w[1].start %}
{% endfor %}
<!-- OLS-4-->
{% assign ols-4-projects = site.data.cohorts.ols-4.projects %}
{% assign ols-4-experts = site.data.cohorts.ols-4.metadata.experts | uniq | size %}
{% capture all-experts %}{{ all-experts}}, {{ site.data.cohorts.ols-4.metadata.experts | join: ', ' }}{% endcapture %}
{% assign ols-4-facilitators = site.data.cohorts.ols-4.metadata.facilitators | uniq | size %}
{% capture all-facilitators %}{{ all-facilitators}}, {{ site.data.ols-4-metadata.facilitators | join: ', ' }}{% endcapture %}
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
{% assign ols-4-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-mentors %}{{ all-mentors}}, {{ mentors }}{% endcapture %}
{% assign ols-4-participants = participants | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-participants %}{{ all-participants}}, {{ participants }}{% endcapture %}
{% assign ols-4-projects = ols-4-projects | size %}
{% assign ols-4-schedule = site.data.cohorts.ols-4.schedule %}
{% assign ols-4-end = '' %}
{% for w in ols-4-schedule.weeks %}
    {% assign ols-4-end = w[1].start %}
{% endfor %}
<!-- OLS-5-->
{% assign ols-5-projects = site.data.cohorts.ols-5.projects %}
{% assign ols-5-experts = site.data.cohorts.ols-5.metadata.experts | uniq | size %}
{% capture all-experts %}{{ all-experts}}, {{ site.data.cohorts.ols-5.metadata.experts | join: ', ' }}{% endcapture %}
{% assign ols-5-facilitators = site.data.cohorts.ols-5.metadata.facilitators | uniq | size %}
{% capture all-facilitators %}{{ all-facilitators}}, {{ site.data.cohorts.ols-5.metadata.facilitators | join: ', ' }}{% endcapture %}
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
{% assign ols-5-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-mentors %}{{ all-mentors}}, {{ mentors }}{% endcapture %}
{% assign ols-5-participants = participants | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-participants %}{{ all-participants}}, {{ participants }}{% endcapture %}
{% assign ols-5-projects = ols-5-projects | size %}
{% assign ols-5-schedule = site.data.cohorts.ols-5.schedule %}
{% assign ols-5-end = '' %}
{% for w in ols-5-schedule.weeks %}
    {% assign ols-5-end = w[1].start %}
{% endfor %}
<!-- OLS-6-->
{% assign ols-6-projects = site.data.cohorts.ols-6.projects %}
{% assign ols-6-experts = site.data.cohorts.ols-6.metadata.experts | uniq | size %}
{% capture all-experts %}{{ all-experts}}, {{ site.data.cohorts.ols-6.metadata.experts | join: ', ' }}{% endcapture %}
{% assign ols-6-facilitators = site.data.cohorts.ols-6.metadata.facilitators | uniq | size %}
{% capture all-facilitators %}{{ all-facilitators}}, {{ site.data.cohorts.ols-6.metadata.facilitators | join: ', ' }}{% endcapture %}
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
{% assign ols-6-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-mentors %}{{ all-mentors}}, {{ mentors }}{% endcapture %}
{% assign ols-6-participants = participants | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-participants %}{{ all-participants}}, {{ participants }}{% endcapture %}
{% assign ols-6-projects = ols-6-projects | size %}
{% assign ols-6-schedule = site.data.cohorts.ols-6.schedule %}
{% assign ols-6-end = '' %}
{% for w in ols-6-schedule.weeks %}
    {% assign ols-6-end = w[1].start %}
{% endfor %}
<!-- OLS-7-->
{% assign ols-7-projects = site.data.cohorts.ols-7.projects %}
{% assign ols-7-experts = site.data.cohorts.ols-7.metadata.experts | uniq | size %}
{% capture all-experts %}{{ all-experts}}, {{ site.data.cohorts.ols-7.metadata.experts | join: ', ' }}{% endcapture %}
{% assign ols-7-facilitators = site.data.ols-7-metadata.facilitators | uniq | size %}
{% capture all-facilitators %}{{ all-facilitators}}, {{ site.data.cohorts.ols-7.metadata.facilitators | join: ', ' }}{% endcapture %}
{% assign mentors = '' %}
{% assign participants = '' %}
{% for project in ols-7-projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture participants %}{{ participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-7-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-mentors %}{{ all-mentors}}, {{ mentors }}{% endcapture %}
{% assign ols-7-participants = participants | remove_first: ', ' | split: ", " | uniq | sort | size %}
{% capture all-participants %}{{ all-participants}}, {{ participants }}{% endcapture | size %}
{% assign ols-7-projects = ols-7-projects | size %}
{% assign ols-7-schedule = site.data.cohorts.ols-7.schedule %}
{% assign ols-7-end = '' %}
{% for w in ols-7-schedule.weeks %}
    {% assign ols-7-end = w[1].start %}
{% endfor %}
<!-- all -->
{% assign all-participants = all-participants | remove_first: ', ' | split: ", " | uniq | size %}
{% assign all-mentors = all-mentors | remove_first: ', ' | split: ", " | uniq | size %}
{% assign all-facilitators = all-facilitators | remove_first: ', ' | split: ", " | uniq | size %}
{% assign all-experts = all-experts | remove_first: ', ' | split: ", " | uniq | size %}
{% assign all-projects = ols-1-projects | plus: ols-2-projects  | plus: ols-3-projects | plus: ols-4-projects | plus: ols-5-projects | plus: ols-6-projects | plus: ols-7-projects%}


Cohort | Schedule | Projects | Mentors | Experts | Facilitators
--- | --- | --- | --- | --- | ---
[OLS-1]({% link ols-1.md %}) | [{{ ols-1-schedule.weeks['01'].start }} - {{ ols-1-end }}]({% link _ols-1/schedule.md %}) | [{{ ols-1-participants }} mentees](/ols-1/projects-participants#participants) on [{{ ols-1-projects  }} projects](/ols-1/projects-participants#projects) | [{{ ols-1-mentors }} mentors](/ols-1#mentors) | [{{ ols-1-experts }} experts](/ols-1#experts) |
[OLS-2]({% link ols-2.md %}) | [{{ ols-2-schedule.weeks['01'].start }} - {{ ols-2-end }}]({% link _ols-2/schedule.md %}) | [{{ ols-2-participants }} mentees](/ols-2/projects-participants#participants) on [{{ ols-2-projects }} projects](/ols-2/projects-participants#projects) | [{{ ols-2-mentors }} mentors](/ols-2#mentors) | [{{ ols-2-experts }} experts](/ols-2#experts) |
[OLS-3]({% link ols-3.md %}) | [{{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }}]({% link _ols-3/schedule.md %}) | [{{ ols-3-participants }} mentees](/ols-3/projects-participants#participants) on [{{ ols-3-projects }} projects](/ols-3/projects-participants#projects) | [{{ ols-3-mentors }} mentors](/ols-3#mentors) | [{{ ols-3-experts }} experts](/ols-3#experts) | [{{ ols-3-facilitators }} facilitator](/ols-3#facilitators)
[OLS-4]({% link ols-4.md %}) | [{{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }}]({% link _ols-4/schedule.md %}) | [{{ ols-4-participants }} mentees](/ols-4/projects-participants#participants) on [{{ ols-4-projects }} projects](/ols-4/projects-participants#projects) | [{{ ols-4-mentors }} mentors](/ols-4#mentors) | [{{ ols-4-experts }} experts](/ols-4#experts) | [{{ ols-4-facilitators }} facilitators](/ols-4#facilitators)
[OLS-5]({% link ols-5.md %}) | [{{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }}]({% link _ols-5/schedule.md %}) | [{{ ols-5-participants }} mentees](/ols-5/projects-participants#participants) on [{{ ols-5-projects }} projects](/ols-5/projects-participants#projects) | [{{ ols-5-mentors }} mentors](/ols-5#mentors) | [{{ ols-5-experts }} experts](/ols-5#experts) | [{{ ols-5-facilitators }} facilitators](/ols-5#facilitators)
[OLS-6]({% link ols-6.md %}) | [{{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }}]({% link _ols-6/schedule.md %}) | [{{ ols-6-participants }} mentees](/ols-6/projects-participants#participants) on [{{ ols-6-projects }} projects](/ols-6/projects-participants#projects) | [{{ ols-6-mentors }} mentors](/ols-6#mentors) | [{{ ols-6-experts }} experts](/ols-6#experts) | [{{ ols-6-facilitators }} facilitators](/ols-6#facilitators)
[OLS-7]({% link ols-7.md %}) | [{{ ols-7-schedule.weeks['01'].start }} - {{ ols-7-end }}]({% link _ols-7/schedule.md %}) | [{{ ols-7-participants }} mentees](/ols-7/projects-participants#participants) on [{{ ols-7-projects }} projects](/ols-7/projects-participants#projects) | [{{ ols-7-mentors }} mentors](/ols-7#mentors) | [{{ ols-7-experts }} experts](/ols-7#experts) | [{{ ols-7-facilitators }} facilitators](/ols-7#facilitators)
**Total** | | {{ all-participants }} mentees on {{ all-projects }} projects | {{ all-mentors }} mentors | {{ all-experts }} experts | {{ all-facilitators }} facilitators
