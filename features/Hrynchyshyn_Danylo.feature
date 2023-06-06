Feature: Interaction with Dropbox API

  Scenario: Authentication Verification
    Given DropBox api client with access token
      Then a successful response should be received

  Scenario: File Upload
    Given DropBox api client with access token
      When a file is uploaded to Dropbox
        Then the uploaded file should be visible in the Dropbox folder

  Scenario: File Metadata Retrieval
    Given DropBox api client with access token
      Then the metadata of the file should be accessible

  Scenario: File Download
    Given DropBox api client with access token
      When a file is downloaded from Dropbox
        Then the downloaded file should be visible in the local folder

  Scenario: File Deletion
    Given DropBox api client with access token
      When a file is deleted from Dropbox
        Then the deleted file should no longer be visible in the Dropbox folder
