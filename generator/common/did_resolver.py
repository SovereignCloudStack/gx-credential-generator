""" Modified copy from https://github.com/decentralized-identity/universal-resolver-python/blob/master/UniversalResolver.py"""

import requests


class DidResolver:

    def __init__(self, url):
        """
        Inits DidResolver
        @param url: URL of DID resolver
        """
        self.url = url

    def resolve(self, did) -> dict:
        """
        Resolve given DID and returns DID document.
        @param did: DID to be resolved
        @return: DID document and dictionary
        """
        if not self.url.endswith('/'):
            self.url += '/'
        url = self.url + did
        response = requests.get(url)
        if response.status_code is 200:
            return response.json()
