---
layout: page
title: Our Knowledge Management System
image: https://images.unsplash.com/photo-1557201874-98d4f7c33eb3?q=80&w=3270&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
toc: true
photos:
  name: Kumiko SHIMIZU
  license: Unsplash License
  url: https://unsplash.com/photos/closeup-photo-of-grey-gear-part-n55IHMpkSoc
---

Information and data about our different programs, our community, etc are managed via repositories in a [GitHub organization]({{ site.github.owner_url }}), [CiviCRM](https://civicrm.org/), and documents stored in Google Drive.

# OLS community

## Individuals

Individuals who participated in an OLS activity are listed in [People page]({% link people.md %}). This page is generated from the data stored in the `_data/people.yml` file that are extracted from CiviCRM.

```mermaid!
%%{init: {"flowchart": {"htmlLabels": false}} }%%

flowchart LR
    accTitle: OLS people information infrastructure
    accDescr: Some description

    classDef cohort fill:#c3c4a5,stroke:#333
    classDef nonCohort fill:#fff,stroke:#333

    civiPeople["`CiviCRM 
    *(CSV)*`"]:::nonCohort

    subgraph github["Website GitHub repository"]
        peopleYAML["`people 
        *(YAML)*`"]:::nonCohort
    end
    style github fill:#abc7fb,stroke:#abc7fb

    subgraph website["Online Website"]
        peopleHTML["`People
        *(HTML)*`"]:::nonCohort
        anyHTML["`Any page with people information
        *(HTML)*`"]:::nonCohort
    end
    style website fill:#eaa9a9,stroke:#eaa9a9

    civiPeople -- Script --> peopleYAML
    peopleYAML --> peopleHTML
    peopleYAML --> anyHTML
```

### Add people

1. Get a CSV file from CiviCRM using the predefined fields for website:
   - `First name`
   - `Last name`
   - `Email`
   - `Github username`
   - `Twitter username`
   - `Mastodon username`
   - `Website`
   - `ORCID`
   - `Affiliation`
   - `City`
   - `Country`
   - `Pronouns`
   - `Areas of expertise`
   - `Bio`

2. Prepare computational environment (locally or GitPod) as explained in the `README.md` file of the GitHub repository

3. Run the script which extract information from the CSV file, add them to `_data/people.yaml`, and add extra information about localisation

   ```
   $ python bin/prepare_website_data.py extractpeople \
      -df <path to csv file with people> OR -du <URL to csv file with people>
   ```

4. Submit changes by creating a Pull Request

## Organizations

OLS is supported by several organizations as [funders]({% link funders.md %}#funders), as [supporters]({% link funders.md %}#supporters), or as [partners]({% link partners.md %}).

### Add an organization

1. Open the `_data/organizations.yaml` file
2. Create a new entry there (using the name in lowercase, with spaces replaced by `-`) following an alphabetical order
3. Fill in information using the tags:
    - `name` (mandatory)
    - `website`
    - `logo`

        It can be either an URL to an image or the path to the logo added in `images/organizations` folder

    - `description`
    - `country`

4. Submit changes by creating a Pull Request

### Add a funding

1. Make sure the organization is listed in the `_data/organizations.yaml` file and add it otherwise (see above)
2. Open the `_data/funding.yaml` file
3. Create a new entry there
4. Fill in information using the tags:
    - `funder` using the organization short name from the `_data/organizations.yaml` file
    - `amount` of funding
    - `currency` of funding
    - `duration`
    - `date_award`
    - `purpose`
    - `proposal` with link to the proposal
5. Submit changes by creating a Pull Request

### Add a partner or supporter

1. Make sure the organization is listed in the `_data/organizations.yaml` file and add it otherwise (see above)
2. Open the `_data/community.yaml` file
3. Add a new entry in `partners` or `supporter`
4. Fill in information using the tags:
    - `organization` using the organization short name from the `_data/organizations.yaml` file
    - `details` with description of the support or partnership
5. Submit changes by creating a Pull Request

# Website content, outside community and Open Science Training cohorts

## Publications

All publications by OLS team are aggregated in a [Zotero group](https://www.zotero.org/groups/5292095/publications_by_ols), imported weekly into the GitHub repository and then displayed in a [dedicated page]({% link publications.md %})

```mermaid!
%%{init: {"flowchart": {"htmlLabels": false}} }%%

flowchart LR
    classDef cohort fill:#c3c4a5,stroke:#333
    classDef nonCohort fill:#fff,stroke:#333

    zotero["`Zotero 
    *(CSV)*`"]:::nonCohort

    subgraph github["Website GitHub repository"]
        bibtex["`publications
        *(bibtex)*`"]:::nonCohort
    end
    style github fill:#abc7fb,stroke:#abc7fb

    subgraph website["Online Website"]
        publicationHTML["`Publications
        *(HTML)*`"]:::nonCohort
    end
    style website fill:#eaa9a9,stroke:#eaa9a9

    zotero -- Script --> bibtex
    bibtex --> publicationHTML
```

### Add a publication

1. Request membership to the [Zotero group](https://www.zotero.org/groups/5292095/publications_by_ols) 
2. Add publication to the group
3. Wait for weekly update or run the "Update bibliography" [GitHub Action](https://github.com/open-life-science/open-life-science.github.io/actions/workflows/update-bibliography.yml)

## Posts

### Create a new blog post

1. Create a file in the folder `_posts` with a file named following the pattern `yyyy-mm-dd-name.md`
2. Add some metadata on the top of the file

    ```
    ---
    layout: post
    title: <title of the post>
    author: <ID of the authors in people.yml file>
    image: images/yyyy-mm-dd-name.jpg
    ---
    ```

3. Add content of the post to the file in [Markdown](https://www.markdownguide.org/getting-started/)
4. Add images in `images/posts/` directory
5. Submit changes by creating a Pull Request

## Events

We list on the website events either organised by OLS or where we are invited to speak at.

### Add a new event

1. Create a file in the folder `_events` with a file named following the pattern `yyyy-mm-dd-name.md`
2. Add some basic metadata on the top of the file

    ```
    ---
    layout: event
    title: <title of the event>
    type: <conference, workshop or training>
    description: |
        <short description of the event (one or two sentences)>
    
    external: <link to event if external>

    date_start: <starting date of event in YYYY-MM-DD format (e.g., 2024-10-26)>
    date_end: <starting date of event in YYYY-MM-DD format (e.g., 2024-10-26). Optional, if event is more than one day>
    time_start: <time start in HH:MM:SS format and UTC timezone. Optional if daylong event>
    duration: <duration in HH:MM:SS format. Optional if daylong event>

    location:
        name: 

    contributions:

    images:
    ---
    ```

3. Fill in more metadata

    - location:
        
        If online

            ```
            location: 
                name: Online
            ```

        If not online

            ```
            location: 
                geo:
                    lat: 45.78528236218017
                    lon: 4.856445300000001
                name: Online
                city: Lyon
                country: France 
            ```

    - contributions 

        If the event is a **conference** where OLS team and/or the community presented posters and/or talks highlighting OLS:

        ```
        contributions:
            posters:
            - 
                presenters: 
                - <id from people.yaml, one per line>
                title: "<title of the poster>"
                poster: <link to poster>
            talks:
            - 
                speakers:
                - <id from people.yaml, one per line>
                title: "<title of the talk>"
                slides: <link to slides>
        ```

        If the event is a **workshop** or **training** organised by the OLS team and/or the community

        ```
        contributions:
            facilitators:
            - <id from people.yaml, one per line>
            helpers:
            - <id from people.yaml, one per line>
            instructors:
            - <id from people.yaml, one per line>
            organisers:
            - <id from people.yaml, one per line>
            funding:
            - <id from funding.yaml, one per line>

        ```

    - workshop information

        ```
        cost: <free or, e.g. 150 EUR, must be space separated, must include a currency in ISO 4217 format>
        audience: <sentence about the audience>
        contact_email: <contact email>

        registration:
            link: <link for registration> 
            deadline: <date in YYYY-MM-DD format (e.g., 2024-10-26)>
        ```

4. Add content of the event to the file in [Markdown](https://www.markdownguide.org/getting-started/) (below `---`)
4. Add images in `images/events/` directory
5. Submit changes by creating a Pull Request

# Open Science Training cohorts

To organize calls in the different cohorts, we use a shared Spreadsheet containing information about calls: general information like date, time, learning objectives, but also the different activities like talks, group discussions with instructions. This spreadsheet also contains links to full recordings, slides, information about speakers.

We developed scripts for limiting manual work to propagate the information from the spreadsheet but also information about speakers to the OLS website in order to centralize the information there, build the video library. The script also generates templates for the call notes, and add information about participants, projects, and mentors in a cohort. 

```mermaid!
%%{init: {"flowchart": {"htmlLabels": false}} }%%

flowchart LR
    classDef cohort fill:#fff,stroke:#333
    classDef nonCohort fill:#d3d3d3,stroke:#d3d3d3

    teSS["`ELIXIR TeSS 
    Training Registry`"]:::nonCohort
    calendar["Public Google calendar"]:::nonCohort

    subgraph openReview["`OpenReview`"]
        applications["`Accepted
        Applications`"]:::cohort
    end
    style openReview fill:#c9c065,stroke:#c9c065

    subgraph civi["CiviCRM"]
        micrograntHonorariaCivi["`Microgrants & 
        Honoraria`"]:::cohort
        peopleCivi["Contacts"]:::cohort
    end
    style civi fill:#59b5e2,stroke:#59b5e2

    subgraph drive["Google Drive"]
        participantSheet["`Projects, 
        Participants, 
        & Mentors`"]:::cohort
        planningSheet["Planning"]:::cohort
        feedbackCSV["`Participant &
        Mentor Feedback
        Surveys`"]:::cohort
    end
    style drive fill:#6dd076,stroke:#6dd076

    subgraph github["Website GitHub repository"]
        peopleYAML["people"]:::cohort
        subgraph githubProgram["Program"]
            libraryYAML["library"]:::cohort
            subgraph githubCohort["Cohort"]
                projectYAML["projects"]:::cohort
                scheduleYAML["schedule"]:::cohort
                metadataYAML["metadata"]:::cohort
            end
            style githubCohort fill:#ed7a84,stroke:#fff
        end
        style githubProgram fill:#ed7a84,stroke:#fff
        subgraph artifact["Artifacts"]
            artifactCSV["`Data
            Artifacts`"]:::cohort
        end
        style artifact fill:#ed7a84,stroke:#fff
    end
    style github fill:#ed7a84,stroke:#ed7a84

    subgraph cohortGithub["Cohort GitHub repository"]
        callTemplates["Call Templates"]:::cohort
    end
    style cohortGithub fill:#df82d0,stroke:#df82d0

    subgraph etherpad["`Framapad`"]
        callNotes["Call Notes"]:::cohort
    end
    style etherpad fill:#69d2b4,stroke:#69d2b4

    subgraph statGithub["Stat GitHub repository"]
        notebooks["`Data processing & 
        Visualization
        Notebooks`"]:::cohort
    end
    style statGithub fill:#e2944e,stroke:#e2944e

    subgraph youtube["`OLS YouTube channel`"]
        recording["Call recordings"]:::cohort
    end
    style youtube fill:#a7cf4d,stroke:#a7cf4d

    subgraph website["Online Website"]
        communityHTML["Community"]:::cohort
        style websiteProgram fill:#9d96ea,stroke:#fff
        postHTML["`Announcement post`"]:::cohort
        subgraph websiteProgram["Program"]
            libraryHTML["`Video Library
            _Embeded recordings of talks from all cohorts sorted by topic_`"]:::cohort
            allProjectHTML["`Projects
            _Interactive table with all projects_`"]:::cohort
            subgraph websiteCohort["Cohort"]
                syllabusHTML["`Syllabus
                _Mentors, Facilitors, Experts with their expertise, etc_`"]:::cohort
                projectHTML["`Projects, Participants & Mentors`"]:::cohort
                scheduleHTML["`Schedule
                _Weekly schedule with metadata, embeded call recordings, slides, etc_`"]:::cohort
            end
            style websiteCohort fill:#9d96ea,stroke:#fff
        end
        subgraph websiteStat["Stats"]
            communityStatHTML["`Community location`"]:::cohort
            subgraph statProgram["Program"]
                rolesHTML["`Roles`"]:::cohort
                locationHTML["`People Location`"]:::cohort
                projectStatHTML["`Projects`"]:::cohort
                supportHTML["`Microgrants & Honoraria`"]:::cohort
                videoHTML["`Video Library & YouTube`"]:::cohort
                feedbackHTML["`Feedback`"]:::cohort
            end
            style statProgram fill:#9d96ea,stroke:#fff
        end
        style websiteStat fill:#9d96ea,stroke:#fff
    end
    style website fill:#9d96ea,stroke:#6690ce

    applications --> participantSheet
    peopleCivi --> peopleYAML
    peopleCivi --> metadataYAML
    participantSheet --> projectYAML
    planningSheet --> scheduleYAML
    planningSheet --> calendar
    scheduleYAML --> libraryYAML
    planningSheet --> callTemplates
    callTemplates --> callNotes
    projectYAML --> postHTML
    projectYAML --> allProjectHTML
    projectYAML --> projectHTML
    scheduleYAML --> scheduleHTML
    libraryYAML --> libraryHTML
    peopleYAML --> communityHTML
    peopleYAML --> postHTML
    peopleYAML --> websiteProgram
    peopleYAML --> artifactCSV
    metadataYAML --> syllabusHTML
    libraryHTML --> teSS
    scheduleHTML --> teSS
    recording --> scheduleHTML
    recording --> libraryHTML
    githubProgram --> artifactCSV
    artifactCSV --> notebooks
    feedbackCSV --> notebooks
    youtube --> notebooks
    micrograntHonorariaCivi  --> notebooks
    notebooks --> communityStatHTML
    notebooks --> projectStatHTML
    notebooks --> rolesHTML
    notebooks --> locationHTML
    notebooks --> feedbackHTML
    notebooks --> videoHTML
    notebooks --> supportHTML
```

## Prepare infrastructure for a new cohort

1. Prepare computational environment (locally or GitPod) as explained in the `README.md` file of the GitHub repository
2. Run the script which create cohort files:

    ```
    $ python bin/prepare_website_data.py createcohort \
        -p <program, e.g. openseeds>
        -c <cohort id>
    ```
   
3. Add organizers in data
    1. Open `_data/openseeds/ols-x/metadata.yaml` 
    2. Update `organizers`

4. Update the cohort timeline
    1. Open `_data/openseeds/ols-x/schedule.yaml` 
    2. Update `timeline` information

5. Update the cohort schedule as explained below
6. Add possible mentors and experts as explained below


## Add possible mentors and experts with their expertise

1. Get a CSV file from CiviCRM  using the predefined fields for website
2. Prepare computational environment (locally or GitPod) as explained in the `README.md` file of the GitHub repository
3. Run the script which extract information from the CSV file and add them to `_data/<program>/metadata.yaml`:

    ```
    $ python bin/prepare_website_data.py addmentorsexperts \
        -p <program, e.g. openseeds> \
        -c <cohort id> \
        -t <mentors or experts> \
        -df <path to csv file with participants> OR -du <URL to csv file with participants>
    ```

4. Run the script which sort expertise and save information in metadata file:

    ```
    $ python bin/prepare_website_data.py sortexpertises \
        -p <program, e.g. openseeds> \
        -c <cohort id>
    ```

5. Submit changes by creating a Pull Request

## Prepare planning spreadsheet and connect it to the website

1. Make a copy of the planning spreadsheet of a previous cohort on Google drive

    The spreadsheet should include a sheet rows with weeks, calls, and activities, with the following columns: 
    
    Column name | Expected content
    --- | ---
    `Week` | Week number, e.g. `00`, `01` - *mandatory for every row*
    `Start Date` | *mandatory for weeks, calls*
    `Start Time` | *mandatory for calls*
    `End Date` | 
    `Duration` | *mandatory for calls, activities*
    `Title` | *mandatory for calls, activities*
    `Type` | Type of information in the row: Week, Call (Mentor-Mentee, Mentor, Cohort, Skill-up, Q&A), Activities (Presentation, Breakout, Welcome, Silent reflections, Panel)
    `Tag` | Tag for presentations, used for the library ([list of tags](https://docs.google.com/spreadsheets/d/1sDJLG8RuoShWUQN78lvx_mghBbGfusdzlb1WwYrCbjk/edit#gid=0)) - *mandatory for a presentation* 
    `Call lead` | Lead of the call - *mandatory for a call* 
    `Note link` | Link to the notes - *mandatory for a call* 
    `Possible speaker` | 
    `Confirmed speaker` | First name and last name - *mandatory for a presentation* 
    `Slides` | Link to slidedecks - *only for presentation*
    `Recording` | Link to recording on YouTube - *mandatory for a call* 
    `Learning objectives` | List of learning objectives (answering "at the end, participants will be able to:") - *mandatory for a call* 
    `Before` | Instructions to do before a call - *only for call*
    `Icebreaker` | *mandatory for a call* 
    `After` | Instructions to do after a call or an activity
    `Instructions` | Instruction for an activity - *mandatory for breakout or silent reflections* 
    `People per room` | Number of people in each breakout room - *mandatory for breakout* 

2. Make the speadsheet readable by anyone with the link
3. Copy the link
4. Open `bin/<program>/update_schedule.sh` script
5. Add new lines

    ```
    echo "OLS-<cohort id>"
    python bin/prepare_website_data.py \
        updateschedule \
        --program '<program>' \
        --cohort '<cohort id>' \
        --schedule_url "<copied link where 'edit?usp=sharing' is replaced by 'export?format=csv&gid=' and then the id of the sheet in the spreadsheet"
    ```

6. Run the script

    ```
    $ bash bin/<program>/update_schedule.sh
    ```

3. Submit changes by creating a Pull Request

## Update the schedule on GitHub

This is run automatically every week and submitted as a Pull Request. The explanations below are only to run it manually

1. Prepare computational environment (locally or GitPod) as explained in the `README.md` file of the GitHub repository
2. Run the script `bin/<program>/update_schedule.sh`

    ```
    $ bash bin/<program>/update_schedule.sh
    ```

3. Submit changes by creating a Pull Request

## Add information to the public Google calendar

### Add calls

1. Create in the planning spreadsheet a sheet:

    1. Filtering rows in the main sheet to get only the ones where the type is `(Cohort|Skill-up|Q&A|Cafeteria)` (using `=FILTER('Main sheet'!A6:A142, REGEXMATCH('Main sheet'!G6:G142, "(Cohort|Skill-up|Q&A|Cafeteria)"))`)
    2. Having the columns: 

        Column name | Expected content
        --- | ---
        `Week` | `Week` column of main sheet
        `Type` | `Type` column of main sheet
        `Topic` | `Title` column of main sheet
        `Optional`  | `(optional)`if Q&A or `(optional for mentors)`
        `Subject` | Concatenation to get something like "[`Type` Call] Week `Week` - `Subject` (`Optional`) [Lead: `Lead`]"
        `Start Date` | `Start Date` column of main sheet 
        `Start Time` | `Start Time` column of main sheet or another column with the time at the same timezone than the Google calendar
        `End Time` | `End Time` column of main sheet  or another column with the time at the same timezone than the Google calendar
        `Note link` | `Note link` column of main sheet
        `Description` | Concatenation to get 3 lines with link to note, link to time zone and link to schedule on website
        
2. Download the sheet as CSV
3. Add events to [Google calendar](https://support.google.com/calendar/answer/37118#advanced&zippy=%2Ccreate-or-edit-a-csv-file).

### Add weeks

1. Create in the planning spreadsheet a sheet
    1. Filtering rows in the main sheet to get only the ones where the type is `Week` (using `=FILTER('Main sheet'!A6:A142, REGEXMATCH('Main sheet'!G6:G142, "Weeks"))`)
    2. Having the columns: 

        Column name | Expected content
        --- | ---
        `Week` | `Week` column of main sheet
        `Start Date` | `Start Date` column of main sheet 
        `End Date` | `Start Date`$ + 6$
        `All Day Event` | `TRUE`
        `Description` | Concatenation to get something like "OLS-N - Week `Week`"

## Add project, participants, and mentors

1. Get a CSV file with the following information
   - `Title`
   - `Mentor 1`
   - `Authors`
   - `Project-description`
   - `Comment regarding review` (with `rejected` if needed)
   - `Keywords`

2. Get a CSV file from CiviCRM  using the predefined fields for website with participant information

3. Prepare computational environment (locally or GitPod) as explained in the `README.md` file of the GitHub repository

4. Run the script which extracts project information from a CSV file and add them in project file:

    ```
    $ python bin/prepare_website_data.py addprojects \
        --program '<program>' \
        -c <cohort id> \
        -pf <path to csv file with projects> OR -pu <URL to csv file with projects> \
        -df <path to csv file with participants> OR -du <URL to csv file with participants>
    ```

5. Submit changes by creating a Pull Request

## Generate call templates

1. Make sure the planning spreadsheet is up-to-date with talks, speakers, activities (breakouts, silent reflection), learning objectives, icebreaker, etc
2. Open `bin/<program>/create_call_templates.sh` script
3. Make sure the link there corresponds to the spreadsheet
4. Prepare computational environment (locally or GitPod) as explained in the `README.md` file of the GitHub repository
5. Run the script `bin/<program>/create_call_templates.sh`

    ```
    $ bash bin/<program>/create_call_templates.sh
    ```  

6. Submit changes to call templates in the cohort Github repository

# Data and stats

Data about the community (e.g. members' location), the cohort (e.g. feedback or roles), and the video library are explored and visualized via Jupyter Notebooks, stored in a [GitHub repository]({{ site.github.owner_url }}/ols-stats/) and rendered in a dedicated [OLS stat website]({{ site.url }}/ols-stats/).


```mermaid!
%%{init: {"flowchart": {"htmlLabels": false}} }%%

flowchart LR
    classDef cohort fill:#fff,stroke:#333
    classDef nonCohort fill:#d3d3d3,stroke:#333

    youtube["OLS YouTube channel"]:::nonCohort

    subgraph drive["Google Drive"]
        micrograntSheet["`Microgrants
        *(before OLS-6)*`"]:::cohort
        honorariaSheet["`Honoraria
        *(before OLS-6)*`"]:::cohort
        feedbackCSV["Anonymized Participants & Mentor feedback"]:::cohort
    end
    style drive fill:#fbec5d,stroke:#fbec5d

    subgraph civi["CiviCRM"]
        micrograntCSV["`Microgrants
        *(after OLS-6)*`"]:::cohort
        honorariaCSV["`Honoraria
        *(after OLS-6)*`"]:::cohort
    end
    style civi fill:#d3d3d3,stroke:#d3d3d3

    subgraph github["Website GitHub repository"]
        peopleYAML["`people 
        *(YAML)*`"]:::cohort
        projectYAML["`projects 
        *(YAML)*`"]:::cohort
        scheduleYAML["`schedule 
        *(YAML)*`"]:::cohort
        metadataYAML["`metadata 
        *(YAML)*`"]:::cohort
        libraryYAML["`library 
        *(YAML)*`"]:::cohort
        subgraph artifact["Artifacts"]
            peopleCSV["`people 
            *(CSV)*`"]:::cohort
            subgraph githubProgram["Program"]
                libraryCSV["`library 
                *(CSV)*`"]:::cohort
                projectCSV["`projects 
                *(YAML)*`"]:::cohort
                rolesCSV["`roles 
                *(CSVs)*`"]:::cohort
                peopleRolesCSV["`people + roles
                *(CSV)*`"]:::cohort
            end
            style githubProgram fill:#abc7fb,stroke:#fff
        end
        style artifact fill:#abc7fb,stroke:#fff
    end
    style github fill:#abc7fb,stroke:#abc7fb

    subgraph statsGitHub["Stat GitHub repository"]
        locationNotebook["`Community location
        *(notebook)*`"]:::cohort
        subgraph statsGitHubProgram["Program"]
            programLocationNotebook["`People location
            *(notebook)*`"]:::cohort
            projectNotebook["`Projects
            *(notebook)*`"]:::cohort
            rolesNotebook["`Roles
            *(notebook)*`"]:::cohort
            feedbackNotebook["`Feedback
            *(notebook)*`"]:::cohort
            libraryNotebook["`Video Library & YouTube
            *(notebook)*`"]:::cohort
            micrograntHonorariaNotebook["`Microgrants & Honoraria
            *(notebook)*`"]:::cohort
        end
        style statsGitHubProgram fill:#9fe2bf,stroke:#fff
    end
    style statsGitHub fill:#9fe2bf,stroke:#9fe2bf

    subgraph website["Stat Website"]
        locationHTML["`Community location
        *(HTML)*`"]:::cohort
        subgraph websiteProgram["Program"]
            programLocationHTML["`People location`"]:::cohort
            projectHTML["`Projects`"]:::cohort
            rolesHTML["`Roles`"]:::cohort
            feedbackHTML["`Feedback`"]:::cohort
            libraryHTML["`Video Library & YouTube`"]:::cohort
            micrograntHonorariaHTML["`Microgrants & Honoraria`"]:::cohort
        end
        style websiteProgram fill:#eaa9a9,stroke:#fff
    end
    style website fill:#eaa9a9,stroke:#eaa9a9

    peopleYAML --> peopleCSV
    peopleYAML --> peopleRolesCSV
    projectYAML --> projectCSV
    libraryYAML --> libraryCSV
    scheduleYAML --> rolesCSV
    metadataYAML --> rolesCSV
    scheduleYAML --> peopleRolesCSV
    metadataYAML --> peopleRolesCSV
    peopleCSV --> locationNotebook
    rolesCSV --> rolesNotebook
    projectCSV --> projectNotebook
    youtube --> libraryNotebook
    libraryCSV --> libraryNotebook
    feedbackCSV --> feedbackNotebook
    micrograntSheet --> micrograntHonorariaNotebook
    honorariaSheet --> micrograntHonorariaNotebook
    micrograntCSV --> micrograntHonorariaNotebook
    honorariaCSV --> micrograntHonorariaNotebook
    peopleRolesCSV --> programLocationNotebook
    projectNotebook --> projectHTML
    locationNotebook --> locationHTML
    rolesNotebook --> rolesHTML
    feedbackNotebook --> feedbackHTML
    libraryNotebook --> libraryHTML
    micrograntHonorariaNotebook --> micrograntHonorariaHTML
    programLocationNotebook --> programLocationHTML
```
