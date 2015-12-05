import unittest
from lib import signer
import re
import datetime
import requests
import json
import uuid


URL_BASE = "https://demo-api.fidem360.com"

PATH_CONTENT_MENUS = "/api/content/menus"
PATH_CONTENT_NEWLISTS = "/api/content/newslists"
PATH_CONTENT_PAGES = "/api/content/pages"
PATH_CONTESTS = "/api/contests"
PATH_GAMIFICATION_ACTIONS = "/api/gamification/actions"
PATH_MEMBERS = "/api/members"
URL_CONTENT_MENUS = "%s%s" % (URL_BASE, PATH_CONTENT_MENUS)
URL_CONTENT_NEWSLISTS = "%s%s" % (URL_BASE, PATH_CONTENT_NEWLISTS)
URL_CONTENT_PAGES = "%s%s" % (URL_BASE, PATH_CONTENT_PAGES)
URL_CONTESTS = "%s%s" % (URL_BASE, PATH_CONTESTS)
URL_GAMIFICATION_ACTIONS = "%s%s" % (URL_BASE, PATH_GAMIFICATION_ACTIONS)
URL_MEMBERS = "%s%s" % (URL_BASE, PATH_MEMBERS)

ACCESS_KEY_ID = "myAccessKeyId"
SECRET_ACCESS_KEY = "mySecretAccessKey"

REGEX_FIDEM_AUTH = re.compile(r'FIDEM4-HMAC-SHA256 Credential=%s\/\d{8}\/fidem, SignedHeaders=date;x-fidem-date, Signature=[0-9a-f]{64}' % ACCESS_KEY_ID)


class FidemSignerTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # -----------------------------------------------------------------------------------------

    def test_signer(self):
        """
        Basic test - auth headers generation, sign, verify
        :return:
        """
        request = {
            'headers': {
                'date': "%s" % datetime.datetime.utcnow().isoformat()
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        self.assertIn('headers', request)
        self.assertIn('X-Fidem-Date', request['headers'])
        self.assertIn('Authorization', request["headers"])

        match = re.match(REGEX_FIDEM_AUTH, request['headers']['Authorization'])
        self.assertIsNotNone(match)

        result = signer.verify(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        self.assertTrue(result)

    # -----------------------------------------------------------------------------------------

    def test_api_content_menus(self):
        """
        test endpoint - GET /api/content/menus
        Lists Menu
        :return:
        """
        request = {
            'method': 'GET',
            'path': PATH_CONTENT_MENUS,
            'headers': {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        r = requests.get(
            url=URL_CONTENT_MENUS,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_content_newslists(self):
        """
        test endpoint - GET /api/content/newslists/{newslist-id}
        Get news list
        :return:
        """
        test_newslist_id = "N1le9WO1c"
        url = "%s/%s" % (URL_CONTENT_NEWSLISTS, test_newslist_id)

        request = {
            'method': 'GET',
            'path': '%s/%s' % (PATH_CONTENT_NEWLISTS, test_newslist_id),
            'headers': {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        r = requests.get(
            url=url,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_content_pages(self):
        """
        test endpoint - GET /api/content/pages/{page-id}
        Get page
        :return:
        """
        test_page_id = "NJlecXOJc"
        url = "%s/%s" % (URL_CONTENT_PAGES, test_page_id)

        request = {
            'method': 'GET',
            'path': '%s/%s' % (PATH_CONTENT_PAGES, test_page_id),
            'headers': {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        r = requests.get(
            url=url,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_contests(self):
        """
        test endpoint - GET /api/contests
        Get active contests list
        :return:
        """

        request = {
            'method': 'GET',
            'path': PATH_CONTESTS,
            'headers': {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        r = requests.get(
            url=URL_CONTESTS,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_gamification_actions(self):
        """
        test endpoint - POST /api/gamification/actions
        Log an action
        :return:
        """

        request = {
            "method": "POST",
            "path": PATH_GAMIFICATION_ACTIONS,
            "headers": {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            },
            "body": {
                "type": "test"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        r = requests.post(
            url=URL_GAMIFICATION_ACTIONS,
            headers=request['headers'],
            json=request['body']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_members_post(self):
        """
        test endpoint - POST /api/members
        Create member
        :return:
        """

        request = {
            "method": "POST",
            "path": PATH_MEMBERS,
            "headers": {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                'Content-Type': 'application/json'
            },
            "body": {
                "external_id": unicode(uuid.uuid4()),
                "profile": {
                    "alias": "jcvd",
                    "first_name": "JC",
                    "last_name": "VD",
                    "picture_url": "https://mightycast-api-dev.appspot.com/img/ok.png",
                    "email": "jc@vandamme.com",
                    "phone": "1-976-TAMERE-0",
                    "address": {
                        "line": "1234 Sesame Street",
                        "city": "Beverly Hills",
                        "state": "CA",
                        "country": "US",
                        "postal_code": "90210"
                    }
                },
                "preferred_locale": "EN"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        body = json.dumps(request['body'])
        r = requests.post(
            url=URL_MEMBERS,
            headers=request['headers'],
            json=request['body']
        )
        self.assertEqual(201, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_members_get(self):
        """
        test endpoint - GET /api/members/{memberId}
        Get member profile
        :return:
        """
        test_member_id = "E1xJe_e8Y"
        url = "%s/%s" % (URL_MEMBERS, test_member_id)

        request = {
            'method': 'GET',
            'path': '%s/%s' % (PATH_MEMBERS, test_member_id),
            'headers': {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        match = re.match(REGEX_FIDEM_AUTH, request['headers']['Authorization'])
        self.assertIsNotNone(match)

        r = requests.get(
            url=url,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_members_put(self):
        """
        test endpoint - PUT /api/members/{member-id}
        Update member profile
        :return:
        """

        test_member_id = "E1xJe_e8Y"
        url = "%s/%s" % (URL_MEMBERS, test_member_id)

        request = {
            'method': 'GET',
            'path': '%s/%s' % (PATH_MEMBERS, test_member_id),
            'headers': {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        r = requests.get(
            url=url,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

        dico = r.json()
        self.assertIn('data', dico)
        self.assertIn('__v', dico['data'])
        version = dico['data']['__v']

        request = {
            "method": "PUT",
            "path": "%s/%s" % (PATH_MEMBERS, test_member_id),
            "headers": {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            },
            "body": {
                "__v": version,
                "profile": {
                    "picture_url": "https://mightycast-api-dev.appspot.com/img/ok.png"
                }
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        match = re.match(REGEX_FIDEM_AUTH, request['headers']['Authorization'])
        self.assertIsNotNone(match)

        r = requests.put(
            url=url,
            headers=request['headers'],
            json=request['body']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_members_challenges(self):
        """
        test endpoint - GET /api/members/{member-id}/challenges
        Gets all challenges for a member
        :return:
        """

        test_member_id = "E1xJe_e8Y"
        path = "%s/%s/challenges" % (PATH_MEMBERS, test_member_id)
        url = "%s/%s" % (URL_BASE, path)

        request = {
            "method": "GET",
            "path": path,
            "headers": {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        match = re.match(REGEX_FIDEM_AUTH, request['headers']['Authorization'])
        self.assertIsNotNone(match)

        r = requests.get(
            url=url,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_members_challenges_done(self):
        """
        test endpoint - GET /api/members/{member-id}/challenges/done
        Gets all done member challenges
        :return:
        """

        test_member_id = "E1xJe_e8Y"
        path = "%s/%s/challenges/done" % (PATH_MEMBERS, test_member_id)
        url = "%s/%s" % (URL_BASE, path)

        request = {
            "method": "GET",
            "path": path,
            "headers": {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        match = re.match(REGEX_FIDEM_AUTH, request['headers']['Authorization'])
        self.assertIsNotNone(match)

        r = requests.get(
            url=url,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)

    # -----------------------------------------------------------------------------------------

    def test_api_members_challenges_todo(self):
        """
        test endpoint - GET /api/members/{member-id}/challenges/todo
        Gets all member challenge to do
        :return:
        """

        test_member_id = "E1xJe_e8Y"
        path = "%s/%s/challenges/todo" % (PATH_MEMBERS, test_member_id)
        url = "%s%s" % (URL_BASE, path)

        request = {
            "method": "GET",
            "path": path,
            "headers": {
                "date": "%s" % datetime.datetime.utcnow().isoformat(),
                "Content-Type": "application/json"
            }
        }

        request = signer.sign(request, {
            'AccessKeyId': ACCESS_KEY_ID,
            'SecretAccessKey': SECRET_ACCESS_KEY
        })

        match = re.match(REGEX_FIDEM_AUTH, request['headers']['Authorization'])
        self.assertIsNotNone(match)

        r = requests.get(
            url=url,
            headers=request['headers']
        )
        self.assertEqual(200, r.status_code)
