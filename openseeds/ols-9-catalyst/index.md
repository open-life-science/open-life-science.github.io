---
layout: page
title: Welcome to Open Seeds Cohort 9 - Catalyst track
image: /images/syllabus.jpg
photos:
  name: Niklas Morberg
  license: CC BY-NC 2.0
  url: https://flic.kr/p/5BXB6s
toc: true
---



{% include _includes/cohort-metadata.html cohort='ols-9-catalyst' program='openseeds' %}

# Timeline

{% include _includes/timeline.md %}

# Schedule

{% include _includes/overall-schedule.md %}

# Role Descriptions

## Project leads (aka Mentees)


<!-- For the ninth round of the Open Seeds program, we welcome [{{ p-participants | size }} participants](/ols-9/projects-participants#participants) with [{{ projects | size }} projects](/ols-9/projects-participants#projects).-->

## Mentors

Our project leads are supported in this program by our mentor-community who are paired based on the compatibility of expertise, interests and requirements of their projects.
Our mentors are Open Science practitioners and champions with previous experiences in training and mentoring. They are currently working in different professions in data science, publishing, community building, software development, clinical studies, industries, scientific training and IT services.

Mentors advise and inspire
- Connect: to people, programs, companies
- Recommend: resources, readings, classes, experiences
- Feedback: for the project leads to consider

We thank the {{ p-mentors | size }} mentors this round.
<div class="people">
{% for entry in p-mentors %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div> 

## Experts

Experts are invited to join cohort calls or individual mentorship calls to share their experience and expertise during the program.

<!-- Any modification of the content should be done in the _data/ols-9-metadata.yaml file -->

We thank the **{{ metadata.experts | size }} persons who registered to be experts** in this round.

<div class="people">
    {% for mentor in metadata.experts %}
        {% assign username = mentor %}
        {% assign user = site.data.people[username] %}
        {% include _includes/people.html user=user username=username %}
    {% endfor %}
</div>

{% if metadata.experts-with-expertise %}

<div class="expertise">
    <h4 class="expertise-detail-question">
        <a class="expertise-detail-toggle">
            Experts sorted by their expertise areas
            <i class="fa fa-angle-down"></i>
        </a>
    </h4>
    <ul class="expertise-detail is-hidden">
        {% for expertise in metadata.experts-with-expertise %}
        <li class="expertise-question">
            <a class="expertise-toggle">
                {{ expertise[0] }}
                <i class="fa fa-angle-down"></i>
            </a>
            <div class="peoples is-hidden">
                <div class="people">
                {% for mentor in expertise[1] %}
                    {% assign username = mentor %}
                    {% assign user = site.data.people[username] %}
                    {% include _includes/people.html user=user username=username %}
                {% endfor %}
                </div>
            </div>
        </li>
        {% endfor %}
    </ul>
</div>
{% endif %}

A dedicated slack channel will facilitate open discussions among experts and other participants in OLS-9 to help them expand their network while discussing relevant topics (contact the team if you are not yet on this channel).

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

### Facilitators

Facilitators work closely with the OLS organisers to manage and run cohort calls. They lead efforts in preparing cohort call notes, co-hosting cohort calls and ensuring the sharing of call recordings and resources through OLS channelss

<!-- Any modification of the content should be done in the _data/ols-9-metadata.yaml file -->

We thank the **{{ metadata.facilitators | size }} persons who facilitated** in this round.

<div class="people">
    {% for p in metadata.facilitators %}
        {% assign username = p %}
        {% assign user = site.data.people[username] %}
        {% include _includes/people.html user=user username=username %}
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

# Collaborators

This cohort is a [joined effort]({% link _posts/2023-08-15-OLS-joining-forces-with-communities-to-broaden-participation-in-open-science.md %}) between OLS and 3 international organisations and communities:
- Africa-OLS with [Bioinformatics Hub of Kenya initiative (BHKi)](https://bhki.org/) amd the South African Center for Digital Language Resources [(SADiLaR)](https://sadilar.org/index.php/en/) via the [ESCALATOR programme](https://escalator.sadilar.org/)
- [VU Amsterdam](https://vu.nl/en)
- [MetaDocencia](https://www.metadocencia.org/)

# Resources

The resources available to the OLS-9 cohort members will facilitate their communication, training, mentoring and learning process during their participation in the program.

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

Look up the shared notes for each call linked to the [schedule]({% link openseeds/ols-9-catalyst/schedule.md %}) in this website.
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

Look up the shared notes for each call linked to the [schedule]({% link openseeds/ols-9-catalyst/schedule.md %}) in this website.
You will also be updated via email each week by the organisers with additional details to aid your participation.

## Q&A calls

The Q&A sessions take place in weeks during which there is not cohort call.
These calls are optional but highly valuable for enhancing your understanding of the materials discussed in OLS-4 with the help of other participants.

The calls will be hosted online using the Zoom web-conferencing option. A link for the calls will be shared for each meeting separately.

### Mentor calls

4 mentor calls will take place during the program.

The calls will be hosted online using the Zoom web-conferencing option. A link for the calls will be shared for each meeting separately.

## Speaker Guide

We have [a short guide for invited speakers]({% link openseeds/ols-9-dra/speaker-guide.md %}).


# Community Participation Guidelines

{% include CODE_OF_CONDUCT.md %}