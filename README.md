# PMI-Intern-Sign-In

## Template Names Need to Be Changed

person_list.html = list of active work sessions, seen by interns

past_time.html = doesnt need changing, past log hours

new_person.html = new work session

item_edit.html = clock out of current work session, end work session

datefilter.html = Admin view with name and date range filter of all intern work sessions

edit_hours.html = doesnt need changing, editing hours. 

person_confirm_delete.html = delete work session/hours from log.

new_record.html = add new work session (forgot to clock in or something) Admin use. 


Should probably also change the folder from "ogdb" to timesheet or clockin or something. 

## Synopsis

Internship signin web app developed using Django for Paradyme Management's 2017 summer internship program. 


## Interns Quickstart

Sign in.

Create New Session.

Select "Clock in"

When complete with work for the day, select current active session and click "End Session"

Select "Clock out"

Sign out.

Repeat. 

Past history of hours worked and work sessions can be found by navigating to "Past Logs" located at the top right of the webpage. 

Password can be changed by navigating to /admin

## Admin Quickstart

Create Users (the interns) as staff NOT as superusers. 

NOTE: MAKE SURE TO CREATE AN INTERN ENTRY FOR EVERY USER WITH CORRESPONDING USERNAME! SPELLING COUNTS!




