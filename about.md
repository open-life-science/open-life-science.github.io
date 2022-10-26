---
layout: page
title: OLS program
image: /images/about.jpg
photos:
  name: Bérénice Batut
  license: CC BY-SA 4.0
  url: https://flic.kr/p/2gHNtNq
---


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

*To illustrate the OLS journey, we use a persona/story of Joy, a mentee participating in the program, and Sam, their [mentor](about#mentors), as they progress through their open science training.*

Joy will provide an outline of a project in their application that they will develop in the program. Additionally, they will indicate their interests in learning particular aspects of Open Science and research.

Sam will register as a mentor and list their expertise that they would like to share with their mentee.

After the selection process, they will be involved in the following steps of this program:

1. Based on their common interests, they will be introduced to each other as suitable mentee and mentor

    They will meet every 2nd week on **mentee-mentor calls** (around 30 minutes). Sam will help Joy evaluate their understanding of the new topics introduced in the program, and guide their progress by providing constructive feedback.
    Joy will be given assignments before these calls to help them apply new skills to their project. When needed, Joy and Sam will connect with other [experts](about#experts) to invite consultation on their project.

2. Joy will participate in online [training calls](ols-4#calls) and share insights with other participants in the program.

    In these **cohorts calls**, they will be introduced to new topics and resources, participate in break-out discussions, and listen to [expert talks](about#experts).

3. Joy will get to know their peers from the cohort during social and co-working calls.

    They will share their project ideas, learn about others' projects and discuss assignments.

4. A final graduation call will allow Joy to present their project to other participants and exchange values.

Sam will also participate in **mentor training** calls and attend topic-based discussions with other mentors aimed at enhancing their mentoring skills.

A self-evaluation survey, mid-cohort survey and post-cohort survey will help Joy and Sam in positioning their knowledge in open science leadership before, during and after the program.

For the next round, Joy may share what they learned by [mentoring](about#mentors) a new project in the future cohort and Sam will continue their mentoring effort or take an [expert](about#experts) role.

# Projects

Participants join this program with a project that they either are already working on or want to develop during this program individually or in teams.
Project ideas can range from solving technical questions to creating an open data project or report, developing an open source software project, writing an open publication, facilitating community/team culture movements, advancing open educational resources or contributing to other existing projects/communities.

**Check out the projects developed in the previous cohorts:**
- [{{ ols-1-projects | size }} projects](/ols-1/projects-participants#projects) ([{{ ols-1-participants | size }} participants](/ols-1/projects-participants#participants)) for [**OLS-1**]({% link ols-1.md %}) ({{ ols-1-schedule.weeks['01'].start }} - {{ ols-1-end }})
- [{{ ols-2-projects | size }} projects](/ols-2/projects-participants#projects) ([{{ ols-2-participants | size }} participants](/ols-2/projects-participants#participants)) for [**OLS-2**]({% link ols-2.md %}) ({{ ols-2-schedule.weeks['01'].start }} - {{ ols-2-end }})
- [{{ ols-3-projects | size }} projects](/ols-3/projects-participants#projects) ([{{ ols-3-participants | size }} participants](/ols-3/projects-participants#participants)) for [**OLS-3**]({% link ols-3.md %}) ({{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }})
- [{{ ols-4-projects | size }} projects](/ols-4/projects-participants#projects) ([{{ ols-4-participants | size }} participants](/ols-4/projects-participants#participants)) for [**OLS-4**]({% link ols-4.md %}) ({{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }})
- [{{ ols-5-projects | size }} projects](/ols-5/projects-participants#projects) ([{{ ols-5-participants | size }} participants](/ols-5/projects-participants#participants)) for [**OLS-5**]({% link ols-5.md %}) ({{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }})
- [{{ ols-s-projects | size }} projects](/ols-6/projects-participants#projects) ([{{ ols-6-participants | size }} participants](/ols-6/projects-participants#participants)) for [**OLS-6**]({% link ols-6.md %}) ({{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }})

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

Our mentees are science researchers and bioinformaticians who are interested in contributing to Open Science projects and communities. In this program they will be supported by the organisers, mentors, experts, and other mentees in getting started with their journey as Open Scientists.

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

- [{{ ols-1-participants | size }} mentees](/ols-1/projects-participants#participants) working on [{{ ols-1-projects | size }} projects](/ols-1/projects-participants#projects) for [**OLS-1**]({% link ols-1.md %}) ({{ ols-1-schedule.weeks['01'].start }} - {{ ols-1-end }})
- [{{ ols-2-participants | size }} mentees](/ols-2/projects-participants#participants) working on [{{ ols-2-projects | size }} projects](/ols-2/projects-participants#projects) for [**OLS-2**]({% link ols-2.md %}) ({{ ols-2-schedule.weeks['01'].start }} - {{ ols-2-end }})
- [{{ ols-3-participants | size }} mentees](/ols-3/projects-participants#participants) working on [{{ ols-3-projects | size }} projects](/ols-3/projects-participants#projects) for [**OLS-3**]({% link ols-3.md %}) ({{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }})
- [{{ ols-4-participants | size }} mentees](/ols-4/projects-participants#participants) working on [{{ ols-4-projects | size }} projects](/ols-4/projects-participants#projects) for [**OLS-4**]({% link ols-4.md %}) ({{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }})
- [{{ ols-5-participants | size }} mentees](/ols-5/projects-participants#participants) working on [{{ ols-5-projects | size }} projects](/ols-5/projects-participants#projects) for [**OLS-5**]({% link ols-5.md %}) ({{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }})
- [{{ ols-6-participants | size }} mentees](/ols-6/projects-participants#participants) working on [{{ ols-6-projects | size }} projects](/ols-6/projects-participants#projects) for [**OLS-6**]({% link ols-6.md %}) ({{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }})

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

- [{{ ols-1-mentors | size }} mentors](/ols-1#mentors) for [**OLS-1**]({% link ols-1.md %}) ({{ ols-1-schedule.weeks['01'].start }} - {{ ols-1-end }})
- [{{ ols-2-mentors | size }} mentors](/ols-2#mentors) for [**OLS-2**]({% link ols-2.md %}) ({{ ols-2-schedule.weeks['01'].start }} - {{ ols-2-end }})
- [{{ ols-3-mentors | size }} mentors](/ols-3#mentors) for [**OLS-3**]({% link ols-3.md %}) ({{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }})
- [{{ ols-4-mentors | size }} mentors](/ols-4#mentors) for [**OLS-4**]({% link ols-4.md %}) ({{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }})
- [{{ ols-5-mentors | size }} mentors](/ols-5#mentors) for [**OLS-5**]({% link ols-5.md %}) ({{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }})
- [{{ ols-6-mentors | size }} mentors](/ols-6#mentors) for [**OLS-6**]({% link ols-6.md %}) ({{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }})

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

- [{{ ols-1-experts | uniq | size }} experts](/ols-1#experts) for [**OLS-1**]({% link ols-1.md %}) ({{ ols-1-schedule.weeks['01'].start }} - {{ ols-1-end }})
- [{{ ols-2-experts | uniq | size }} experts](/ols-2#experts) for [**OLS-2**]({% link ols-2.md %}) ({{ ols-2-schedule.weeks['01'].start }} - {{ ols-2-end }})
- [{{ ols-3-experts | uniq | size }} experts](/ols-3#experts) for [**OLS-3**]({% link ols-3.md %}) ({{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }})
- [{{ ols-4-experts | uniq | size }} experts](/ols-4#experts) for [**OLS-4**]({% link ols-4.md %}) ({{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }})
- [{{ ols-5-experts | uniq | size }} experts](/ols-5#experts) for [**OLS-5**]({% link ols-5.md %}) ({{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }})
- [{{ ols-6-experts | uniq | size }} experts](/ols-6#experts) for [**OLS-6**]({% link ols-6.md %}) ({{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }})

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

- [{{ ols-3-facilitators | uniq | size }} facilitator(s)](/ols-3#facilitators) for [**OLS-3**]({% link ols-3.md %}) ({{ ols-3-schedule.weeks['01'].start }} - {{ ols-3-end }})
- [{{ ols-4-facilitators | uniq | size }} facilitator(s)](/ols-4#facilitators) for [**OLS-4**]({% link ols-4.md %}) ({{ ols-4-schedule.weeks['01'].start }} - {{ ols-4-end }})
- [{{ ols-5-facilitators | uniq | size }} facilitator(s)](/ols-5#facilitators) for [**OLS-5**]({% link ols-5.md %}) ({{ ols-5-schedule.weeks['01'].start }} - {{ ols-5-end }})
- [{{ ols-6-facilitators | uniq | size }} facilitator(s)](/ols-6#facilitators) for [**OLS-6**]({% link ols-6.md %}) ({{ ols-6-schedule.weeks['01'].start }} - {{ ols-6-end }})