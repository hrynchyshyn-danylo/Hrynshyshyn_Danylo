from behave import given, when, then
from src.DropboxAPI import DropboxAPI
import os


def get_remote_file_metadata(context) :
    return context.api.get_file_metadata(context.config.userdata.get('path_remote_file_uploaded'))

@given('DropBox api client with access token')
def step_given_dropbox_api_client_with_access_token(context):
    access_token = context.config.userdata.get('access_token')
    context.api = DropboxAPI(access_token)
    assert context.api is not None, "Failed to create Dropbox API client"

@then('a successful response should be received')
def step_then_successful_response_received(context):
    response = context.api.verify_token()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}, {response.text}"

@when('a file is uploaded to Dropbox')
def step_when_file_uploaded_to_dropbox(context):
    file_path = context.config.userdata.get('path_local_file_created')
    with open(file_path, 'w') as f:
        f.write(context.config.userdata.get('file_content'))
    response = context.api.upload_file(file_path, context.config.userdata.get('path_remote_file_uploaded'))
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}, {response.text}"

@then('the uploaded file should be visible in the Dropbox folder')
def step_then_file_visible_in_dropbox(context):
    response = get_remote_file_metadata(context)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}, {response.text}"

@then('the metadata of the file should be accessible')
def step_then_metadata_accessible(context):
    response = get_remote_file_metadata(context)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}, {response.text}"

@when('a file is downloaded from Dropbox')
def step_when_file_downloaded_from_dropbox(context):
    response = context.api.download_file(
        context.config.userdata.get('path_local_file_downloaded'),
        context.config.userdata.get('path_remote_file_uploaded')
    )
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}, {response.text}"

@then('the downloaded file should be visible in the local folder')
def step_then_file_visible_in_local_folder(context):
    download_path = context.config.userdata.get('path_local_file_downloaded')
    assert os.path.exists(download_path), f"File {download_path} does not exist"

@when('a file is deleted from Dropbox')
def step_when_file_deleted_from_dropbox(context):
    response = context.api.delete_file(context.config.userdata.get('path_remote_file_uploaded'))
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}, {response.text}"

@then('the deleted file should no longer be visible in the Dropbox folder')
def step_then_file_not_visible_in_dropbox(context):
    response = get_remote_file_metadata(context)
    assert response.status_code == 409, f"Expected status code 409, but got {response.status_code}"
