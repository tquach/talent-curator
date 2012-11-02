import logging
import requests

logger = logging.getLogger(__name__)


class GoogleDriveAPI(object):

    def get_document(self, access_token, document_id):
        headers = {
            'Authorization': '  Bearer ' + access_token,
            'Content-type': 'application/json',
        }
        r = requests.get('https://www.googleapis.com/drive/v2/files/' + document_id,
                headers=headers)

        logger.debug(r.request.headers)
        logger.debug(r.request.data)
        file_resource = ""
        if r.status_code == requests.codes.ok:
            file_resource = r.json
            logger.debug("File found: %s", file_resource)
        else:
            logger.error("Failed to find document: %s", r.reason)
            logger.error("Full response %s", r.text)
            r.raise_for_status()
        return (file_resource, r.json)
