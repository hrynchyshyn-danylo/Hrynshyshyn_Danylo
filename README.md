before running anything, create venv and install requirements
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

behave.ini contains all pre-defined testing values related to file paths and file contents, they can be changed

your dropbox api access token can be found here: https://www.dropbox.com/developers/apps/info/your_app_id
to run tests with your access token, you can : 
1. export it as an environment variable :
    ```
    export DROPBOX_ACCESS_TOKEN=<your access token>
    behave -D access_token=$DROPBOX_ACCESS_TOKEN
    ```
2. or pass it as a parameter explicitly :
    ```
    behave -D access_token=<your access token>
    ```

run all tests and save report in basic format :
```
behave -D access_token=$DROPBOX_ACCESS_TOKEN -o report.txt -f plain
```

run all tests and save report in json format :
```
behave -D access_token=$DROPBOX_ACCESS_TOKEN -o report.json -f json.pretty
```
