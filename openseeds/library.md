---
layout: page
toc: true
title: Open Seeds Video Library
image: https://images.unsplash.com/photo-1481137344492-d5a150a97f8b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80
photos:
  name: Chris Lawton
  license: CC BY-SA 2.0
  url: https://unsplash.com/photos/Hys5qHaDbZQ
---

{% assign library = site.data.openseeds.library %}
{% assign video_nb = 0 %}
{% assign all-speakers = '' %}

<script type="application/ld+json" >
[
{%- assign sep="" -%}
{%- for topic in library -%}
    {%- for tag in topic[1] -%}
        {%- assign video_nb = video_nb | plus: tag[1].talks.size -%}
        {%- for v in tag[1].talks -%}
            {%- capture all-speakers -%}{{ all-speakers }},{{ v.speakers | join:"," }}{%- endcapture -%}
            {%- if v.recording -%}
                {%- assign speakers = '' -%}
                {%- for s in v.speakers -%}{% capture speakers %} {{ speakers }} {%- unless forloop.last -%},{%- endunless -%}{{ site.data.people[s].first-name }} {{ site.data.people[s].last-name }}{% endcapture %}{%- endfor -%}
    {{ sep }}{
        "@context": "https://schema.org",
        "@type": "LearningResource",
        "@id": "{{ topic[0] }}-{{ tag[0] }}-{{ forloop.index }}",
        "dct:conformsTo": {
            "https://purl.org/dc/terms/conformsTo": {
                "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE",
                "@type": "CreativeWork"
            }
        },
        "description": "Video from the talk '{{ v.title }}', by {{ speakers }}, on {{ v.date }}, in Open Seeds {{ v.cohort }} cohort",
        "keywords": ["Open Science", "{{ topic[0] }}", "{{ tag[0] }}"],
        "name": "Recording of the talk '{{ v.title }}', by {{ speakers }}, on {{ v.date }}",
        "educationalLevel": "Beginner",
        "inLanguage": "en-US",
        "learningResourceType": "video",
        "license": "https://creativecommons.org/licenses/by-sa/4.0/",
        "url": "{{ v.recording | replace: 'youtu.be/', 'youtube.com/embed/' | replace: '?t', '?start' }}",
        "contributor":  [
            {
                "@type": "Organization",
                "name": "Open Life Science",
                "email": "{{ site.email }}",
                "url": "{{ site.url }}"
            }
            {%- for s in v.speakers -%}
            ,{
                "@type": "Person",
                "name": "{{ site.data.people[s].first-name }} {{ site.data.people[s].last-name }}",
                "url": "{{ site.url }}/people#{{ s }}"
            }
            {%- endfor -%}
        ],
        "dateCreated": "{{ v.date | date: "%Y-%m-%d" }}",
        {%- if v.slides %}
        "hasPart": {
            "@type": "CreativeWork",
            "url": "{{ v.slides }}",
            "name": "Slides for the talk '{{ v.title }}', by {{ speakers }}, on {{ v.date }}"
        },
        {% endif -%}
        "isPartOf": {
            "@context": "https://schema.org",
            "@type": "Course",
            "@id": "{{ site.url }}/{{ v.cohort }}",
            "dct:conformsTo": {
                "https://purl.org/dc/terms/conformsTo": {
                    "@id": "https://bioschemas.org/profiles/Course/1.0-RELEASE",
                    "@type": "CreativeWork"
                }
            },
            "description": "{{ site.title }} is a mentoring mentoring & training program for Open Science ambassadors. It runs cohorts with calls every 1-2 weeks.",
            "keywords": "Open Science",
            "name": "Open Seeds {{ v.cohort }} cohort",
            "url": "{{ site.url }}/openseeds/{{ v.cohort }}",
            "educationalLevel": "Beginner",
            "inLanguage": "en-US",
            "provider":  [{
                "@type": "Organization",
                "name": "Open Life Science",
                "email": "{{ site.email }}",
                "url": "{{ site.url }}"
            }]
        }
    }
            {%- assign sep="," -%}
            {%- endif -%}
        {%- endfor -%}
    {%- endfor -%}
{%- endfor -%}
]
</script>

{% assign speaker_nb = all-speakers | remove_first: ',' | split: "," | uniq | sort | size %}

This page shows you the full library of available videos from talks in Open Seeds cohort calls: **{{ video_nb }} videos** by **{{ speaker_nb }} speakers**.

Below are all of the individual videos, but the videos are part of cohort calls that you can watch directly from the same links. You can use these for self-study, courses, and more!

{% for topic in library %}
    {% assign topic-name = topic[0] | slugify %}

## {{ topic[0] | replace: '-',' ' }}

    {% for tag in topic[1] %}
        {% assign tag-name = tag[0] | slugify %}
        {% capture parent_id %}{{ topic-name }}-{{ tag-name }}-{{ forloop.index }}{% endcapture %}

### {{ tag[0] | replace: '-',' ' }}

{{ tag[1].description }}

<div id="{{ parent_id }}">
        {% for video in tag[1].talks %}    
            {% if video.recording %}
                {% assign id = video.title | slugify %}
                {% capture card_id %}{{ parent_id }}-{{ forloop.index }}{% endcapture %}
                {% assign speakers = '' %}
                {% for s in video.speakers %}
                    {% assign speaker = site.data.people[s] %}
                    {% capture speakers %} {{ speakers }} {%- unless forloop.last -%},{%- endunless -%}{{ speaker.first-name }} {{ speaker.last-name }}{% endcapture %}
                {% endfor %}
    <div class="card">
        <header class="card-header">
            <p class="card-header-title">"{{ video.title }}" - {{ speakers }} - {{ video.date }}</p>
            <a href="#collapsible-card-{{ card_id }}" data-action="collapse" class="card-header-icon is-hidden-fullscreen" aria-label="more options">
                <span class="icon">
                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                </span>
          </a>
        </header>
        <div id="collapsible-card-{{ card_id }}" class="is-collapsible">
            <div class="card-content">
                <div class="columns">
                    <div class="column is-two-thirds">
                        <div>
                            <iframe
                                style="width:100%;height:100%;min-height:300px;"
                                src="{{ video.recording | replace: 'youtu.be/', 'youtube.com/embed/' | replace: '?t', '?start' }}"
                                title="YouTube video player"
                                frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                allowfullscreen>
                            </iframe>
                        </div>
                        <div style="margin-top:1em;" class="video-metadata">
                            <table>
                                <tr>
                                    <td><strong>Recorded</strong></td>
                                    <td>{{ video.date }}</td>
                                </tr>
                                {% if video.slides %}
                                <tr>
                                    <td><strong>Material</strong></td>
                                    <td><a href="{{ video.slides }}"><i class="fab fa-slideshare"></i> Slides</a></td>
                                </tr>
                                {% endif %}
                                <tr>
                                    <td><strong>Cohort</strong></td>
                                    <td><a href="{% link openseeds/{{ video.cohort }}/index.md %}">{{ video.cohort }}</a></td>
                                </tr>
                            </table>
                        </div>
                    </div>
                    <div class="column">
                        {% for username in video.speakers %}
                            {% assign user = speaker %}
                            {% include _includes/people.html user=speaker username=video.speaker %}
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
            {% endif %}
        {% endfor %}
    </div>
    {% endfor %}
{% endfor %}
