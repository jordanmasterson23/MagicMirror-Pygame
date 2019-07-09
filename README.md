# Pygame Magic Mirror 
Created By: Jordan Masterson

This is a Magic Mirror project scripted in Python using the Pygame module.

NOTE:  This is still in development. It is very basic at the moment but I will continue to add more features.

##CURRENT FEATURES:
 - Displays the current temp of your set location
 - 12 Hour Digital Clock
 - Top 10 news headlines that cycle every 5 seconds
 
##FUTURE PLANS:
 - Calender widget
 - Changeable borders
 - Facial Recognition for multiple users
 
##SETUP:
1. Set the WIDTH and HEIGHT variables to your screens resolution
2. Get Weather API Key from - https://home.openweathermap.org
    - Sign up for free account
    - Paste the API Key over the 'paste-key-here' in the WEATHER_KEY variable
3. Get News API Key from - https://newsapi.org
    - Sign up for free account
    - Paste the API Key over the 'paste-key-here' in the NEWS_KEY variable
4. Set your CITY, STATE and COUNTRY variables (Ex: 'Los Angeles', 'CA', 'us')
5. Set your desired NEWS_SOURCE variable.  You can get this from https://newsapi.org/sources

##NOTES:
You also have the ability to add whatever font you want. Just copy any '.ttf' file into the fonts directory 
and set the FONT_NAME variable to that file name (Ex: 'arial.ttf')
 