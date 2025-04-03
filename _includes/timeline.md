{% assign schedule = site.data[program][cohort].schedule %}

{% for e in schedule.timeline %}
{% assign type = '' %}
{% if e.type %}
    {% for t in e.type %}
        {% capture type %}{{ type }} + {% if t == 'Talk' %}<i class="fas fa-chalkboard-teacher"></i> Talk{% elsif t == 'Q&A' %}<i class="fas fa-question"></i> Q&A{% elsif t == 'Recording' %}<i class="fab fa-youtube"></i> Recording{% endif %}{% endcapture %}
    {% endfor %}
    {% assign type = type | remove_first: ' + ' %}
{% endif %}
{% if e.date %}
- **{{ e.date }}** {% if e.time %}([{{ e.time }} Universal Time](https://arewemeetingyet.com/UTC/{{ e.date | date: "%Y-%m-%d" }}/{{ e.time }}/OLS%20Application%20Call)){% endif %}: {{ e.description }}{% if e.type %}({{ type }}){% endif %}{% if e.notes %} - <i class="fas fa-clipboard"></i> [Notes with Zoom call link]({{ e.notes }}){% endif %}{% if e.recording %} - <i class="fab fa-youtube"></i> [Recording]({{ e.recording }}){% endif %}{% if e.details %}

    {{ e.details }}

{% endif %}
{% endif %}
{% endfor %}
- **{{ schedule.weeks['01'].start }}**: Start of the program

{% assign end = '' %}
{% for w in schedule.weeks %}
{% assign end = w[1].start %}
{% endfor %}
- **{{ end }}**: End of the program

