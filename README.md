# Pygame Magic Mirror 
Created By: Jordan Masterson

This is a Magic Mirror project scripted in Python using the Pygame module.

NOTE:  This is designed for a 1080 X 1920 resolution set to portrait mode.  

CURRENT FEATURES:
 - Displays Current Temperature and Condition Icon for set location
 - 12 Hour Digital Clock and Date
 - Top 10 news headlines that cycle every 7 seconds
 
FUTURE FEATURES:
 - Calender widget
 - New algorithm to resize font depending on screen resolution
 - Facial Recognition for multiple users

![alt text](https://i.imgur.com/m0PiCoL.png)
 
SETUP:
1. Install pygame, pillow and newsapi-python modules.
2. Set the WIDTH and HEIGHT variables to your screens resolution (1080w X 1920h is what this is designed for). Ensure your display is set to Portrait mode (Hotdog style!).
3. Get Weather API Key from - https://home.openweathermap.org
    - Sign up for free account
    - Paste the API Key over the 'paste-key-here' in the WEATHER_KEY variable
4. Get News API Key from - https://newsapi.org
    - Sign up for free account
    - Paste the API Key over the 'paste-key-here' in the NEWS_KEY variable
5. Set your CITY, STATE and COUNTRY variables (Ex: 'Los Angeles', 'CA', 'us')
6. Set your desired sources NEWS_SOURCE list.  You can get these from https://newsapi.org/sources

NOTES: 
You also have the ability to add whatever font you want. Just copy any '.ttf' file into the fonts directory 
and set the FONT_NAME variable to that file name (Ex: 'arial.ttf')

KNOWN ISSUES:
 - Certain font sizes will cause some text to display further apart or closer to each other depending on the screen resolution