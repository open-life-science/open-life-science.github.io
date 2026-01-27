---
layout: page
title: 'OLS Collaborative Research'
description: Collaborative research projects led by OLS in partnership with other organizations.
image: https://images.unsplash.com/photo-1627686376555-1c60617dbda8
photos:
  name: Townsend Walton
  license: Unsplash License
  url: https://unsplash.com/@twalton
---


{% assign community = site.data.community %}
{% assign people = site.data.people %}

## OSPARK 

In collaboration with [Digital Research Academy (DRA)](https://digital-research.academy/), the OLS team will contribute to the Open Science Promotion and Advocacy for Research Knowledge (OSPARK) project.

Started in 2025, this 2-year initiative is funded through the [Open Science Clusters’ Action for Research and Society (OSCARS)](https://oscars-project.eu/), and represents our approach to equipping the Open Science community with practical marketing and communication skills to help create visibility for services provided by research support infrastructures as well as for researchers and their research findings.

The OSPARK project aims to develop a training program implemented in a multi-week bootcamp with both online and onsite participation to empower members of the OSCARS Science Clusters and the broader Open Science community with evidence-based marketing and communication skills.

In the first year of the project, the curriculum for the bootcamp will be developed based on research into both current best-practices and knowledge from experts in the field. Once the curriculum is developed, the bootcamp will be iteratively implemented in the second year to fine-tune the curriculum and participant experience.

Read more about the OSPARK project on the [OSCARS Project Website](https://oscars-project.eu/projects/ospark-bootcamp-open-science-promotion-and-advocacy-research-knowledge-bootcamp)

Watch [our video](https://www.youtube.com/watch?v=qMN0zPF653Y) (from OSCARS YouTube channel).

Sign up for [the mailing list](https://digiresacademy.kit.com/b9b1ac6ad1), to keep up-to-date on OSPARK bootcamp developments.

For specific inquiries, please contact us at [ospark-project[at]digiresacademy.org](mailto:ospark-project@digiresacademy.org).

### Researchers

<div class="people">
{% for entry in community.ospark %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

## Previous Projects

### Skills Policy Research

Funded by the [Turing Skills Policy Award (SPA) 2023/2024](https://www.turing.ac.uk/skills-policy-awards-20232024), this research was carried out to engage with and influence institional policies with a goal to widen participation in open data science. The research involved literature review, policy landscape analysis and participatory workshop to inform outputs listed below.

#### Outputs

- **Policy Briefings:**
  - Sundukova, M., Azevedo, F., Chimpén-López, C. A., Iley, B., & Yehudi, Y. (2024). Policy brief: Widening participation in data science: implementing policy for well-being in the workplace. Zenodo. [https://doi.org/10.5281/zenodo.12759410](https://doi.org/10.5281/zenodo.12759410)
  - Iley, B., Azevedo, F., Bennett, A., GOKTAS, P., Kiersz, D. A., Sundukova, M., Unshur, A., & Yehudi, Y. (2024). Policy brief: Equitable & Inclusive Team Science. Zenodo. [https://doi.org/10.5281/zenodo.15302045](https://doi.org/10.5281/zenodo.15302045)

#### Researchers

<div class="people">
{% for entry in community.turingspa %}
    {% assign username = entry %}
    {% assign user = people[username] %}
    {% include _includes/people.html username=username user=user %}
{% endfor %}
</div>

