# Notes App

Welcome to the Notes  App - a powerful and user-friendly application built with Django framework! Manage your notes effortlessly with features like Note labeling, Archive & Unarchive options, and secure Sign in/Sign Up functionalities. Stay organized and productive as you seamlessly categorize, access, and modify your notes with ease. Get started today and experience the convenience of a well-structured note-taking platform!

### Home Page 
This section allows the current user to view and access all their created notes in one centralized location. Easily keep track of your notes, users can archive the notes and retrieve important information whenever they need it!
### Sign up 
Sign up page for users.
### Login 
Login Page for users.
After login users will be redirected to My Notes page.
### Create Note 
Logged In User can create note with title, description and attach required label to that current note.
###Archive 
Users can see the archieved notes.
###Lables
Users can track their labeled notes here.
### Logout 
Logout functionality for users.

### APIs

`/`: Returns the home page

`register/`: Save user details to database

`logout/`: Loggin Out

`login/`:  Logging In 

`create/`:  Used to create note

`delete/<id>/`: Delete specific note

`archive/<id>/`: Archive specific note

`archived_notes/`: Returns archieved notes for currently logged in user.

`unarchive/<id>/`: Unarchive specific note

`labled_notes/<label>/`: Returns labeled notes for selected label

`create_label/`: Create a new label

`delete_label/`: Delete a existing label

## **Demo**

#### YouTube Link: https://youtu.be/iMYKGwiIcnQ

![demoVideo](https://github.com/soninirav/Notes/blob/master/notesDemo.gif)
