---
layout: page
title: Welcome to the first cohort of Open Life Science program!
image: /images/syllabus.jpg
photos:
  name: Niklas Morberg
  license: CC BY-NC 2.0
  url: https://flic.kr/p/5BXB6s
---

{% assign people = site.data.people %}
{% assign projects = site.data.ols-1-projects %}
{% assign experts-speakers = site.data.ols-1-experts-speakers %}

{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }} {% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture all-mentors %}{{ all-mentors }}, {{ m }} {% endcapture %}
    {% endfor %}
{% endfor %}

{% assign p-participants = all-participants | remove_first: ', ' | split: " , " | uniq | sort %}
{% assign p-mentors = all-mentors | remove_first: ', ' | split: " , " | uniq | sort %}


# The OLS-1 program
{:.no_toc}

**Purpose**: Training for early stage researchers and young leaders interested in furthering their
Open Science skills

**Outcome**: Ambassadors for Open Science practice, training and education across multiple European
and international bioinformatics communities.

**Process**: A 15-week mentoring & training program, based on the [Mozilla Open Leader program](https://foundation.mozilla.org/en/opportunity/mozilla-open-leaders/), helping participants in becoming Open Science ambassadors by using three principles:

1. **Sharing** essential knowledge required to create, lead, and sustain an Open Science project.
2. **Connecting** members across different communities, backgrounds, and identities by creating space in this program for them to share their experiences and expertise.
3. **Empowering** them to become effective Open Science ambassadors in their communities.

# Table of content
{:.no_toc}

1. TOC
{:toc}

# Goals and Learning Objectives

The vision of Open Life Science program is to strengthen Open Science skills for early stage researchers and young leaders in life science.

At the end of the program, our participants will be able to:
- Describe and define the terms *openness*, *open science*, *open leadership*, *community interactions*, *value exchanges*, *inclusivity*, *accessibility*, *open Science practices in developing resources and training*
- Learn how to apply those principles to open leadership and working open in their projects and communities
. Learn how to collect, invite, and tell stories that demonstrate how and why openness benefits the communities they serve
- Give original examples for the types of openness in science
- Design
  - Illustrate the need for a project, its vision, and its goals
  - Embrace and communicate the benefits of Open Science and how to strategically apply different open practices to their work
  - Identify the public resources to share their data
  - Identify the different type of Open Access and associated journals
- Build
  - Start any project with openness in mind from day one
  - Setup a project repository on GitHub using best practices for enabling collaboration
  - Choose and apply open licenses appropriately
- Empower
  - Create and enforce a safe working environment
  - Promote the values of Open Science to empower others to lead and collaborate
  - Include a broad range of contributors in their work
  - Communicate their work and vision in a 2min demo of elevator pitch
- Lead an open project in science

# Timeline

OLS's first cohort (OLS-1), known as “Open Seeds”, was conducted from January 2020 until May 2020 with [{{ p-participants | size }} project leaders](/ols-1/projects-participants#participants) working on [{{ projects | size }} projects](/ols-1/projects-participants#projects).

{% include _includes/ols-1-timeline.md %}

# Schedule

<iframe class="calendar" src="https://calendar.google.com/calendar/embed?src=n3rqhvuff05ojkl0opfsvh49fk%40group.calendar.google.com"  frameborder="0" scrolling="no"></iframe>

| Week | Call type | Duration | Date | Topic                             | Rough Agenda                             |
|:-----|:----------|:---------|:-----|:----------------------------------|:-----------------------------------------|
| 1    | Mentor | 30 min | Week of January 20, 2020 | [**Meet your mentor!**]({% link _ols-1/week01.md %}) | Meet each other and discuss your personal motivation, expectations, working practices and project goals |
| 2    | Cohort | 90 min | January 29, 2020 (2pm CET) | [**Welcome to Open Life Science!**]({% link _ols-1/week02.md %}) | Meet other members of your cohort, Share project vision, Intro to working openly (open canvas) |
| 3    | Mentor | 30 min | Week of February 3, 2020 | [**Meet your mentor!**]({% link _ols-1/week03.md %}) | Discuss assignments from the cohort call & concrete implementations |
| 4    | Cohort | 90 min | February 12, 2020 (7pm CET) | [**Tooling and roadmapping for Open projects**]({% link _ols-1/week04.md %}) | Working with GitHub as a community hub: Markdown as a tool to make websites, Licence, Goals and Roadmap, Contributors, Code of Conduct |
| 5   | Mentor | 30 min | Week of February 17, 2020 | [**Meet your mentor!**]({% link _ols-1/week05.md %}) | |
|     | (Optional) Cohort | 60 min | February 19, 2020 (2pm CET) | [**GitHub Tutorial**]({% link _ols-1/week05-extra.md %}) | |
| 6    | Cohort | 90 min | February 26, 2020 (2pm CET) | [**Open Science I: Project Development**]({% link _ols-1/week06.md %}) | Developing Open Projects: Open-Source, Software, Hardware, Data  |
| 7    | Mentor | 30 min | Week of March 2, 2020 | [**Meet your mentor!**]({% link _ols-1/week07.md %}) | |
| 8    | Cohort | 90 min | March 11, 2020 (7pm CET) | [**Open Science II: Knowledge Dissemination**]({% link _ols-1/week08.md %}) | Sharing Open Project: Preprint publications, DOI and citation, Open protocols, Open Education & Training |
| 9    | Mentor | 30 min | Week of March 16, 2020 | [**Meet your mentor!**]({% link _ols-1/week09.md %}) |
| 10   | Cohort | 90 min | March 25, 2020 (2pm CET) | [**Designing & Empowering for inclusivity**]({% link _ols-1/week10.md %}) | Personas and pathways for contributors, Implicit bias & mental health care, Community interactions & Ally-skill |
| 11   | (Optional) Cohort | 90 min | April 1, 2020 (7pm CET) | [**Career Guidance Call**]({% link _ols-1/week11.md %}) | |
| 12   | Mentor | 30 min | Week of April 6, 2020 |  [**Meet your mentor!**]({% link _ols-1/week12.md %}) | Invite an expert with mentor |
| 13   | Cohort | 90 min | April 15, 2020 (2pm CET) | [**Giving feedback & Project Review (preparation and practice)**]({% link _ols-1/week13.md %}) | Giving feedback, Preparation of final presentation |
| 14   | Mentor | 30 min | Week of April 20, 2020 | [**Meet your mentor!**]({% link _ols-1/week14.md %}) | Preparation for the final demos |
|      | Cohort | 90 min | April 22, 2020 (7pm CET) | [**Group 1 - Final presentation rehearsal**]({% link _ols-1/week14.md %}) | Test of the final demos for the group 1 |
| 15   | Cohort | 90 min | April 29, 2020 (7pm CET) | [**Group 1 - Final presentations & Graduation!**]({% link _ols-1/week15.md %}) | 5-minute demos of projects for group 1 (Audience: entire community & public, Open and recorded call) |
| 17   | Cohort | 90 min | May 13, 2020 (7pm CET) | [**Group 2 - Final presentation rehearsal**]({% link _ols-1/week17.md %}) | Test of the final demos for the group 2 |
| 18   | Cohort | 90 min | April 29, 2020 (7pm CET) | [**Group 2 - Final presentations & Graduation!**]({% link _ols-1/week18.md %}) | 5-minute demos of projects for group 2 (Audience: entire community & public, Open and recorded call) |

# Role Descriptions

## Mentees

Participants join this program with a project that they either are already working on or want to develop during this program. More details about the role of a mentee can be found [here](/about#mentees)

For the first round of the Open Life Science program, we are happy to have [{{ p-participants | size }} participants](/ols-1/projects-participants#participants) with [{{ projects | size }} projects](/ols-1/projects-participants#projects). 

## Mentors

Our mentees are supported in this program by our mentors' community who have been paired based on the compatibility of expertise and interests of mentors with the requests and requirements of our mentees. Our mentors are Open Science champions with previous experiences in training and mentoring. They are currently working in different professions in data science, publishing, community building, software development, clinical studies, industries, scientific training and IT services.

{{ p-mentors }}

<div class="people">
{% for entry in p-mentors %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

## Experts

Experts are invited to join cohort calls or individual mentorship calls to share their experience and expertise during the program.

<div class="people">
{% for entry in experts-speakers.experts %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

# Joining calls

**Cohort and mentor-only calls**: The calls will be hosted online using the Zoom web-conferencing option.

  Link for the calls will be shared for each meeting separately.

**Mentee-mentor calls**: You can use the online communication options that both mentor and mentee agree to use. A few options to explore are the following:
- Zoom: 40 mins limit for each call
- Google hangout: Free for members with google account
- Skype: Free, download the app
- Whereby.com: Free option, valid upto 4 participants

**If you can't make it to a call**:
- If you have to miss a call, please write your name in the cohort note under "apologies".

  The cohorts calls will be recorded each week and sent out with the review emails.

- If you miss two or more calls during the program, we'll evaluate if you would be able to finish the program.
- If a mentor has to miss a mentee-mentor meeting, please discuss it with your mentee and reschedule your call. 

  If you are unable to make it to any slot together, please find other ways (asynchronous documentation) to interact with your mentee.

# Mentoring training

Mentors advice and inspire
- Connect: to people, programs, companies
- Recommend: resources, readings, classes, experiences
- Feedback: for the mentee to consider

Becoming a mentor can be frightening. Mentors will be then guided specially via a mentoring training with 4 calls. Our mentors will gain mentoring skills (active listening, effective questioning, giving feedback) via mentoring training to learn to celebrate successes and approach challenges in mentoring.

# FAQ

## What meetings are taking place during the entire cohort?

Full cohort meetings
- Takes place every 2 weeks (unless mentioned otherwise)
- Duration: 90 minutes
- Organisers/hosts will introduce new topic of the week
- Speakers will present their work related to the topic of the week
- Mentees will be given group discussion exercises during the calls
- An open Q&A will be run and notes will be co-developed
- Exercises will be given for the week to be completed before the mentee-mentor meeting
- Look for cohort notes shared with you by organisers

Mentee-Mentor Meetings
- Takes place every 2 weeks (unless mentioned otherwise)
- Duration: 30 minutes
- Mentors help their mentees evaluate their understanding of the new topics
- Mentees will complete their task assigned at the cohort calls using new skills learned that week 
- Review progress together where mentees provide constructive feedback. 
- Connect with other experts and get consulted on their project when needed.
- Look for 1:1 notes shared with you by your mentor

Mentor-only Meetings
- A maximum of 4 calls will take place during the mentorship round
- 2 training calls in the beginning of the cohort to get participants trained and prepared for their role as mentors
- 1 catch-up call in the middle of the cohort to discuss new topics and challenges that might have occurred and address them
- 1 call at the end to capture experiences of mentors and assess their interest in future cohorts
- A public gitter channel will facilitate open discussions among mentors to help them discuss their experiences, challenges and tips and tricks

# Community Participation Guidelines

{% include CODE_OF_CONDUCT.md %}