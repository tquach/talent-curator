import requests
from talent_curator import app
GOOGLE_DRIVE_API_URI = 'https://www.googleapis.com/drive/v2/files/'

logger = app.logger
HEADERS = {
    'Authorization': "Bearer {access_token}",
    'Content-type': "application/json",
}


class GoogleDriveAPI(object):
    def get_document(self, access_token, document_id):
        headers = self.build_headers(access_token=access_token)

        r = requests.get(GOOGLE_DRIVE_API_URI + document_id, headers=headers)
        file_resource = None
        if r.status_code == requests.codes.ok:
            file_resource = r.json
            logger.debug("File found: %s", file_resource)
        else:
            logger.error("Failed to find document: %s", r.reason)
            logger.error("Full response %s", r.text)
        return file_resource

    def search(self, access_token, query):
        headers = self.build_headers(access_token=access_token)
        query_string = {'q': query}
        r = requests.get(GOOGLE_DRIVE_API_URI, headers=headers, params=query_string)
        if r.status_code != requests.codes.ok:
            return None

        logger.debug("Response %s" % r.text)
        results_list = r.json['items']
        return results_list

    def children(self, access_token, folder_id):
        headers = self.build_headers(access_token=access_token)
        r = requests.get(GOOGLE_DRIVE_API_URI + folder_id + '/children', headers=headers, params={'maxResults': 5})
        logger.debug("Response %s" % r.json['items'])
        if r.status_code != requests.codes.ok:
            return None
        return r.json['items']

    def build_headers(self, *args, **kwargs):
        headers = {}
        for key, val in HEADERS.iteritems():
            headers[key] = val.format(**kwargs)
        return headers
