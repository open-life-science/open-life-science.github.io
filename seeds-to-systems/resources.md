---
layout: default
title: Seeds to Systems - Session Resources
description: Recordings, slides, and transcripts for each Seeds to Systems cohort session.
image: https://images.unsplash.com/photo-1440342359743-84fcb8c21f21?fm=jpg&q=80&w=1400&auto=format&fit=crop
photos:
  name: kazuend
  license: Unsplash License
  url: https://unsplash.com/@kazuend
---

<div class="seeds-to-systems">
{% include _includes/seeds-to-systems-subnav.html %}
<section class="section">
    <div class="container">
        <h2 class="section-title is-size-3">Session resources</h2>
        <p>Recordings, slides, and transcripts from each cohort session, added as they become available.</p>

        {% assign cohort_schedule = site.data['seeds-to-systems'].schedule %}
        {%- assign sorted_weeks = cohort_schedule.weeks | sort %}
        <div class="columns is-multiline" style="margin-top: 1.5rem;">
        {%- for w in sorted_weeks %}
        {%- for c in w[1].calls %}
            {%- include _includes/seeds-to-systems-resource-card.html call=c %}
        {%- endfor %}
        {%- endfor %}
        </div>
    </div>
</section>
</div>
