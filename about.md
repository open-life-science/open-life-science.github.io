---
layout: page
title: About
image: /images/about.jpg
photos:
  name: Bérénice Batut
  license: CC BY-SA 4.0
  url: https://flic.kr/p/2gHNtNq
---

This program can only run with the active involvements of our volunteer community who share a passion for Open Research and inclusiveness in Open Science:

- [Mentees](#mentees)
- [Mentors](#mentors)
- [Experts](#experts)
- [Organizers](#organizers)
- [Partners and sponsors](#partners-and-sponsors)

# Mentees

Our mentees are life science researchers and bioinformaticians who are interested in contributing to Open Science projects and communities. In this program they will be supported by the organisers, mentors, experts, and other mentees in getting started with their journey as Open Life Scientists.

**Our mentees will:**

- gain a better understanding of Open Science and best practices
- fill gaps related to Open Science in their research
- learn to navigate their path in bioinformatics communities
- design equitable opportunities in their projects for the diverse community members
- increase their visibility as Open Life Scientist
- become Open Science ambassadors for their community

## Becoming a mentee

A mentee dedicates about 2 hours per week to the program to attend cohort/mentor meetings and doing self-guided assignments.

Recruitment of the mentees will start in November. Stay tuned!

# Mentors

Mentors work closely with participants to help further their Open Science skills and become ambassadors for Open Science practice, training and education in their communities. The mentors will be assigned to one or more projects (based on their availability) proposed in the program.

**Our mentors are:**

- contributors of one or several Open Science projects or communities
- interested in sharing the benefit they receive from the Open Science communities
- look for opportunities to gain mentoring experience
- love to share their enthusiasm about Open Science
- want to build their profile as Open Leaders

## What do mentors do?

Mentors advise and inspire:
- **Connect** to people, programs
- **Recommend** resources, readings, experiences
- **Feedback** to consider

A mentor spend around **1 hour per week** dedicated to the program, but also some time before the program to review applications.

They will meet their mentees every two weeks during the program and will attend group calls with other mentors to exchange notes and develop their mentoring skills further.

## What are the benefits to be a mentor?

Our mentors will 

- gain mentoring skills (active listening, effective questioning, giving feedback) via mentoring training
- learn to celebrate successes and approach challenges in mentoring
- connect with a community of mentors
- expand their knowledge on Open Science

## Becoming a mentor

We are currently recruiting the mentors for the second round. Please reach out to one of the organizers if you are interested.

## Our mentors

Our program is only possible thanks to our awesome mentors:

<!-- OLS-1 -->
{% assign projects = site.data.ols-1-projects %}
{% assign mentors = '' %}
{% for project in projects %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-1-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
<!-- OLS-2 -->
{% assign projects = site.data.ols-2-projects %}
{% assign mentors = '' %}
{% for project in projects %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-2-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}
<!-- OLS-3 -->
{% assign projects = site.data.ols-3-projects %}
{% assign mentors = '' %}
{% for project in projects %}
    {% for m in project.mentors %}
        {% capture mentors %}{{ mentors }}, {{ m }}{% endcapture %}
    {% endfor %}
{% endfor %}
{% assign ols-3-mentors = mentors | remove_first: ', ' | split: ", " | uniq | sort %}

- [The {{ ols-1-mentors | size }} mentors for **OLS-1** (January to May 2020)](/ols-1#mentors)
- [The {{ ols-2-mentors | size }} mentors for **OLS-2** (September to December 2020)](/ols-2#mentors)
- [The {{ ols-3-mentors | size }} mentors for **OLS-3** (February to May 2021)](/ols-3#mentors)

# Experts

Experts will be invited to join cohort calls or individual mentorship calls to share their experience and expertise during the program.

**Our experts are:**

- motivated Open Life Scientists
- understand and advocate the value of working openly
- look for opportunities to support or give back to the research community
- enjoy sharing their resources to facilitate others work
- develop and teach skills collaboratively in the community
- want to gain/improve leadership skills through their engagements in this program

## Becoming an expert

Experts may be invited to:
- give a ~20 minute talk at one of our cohort calls, which happen every two weeks.
- be interviewed by the organisers (~15 minutes)
- invited by mentor-mentee pair to share their expert consultation on certain projects. (~30 minutes)

We are currently recruiting the experts for the second round.

## Our experts

Our experts are essential for the program:

{% assign ols-1-experts = site.data.ols-1-metadata.experts %}
{% assign ols-2-experts = site.data.ols-2-metadata.experts %}
{% assign ols-3-experts = site.data.ols-3-metadata.experts %}

- [The {{ ols-1-experts | uniq | size }} experts for **OLS-1** (January to May 2020)](/ols-1#experts)
- [The {{ ols-2-experts | uniq | size }} experts for **OLS-2** (September to December 2020)](/ols-2#experts)
- [The {{ ols-3-experts | uniq | size }} experts for **OLS-3** (February to May 2021)](/ols-3#experts)

# Cofounder

We are graduates, mentors, and hosts of various [Mozilla Open Leaders](https://foundation.mozilla.org/en/opportunity/mozilla-open-leaders/) cohorts, in which we have gained expertise in the technical and culture track.

{% assign organizers = site.data.ols-1-metadata.organizers %}
<div class="people">
{% for entry in organizers %}
    {% assign username = entry %}
    {% assign user = site.data.people[username] %}
    {% include _includes/people.html user=user username=username %}
{% endfor %}
</div>

We also participate in a wide range of activities in different international communities of practice in the life sciences:
- [ELIXIR (European bioinformatics network)](https://elixir-europe.org/)
- [Galaxy](https://galaxyproject.org/)
- [The Carpentries](https://carpentries.org/)
- [Software Sustainability Institute (SSI)](https://www.software.ac.uk/)
- [Open Bioinformatics Foundation (OBF)](https://www.open-bio.org/)
- [Mozilla](https://foundation.mozilla.org/en/)

## Our values

We have high ethical standards, including:

- **Education**: Educate scientists about open science
- **Transparency**: Emphasize transparency and the sharing of resources, material, knowledge and experiences
- **Open science**: Promote citizen science and decentralized access to science
- **Modesty**: Know you don't know everything
- **Community**: Carefully listen to any concerns and questions and respond honestly
- **Respect**: Respect humans and all living systems
- **Responsibility**: Recognize the complexity and dynamics of life science and research and our responsibility towards them

# Partners and sponsors

This program is made possible thanks to our partners and sponsors!

<div class="partners">
{% for entry in site.data.partners %}
    {% assign partnername = entry[0] %}
    {% assign partner = site.data['partners'][partnername] %}
    {% include _includes/partners.html partner=partner %}
{% endfor %}
</div>

# Get involved

If you think you can help then please check out [our contributors'
guidelines]({{ site.github.repository_url }}/blob/master/CONTRIBUTING.md) and
our [project board]({{ site.github.repository_url }}/projects).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us
we ask that you follow our [code of conduct]({% link code-of-conduct.md %}) in all interactions both on and offline.
