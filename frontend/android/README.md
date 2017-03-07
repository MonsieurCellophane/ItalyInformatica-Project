# IIP Android App

In order to let everyone work with their own urls, the app is setup to retrieve them from a 
.properties file that you need to create: 

 1. Navigate to app/src/main/res
 2. Create a folder called "raw" and move inside it
 3. Create a file called "config.properties"
 4. Write values for all the endpoints you need. BASE_URL, API_AUTH_TOKEN and API_AUTH_VERIFY
    are required to login 
 
Es:

BASE_URL = http://localhost:8000

API_AUTH_TOKEN = /api/auth/token/

API_AUTH_VERIFY = /api/auth/verify/

