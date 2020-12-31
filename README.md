# gooddeedswebapp

This is a cs50 introduction to computer science final project called Gooddeeds.
it is a web app where users can check if there is any volunteer work(good deed) posted by other users and join to participate or create one themselves.

### Technologies used:
    -html, css and twitter bootstrap for the front end.
    -python flask web framework for the back end.
    -sqlite for the database.
    
## Features of Gooddeeds:
there is the authentication and gooddeeds features.
### Authentication Features:
    -sign up functionality which allows users to register to gain access to features of the website.
    -login functionality which allows registered users to gain access to the gooddeeds features of the website.
    -log out functionality which allows users to kill their session on the app.
### Gooddeeds features:
    - dashboard where the link to other features can be seen and navigated to and from.
    - current deeds tab where all the available current deeds which hasn't been done or completed is listed.
    - create deeds tab where authenticated users can create a new deed for other users to join.
    - completed deeds tab where all deeds marked done by the author are shown.
    - joined tab where the deeds joined can be easily seen and listed.
    - edit tab which provides room for editing or deleting the posted deeds.
    - details tab which shows the complete details of a deed that was posted. It can be viewed from any of the tabs except the edit tab.
 
 ### Thanks to all cs50 staff for the lectures. it was rewarding and just as Dr David J. Malan said - I am proud of where I am at the end of this course compared to where I was at the beginning.

 #### To run the app:
        In a python virtual environment run:
        $ export FLASK_APP=gooddeeds
        $ export FLASK_ENV=development
        $ flask run

        for windows: use set instead of export
