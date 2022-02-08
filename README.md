# speedtest-google-sheets

This is a small python script which runs a speedtest using [speedtest.net](https://speedtest.net) and inserts it into a [Google Docs Spreadsheet](https://workspace.google.com/products/sheets/).

## Setup

1. Create a new Project in the [Google Cloud Platform Console](https://console.cloud.google.com).

2. Enable the [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com) in the API Library.

![Google Sheets API](https://user-images.githubusercontent.com/37078297/153071086-237f5325-ff7c-4b9b-a3cd-044f2f279eb3.png)

3. Go to [Credentials](https://console.cloud.google.com/apis/credentials) and create a new OAuth 2.0 Client ID for Desktop Applications.

4. Download the Credentials in the format of a json file.

![Download Button](https://user-images.githubusercontent.com/37078297/153071822-dce4b891-0419-4657-8f93-fa6e02fe0cf7.png).

5. Rename the file to `credentials.json`.

6. If you don't want to use [Docker](https://docker.com), you can now just run `main.py` and you are good to go. Otherwise you need to run the app locally to generate a google login and need to mount the `credentials.json` and `token.json` into the docker container, see [docker-compose.yml](docker-compose.yml) for an example. Also don't forget to set your Google Sheet ID in the `SPREADSHEET_ID` environment variable. Also your sheet needs to be named `Speedtest`.
