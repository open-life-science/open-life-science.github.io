---
layout: post
title: "Launching the Open Seeds Video Library"
authors:
- bebatut
image: https://images.pexels.com/photos/114820/pexels-photo-114820.jpeg
photos:
  name: Mike Bird
  url: https://www.pexels.com/photo/elvis-presley-digital-wallpaper-114820/
  licence: CC-BY
---

{% assign cohort-calls = 0 %}
{% assign cohorts = site.data.openseeds | sort %}

{% for cohort in cohorts %}
    {% assign schedule = cohort[1].schedule %}
    {% for w in schedule.weeks %}
        {% for c in w[1].calls %}
            {% if c.type != "Mentor-Mentee" %}
                {% assign cohort-calls = cohort-calls | plus: 1 %}
            {% endif %}
        {% endfor %}
    {% endfor %}
{% endfor %}

{% assign library = site.data.openseeds.library %}
{% assign video_nb = 0 %}
{% assign all-speakers = '' %}
{% for topic in library %}
    {% for tag in topic[1] %}
        {% assign video_nb = video_nb | plus: tag[1].talks.size %}
        {% for v in tag[1].talks %}
            {% capture all-speakers %}{{ all-speakers }},{{ v.speakers | join:"," }}{% endcapture %}
        {% endfor %}
    {% endfor %}
{% endfor %}
{% assign speaker_nb = all-speakers | remove_first: ',' | split: "," | uniq | sort | size %}

Since its launch in 2020, OLS ran **7 cohorts**, **{{ cohort-calls }} cohort calls** with **{{ video_nb }} talks** by **{{ speaker_nb }} speakers**. The cohort calls are all available on [OLS YouTube channel]({{ site.youtube }}) and linked in the dedicated cohort schedule. But **all these talks were also interesting individually and are currently hard to find**.

To improve talk findability and give more visibility to these experts, we created the [**Open Seeds Video Library**]({% link openseeds/library.md %}). This page shows the full library of available videos from talks in Open Seeds cohort calls: **{{ video_nb }} videos** by **{{ speaker_nb }} speakers**, **organized by topic** (Open Science, Tooling for Collaboration, Project, Community & Personal Management, etc), **annotated** with the recording date, **information about the speakers**, and slidedeck link when available.

![Screenshot of the Open Seeds Video Library, showing the table of content on the left, the Open Science section on the middle with a talk on Open Hardware expanded](/images/2023-07-17-video-library-launching.png){: width="80%"}

The library is **automatically** created from the information listed in the schedule for each cohort, which is **updated every week**. In order to make this **Open Education Material more FAIR**, all videos, as the cohort calls in the schedule pages, are **annotated** with [**Bioschemas training profiles**](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011120), and will be listed on [ELIXIR TeSS (Training eSupport System) catalog](https://tess.elixir-europe.org/about).