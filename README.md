# Smite-Item-god-Analysis
A personal project that in short scrapes the wikis for smite items and their stats, and gods and and stored into a csv. then updated into a google sheet.

[Note] Please Note this was one of my first big projects and first time uses classes, the code has already been cleaned like 5 times from this point and is still extreamly messy due to learning. Its going to be very insufcient but a monumental change in my coding capabilities that needed to be documented.

-First thing to do, if you want a updated list, is copy and paste a list of the SmiteGame Items from the wiki to the SmiteItemName.csv this list will be used to generate all the necessary urls to scrape the webpages for desired attributes of that item.

-you can run the ItemNameCleanup.py that will remove the png file text from the list and create a clean list of Smite item names.

-First python codes to run is the SmiteItemWikiScraping.py & SmiteGodWikiScraping.py these two scripts will take a minute or two to run because of all the URL's they have to pull to scrape the HTML for the wanted information.

-secondly you could change the Token and make your own google API account to run the GoogleSheetsAPI.py script that will create a clean google sheet for the Smite gods attributes and the Smite item Attributes....... If you just want to see the result or update the google sheet the API is set for you can go to this link
[https://docs.google.com/spreadsheets/d/1yzMqIsI2B7Asgo-QzTDGg42YlebmikCVBxGvb72eooQ/edit?usp=sharing]

-third, if you are interested in some code that tests potential smite builds, as of now I have the SmiteTest.py which does a scenrio amount of damage and runs through all possible builds to take the least amount of dmg. this returns top 10 builds to the terminal, but still working on this part as its not super effective.

