---
layout: page
title: SOP for OLS
---


# Post Cohort

## Send surveys

- Send the mentor exit survey with the honorarium survey in it
- Send the participant exit survey

## Process the post OLS Survey

- Create a spreadsheet with the answers from the form
- Create certificates
    - Create a sheet to select columns with participant name and projects and name them `name` and `projects`
    - Download as CSV
    - Get the [`branding`](https://github.com/open-life-science/branding) repository
    - Go to certificate folder
    - Copy last cohort certificate and edit it
    - Follow the README file to generate the certificates automatically
    - Sign the generated certificates
    - Upload them to Google folder
- Extract possible mentors for next cohort
    - Create a sheet named `OLS-x-possible-mentors`
    - Extract participants who answered "Yes I'd like to return as a mentor" with their name and their email
    
    ```
    =FILTER('Form responses 1'!N2:N148, REGEXMATCH('Form responses 1'!L2:L148, "Yes I'd like to return as a mentor"))
    ```

- Extract possible experts for next cohort
    - Create a sheet named `OLS-x-possible-experts`
    - Extract participants who answered "Yes I'd like to return as an expert" with their name and their email
    
    ```
    =FILTER('Form responses 1'!N2:N148, REGEXMATCH('Form responses 1'!L2:L148, "Yes I'd like to return as an expert"))
    ```

- Extract unsure people for next cohort
    - Create a sheet named `Unsure-for-OLS-x`
    - Extract participants who answered "I am not sure yet, but ask me later when you have launched OLS-x" with their name and their email
    
    ```
    =FILTER('Form responses 1'!N2:N148, REGEXMATCH('Form responses 1'!L2:L148, "I am not sure yet, but ask me later when you have launched OLS-x"))
    ```

## Process the post OLS Survey for mentors

- Create a spreadsheet with the answers from the form
- Extract possible mentors for next cohort
    - Create a sheet named `OLS-x-possible-mentors`
    - Extract participants who answered "Yes I'd like to return as a mentor" with their name and their email
    
    ```
    =FILTER('Form responses 1'!N2:N148, REGEXMATCH('Form responses 1'!L2:L148, "Yes I'd like to return as a mentor"))
    ```

- Extract possible experts for next cohort
    - Create a sheet named `OLS-x-possible-experts`
    - Extract participants who answered "Yes I'd like to return as an expert" with their name and their email
    
    ```
    =FILTER('Form responses 1'!N2:N148, REGEXMATCH('Form responses 1'!L2:L148, "Yes I'd like to return as an expert"))
    ```

- Extract unsure people for next cohort
    - Create a sheet named `Unsure-for-OLS-x`
    - Extract participants who answered "Yes I'd like to return as an expert" with their name and their email
    
    ```
    =FILTER('Form responses 1'!N2:N148, REGEXMATCH('Form responses 1'!L2:L148, "Yes I'd like to return as an expert"))
    ```

- Extract mentees approved (by their mentors) as possible mentors for next cohort
    - Create a sheet named `OLS-4-approved-possible-mentors`
    - Extract mentors who answered "mentor" to "Would you recommend us to invite your mentee(s) to OLS-4?" with their name, the mentee names and the comment
    
    ```
    =FILTER('Form responses 1'!D2:D148, REGEXMATCH('Form responses 1'!N2:N148, "mentor"))
    ```

- Extract mentees approved (by their mentors) as possible experts for next cohort
    - Create a sheet named `OLS-4-approved-possible-experts`
    - Extract mentors who answered "expert" to "Would you recommend us to invite your mentee(s) to OLS-4?" with their name, the mentee names and the comment
    
    ```
    =FILTER('Form responses 1'!D2:D148, REGEXMATCH('Form responses 1'!N2:N148, "expert"))
    ```

- Extract not ready mentees 
    - Create a sheet named `Mentees-not-ready`
    - Extract mentors who answered "not ready yet" to "Would you recommend us to invite your mentee(s) to OLS-4?" with their name, the mentee names and the comment
    
    ```
    =FILTER('Form responses 1'!D2:D148, REGEXMATCH('Form responses 1'!N2:N148, "not ready yet"))
    ```

# Prepare new cohort

## Setup website

## Extract mentors / experts from last round participants

- Open `People to invite - OLS-x`
- Add people that said they could not and asked to be contacted in previous cohort 
- In `Mentors-to-reinvite` sheet
    - In `Interested mentors from mentor survey` and `Interested experts from mentor survey` 
        - Replace in `Email`
            - the link to spreadsheet by the new post OLS Survey (Mentors)
            - `OLS-x` with correct OLS id

        ```
        =IMPORTRANGE("link-to-post-OLS-survey-mentors","OLS-x-possible-mentors!A1:B145")
        ```

        If `#REF` appears, go over it and click on `Allow access`

- In `Mentees-to-invite-as-experts` and `Mentees-to-invite-as-mentors` sheet 
    - In `Interested meentes from mentee survey` and `Unsure meentes from mentee survey` columns
        - Replace in `Email`
            - the link to spreadsheet by the new post OLS Survey
            - `OLS-x` with correct OLS id

        ```
        =IMPORTRANGE("link-to-post-OLS-survey","OLS-x-possible-experts!A1:B145")
        ```
    
    - In `Approved by mentors in the mentor survey` and `Not ready given mentors mentors in the mentor survey` 
        - Replace in `Email`
            - the link to spreadsheet by the new post OLS Survey (Mentors)
            - `OLS-x` with correct OLS id

        ```
        =IMPORTRANGE("link-to-post-OLS-survey-mentors","OLS-x-possible-mentors!A1:B145")
        ```

## Check mentors that signed up

- Compare to last round post-survey
- Add to website
