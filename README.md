# OLS

***Sharing. Connecting. Empowering***

Find all the information about our community and projects at
[https://open-life-science.github.io](https://open-life-science.github.io).

## Welcome!

First and foremost, Welcome! 🎉 Willkommen! 🎊 Bienvenue! 🙏 सुस्वागत (Suswagat)🎈🎈🎈

This document (the `README` file) is a hub to give you some information about the
project. Jump straight to one of the sections below, or just scroll down to find
out more.

## What are we doing?

We are working to create a mentoring program for individuals interested in becoming
ambassadors for Open Science practice, training and education in their communities.

Our outcome is to support early stage researchers and young leaders by sharing
Open Science skills, connecting them to others in the community,
and empowering them to become ambassadors for Open Science practice,
training and education in their communities.

## Who are we?

We are currently a team of people who share a passion for Open Research and inclusiveness in Open Science. Please read me on [our website](https://openlifesci.org/community).

## What do we need?

**You!** In whatever way you can help.

We need expertise in open-science, training, mentoring, communication. We'd love your feedback along the way, and of course.

## Get involved

If you think you can help in any of the areas listed above (and we bet you can)
or in any of the many areas that we haven't yet thought of (and here we're sure
you can) then please check out [our contributors' guidelines](CONTRIBUTING.md)
and our [roadmap](roadmap.md).

Please note that it's very important to us that we maintain a positive and
supportive environment for everyone who wants to participate. When you join us
we ask that you follow our [code of conduct](CODE_OF_CONDUCT.md) in all
interactions both on and offline.


## How can I generate the website and contribute using GitPod?

[GitPod](https://www.gitpod.io/) is an open-source developer platform for remote development. You can use it to generate the website without installing anything on your computer.

1. Setting up GitPod
   1. Create a fork of the OLS GitHub repository (to do only 1 time)
      1. Go on the GitHub repository: [github.com/open-life-science/open-life-science.github.io](https://github.com/open-life-science/open-life-science.github.io)
      2. Click on th Fork button (top-right corner of the page)
   2. Open your browser and navigate to [gitpod.io](https://www.gitpod.io/)
   3. Log in with GitHub
   4. Copy the link to your fork of the GTN, e.g. https://github.com/bebatut/open-life-science.github.io

      Gitpod will now configure your environment. This may take some time.

      Once the setup is finished, you should see a page with:
      - On the Left: All the files in the OLS repository
      - Top: The main window where you can view and edit files
      - Bottom: Terminal window, where you can type commands (e.g. to build the website preview) and read output and error messages

2. Build and preview the OLS website
   1. Type the following command `make serve-gitpod` in the terminal window (bottom)
   2. Click on the link in the terminal to see the OLS in full-screen: `Server address: http://127.0.0.1:4000`

3. Make and view changes
   1. Open and/or create files via the file browser on the left
   2. Make and save the changes in the files
   3. Reload the preview page to view the changes

4. Saving changes back to GitHub
   1. Option 1: via the terminal
      1. Create a new branch with `git checkout`
      2. Commit your changes with `git add` and `git commit`
      3. Push changes with `git push origin`
   2. Option 2: via the web interface
      1. Create a new branch
         1. Click on the bottom-left on the branch logo button on the bottom of the page with the current branch (probably "main")
         2. Give a new name for your new branch (at top of window)
         3. Choose "+ Create new branch..." from the dropdown
      2. Commit changes
         1. Click on the "Source Control" tab button (branch) on the left menu to show changed files
         2. Click on the "+" icon next to the edited files to stage changes stage changes button
         3. Hit the checkmark icon at the top to commit the changes
         4. Enter a commit message (top of window) - Publish changes
         5. Click the cloud button at bottom left to publish your changes publish changes button.

            Changes are now saved to your fork, and you can make a PR via the GitHub interface
   
## How can I generate the website locally?

You need a `ruby` environment (version >= 2.4). Either you have it installed and
you know how to install [Bundler](https://bundler.io/) and
[Jekyll](https://jekyllrb.com/) and then run Jekyll, or you use
(mini-)[conda](https://conda.io/docs/index.html), a package management system
that can install all these tools for you. You can install it by following the
instructions on this page: https://conda.io/docs/user-guide/install/index.html

In the sequel, we assume you use miniconda.

1. Open a terminal
2. Clone this GitHub repository:

   ```
   $ git clone https://github.com/open-life-science/open-life-science.github.io.git
   ```

3. Navigate to the `open-life-science.github.io/` folder with `cd`
4. Set up the conda environment:

   ```
   $ make create-env
   ```

5. Install the project's dependencies:

   ```
   $ make install
   ```

6. Start the website:

   ```
   $ make serve
   ```

7. Open the website in your favorite browser at:
   [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

## Run the link checks

To avoid dead or wrong links, run the link checkers:

```
$ make check-html
```

## Create a new blog post

To create a new blog post:

1. Create a file in the folder `_posts` with a file named following the pattern `yyyy-mm-dd-name.md`
2. Add some metadata on the top of the file

    ```
    ---
    layout: post
    title: <title of the post>
    author: <github id of the author>
    image: images/yyyy-mm-dd-name.jpg
    ---
    ```

4. Add content of the post in the file in Markdown
3. Add images in `images/posts/`

## Add someone as mentor, expert or organizer

Add someone to the list of people:

1. Open the `_data/people.yaml` file
2. Create a new entry there (using the GitHub id, or firstname-lastname if no GitHub id) following the alphabetical order
3. Fill in information using the tags:
    - `first-name` (*mandatory*)
    - `last-name` (*mandatory*)
    - `twitter`
    - `email`
    - `website`
    - `gitter`
    - `orcid`
    - `affiliation`
    - `city`
    - `country` (*mandatory*)
    - `pronouns`
    - `expertise`
    - `bio`

Add the person to their corresponding list to be visible on the website:
- If they are a participant for a cohort, add their GitHub id with their project to `_data/ols-n-projects.yaml`
- If they are a potential mentor for a cohort, add their GitHub id in the `_data/ols-n-metadata.yaml`
- If they are an expert for a cohort, add their GitHub id in the `_data/ols-n-metadata.yaml`
- If they are a speaker for a cohort, add their GitHub id with their talk details in `_data/ols-n-schedule.yaml`

Add many people in a row to `_data/people.yaml`:

1. Create a CSV file with at least the following columns (named this way):
   - `First name`
   - `Last name`
   - `Email`
   - `Github username`
   - `Twitter username`
   - `Website`
   - `ORCID`
   - `Affiliation`
   - `City`
   - `Country`
   - `Pronouns`
   - `Areas of expertise (1 element per line)`
   - `Bio`

   A form like [this one](https://docs.google.com/forms/d/e/1FAIpQLScmsWw0VSvdytz3A1k6HnbfgOnsE4SiJcL9_qkMTs_Na6-l2Q/viewform?usp=pp_url) can be used to generate such csv

2. Get a copy of the CSV file at the root of this folder
3. Activate the conda environment

   ```
   $ source activate open-life-science-website
   ```

   Or alternatively, get locally:
   - Python 3.*
   - pyyaml
   - pandas

4. Run the script which extract information from the CSV file and add them to `_data/people.yaml`

   ```
   $ python bin/prepare_website_data.py extractpeople \
      -df <path to csv file with participants> OR -du <URL to csv file with participants>
   ```

## Add possible mentors and experts for a cohort

1. Create a CSV file with at least the following columns (named this way):
   - `First name`
   - `Last name`
   - `Email`
   - `Github username`
   - `Twitter username`
   - `Website`
   - `ORCID`
   - `Affiliation`
   - `City`
   - `Country`
   - `Pronouns`
   - `Areas of expertise (1 element per line)`
   - `Bio`

   A form like [this one](https://docs.google.com/forms/d/e/1FAIpQLScmsWw0VSvdytz3A1k6HnbfgOnsE4SiJcL9_qkMTs_Na6-l2Q/viewform?usp=pp_url) can be used to generate such csv

2. Activate the conda environment

   ```
   $ source activate open-life-science-website
   ```

   Or alternatively, get locally:
   - Python 3.*
   - pyyaml
   - pandas

4. Run the script which extract information from the CSV file and add them to `_data/people.yaml`

   ```
   $ python bin/prepare_website_data.py addmentorsexperts \
      -c <cohort id> \
      -t <mentors or experts> \
      -df <path to csv file with participants> OR -du <URL to csv file with participants>
   ```

## Add a new organization

1. Open the `_data/organizations.yaml` file
2. Create a new entry there (using the name in lowercase, with spaces replaced by `-`) following an alphabetical order
3. Fill in information using the tags:
    - `name`
    - `website`
    - `description`
    - `country`
4. Add a logo (if possible) named as the entry in `images/organizations` folder
5. Add the path to the logo in `_data/organizations.yaml` using `logo` tag

## Add a partner

1. Make sure the organization is listed in the `_data/organizations.yaml` file and add it otherwise (see above)
2. Open the `_data/partners.yaml` file
3. Create a new entry there
3. Fill in information using the tags:
    - `partner` using its short name from the `_data/organizations.yaml` file
    - `details` with details about the partnership

## Add a funding

1. Make sure the organization is listed in the `_data/organizations.yaml` file and add it otherwise (see above)
2. Open the `_data/funding.yaml` file
3. Create a new entry there
3. Fill in information using the tags:
    - `funder` using its short name from the `_data/organizations.yaml` file
    - `amount` of funding
    - `currency` of funding
    - `duration`
    - `date_award`
    - `purpose`
    - `proposal` with link to the proposal

## Update schedule for a cohort

The schedule displayed in a cohort page is automatically generated from a file `_data/ols-n-schedule.yaml`.

In this file, for each week, it is listed the timeframe and the different calls planned. For each call, several information are given:
- `type`: `Mentor-Mentee`, `Cohort`, `Mentors` or `Coworking`
- `duration` in min
- `title`
- `date` in the format `Month Day, Year`
- `time` in the format '14:00' and for Berlin time
- `calendar-event`: link to calendar event
- `agenda`: tldr
- `notes`: link to notes
- `recording`: link to recording
- `content` with details of the content written in Markdown
- `before` with tasks to do before as a list written in Markdown
- `after` with tasks to do after as a list written in Markdown
- `resources`: list of useful resources with for each of them:
   - `type`: `slides`, `document`, or `external-link`
   - `title`
   - `speaker`: username in `_data/people.yaml`, if slides
   - `link`

## Update schedule automatically

1. Create a spreadsheet or CSV with columns:
   - `Week`
   - `Start Date`
   - `Start Time`
   - `End Date`
   - `Duration`
   - `Title`
   - `Type`
   - `Learning objectives`
   - `Slides`
   - `Confirmed speaker`
   - `Note link`
   - `Recording`
   - `Hosts`
   - `Facilitators`
   - `Before`
   - `After`

2. Adapt the script in `bin/update_schedule.sh` with cohort id and link to CSV export of the spreadsheet

## Order experts and possible mentors by expertise areas

In metadata file for cohort, experts and possible mentors can be ordered by expertise area to be display in cohort page given these areas.

To order them:

1. Activate the conda environment

   ```
   $ source activate open-life-science-website
   ```

   Or alternatively, get locally:
   - Python 3.*
   - pyyaml
   - pandas

2. Run the script which sort expertise and save information in metadata file

   ```
   $ python bin/prepare_website_data.py sortexpertises -c <cohort id>
   ```

## Add projects

1. Create a CSV file with for each project the following information
   - `Title`
   - `Mentor 1`
   - `Authors`
   - `Project-description`
   - `Comment regarding review` (with `rejected` if needed)
   - `Keywords`

2. Create a CSV file with participant information (similar as the one needed to add new people) with an extra column with project name

3. Activate the conda environment

   ```
   $ source activate open-life-science-website
   ```

   Or alternatively, get locally:
   - Python 3.*
   - pyyaml
   - pandas

4. Run the script which extract project information from a CSV file and add them in project file

   ```
   $ python bin/prepare_website_data.py addprojects \
      -c <cohort id> \
      -pf <path to csv file with projects> OR -pu <URL to csv file with projects> \
      -df <path to csv file with participants> OR -du <URL to csv file with participants>
   ```

## Add events to Google calendar

1. Create CSV file with
   - `Week`
   - `Type`
   - `Optional`
   - `Subject`
   - `Start Date`
   - `Start Time`
   - `End Date`
   - `Duration`
   - `End Time`
   - `All Day Event`
   - `Note link`
   - `Description`

2. Add events to [Google calendar](https://support.google.com/calendar/answer/37118#advanced&zippy=%2Ccreate-or-edit-a-csv-file)

## Create files for a new cohort

1. Activate the conda environment

   ```
   $ source activate open-life-science-website
   ```

   Or alternatively, get locally:
   - Python 3.*
   - pyyaml
   - pandas

2. Run the script which create new cohort files

   ```
   $ python bin/prepare_website_data.py createcohort \
      -c <cohort id> \
   ```

3. Update `_config.yml` file to add new cohort in collection

## License

Attribution-ShareAlike 4.0 International

=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
	wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public: 
	wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution-ShareAlike 4.0 International Public
License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-ShareAlike 4.0 International Public License ("Public
License"). To the extent this Public License may be interpreted as a
contract, You are granted the Licensed Rights in consideration of Your
acceptance of these terms and conditions, and the Licensor grants You
such rights in consideration of benefits the Licensor receives from
making the Licensed Material available under these terms and
conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. BY-SA Compatible License means a license listed at
     creativecommons.org/compatiblelicenses, approved by Creative
     Commons as essentially the equivalent of this Public License.

  d. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  e. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  f. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  g. License Elements means the license attributes listed in the name
     of a Creative Commons Public License. The License Elements of this
     Public License are Attribution and ShareAlike.

  h. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  i. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  j. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  k. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  l. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  m. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part; and

            b. produce, reproduce, and Share Adapted Material.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. Additional offer from the Licensor -- Adapted Material.
               Every recipient of Adapted Material from You
               automatically receives an offer from the Licensor to
               exercise the Licensed Rights in the Adapted Material
               under the conditions of the Adapter's License You apply.

            c. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.

       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

  b. ShareAlike.

     In addition to the conditions in Section 3(a), if You Share
     Adapted Material You produce, the following conditions also apply.

       1. The Adapter's License You apply must be a Creative Commons
          license with the same License Elements, this version or
          later, or a BY-SA Compatible License.

       2. You must include the text of, or the URI or hyperlink to, the
          Adapter's License You apply. You may satisfy this condition
          in any reasonable manner based on the medium, means, and
          context in which You Share Adapted Material.

       3. You may not offer or impose any additional or different terms
          or conditions on, or apply any Effective Technological
          Measures to, Adapted Material that restrict exercise of the
          rights granted under the Adapter's License You apply.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material,

     including for purposes of Section 3(b); and
  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.

  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.

  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.

  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.

  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.

  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.

  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.

  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.


=======================================================================

Creative Commons is not a party to its public
licenses. Notwithstanding, Creative Commons may elect to apply one of
its public licenses to material it publishes and in those instances
will be considered the “Licensor.” The text of the Creative Commons
public licenses is dedicated to the public domain under the CC0 Public
Domain Dedication. Except for the limited purpose of indicating that
material is shared under a Creative Commons public license or as
otherwise permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the
public licenses.

Creative Commons may be contacted at creativecommons.org.
