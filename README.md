This is a selenium web scraper that scrapes the groupgolfer.com website
It looks at the daily deal then tells you how far away it is from your location
To use this you need
1: Download PushBullet on your phone and get an API key, put it in a config.ini file in the same folder in the form of:
[API]
key = 
2: Sign up for a google maps developer API key, make sure you can use the distance matrix api functions, setup api key similarly to above:
[GOOGLEAPI]
googleapi = 
3: Create an account on groupgolfer and but the information in the config.ini file as such:
[EMAIL]
email = 
[PASS]
pass =
4: Download and properly install selenium, make sure to have your chromedriver in the same folder as the program.
