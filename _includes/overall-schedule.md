During the program,

- Mentors and mentees meet every 2 weeks [for a 30 minutes call](/{{ cohort }}#mentor-mentee-calls)
- Mentees participate every ~2 weeks to [90-minutes cohort calls](/{{ cohort }}#cohort-calls) during which the program leaders introduce new topics and resources, facilitate break-out discussions, and invite expert from the field to give talks
- Mentees can participate to skill-up, Q&A or coworking session in the weeks without cohort calls
- Mentors take part to [mentoring workshop and calls](/{{ cohort }}#mentor-calls)

![OLS schedule overview. In the middle, the timeline represents the 16 weeks. On the top, boxes in green represent the 8 different cohort calls pointing to the corresponding weeks (even week numbers). Below the week timeline, blue boxes represent the mentor-mentee meetings pointing to the uneven number weeks. Below the blue boxes, are red boxes corresponding to 3 skill-up calls: "GitHub tutorial for beginners" (week 5), "Open Leadership: Academia, industry, and beyond" (week 9), "Self-care & social call" (week 1s)](/images/schedule.png){: .schedule-overview}

Organizers will inform participants of the week schedule by email.

<iframe src="https://calendar.google.com/calendar/embed?height=400&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=Europe%2FParis&amp;src=b3BlbmxpZmVzY2lAZ21haWwuY29t&amp;color=%23EF6C00&amp;mode=AGENDA&amp;showNav=0&amp;showTitle=0&amp;showPrint=0&amp;showTabs=1&amp;showCalendars=0" style="border-width:0" width="1152" height="600" frameborder="0" scrolling="no"></iframe>

[<i class="fas fa-calendar-plus"></i> *Subscribe to the OLS calendar*](https://calendar.google.com/calendar?cid=b3BlbmxpZmVzY2lAZ21haWwuY29t)

<!-- Any modification of the content should be done in the _data/ols-X-schedule.yaml file -->

| Week | Call | Date | Topic | Agenda |
|------|------|------|-------|--------|
{%- for w in schedule.weeks %}
{%- capture w-desc %}**Week {{ w[0] }}** (start. {{ w[1].start }}){% endcapture %}
{%- for c in w[1].calls %}
{%- capture date %}{% if c.type != "Mentor-Mentee" %}{{ c.date }} {% if c.time %}([{{ c.time }} European Time](https://arewemeetingyet.com/Berlin/{{ c.date | date: "%Y-%m-%d" }}/{{ c.time }}/{{ cohort }}%20{{ c.type }}%20Call%20(Week%20{{ w[0] }}))){% endif %}{% endif %}{% endcapture %}
| {{ w-desc }} | [{{ c.type }}](/{{ cohort }}#{{ c.type | downcase | remove: "(" | remove: ")" | remove: "@" | remove: ":" | remove: "," | replace: " ", "-" | remove: "&"  }}-calls) | {{ date }} | [**{{ c.title }}**](/{{ cohort }}/schedule#week-{{ w[0] }}) | {% if c.agenda %}{{ c.agenda }}{% endif %} |
{%- assign w-desc = "" %}
{%- endfor %} 
{%- endfor %} 

<script type="application/ld+json" >
{
  "@context": "https://schema.org",
  "@id": "{{ site.url }}/{{ cohort }}/schedule",
  "@type": "Course",
  "dct:conformsTo": "https://bioschemas.org/profiles/Course/0.9-DRAFT-2020_12_08",
  "description":"{{site.description}}" ,
    "hasCourseInstance": [
        {% for w in schedule.weeks %}
        {%- for c in w[1].calls %}
        {% if c.type != "Mentor-Mentee" %}
        | {{ w-desc }} | {{ c.type }} | {{ date }} | [{{ c.title }}]|{{c.duration}}| {% if c.agenda %}{{ c.agenda }}{% endif %} |
       
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": ["online", "synchronous"],
      "startDate" : "{{c.date}}",
      "endDate" :"{{c.date}}",
      "duration": "{{c.duration}}",
      "name" : "{{c.title}}"
    }
 {%- endfor %} 
{%- endfor %}
  ],

  "keywords": "OLS, Working Open, Cohorts",
  "name": "Cohorts Call for {{cohort}}"
}
</script >

