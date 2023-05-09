---
layout: page
title: OLS Video Library
image: https://images.unsplash.com/photo-1481137344492-d5a150a97f8b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80
photos:
  name: Chris Lawton
  license: CC BY-SA 2.0
  url: https://unsplash.com/photos/Hys5qHaDbZQ
---

This page shows you the full library of available OLS videos from talks in cohort calls. You can use these for self-study, courses, and more! 

Below are all of the individual videos, but the videos are part of cohort calls that you can watch directly from the same links.

{% assign library = site.data.library %}

<div class="accordion" id="accordionvideos">
{% for tag in library %}
    {% assign tag-name = tag[0] | slugify %}
	<h2 id="{{ tag-name }}">{{ tag[0] | replace: '-',' ' }}</h2>
    {% for subtag in tag[1] %}
        {% assign subtag-name = subtag[0] | slugify %}
        <h3 id="{{ subtag-name }}">{{ subtag[0] | replace: '-',' ' }}</h3>
        {% for video in subtag[1] %}
            {% include _includes/video.html video=video tag=tag-name subtag=subtag-name index=forloop.index %}
        {% endfor %}
    {% endfor %}
{% endfor %}
</div>