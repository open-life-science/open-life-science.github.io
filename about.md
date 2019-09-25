---
layout: page
title: About us
image: /images/about.jpg
photos:
  name: Bérénice Batut
  license: CC BY-SA 4.0
  url: https://flic.kr/p/2gHNtNq
---

# Mentors

Mentors work closely with participants to help further their Open Science skills and become ambassadors for Open Science practice, training and education in their communities. 

## Becoming a mentor

We are currently recruiting the mentors for the first round.

If you think yourself as a mentor for Open Science then fill the [following form]().

# Organizers

Our team members share a passion for Open Research and inclusiveness in Open Science.

We are graduates, mentors, and hosts of various Mozilla Open Leaders cohorts, in which we have gained expertise in the technical and culture track. Furthermore, we participate in a wide range of activities in different international communities of practice in the life sciences: ELIXIR (European bioinformatics network), Galaxy, The Carpentries, Software Sustainability Institute (SSI), Open Bioinformatics Foundation (OBF), and Mozilla.

<div class="people">
{% for entry in site.data['people'] %}
    {% assign username = entry[0] %}
    {% assign user = site.data['people'][username] %}
    {% if user.organizer %}
      {% include people.html user=user username=username %}
    {% endif %}
{% endfor %}
</div>

# Our values

We have high ethical standards, including:

- **Education**: Educate the researcher about HTS data analyse, reproducibility, open science
- **Transparency**: Emphasize transparency and the sharing of resources, material, knowledge and experiences
- **Open science**: Promote citizen science and decentralized access to science
- **Modesty**: Know you don't know everything
- **Community**: Carefully listen to any concerns and questions and respond honestly
- **Respect**: Respect humans and all living systems
- **Responsibility**: Recognize the complexity and dynamics of life science and research and our responsibility towards them

# What do we need?

**You!** In whatever way you can help.

## Get involved

If you think you can help in any of the areas listed above (and we bet you can)
or in any of the many areas that we haven't yet thought of (and here we're sure
you can) then please check out [our contributors'
guidelines]({{ site.github.repository_url }}/blob/master/CONTRIBUTING.md) and
our [roadmap]({{ site.github.repository_url }}/blob/master/roadmap.md).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us
we ask that you follow our [code of conduct]({{ site.github.repository_url
}}/blob/master/CODE_OF_CONDUCT.md) in all interactions both on and offline.

# Partners and sponsors

Supporting Partners
- [de.NBI](https://www.denbi.de/) is supporting Bérénice and Malvika through in-kind contribution
- University of Manchester is supporting Yo for her Ph.D. research
- ELIXIR Training Platform
- [Mozilla foundation](https://foundation.mozilla.org/en/) is supporting via a Mozilla Open Leader program