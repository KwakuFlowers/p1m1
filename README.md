# milestone1-kflowers9
1)For API access to Spotify:

-Create a .env file in your root directory, and create a variable named (exactly) "CLIENT_ID" and "CLIENT_SECRET"
-Go to Spotify Devlopers page, login, and create your app with Spotify and put your client ID and Secret from the dashboard into your .env file for each variable respectively. 
-REMEMBER!: Put .env file under your .gitignore file 

2) For API access to Genius 
- Do the same thing for Genius you did for spotify, but instead just follow the instructions on the website in order to get an access token with your CLIENT_ID/CLIENT_SECRET. Since Genius ddoesn't require much for Apps that don't reach an endpoint that looks at User information, we will be using the link that generates an access token for us. This token lasts forever, so we can put that in our GACCESS_TOKEN section in  our .env variable. 