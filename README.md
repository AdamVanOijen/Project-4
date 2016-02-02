Project 4 Conference Central application

To Run This Application Locally:

	- download python google app engine SDK from here: https://cloud.google.com/appengine/downloads?hl=en
	- run python2.7 path/to/google_appengine/appcfg.py path/to/ConferenceCentral_Complete
	- go to http://localhost:8080 from your web browser

To Run the Uploaded Version of This App:

	- go to conference-1124.appspot.com/_ah/api/explorer

Notes:
	- you must run getProfile before running createConference.

How Sessions and Speakers are Implemented:

	 Sessions were implemented as entities in my application
	
	 Speakers were not implemnted as an entity/kind in my application. Speakers only exist as a string property within Session entities.

	 If I implemented speakers as an entity/kind, I could store the corresponding session keys in a property, which would allow me to query sessions in the getSessionsBySpeaker handler by their key directly, but the entity would only contain one property which seems unnecessary. Since I implemented speakers as a string however, I have to create indexes to query sessions by it's speaker property which makes my application larger, but I thought that it would be better to have a slightly larger application (the indexes aren't large since the query only queries one property) than to create a whole new kind which only consists of one property.

Justification of data models:
	
	- the startTime and date properties in the Sessions kind are of type  TimeProperty and DateProperty so that I can add functionality to query for sessions that start at a suitable time for users, by querying for sessions before/after/between a date(s)/time(s), or by ordering or grouping by times/dates etc.

	-duration was implemented as type float instead of type integer because it can give you a more suitable representaion of a duration of time than an integer. For example, if a session went for two and a half hours, the most suitable way to represent it as an integer would be as '150' representing the duration in minutes. The best way to represent two and a half hours as a float would be as '2.5', representing the duration in hours. IMO 2.5 hours is easier to understand than 150 minutes, and it would be bad practice to store a duration as a timeProperty, since they are intended to represent a time of day, plus it would mean the duration of a session would be limited to 24 hours.

two query types added:

	the two queries that I added can be accessed by the getSessionsByDate and getSessionsByTime endpoint methods. They both take two times - a maximum and minimum time - and return all sessions within that timeframe.

The query problem:

	 The problem with querying for sessions where the topic of the Conference does not equal 'workshop' and is before 7pm, is that there is no direct way to query for entities where a specified repeated property does not contain a specified value. One approach to getting around this problem would be predefine a set of possible values in a list and remove the specified value from the list, so that you can query for all Sessions whose ancestor's topic property contains values that are in that modified list of predefined values. I added an endpoint method at line 810 in conference.py that demonstrates this query.