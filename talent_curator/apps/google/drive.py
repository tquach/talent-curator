import logging
import requests
import json

logger = logging.getLogger(__name__)


class GoogleDriveAPI(object):

    def __init__(self, *args, **kwargs):
        super.__init__(GoogleDriveAPI, args, kwargs)

    def new_folder(self, access_token):
        headers = {
            'Authorization': '  Bearer ' + access_token,
            'Content-type': 'application/json',
        }
        data = {
            'title': 'Talent Curator Files',
            'mimeType': 'application/vnd.google-apps.folder',
        }
        r = requests.post('https://www.googleapis.com/drive/v2/files',
                headers=headers, data=json.dumps(data))

        logger.debug(r.request.headers)
        logger.debug(r.request.data)

        if r.status_code == requests.codes.ok:
            file_resource = r.json
            logger.debug("File created: %s", file_resource)
        else:
            logger.error("Failed to initialize folders: %s", r.reason)
            logger.error("Full response %s", r.text)
            r.raise_for_status()
        return r.json
