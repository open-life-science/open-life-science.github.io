---
layout: page
title: Welcome to the 1st cohort of Nebula!
image: /images/syllabus.jpg
photos:
  name: Niklas Morberg
  license: CC BY-NC 2.0
  url: https://flic.kr/p/5BXB6s
toc: true
---

{% include _includes/cohort-metadata.html cohort='neb-1' program='nebula'  %}

# The NEB-1 program
{:.no_toc}

**Purpose**: Training for early stage researchers and young leaders interested in furthering their
Open Science skills

**Outcome**: Ambassadors for Open Science practice, training and education across multiple European
and international bioinformatics communities.

**Process**: A 15-week mentoring & training program, based on the [Mozilla Open Leader program](https://foundation.mozilla.org/en/opportunity/mozilla-open-leaders/), helping participants in becoming Open Science ambassadors by using three principles:

1. **Sharing** essential knowledge required to create, lead, and sustain an Open Science project.
2. **Connecting** members across different communities, backgrounds, and identities by creating space in this program for them to share their experiences and expertise.
3. **Empowering** them to become effective Open Science ambassadors in their communities.

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

OLS's first cohort (neb-1), was conducted from March 2024 until April 2024 with [{{ p-participants | size }} project leaders]({% link nebula/neb-1/projects-participants.md %}#participants) working on [{{ projects | size }} projects]({% link nebula/neb-1/projects-participants.md %}#projects).

{% include _includes/timeline.md %}

# Schedule

{% include _includes/overall-schedule.md %}

# Role Descriptions

## Mentees

Participants join this program with a project that they either are already working on or want to develop during this program. More details about the role of a mentee can be found [here]({% link nebula/index.md %}#mentees)

For the first round of the Open Life Science program, we are happy to have [{{ p-participants | size }} participants]({% link nebula/neb-1/projects-participants.md %}#participants) with [{{ projects | size }} projects]({% link nebula/neb-1/projects-participants.md %}#projects).

## Mentors

Our mentees are supported in this program by our mentors' community who have been paired based on the compatibility of expertise and interests of mentors with the requests and requirements of our mentees. Our mentors are Open Science champions with previous experiences in training and mentoring. They are currently working in different professions in data science, publishing, community building, software development, clinical studies, industries, scientific training and IT services.

Mentors advice and inspire
- Connect: to people, programs, companies
- Recommend: resources, readings, classes, experiences
- Feedback: for the mentee to consider

<!-- Any modification of the content should be done in the _data/neb-1-projects.yaml file -->

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

<!-- Any modification of the content should be done in the _data/neb-1-metadata.yaml file -->

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
    {% assign user = people[username] %}
    {% include _includes/people.html user=user username=username %}
{% endfor %}
</div>

# Community Participation Guidelines

{% include CODE_OF_CONDUCT.md %}