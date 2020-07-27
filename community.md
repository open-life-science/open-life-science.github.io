---
layout: page
title: Community
---

Thank You! to the {{ site.data.people | size }} awesome persons who participate(d) to Open Life Science! 


<div class="community">
{% for user in site.data.people %}
  {% assign username = user[0] %}
  {% assign details = user[1] %}
<div class="card people-card" id="{{ username }}">
  <div class="card-content">
    <div class="media">
      <div class="media-left people-card-avatar">
        <figure class="image is-48x48">
          <img
            class="is-rounded"
            src="https://avatars.githubusercontent.com/{{ username }}"
            alt="The GitHub avatar of {{ details.name }}"
          />
        </figure>
      </div>
    </div>
  </div>
</div>
{% endfor %}
</div>
