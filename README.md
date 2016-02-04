#Project 4 Conference Central application

##To Run This Application Locally:

	- download python google app engine SDK from here: https://cloud.google.com/appengine/downloads?hl=en
	- run python2.7 path/to/google_appengine/dev_appserver.py path/to/Project-4
	- go to http://localhost:8080 from your web browser

##To Run the Uploaded Version of This App

	- go to conference-1124.appspot.com/_ah/api/explorer

##Session/Speaker Implementation
	 Sessions were implemented as entities in my application
	
	 Speakers were not implemnted as an entity/kind in my application.
	 Speakers only exist as a string property within Session entities.

	 If I implemented speakers as an entity/kind, I could store the
	 corresponding session keys in a property, which would allow me to query
	 sessions in the getSessionsBySpeaker handler by their key directly, but 
	 the entity would only contain one property which seems unnecessary. 
	 Since I implemented speakers as a string however, I have to create 
	 indexes to query sessions by it's speaker property which makes my 
	 application larger, but I thought that it would be better to have a 
	 slightly larger application (the indexes aren't large since the query 
	 only queries one property) than to create a whole new kind which only 
	 consists of one property.

##Justification of Data Models
	- the startTime and date properties in the Sessions kind are of type  
	TimeProperty and DateProperty so that I can add functionality to query for 
	sessions that start at a suitable time for users, by querying for sessions 
	before/after/between a date(s)/time(s), or by ordering or grouping by times
	/dates etc.

	-duration was implemented as type float instead of type integer because it 
	can give you a more suitable representaion of a duration of time than an 
	integer. For example, if a session went for two and a half hours, the most 
	suitable way to represent it as an integer would be as '150' representing 
	the duration in minutes. The best way to represent two and a half hours as 
	a float would be as '2.5', representing the duration in hours. IMO 2.5 
	hours is easier to understand than 150 minutes, and it would be bad 
	practice to store a duration as a timeProperty, since they are intended to 
	represent a time of day, plus it would mean the duration of a session 
	would be limited to 24 hours.

##Two Query Types Added:

	the two queries that I added can be accessed by the getSessionsByDate and 
	getSessionsByTime endpoint methods. They both take two times - a maximum 
	and minimum time - and return all sessions within that timeframe.

##The Query Problem:

	 The problem with querying for sessions where the topic of the Conference 
	 does not equal 'workshop' and is before 7pm, is that you cannot you 
	 cannot use inequality operators for more than one property of an entity 
	 in a query. One way to work around this is to query by one property via. 
	 Session.query (in my case i queried by startTime), and then do further 
	 aggregation in python. I implimented this query as the endpoints method, 
	 randomQuery.
