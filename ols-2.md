---
layout: page
title: Welcome to the 2nd cohort of Open Life Science program!
image: /images/syllabus.jpg
photos:
  name: Niklas Morberg
  license: CC BY-NC 2.0
  url: https://flic.kr/p/5BXB6s
---

{% assign people = site.data.people %}
{% assign projects = site.data.ols-2-projects %}
{% assign metadata = site.data.ols-2-metadata %}
{% assign schedule = site.data.ols-2-schedule %}
{% assign cohort = 'ols-2' %}

{% assign all-participants = '' %}
{% assign all-mentors = '' %}
{% for project in projects %}
{% assign p-participants = '' %}
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
{% assign all-hosts = '' %}
{% for w in schedule.weeks %}
{% for c in w[1].calls %}
{% if c.type == 'Cohort' %}
{% for r in c.resources %}
{% if r.type == 'slides' and r.speaker %}
{% capture all-speakers %}{{ all-speakers}}, {{ r.speaker }}{% endcapture %}
{% endif %}
{% endfor %}
{% endif %}
{% if c.hosts %}
{% for h in c.hosts %}
{% capture all-hosts %}{{ all-hosts}}, {{ h }}{% endcapture %}
{% endfor %}
{% endif %}
{% endfor %}
{% endfor %}
{% assign p-speakers = all-speakers | remove_first: ', ' | split: ", " | uniq | sort %}
{% assign p-hosts = all-hosts | remove_first: ', ' | split: ", " | uniq | sort %}

# The OLS-2 program

{:.no_toc}

**Purpose**: Training for early stage researchers and young leaders interested in furthering their
Open Science skills

**Outcome**: Ambassadors for Open Science practice, training and education across multiple European
and international bioinformatics communities.

**Process**: A 16-week mentoring & training program, based on the [Mozilla Open Leader program](https://foundation.mozilla.org/en/opportunity/mozilla-open-leaders/), helping participants in becoming Open Science ambassadors by using three principles:

1. **Sharing** essential knowledge required to create, lead, and sustain an Open Science project.
2. **Connecting** members across different communities, backgrounds, and identities by creating space in this program for them to share their experiences and expertise.
3. **Empowering** them to become effective Open Science ambassadors in their communities.

{% include _includes/toc.html %}

# Goals and Learning Objectives

The vision of Open Life Science program is to strengthen Open Science skills for early stage researchers and young leaders in life science.

At the end of the program, our participants will be able to:

- Describe and define the terms _openness_, _open science_, _open leadership_, _community interactions_, _value exchanges_, _inclusivity_, _accessibility_, _open Science practices in developing resources and training_
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

OLS's second cohort (OLS-2) will be conducted from September 2020 until December 2020.

{% include _includes/timeline.md %}

# Schedule

{% include _includes/overall-schedule.md %}

# Role Descriptions

## Project leads (aka Mentees)

Participants join this program with a project that they either are already working on or want to develop during this program. More details about the role of a project lead (mentee) can be found [here](/about#mentees).

For the second round of the Open Life Science program, we welcome [{{ p-participants | size }} participants](/ols-2/projects-participants#participants) with [{{ projects | size }} projects](/ols-2/projects-participants#projects).

## Mentors

Our project leads are supported in this program by our mentor-community who are paired based on the compatibility of expertise, interests and requirements of their projects.
Our mentors are Open Science practitioners and champions with previous experiences in training and mentoring. They are currently working in different professions in data science, publishing, community building, software development, clinical studies, industries, scientific training and IT services.

Mentors advise and inspire

- Connect: to people, programs, companies
- Recommend: resources, readings, classes, experiences
- Feedback: for the project leads to consider

<!-- Any modification of the content should be done in the _data/ols-2-projects.yaml file -->

<!--**Pool of mentors for OLS-2**

<div class="people">
{% for entry in metadata.possible-mentors %}
    {% assign username = entry %}
    {% assign user = site.data.people[username] %}
    {% include _includes/people.html user=user username=username %}
{% endfor %}
</div>-->

<div class="people">
{% for entry in p-mentors %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

### Mentoring training

Mentorship roles can sound like a big personal responsibility and can be overwhelming for new mentors.
To support our mentors in this program, we will offer training, topic-based guided discussions and opportunity for social interaction over 4 calls during the mentorship round:

- 2 training calls in the beginning of the cohort to get participants trained and prepared for their role as mentors
- 1 catch-up call in the middle of the cohort to discuss new topics and challenges that might have occurred and address them
- 1 call at the end to capture experiences of mentors and assess their interest in future cohorts
- Social and co-working calls schedule will be agreed among the mentors as per their needs and interests

In the mentor training, our mentors will then gain mentoring skills (active listening, effective questioning, giving feedback), learn to celebrate successes and gain confidence on navigating challenges in mentoring.

A dedicated slack channel will facilitate open discussions among mentors to help them discuss their experiences, challenges and tips and tricks (contact the team if you are not yet on this channel).

## Experts

Experts are invited to join cohort calls or individual mentorship calls to share their experience and expertise during the program.

<!-- Any modification of the content should be done in the _data/ols-2-metadata.yaml file -->

<div class="people">
{% for entry in metadata.experts %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

A dedicated slack channel will facilitate open discussions among experts and other participants in OLS-2 to help them expand their network while discussing relevant topics (contact the team if you are not yet on this channel).

{% if all-speakers != '' %}

### Speakers during cohort calls

<div class="people">
{% for entry in p-speakers %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
{% endif %}

## Organizers

<div class="people">
{% for entry in metadata.organizers %}
    {% assign username = entry %}
    {% assign user = site.data.people[username] %}
    {% include _includes/people.html user=user username=username %}
{% endfor %}
</div>

{% if all-hosts != '' %}

### Hosts for calls

<div class="people">
{% for entry in p-hosts %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>
{% endif %}

# Collaborators

OLS team have established the following collaborations to support organisation specific projects within the OLS-2 cohort:

## OLS-2 for Turing

Under the collaboration name **OLS-2 for Turing**, Open Life Science has partnered with [_The Turing Way_](https://github.com/alan-turing-institute/the-turing-way), a project within the [Tools, Practices and Systems Research Program](https://www.turing.ac.uk/research/research-programmes/tools-practices-and-systems) in [The Alan Turing Institute](https://www.turing.ac.uk/).

This partnership will offer training and mentoring to interested members from Turing and _The Turing Way_ communities to join the second cohort (OLS-2) individually or in teams.
They will have an opportunity to develop Open Science aspects in the projects that they either already have been working on, or want to develop in the near future.
Mentors will be preferably selected from The Alan Turing Institute but there will be a possibility to match projects with the right mentor from the broader cohort.
The roles and benefits for the participants and the eligibility of proposed projects will be as described for our main program.

Since this partnership was announced close to the deadline of the OLS-2 application call, we will welcome applications for **OLS-2 for Turing** projects until **15 July 2020** via [EasyChair](https://easychair.org/conferences/?conf=ols2).
This extension in deadline will ensure that the interested participants have sufficient time to discuss their plans with their supervisors within the organisation.

To share this announcement with the potential mentors, experts and project leads from the Turing and _The Turing Way_, please use our [promotion pack](https://tinyurl.com/tw-ols2).

# Resources

The resources available to the OLS-2 cohort members will facilitate their communication, training, mentoring and learning process during their participation in the program.

## Calls

### Cohort calls

The full cohort meetings take place **every 2 weeks** (unless mentioned otherwise) and last for **90 minutes**.

During these calls:

- Organisers/hosts will introduce new topic of the week
- Speakers will present their work related to the topic of the week
- Participants will be given group discussion exercises
- An open Q&A will be run and notes will be co-developed
- Exercises will be given for the week to be completed before the mentee-mentor meeting

The calls will be hosted online using the Zoom web-conferencing option.
A link for the calls will be shared for each meeting separately.

Look up the shared notes for each call linked to the [schedule](#schedule) in this website.
You will also be updated via email each week by the organisers with additional details to aid your participation.

**If you can't make it to a call**:

The call will be recorded and available on the [OLS YouTube channel]({{ site.youtube }}) after the call.

If you can not attend most calls during the program due to the time zone incompatibility or other personal obligation, please let the organisers know.
If you are unable to communicate with your mentor regularly or do not engage in the program as planned, we may need to evaluate if you are able to finish the program.

### Mentor-mentee calls

The Mentor-mentee calls take place **every 2 weeks** (unless mentioned otherwise) and last for **30 minutes**.

During these calls:

- Mentors help their mentees evaluate their understanding of the new topics
- Mentees will complete their task assigned at the cohort calls using new skills learned that week
- Mentors and mentee will review progress together where mentees provide constructive feedback
- Mentors will connect mentees with other experts and get consulted on their project when needed

Coordinate with your mentor how you manage the notes and assignments for your 1:1 calls.

The online communication options can be agreed upon by the mentor-mentee pairs.
A few options to explore are the following:

- Zoom: 40 mins limit for each call
- Google hangout: Free for members with google account
- Skype: Free, download the app
- Whereby.com: Free option, valid upto 4 participants
- [Jitsi](https://meet.jit.si/): Free, open source web-based call is possible
- Whatsapp or other phone-based calls: Only if both mentor and mentee are comfortable with exchanging numbers

If a mentor has to miss a mentee-mentor meeting, please discuss it with your mentee and reschedule your call.
If you are unable to make it to any slot together, please find other ways (asynchronous documentation) to interact with your mentee.

If a mentor has to step back from the program for any reason, please communicate with the organisers to identify an alternative for their mentees.

### Skill-up calls

In some weeks during which there is not cohort call, we will offer some optional skill-up calls.

The calls will be hosted online using the Zoom web-conferencing option.
A link for the calls will be shared for each meeting separately.

Look up the shared notes for each call linked to the [schedule](#schedule) in this website.
You will also be updated via email each week by the organisers with additional details to aid your participation.

### Coworking calls

The coworking sessions take place in weeks during which there is not cohort call.
These calls are optional but highly valuable for enhancing your understanding of the materials discussed in OLS-2 with the help of other participants.

During these calls,

- Participants can work together on the assignments
- Participants connect and talk about their projects

The calls will be hosted online using the Zoom web-conferencing option. A link for the calls will be shared for each meeting separately.

### Mentor calls

4 mentor calls will take place during the program.

The calls will be hosted online using the Zoom web-conferencing option. A link for the calls will be shared for each meeting separately.

## OLS Speaker Guide

We have [a short guide for invited speakers]({% link _ols-2/speaker-guide.md %}).

## Communication channels

### Communication within the cohort members

#### OLS-2 Slack Channel

A dedicated Slack channel has been setup to facilitate real-time as well as asynchronous communication among the all members of the OLS-2 cohort.
A personal invitation link will be shared with the participants via an email.

#### OLS-2 private Google group

Organizers inform participants of the week schedule by email. An archive of all emails can be found on the private OLS-2 Google group.

An invitation is sent to all participants (mentees, mentors, etc) at the beginning of the program. If it is not the case, please [contact the team](mailto:{{ site.email }})

### Communication with members not in the cohort

#### Twitter

General updates from the program such as new posts, collaborations and relevant retweets will be shared via our [official Twitter channel](https://twitter.com/{{ site.twitter }}).

#### Gitter

We have a public [Gitter](https://gitter.im/{{ site.gitter }}) channel that can be used by members of the public contact the OLS team and community.

#### OLS Google group

Updates regarding new calls for applications, announcements, and final project presentations are posted on the [OLS public Google group]({{ site.announcement_list }})

# Community Participation Guidelines

{% include CODE_OF_CONDUCT.md %}
