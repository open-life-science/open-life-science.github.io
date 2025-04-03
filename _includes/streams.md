<div class="columns is-multiline three-pillars">
    {% for stream in page.streams %}
    <div class="column is-one-third">
        <a href="#{{ stream.title | slugify }}">
            <div class="card stream-card">
                <div class="card-content">
                    {% if stream.image %}
                    <img src="{{ stream.image.link }}" alt="{{ stream.image.alt }}">
                    {% endif %}
                    <h2 class="title is-4">{{ stream.title }}</h2>
                    <p class="content" markdown=1>{{ stream.description | markdownify | strip_html | truncatewords: 20 }}</p>
                </div>
            </div>
        </a>
    </div>
  {% endfor %}
</div>

{% for stream in page.streams %}

## {{ stream.title }}

{{ stream.description }}

  {% if stream.key_personal %}
### Key personnel

{{ stream.key_personal.roles }}

<div class="people">
    {% for entry in stream.key_personal.ids %}
        {% assign username = entry %}
        {% assign user = site.data.people[entry] %}
        {% include _includes/people.html username=username user=user %}
    {% endfor %}
</div>

  {% endif %}

{% endfor %}