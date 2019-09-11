---
layout: page
title: About us
---

We are working to create a mentoring program for individuals interested in becoming ambassadors for Open Science practice, training and education in their communities.

Our outcome is to train early stage researchers and young leaders interested in furthering their Open Science skills to becoming ambassadors for Open Science practice, training and education in their communities.

# A mentoring program for Open Science in Life Science

Our aim to to train early stage researchers and young leaders interested in furthering their Open Science skills to becoming ambassadors for Open Science practice, training and education across multiple European and international bioinformatics communities. 

We will help participants of this program in becoming open leaders by using three principles:

1. **Sharing** essential knowledge required to create, lead, and sustain an Open Source project.
2. **Connecting** members across different communities, backgrounds, and identities by creating space in this program for them to share their experiences and expertise.
3. **Empowering** them to become effective Open Science Leaders in their communities as ambassadors for Open Science practices.

# Who are we?

Our team members share a passion for Open Research and inclusiveness in Open Science:

<div class="people">
{% for entry in site.data['people'] %}
    {% assign username = entry[0] %}
    {% include people.html username=username %}
{% endfor %}
</div>

As the graduates, mentors, and hosts of various Mozilla Open Leaders cohorts, they have gained expertise in the technical and culture track. Furthermore, they participate in a wide range of activities in different international communities of practice in the life sciences: ELIXIR (European bioinformatics network), Galaxy, The Carpentries, Software Sustainability Institute (SSI), Open Bioinformatics Foundation (OBF), and Mozilla.

## Partners and sponsors

Supporting Partners
- [de.NBI](https://www.denbi.de/) is supporting Bérénice and Malvika through in-kind contribution
- University of Manchester is supporting Yo for her Ph.D. research
- ELIXIR Training Platform
- [Mozilla foundation](https://foundation.mozilla.org/en/) is supporting via a Mozilla Open Leader program

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

We need expertise in open-science, training, mentoring, communication. We'd love your feedback along the way, and of course.

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

You are very welcomed and invited to join the community: Come and chat with us on [Gitter](https://gitter.im/{{ site.gitter }}).