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
{% assign metadata = site.data.ols-1-metadata %}
{% assign schedule = site.data.ols-1-schedule %}

{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in projects %}
    {% assign p-pparticipants = '' %}
    {% for p in project.participants %}
        {% capture all-participants %}{{ all-participants}}, {{ p }}{% endcapture %}
    {% endfor %}
    {% for m in project.mentors %}
        {% capture all-mentors %}{{ all-mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}

{% assign p-participants = all-participants | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign p-mentors = all-mentors | remove_first: ', ' | split: ", " | uniq | sort %}

{% assign all-speakers = '' %}
{% for w in schedule %}
    {% for c in w[1].calls %}
        {% if c.type == 'Cohort' %}
            {% for r in c.resources %}
                {% if r.type == 'slides' %}
                    {% capture all-speakers %}{{ all-speakers}}, {{ r.speaker }}{% endcapture %}
                {% endif %}
            {% endfor %}
        {% endif %}
    {% endfor %}
{% endfor %}
{% assign p-speakers = all-speakers | remove_first: ', ' | split: ", " | uniq | sort %}

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

During the program,

- Mentors and mentees meet every 2 weeks [for a 30 minutes call](#mentor-mentee-calls)
- Mentees participate every 2 weeks to [90-minutes cohort calls](#cohort-calls) during which the program leaders introduce new topics and resources, facilitate break-out discussions, and invite experts from the field to give talks
- Mentors take part to [4 mentoring calls](#mentors-calls)

Organizers will inform participants of the week schedule by email.

Outside of the calls, participants (mentees, mentors, etc) are encouraged to discuss together via [Gitter](https://gitter.im/{{ site.gitter }}).  

<iframe class="calendar" src="https://calendar.google.com/calendar/embed?src=n3rqhvuff05ojkl0opfsvh49fk%40group.calendar.google.com"  frameborder="0" scrolling="no"></iframe>

[<i class="fas fa-calendar-plus"></i> *Subscribe to the OLS calendar*](https://calendar.google.com/calendar/r?cid=n3rqhvuff05ojkl0opfsvh49fk@group.calendar.google.com)

<!-- Any modification of the content should be done in the _data/ols-1-schedule.yaml file -->

| Week | Call | Date | Topic | Agenda |
|------|------|------|-------|--------|
{%- for w in schedule %}
{%- capture w-desc %}**Week {{ w[0] }}**: {{ w[1].timeframe }}{% endcapture %}
{%- for c in w[1].calls %}
{%- capture date %}{% if c.type == "Cohort" %}{{ c.date }} ([{{ c.time }} European Time](https://arewemeetingyet.com/Berlin/{{ c.date | date: "%Y-%m-%d" }}/{{ c.time }}/OLS-1%20Cohort%20Call%20(Week%20{{ w[0] }}))){% endif %}{% endcapture %}
| {{ w-desc }} | [{{ c.type }}](#{{ c.type | downcase | remove: "(" | remove: ")" | remove: "@" | remove: ":" | remove: "," | replace: " ", "-" }}-calls) | {{ date }} | [**{{ c.title }}**](/ols-1/week{{ w[0] }}) | {% if c.agenda %}{{ c.agenda }}{% endif %} |
{%- assign w-desc = "" %}
{%- endfor %}
{%- endfor %}

# Role Descriptions

## Mentees

Participants join this program with a project that they either are already working on or want to develop during this program. More details about the role of a mentee can be found [here](/about#mentees)

For the first round of the Open Life Science program, we are happy to have [{{ p-participants | size }} participants](/ols-1/projects-participants#participants) with [{{ projects | size }} projects](/ols-1/projects-participants#projects). 

## Mentors

Our mentees are supported in this program by our mentors' community who have been paired based on the compatibility of expertise and interests of mentors with the requests and requirements of our mentees. Our mentors are Open Science champions with previous experiences in training and mentoring. They are currently working in different professions in data science, publishing, community building, software development, clinical studies, industries, scientific training and IT services.

Mentors advice and inspire
- Connect: to people, programs, companies
- Recommend: resources, readings, classes, experiences
- Feedback: for the mentee to consider

<!-- Any modification of the content should be done in the _data/ols-1-projects.yaml file -->

<div class="people">
{% for entry in p-mentors %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

### Mentoring training

Becoming a mentor can be frightening. Mentors will be then guided specially via a mentoring training with 4 calls during the mentorship round:

- 2 training calls in the beginning of the cohort to get participants trained and prepared for their role as mentors
- 1 catch-up call in the middle of the cohort to discuss new topics and challenges that might have occurred and address them
- 1 call at the end to capture experiences of mentors and assess their interest in future cohorts

A public gitter channel will facilitate open discussions among mentors to help them discuss their experiences, challenges and tips and tricks

Our mentors will then gain mentoring skills (active listening, effective questioning, giving feedback) via mentoring training to learn to celebrate successes and approach challenges in mentoring.

## Experts

Experts are invited to join cohort calls or individual mentorship calls to share their experience and expertise during the program.

<!-- Any modification of the content should be done in the _data/ols-1-metadata.yaml file -->

<div class="people">
{% for entry in metadata.experts %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

### Speakers during cohort calls

<div class="people">
{% for entry in p-speakers %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

## Organizers

<div class="people">
{% for entry in metadata.organizers %}
    {% assign username = entry %}
    {% assign user = site.data.people[username] %}
    {% include _includes/people.html user=user username=username %}
{% endfor %}
</div>

# Calls

## Cohort calls

The full cohort meetings take place **every 2 weeks** (unless mentioned otherwise) and last for **90 minutes**.

During these calls:
- Organisers/hosts will introduce new topic of the week
- Speakers will present their work related to the topic of the week
- Participants will be given group discussion exercises
- An open Q&A will be run and notes will be co-developed

  Look for cohort notes shared with you by organisers

- Exercises will be given for the week to be completed before the mentee-mentor meeting

The calls will be hosted online using the Zoom web-conferencing option. A link for the calls will be shared for each meeting separately.

**If you can't make it to a call**:
- If you have to miss a call, please write your name in the cohort note under "apologies".

  The call will be recorded and available on the [OLS YouTube channel]({{ site.youtube }}) after the call.

- If you miss two or more calls during the program, we'll evaluate if you would be able to finish the program.

## Mentor-mentee calls

The Mentor-mentee calls take place **every 2 weeks** (unless mentioned otherwise) and last for **30 minutes**.

During these calls:
- Mentors help their mentees evaluate their understanding of the new topics
- Mentees will complete their task assigned at the cohort calls using new skills learned that week 
- Mentors and mentee will review progress together where mentees provide constructive feedback

  Look for 1:1 notes shared with you by your mentor

- Mentors will connect mentees with other experts and get consulted on their project when needed

The calls can use the online communication options that both mentor and mentee agree to use. A few options to explore are the following:
- Zoom: 40 mins limit for each call
- Google hangout: Free for members with google account
- Skype: Free, download the app
- Whereby.com: Free option, valid upto 4 participants

If a mentor has to miss a mentee-mentor meeting, please discuss it with your mentee and reschedule your call.

If you are unable to make it to any slot together, please find other ways (asynchronous documentation) to interact with your mentee.

## Mentors calls

4 mentor call take place during the program.

The calls will be hosted online using the Zoom web-conferencing option. A link for the calls will be shared for each meeting separately.

# Communication channels

## OLS-1 private Google group

Organizers inform participants of the week schedule by email. An archive of all emails can be found on the private OLS-1 Google group. 

An invitation is sent to all participants (mentees, mentors, etc) at the beginning of the program. If it is not the case, please [contact the team](mailto:{{ site.email }})

## Gitter

Outside of the calls, participants (mentees, mentors, etc) are encouraged to discuss together via [Gitter](https://gitter.im/{{ site.gitter }}).

## OLS Google group

Updates regarding new calls for applications, announcements, and final project presentations are posted on the [OLS public Google group]({{ site.announcement_list }})

# Community Participation Guidelines

{% include CODE_OF_CONDUCT.md %}
