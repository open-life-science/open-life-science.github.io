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

Recruitment of the mentees will start in November. Stay tuned!

# Mentors

Mentors work closely with participants to help further their Open Science skills and become ambassadors for Open Science practice, training and education in their communities.

The mentors will be assigned to different projects proposed in the program. The mentors will meet  their mentees every two weeks during the program.

There will be group calls for mentors to exchange notes and developing their mentoring skills further.

**Our mentors are:**

- contributors of one or several Open Science projects or communities
- interested in sharing the benefit they receive from the Open Science communities
- look for opportunities to gain mentoring experience
- love to share their enthusiasm about Open Science
- want to build their profile as Open Leaders

## Becoming a mentor

We are currently recruiting the mentors for the first round. Please reach out to one of the organizers.

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

We are currently recruiting the experts for the first round.

# Organizers

We are graduates, mentors, and hosts of various [Mozilla Open Leaders](https://foundation.mozilla.org/en/opportunity/mozilla-open-leaders/) cohorts, in which we have gained expertise in the technical and culture track.
<div class="people">
{% for entry in site.data['people'] %}
    {% assign username = entry[0] %}
    {% assign user = site.data['people'][username] %}
    {% if user.organizer %}
      {% include people.html user=user username=username %}
    {% endif %}
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

This program is only possible thanks to our partners and sponsors:

- [de.NBI](https://www.denbi.de/) is supporting Bérénice and Malvika through in-kind contribution
- University of Manchester is supporting Yo for her Ph.D. research
- ELIXIR Training Platform
- [Mozilla foundation](https://foundation.mozilla.org/en/) is supporting via a Mozilla Open Leader program

# Get involved

If you think you can help in any of the areas listed above (and we bet you can)
or in any of the many areas that we haven't yet thought of (and here we're sure
you can) then please check out [our contributors'
guidelines]({{ site.github.repository_url }}/blob/master/CONTRIBUTING.md) and
our [roadmap]({{ site.github.repository_url }}/blob/master/roadmap.md).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us
we ask that you follow our [code of conduct]({{ site.github.repository_url
}}/blob/master/CODE_OF_CONDUCT.md) in all interactions both on and offline.
