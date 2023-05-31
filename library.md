---
layout: page
title: OLS Video Library
image: https://images.unsplash.com/photo-1481137344492-d5a150a97f8b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80
photos:
  name: Chris Lawton
  license: CC BY-SA 2.0
  url: https://unsplash.com/photos/Hys5qHaDbZQ
---

{% assign library = site.data.library %}

{% assign video_nb = 0 %}
{% assign speakers = '' %}
{% for tag in library %}
    {% for subtag in tag[1] %}
        {% assign video_nb = video_nb | plus: subtag[1].size %}
        {% for video in subtag[1] %}
            {% capture speakers %}{{ speakers }},{{ video.speakers | join:"," }}{% endcapture %}
        {% endfor %}
    {% endfor %}
{% endfor %}
{% assign speaker_nb = speakers | remove_first: ',' | split: "," | uniq | sort | size %}

This page shows you the full library of available OLS videos from talks in cohort calls: **{{ video_nb }} videos** by **{{ speaker_nb }} speakers**.

Below are all of the individual videos, but the videos are part of cohort calls that you can watch directly from the same links. You can use these for self-study, courses, and more! 

{% for topic in library %}
    {% assign topic-name = topic[0] | slugify %}
<h2 id="{{ topic-name }}">{{ topic[0] | replace: '-',' ' }}</h2>
    {% for tag in topic[1] %}
        {% assign tag-name = tag[0] | slugify %}
        {% capture parent_id %}{{ topic-name }}-{{ tag-name }}-{{ index }}{% endcapture %}
<h3 id="{{ tag-name }}">{{ tag[0] | replace: '-',' ' }}</h3>
<!-- Add description -->
<div id="{{ parent_id }}">
        {% for video in tag[1] %}
            {% include _includes/video.html video=video parent_id=parent_id index=forloop.index %}
        {% endfor %}
</div>
    {% endfor %}
{% endfor %}
