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

[Apply via Open Review](https://openreview.net/group?id=openlifesci.org/Open_Life_Science/2023/Cohort_8){:.button .is-link .is-fullwidth}

*Please register on Open Review before July 3, 2023 to allow activation of your Open Review profile as described in the [OLS-8 application guidelines and templates](https://github.com/open-life-science/application-forms).*

OLS-8 runs from September 2023 to January 2024. We are not sure if we will run OLS-9 in the same format - see our [blog post]({% link _posts/2023-05-05-NASA-grant-announcement.md %}). [Sign up to our low-traffic news list]({{ site.announcement_list }}) to get updates. 

## Timeline

{% assign schedule = site.data.cohorts.ols-8.schedule %}
{% include _includes/timeline.md %}

Have a question or need any support to join this cohort?
We are here to help - feel free to email [{{ site.email|replace:'@','[at]' }}](mailto:{{ site.email }}), or connect on Twitter [@{{ site.twitter }}](https://twitter.com/{{ site.twitter }}).

# Cohorts
{% assign all_participants = '' %}
{%- assign all_mentors = '' -%}
{%- assign all_experts = '' -%}
{%- assign all_facilitators = '' -%}
{%- assign all_projects = '' -%}
{%- assign cohorts = site.data.cohorts | sort %}

| Cohort | Schedule | Projects | Mentors | Experts | Facilitators |
| --- | --- | --- | --- | --- | --- |
{%- for cohort_folder in cohorts -%}
  {%- assign cohortName = cohort_folder[0] -%}
  {%- assign cohortData = cohort_folder[1] -%}
  {%- assign experts = site.data.cohorts[cohortName].metadata.experts | uniq | size -%}
  {%- capture all_experts %}{{ all_experts }}, {{ site.data.cohorts[cohortName].metadata.experts | join: ', ' }}{% endcapture -%}
  {%- assign facilitators = site.data.cohorts[cohortName].metadata.facilitators | uniq | size -%}
  {%- capture all_facilitators %}{{ all_facilitators }}, {{ site.data.cohorts[cohortName].metadata.facilitators | join: ', ' }}{% endcapture -%}
  {%- assign projects = site.data.cohorts[cohortName].projects -%}
  {%- assign mentors = '' -%}
  {%- assign participants = '' -%}
  {%- assign projectName = '' -%}
  {%- for project in projects -%}
      {%- for p in project.participants -%}
          {%- capture participants %}{{ participants }}, {{ p }}{% endcapture -%}
      {%- endfor -%}
      {%- for m in project.mentors -%}
          {%- capture mentors %}{{ mentors }}, {{ m }}{% endcapture -%}
      {%- endfor -%}
      {%- for p-name in project.name -%}
          {%- capture projectName %}{{ projectName }}, {{ p-name }}{% endcapture -%}
      {%- endfor -%}
  {%- endfor %}
  {%- assign cohortMentors = mentors | remove_first: ', ' | split: ", " | uniq | sort | size -%}
  {%- capture all_mentors %}{{ all_mentors }}, {{ mentors }}{% endcapture -%}
  {%- assign cohortParticipants = participants | remove_first: ', ' | split: ", " | uniq | sort | size -%}
  {%- capture all_participants %}{{ all_participants }}, {{ participants }}{% endcapture -%}
  {%- assign cohortProjects = projectName | remove_first: ', ' | split: ", " | uniq | sort | size -%}
  {%- capture all_projects %}{{ all_projects }}, {{ projectName }}{% endcapture -%}
  {%- assign cohortSchedule = site.data.cohorts[cohortName].schedule -%}
  {%- assign cohortStart = cohortSchedule.weeks['01'].start -%}
  {%- assign cohortEnd = '' -%}
  {%- for week in cohortSchedule.weeks -%}
      {%- assign cohortEnd = week[1].start -%}
  {%- endfor %}
| [{{ cohortName | upcase }}](/{{ cohortName }}.html) | [{{ cohortStart }} - {{ cohortEnd }}](/{{ cohortName }}/schedule) | {%- if cohortParticipants > 0 -%}[{{ cohortParticipants }} mentees](/{{ cohortName }}/projects-participants#participants) on {%- endif -%} {%- if cohortProjects > 0 -%}[{{ cohortProjects }} projects](/{{ cohortName }}/projects-participants#projects) {%- endif -%}| {%- if cohortMentors > 0 -%}[{{ cohortMentors }} mentors](/{{ cohortName }}#mentors) {%- endif -%}| {%- if experts > 0 -%}[{{ experts }} experts](/{{ cohortName }}#experts) {%- endif -%}| {%- if facilitators > 0 -%}[{{ facilitators }} facilitator(s)](/{{ cohortName }}#facilitators) {%- endif -%} |
{%- endfor -%}
{%- assign all_participants = all_participants | remove_first: ', ' | split: ", " | uniq | size -%}
{%- assign all_mentors = all_mentors | remove_first: ', ' | split: ", " | uniq | size -%}
{%- assign all_facilitators = all_facilitators | remove_first: ', ' | split: ", " | uniq | size -%}
{%- assign all_experts = all_experts | remove_first: ', ' | split: ", " | uniq | size -%}
{% assign all_projects = all_projects | remove_first: ', ' | split: ", " | uniq | size %}
| **Total** | | {{ all_participants }} mentees on {{ all_projects }} projects | {{ all_mentors }} mentors | {{ all_experts }} experts | {{ all_facilitators }} facilitators |
