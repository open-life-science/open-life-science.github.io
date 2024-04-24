---
layout: page
title: Team # & Community
image: /images/about.jpg
photos:
  name: Bérénice Batut
  license: CC BY-SA 4.0
  url: https://flic.kr/p/2gHNtNq
---

{% assign community = site.data.community %}
{% assign people = site.data.people %}

## Our values

We have high ethical standards, including:

- **Education**: Educate scientists about open science
- **Transparency**: Emphasize transparency and the sharing of resources, material, knowledge and experiences
- **Open science**: Promote citizen science and decentralized access to science
- **Modesty**: Know you don't know everything
- **Community**: Carefully listen to any concerns and questions and respond honestly
- **Respect**: Respect humans and all living systems
- **Responsibility**: Recognize the complexity and dynamics of science and research and our responsibility towards them

# Core team

<!--As the graduates, mentors, and hosts of various Mozilla Open Leaders cohorts, we have gained expertise in the technical and culture track. Furthermore, we participate in a wide range of activities in different international communities of practice in the sciences: ELIXIR (European bioinformatics network), Galaxy, The Carpentries, Software Sustainability Institute (SSI), Open Bioinformatics Foundation (OBF), and Mozilla.-->

<div class="people">
{% for entry in community.team.current %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

# Alumni

<div class="people">
{% for entry in community.team.alumni %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

<!--
# Informal advisors
Community leaders from different projects who take on advisory roles in OLS

<div class="people">
{% for entry in community.advisors %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

# Trainers

## OLS skills

<div class="people">
{% for entry in community.trainers.ols %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

## Ally skills

<div class="people">
{% for entry in community.trainers.ally %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

## Technical skills

<div class="people">
{% for entry in community.trainers.technical %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

# Task forces

## Hiring committee

<div class="people">
{% for entry in community.task_forces.hiring %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

## Localisation team

<div class="people">
{% for entry in community.task_forces.localization %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

-->

# Get involved

If you think you can help then please check out [our contributors'
guidelines]({{ site.github.repository_url }}/blob/master/CONTRIBUTING.md) and
our [project board]({{ site.github.repository_url }}/projects).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us
we ask that you follow our [code of conduct]({% link code-of-conduct.md %}) in all interactions both on and offline.
