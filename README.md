# groupme-bot
A groupme bot built in python, using the GroupyAPI, intended to be run on django

###Commands

* Help <Command>  
   Outputs the list of commands.  
   Given the optional command parameter, outputs additional similar commands.
* Ping  
   Pong!
* Sleep  
   Turns the bot off for the night.
* Cookie [Target]  
   Gives a cookie to the target.
* Party  
   Outputs a string and some party emojis.
* Lennyface  
   Outputs a random lenny face emoticon.
* Fliptable  
   Outputs a random table flipping emoticon.
* Sentient  
   Outputs a random quote.
* Daze  
   Outputs how many days are left until St. Pat's.
* D[number]   
   Outputs a random number from the set of 1 to the number given.
* Weather <Location>  
   Outputs the current temperature, along with the high and low.
  * High/Low
     Outputs the high and low temperature for the day.
  * Sunrise/Sunset/Sun  
     Outputs the time of sunrise and sunset, no matter whether you type "sunrise" or "sunset."
  * Weather Week  
     Outputs the 7-day forecast.
  * Meteorology  
     Outputs the temperature, humidity, pressure, rain, and wind.

  
###To-Do

* [ ] Create optional parameter for "Help" command
* [X] Create "Weather Sunrise/Sunset" command
* [ ] Create "Weather Week" command
* [X] Create "Weather Specific" command
* [ ] Create a function that interacts with the strawpoll api
