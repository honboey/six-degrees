# Six Degrees of the Rap Nation

This is a Python project

## Running the project

### Setting up a virtual environment

It's a good idea to setup a virtual environment when running this project. To learn how to do this, freeCodeCamp have a [good walkthrough](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) of the process.


### Installing the requirements

When that's done, run `pip install -r requirements.txt`.


### Connecting to the Spotify Web API

You will now need a Spotify `Client ID` and `Client Secret` in order to connect to the Spotify API. To do so, follow the steps in Spotify's [Getting started with Web API](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) up to the step "Request an access token".

Once you have your `ClientID` and `Client Secret` then create an `.env` file in the root of the project. In that file add the following:
```
CLIENT_ID=<put your Client ID here>
CLIENT_SECRET=<put your Client Secret here>
```

### Running the app

Run `python six_degrees.py`
