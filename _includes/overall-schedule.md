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
  "@id": "https://4000-docelijah-openlifescien-imqv6d2ud7l.ws-eu71.gitpod.io/ols-6/schedule/",
  "@type": "Course",
  "dct:conformsTo": "https://bioschemas.org/profiles/Course/0.9-DRAFT-2020_12_08",
  "description": "The OLS program is for people interested in applying open principles in their work and becoming Open Science ambassadors in their communities.",
  "hasCourseInstance": [
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Welcome to OLS",
      "endDate": "2022-10-05",
      "location": "online",
      "startDate": "2022-09-27"
    },
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Tooling and roadmapping for Open projects",
      "endDate": "",
      "location": "online",
      "startDate": "2022-10-12"
    },
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Open Science I: Project Development and Introduction to Working Open",
      "endDate": "",
      "location": "online",
      "startDate": "2022-10-25"
    },
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Community design for inclusivity",
      "endDate": "",
      "location": "online",
      "startDate": "2022-11-09"
    },
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Open Science II: Knowledge Dissemination",
      "endDate": "",
      "location": "online",
      "startDate": "2022-11-22"
    },
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Diversity and Inclusion & Ally skills",
      "endDate": "",
      "location": "online",
      "startDate": "2022-12-07"
    },
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Open Science III: Next steps - applying FAIR research principles",
      "endDate": "",
      "location": "online",
      "startDate": "2022-12-20"
    },
    {
      "@context": "https://schema.org",
      "@type": "CourseInstance",
      "dct:conformsTo": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06",
      "courseMode": "Final presentations & Graduation",
      "endDate": "2023-01-18",
      "location": "online",
      "startDate": "2023-01-17"
    }
  ],
  "keywords": "OLS, Working Open, Cohorts",
  "name": "Cohorts Call"
}
</script >

