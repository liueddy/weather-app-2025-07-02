Hello,

Here's the rundown:
- /depreciated/ is some depreciated files i used in testing / labs
- /react/  folder is the react frontend of the server.
- /server/ folder is the flask server
    - \[**FetchWeather**\] cleans user input and fetches from OpenWeatherMap API
    - \[**FlaskWeather**\] sets up flask server to handle requests w/ flask router
    - \[**LogWrapper**\] is a custom wrapper for FlaskWeather which logs to log file. 

- \[**mrws_c.py**\] (map-reduce-william-shakespeare-common) extracts and counts up the number instances of each word 
- \[**mrws.py**\]   (map-reduce-william-shakespeare) extracts and counts up the number instances of each word AND role AND stores word counts by act number
- \[**ws.txt**\] is shakespeare's A Midsummer Night's Dream the file to read from
- \[**mymongo.py**\] is a template for how i'd implement a connection to mongo