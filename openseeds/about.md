---
layout: page
title: Open Seeds program
description: Structure, timeline, and roles in the Open Seeds mentoring and training program.
image: /images/about.jpg
photos:
  name: Bérénice Batut
  license: CC BY-SA 4.0
  url: https://flic.kr/p/2gHNtNq
---

{% include _includes/cohort-loop.html %}

*To illustrate the Open Seeds journey, we use a persona/story of Joy, a mentee participating in the program, and Sam, their [mentor]({% link openseeds/about.md %}#mentors), as they progress through their Open Seeds training.*

<div class="columns">
  <div class="column is-5" markdown="1">

  ![Structure of Open Seeds program as described on the right](/images/openseeds_structure.png)
  </div>
  <div class="column" markdown="1">

Joy will provide an outline of a project in their application that they will develop in the program. Additionally, they will indicate their interests in learning particular aspects of Open Science and research.

Sam will register as a mentor and list their expertise that they would like to share with their mentee.

After the selection process, they will be involved in the following steps of this program:

1. Based on their common interests, they will be introduced to each other as suitable mentee and mentor

    They will meet every 2nd week on **mentee-mentor calls** (around 30 minutes). Sam will help Joy evaluate their understanding of the new topics introduced in the program, and guide their progress by providing constructive feedback.
    Joy will be given assignments before these calls to help them apply new skills to their project. When needed, Joy and Sam will connect with other [experts]({% link openseeds/about.md %}#experts) to invite consultation on their project.

2. Joy will participate in online [training calls]({% link openseeds/ols-4/index.md %}#calls) and share insights with other participants in the program.

    In these **cohorts calls**, they will be introduced to new topics and resources, participate in break-out discussions, and listen to [expert talks]({% link openseeds/about.md %}#experts).

3. Joy will get to know their peers from the cohort during social and co-working calls.

    They will share their project ideas, learn about others' projects and discuss assignments.

4. A final graduation call will allow Joy to present their project to other participants and exchange values.

Sam will also participate in **mentor training** calls and attend topic-based discussions with other mentors aimed at enhancing their mentoring skills.

A self-evaluation survey, mid-cohort survey and post-cohort survey will help Joy and Sam in positioning their knowledge in open science leadership before, during and after the program.

For the next round, Joy may share what they learned by [mentoring]({% link openseeds/about.md %}#mentors) a new project in the future cohort and Sam will continue their mentoring effort or take an [expert]({% link openseeds/about.md %}#experts) role.

  </div>
</div>

# Projects

Participants join this program with a project that they either are already working on or want to develop during this program individually or in teams.
Project ideas can range from solving technical questions to creating an open data project or report, developing an open source software project, writing an open publication, facilitating community/team culture movements, advancing open educational resources or contributing to other existing projects/communities.

**[Check out the projects developed in the previous cohorts]({% link openseeds/projects.md %})**.

{% for cohort in cohorts %}
    {% assign cohort_name = cohort[0] %}
    {% assign projects = cohort[1].projects %}
    {% assign schedule = cohort[1].schedule %}
    {% assign cohort_start = schedule.weeks['01'].start %}
    {% assign cohort_end = '' %}
    {% for week in schedule.weeks %}
        {% assign cohort_end = week[1].start %}
    {% endfor %}
    {% assign participants = '' %}
    {% for project in projects %}
        {% for p in project.participants %}
            {% capture participants %}{{ participants }}, {{ p }}{% endcapture %}
        {% endfor %}
    {% endfor %}
    {% assign participants = participants | remove_first: ', ' | split: ', ' | uniq | size %}
    {% if participants > 0 %}
- [{{ projects | size }} projects]({% link openseeds/{{ cohort_name }}/projects-participants.md %}#projects) ([{{ participants }} participants]({% link openseeds/{{ cohort_name }}/projects-participants.md %}#participants)) for [**{{ cohort_name | upcase }}**]({% link openseeds/{{ cohort_name }}/index.md %}) ({{ cohort_start | date: "%B %d, %Y" }} - {{ cohort_end | date: "%B %d, %Y" }})
    {% endif %}
{% endfor %}

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

# The roles

This program can only run with the active involvements of our volunteer community who share a passion for Open Research and inclusiveness in Open Science:

- [Mentees](#mentees)
- [Mentors](#mentors)
- [Experts](#experts)
- [Facilitators](#facilitators)

# What's in it for you?

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

## Mentees

Our mentees are scientists and researchers (whether in academia or outside) who are interested in contributing to Open Science projects and communities. In this program they will be supported by the organisers, mentors, experts, and other mentees in getting started with their journey as Open Scientists.

**Our mentees will:**

- gain a better understanding of Open Science and best practices
- fill gaps related to Open Science in their research
- learn to navigate their path in bioinformatics communities
- design equitable opportunities in their projects for the diverse community members
- increase their visibility as Open Scientist
- become Open Science ambassadors for their community

### Becoming a mentee

A mentee dedicates about 2 hours per week to the program to attend cohort/mentor meetings and doing self-guided assignments.

Recruitment of the mentees for the next cohort will start in few months. Stay tuned!

### Our mentees

{% for cohort in cohorts %}
    {% assign cohort_name = cohort[0] %}
    {% assign projects = cohort[1].projects %}
    {% assign schedule = cohort[1].schedule %}
    {% assign cohort_start = schedule.weeks['01'].start %}
    {% assign cohort_end = '' %}
    {% for week in schedule.weeks %}
        {% assign cohort_end = week[1].start %}
    {% endfor %}
    {% assign participants = '' %}
    {% for project in projects %}
        {% for p in project.participants %}
            {% capture participants %}{{ participants }}, {{ p }}{% endcapture %}
        {% endfor %}
    {% endfor %}
    {% assign participants = participants | remove_first: ', ' | split: ', ' | uniq | size %}
    {% if participants > 0 %}
- [{{ participants }} mentees]({% link openseeds/{{ cohort_name }}/projects-participants.md %}#participants) working on ([{{ projects | size }} projects]({% link openseeds/{{ cohort_name }}/projects-participants.md %}#projects)) for [**{{ cohort_name | upcase }}**]({% link openseeds/{{ cohort_name }}/index.md %}) ({{ cohort_start | date: "%B %d, %Y" }} - {{ cohort_end | date: "%B %d, %Y" }})
    {% endif %}
{% endfor %}

## Mentors

Mentors work closely with participants to help further their Open Science skills and become ambassadors for Open Science practice, training and education in their communities. The mentors will be assigned to one or more projects (based on their availability) proposed in the program.

**Our mentors are:**

- contributors of one or several Open Science projects or communities
- interested in sharing the benefit they receive from the Open Science communities
- look for opportunities to gain mentoring experience
- love to share their enthusiasm about Open Science
- want to build their profile as Open Leaders

### What do mentors do?

Mentors advise and inspire:
- **Connect** to people, programs
- **Recommend** resources, readings, experiences
- **Feedback** to consider

A mentor spend around **1 hour per week** dedicated to the program, but also some time before the program to review applications.

They will meet their mentees every two weeks during the program and will attend group calls with other mentors to exchange notes and develop their mentoring skills further.

### What are the benefits to be a mentor?

Our mentors will

- gain mentoring skills (active listening, effective questioning, giving feedback) via mentoring training
- learn to celebrate successes and approach challenges in mentoring
- connect with a community of mentors
- expand their knowledge on Open Science

### Becoming a mentor

Mentoring is usually an invitation-based role. Mentors join by graduating from a previous cohort, by becoming an expert for at least one round, or by invitation when a specific skills gap is needed. Please reach out to one of the organizers if you are interested.

### Our mentors

Our program is only possible thanks to our awesome mentors:

{% for cohort in cohorts %}
    {% assign cohort_name = cohort[0] %}
    {% assign projects = cohort[1].projects %}
    {% assign schedule = cohort[1].schedule %}
    {% assign cohort_start = schedule.weeks['01'].start %}
    {% assign cohort_end = '' %}
    {% for week in schedule.weeks %}
        {% assign cohort_end = week[1].start %}
    {% endfor %}
    {% assign mentors = '' %}
    {% for project in projects %}
        {% for mentor in project.mentors %}
            {% capture mentors %}{{ mentors }}, {{ mentor }}{% endcapture %}
        {% endfor %}
    {% endfor %}
    {% assign mentors = mentors | remove_first: ', ' | split: ', ' | uniq | size %}
    {% if mentors > 0 %}
- [{{ mentors }} mentors]({% link openseeds/{{ cohort_name }}/index.md %}#mentors) for [**{{ cohort_name | upcase }}**]({% link openseeds/{{ cohort_name }}/index.md %}) ({{ cohort_start | date: "%B %d, %Y" }} - {{ cohort_end | date: "%B %d, %Y" }})
    {% endif %}
{% endfor %}

## Experts

Experts will be invited to join cohort calls or individual mentorship calls to share their experience and expertise during the program.

**Our experts are:**

- motivated Open Scientists
- understand and advocate the value of working openly
- look for opportunities to support or give back to the research community
- enjoy sharing their resources to facilitate others work
- develop and teach skills collaboratively in the community
- want to gain/improve leadership skills through their engagements in this program

### Becoming an expert

Experts may be invited to:
- give a ~20 minute talk at one of our cohort calls, which happen every two weeks.
- be interviewed by the organisers (~15 minutes)
- invited by mentor-mentee pair to share their expert consultation on certain projects. (~30 minutes)

We are currently recruiting the experts - this route is a good way to join the program if you are already an open research practitioner and don't wish to participate as a cohort member.

### Our experts
{% for cohort in cohorts %}
    {% assign cohort_name = cohort[0] %}
    {% assign experts = cohort[1].metadata.experts | uniq | size %}
    {% assign projects = cohort[1].projects %}
    {% assign schedule = cohort[1].schedule %}
    {% assign cohort_start = schedule.weeks['01'].start %}
    {% assign cohort_end = '' %}
    {% for week in schedule.weeks %}
        {%- assign cohort_end = week[1].start %}
    {% endfor %}
    {% if experts > 0 %}
- [{{ experts }} experts ]({% link openseeds/{{ cohort_name }}/index.md %}#experts) for [**{{ cohort_name | upcase }}**]({% link openseeds/{{ cohort_name }}/index.md %}) ({{ cohort_start | date: "%B %d, %Y" }} - {{ cohort_end | date: "%B %d, %Y" }})
    {% endif %}
{% endfor %}

## Facilitators

Facilitators work closely with the OLS organisers to manage and run cohort calls. They lead efforts in preparing cohort call notes, co-hosting cohort calls and ensuring the sharing of call recordings and resources through OLS channels.

**Our facilitators are:**
- Project leads, mentors or experts in a previous cohort
- Keen to learn more about the operations of OLS and take a vital role in leading/facilitating the cohort calls
- Committed to contribute time and leadership skills towards building a collaborative experience for the attendees of OLS cohort call.

### Becoming a facilitator

Facilitators are invited to:
- attend an onboarding call (30 mins)
- sign up for responsibilities pre-, during or after one or more cohort calls, ranging from 15 mins to 2hours
- participate in a feedback call at the end of a cohort (30 mins)

This is an invitation-based role. Facilitators are offered an honourarium in recognition of their valuable contributions to the programme.

### Our facilitators

Our facilitators are essential for the program:
{% for cohort in cohorts %}
    {% assign cohort_name = cohort[0] %}
    {% assign facilitators = cohort[1].metadata.facilitators | uniq | size %}
    {% assign projects = cohort[1].projects %}
    {% assign schedule = cohort[1].schedule %}
    {% assign cohort_start = schedule.weeks['01'].start %}
    {% assign cohort_end = '' %}
    {% for week in schedule.weeks %}
        {% assign cohort_end = week[1].start %}
    {% endfor %}
    {% if facilitators > 0 %}
- [{{ facilitators }} facilitators]({% link openseeds/{{ cohort_name }}/index.md %}#facilitators) [**{{ cohort_name | upcase }}**]({% link openseeds/{{ cohort_name }}/index.md %}) ({{ cohort_start | date: "%B %d, %Y" }} - {{ cohort_end | date: "%B %d, %Y" }})
    {% endif %}
{% endfor %}
