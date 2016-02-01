Project 4 Conference Central application

To Run This Application Locally:

	- download python google app engine SDK from here: https://cloud.google.com/appengine/downloads?hl=en
	- run python2.7 path/to/google_appengine/appcfg.py path/to/ConferenceCentral_Complete
	- go to http://localhost:8080 from your web browser

To Run the Uploaded Version of This App:

	- go to conference-1124.appspot.com/_ah/api/explorer

Notes:
	- you must run getProfile before running createConference.
	- a Speaker must be registered via registerSpeaker before creating a session 

Design Decisions:
	 
	 I chose to store corresponding session keys in a speaker entity because it allows me to query corresponding sessions by their key directly. Querying sessions by their key means I can use less indexes in my application.