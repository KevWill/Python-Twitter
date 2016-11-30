import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
import os

class Twitter():

    def __init__(self):

        self.config = {}
        self.oauth = OAuth1(self.config['consumer_key'],
                       self.config['consumer_secret'],
                       self.config['access_token'],
                       self.config['access_secret']
                       )

        self.base_url = 'https://api.twitter.com/1.1'


    def setAuth(self, consumer_key, consumer_secret, access_token, acces_secret):

        self.oauth = OAuth1(consumer_key, consumer_secret, access_token, acces_secret)

    def showFriendship(self, source, target):

        url = self.base_url + '/friendships/show.json'
        params = {'source_screen_name': source,
                  'target_screen_name': target}
        r = self._request(url, params)
        friendship = r.json()
        return {'following': friendship['relationship']['source']['following'],
                'followed': friendship['relationship']['source']['followed_by']}


    def getFollowers(self, user, cursor = -1, count = 5000):

        url = self.base_url + '/followers/ids.json'
        params = {'cursor': cursor,
                  'screen_name': user,
                  'count': count}
        r = self._request(url, params)
        user_ids = r.json()
        return user_ids


    def getUserInfo(self, users):

        url = self.base_url + '/users/lookup.json'
        if isinstance(users, list):
            if isinstance(users[0], int):
                params = {'id': ','.join(users)}
            else:
                params = {'screen_name': ','.join(users)}
        elif isinstance(users, basestring):
            params = {'screen_name': users}
        elif isinstance(users, int):
            params = {'id': users}
        else:
            raise TypeError("Users should be list, string or int, not {}.".format(str(type(users))))

        r = self._request(url, params).json()
        return r


    def followUser(self, user):

        url = self.base_url + '/friendships/create.json'
        if isinstance(user, basestring):
            params = {'screen_name': user}
        elif isinstance(user, int):
            params = {'id': user}
        else:
            raise TypeError("User should be list or string, not {}.".format(str(type(user))))

        r = self._request(url, params, method="POST").json()
        return r

    def getRateLimit(self, resources):

        url = self.base_url + '/application/rate_limit_status.json'
        if isinstance(resources, list):
            params = {'resources': ','.join(resources)}
        elif isinstance(resources, basestring):
            params = {'resources': resources}
        else:
            raise TypeError("Resources should be list or string, not {}.".format(str(type(resources))))

        r = self._request(url, params).json()
        return r['resources']


    def _request(self, url, params, method='GET'):

        if method == 'GET':
            r = requests.get(url = url, params = params, auth = self.oauth)
        elif method == 'POST':
            r = requests.post(url = url, params = params, auth = self.oauth)
        else:
            raise TypeError("'Method' should be either POST or GET.")
        return r