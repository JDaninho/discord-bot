import os
import logging
import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()
APEX_API_KEY = os.getenv("TRACKER_API_KEY")


class ApexAPI:
    @staticmethod
    def get_stats(username):
        return ApexAPI.request("profile/5/{}".format(username))

    # Creating a request method that uses the API url and the API key
    @staticmethod
    def request(method):
        try:
            r = requests.get('https://public-api.tracker.gg/v2/apex/standard/{}'.format(method),
                             headers={'TRN-Api-Key': APEX_API_KEY, 'Accept': 'application/vnd.api+json'},
                             timeout=10)
            if r.status_code == 200:
                return r.json()
        except Exception as e:
            logging.error(e)

        return None
