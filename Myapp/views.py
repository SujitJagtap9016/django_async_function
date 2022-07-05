from django.shortcuts import render
import asyncio
import aiohttp

# Here we have written all the actual code in this views.py file
# All functionality we need to perform in this field.

# Create your views here.

# as per the requirenment I have used the async function here, for accessing the async funcationality,
# we need to import the python async modules as per the requrnments that is asyncio and aiohttp.

# For using async function we need to use acync funcation name. 
# Also I have passed request in this functions, when the the user reqested then it will pass in this functions and do the functionality

async def index(request):
    
    # as per my knowladge ClientSession is the heart and the main entry point for all client API operations.
    # Create the session first, use the instance for performing HTTP requests and initiating WebSocket connections.
    # The session contains a cookie storage and connection pool, thus cookies and connections are shared between HTTP requests sent by the same session.
    # The keyword async before a function makes the function return a promise:

     async with aiohttp.ClientSession() as session:
         async with session.get("https://pokeapi.co/api/v2/pokemon/1") as res:

            # The await keyword is only valid inside async functions within regular JavaScript code.
            # await makes a function wait for a Promise
            # To featch the date from async with session.get an print that 
             data = await res.json()

             print(data)

    # return function we will use for give the response to the user from the Html templetes format 
     return render(
         request,
         "index.html",
         {"data": data},
     )