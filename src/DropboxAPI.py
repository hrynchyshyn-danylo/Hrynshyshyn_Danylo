import json
import os
from typing import Optional
import requests

class API :
    def __init__(self, access_token):
        self.access_token = access_token

    def get_bearer_headers(self):
        return {
            "Authorization" : "Bearer " + self.access_token,
        }

    def get_json_headers(self):
        bearer_header = self.get_bearer_headers()
        bearer_header["Content-Type"] = "application/json"
        return bearer_header

class DropboxAPI(API) :
    def __init__(self, access_token) :
        super().__init__(access_token)
        self.api_url = "https://api.dropboxapi.com/2"
        self.content_url = "https://content.dropboxapi.com/2"

    def get_api_url(self, method):
        return f"{self.api_url}/{method}"

    def get_content_url(self, method):
        return f"{self.content_url}/{method}"

    def verify_token(self):
        r = requests.post(
            self.get_api_url('check/user'),
            headers = self.get_json_headers(),
            json = {'query' : 'foo'}
        )
        return r

    def upload_file(self, file_path, dropbox_file_path):
        headers = self.get_bearer_headers()
        headers.update({
            "Dropbox-API-Arg": "{\"autorename\":false,\"mode\":\"add\",\"mute\":false,\"path\":\"%s\",\"strict_conflict\":false}" % dropbox_file_path,
            "Content-Type": "application/octet-stream"
        })
        with open(file_path, 'rb') as f:
            r = requests.post(self.get_content_url("files/upload"), headers=headers, data=f.read())
        return r

    def get_file_metadata(self, dropbox_file_path):
        data = {'path' : dropbox_file_path}
        r = requests.post(
            self.get_api_url('files/get_metadata'),
            headers = self.get_json_headers(),
            json = data
        )
        return r

    def download_file(self, download_path, dropbox_file_path):
        headers = self.get_bearer_headers()
        headers['Dropbox-API-Arg'] = json.dumps({'path' : dropbox_file_path})
        r = requests.post(
            self.get_content_url('files/download'),
            headers = headers
        )
        with open(download_path, 'wb') as f:
            f.write(r.content)
        return r

    def delete_file(self, dropbox_file_path):
        r = requests.post(
            self.get_api_url('files/delete'),
            headers = self.get_json_headers(),
            json = {'path' : dropbox_file_path}
        )
        return r

