A personal project that in short scrapes the wikis for smite items and their stats, and gods and stored them into a CSV. then updated into a Google sheet.

[Note] Please Note this was one of my first big projects and the first time using classes, the code has already been cleaned like 5 times from this point and is still extremely messy due to learning. Its going to be very insufficient but a monumental change in my coding capabilities that needed to be documented.

-First thing to do, if you want an updated list, is copy and paste a list of the SmiteGame Items from the wiki to the SmiteItemName.csv this list will be used to generate all the necessary URLs to scrape the webpages for desired attributes that item.

-you can run the ItemNameCleanup.py which will remove the png file text from the list and create a clean list of Smite item names.

-First Python codes to run is the SmiteItemWikiScraping.py & SmiteGodWikiScraping.py these two scripts will take a minute or two to run because of all the URLs they have to pull to scrape the HTML for the wanted information.

-secondly, you could change the Token and make your own Google API account to run the GoogleSheetsAPI.py script that will create a clean Google sheet for the Smite gods attributes and the Smite item Attributes....... If you just want to see the result or update the Google sheet the API is set for you can go to this link [https://docs.google.com/spreadsheets/d/1yzMqIsI2B7Asgo-QzTDGg42YlebmikCVBxGvb72eooQ/edit?usp=sharing]

-third, if you are interested in some code that tests potential smite builds, as of now I have the SmiteTest.py which does a scenario amount of damage and runs through all possible builds to take the least amount of dmg. this returns the top 10 builds to the terminal, but still working on this part as it's not super effective.
