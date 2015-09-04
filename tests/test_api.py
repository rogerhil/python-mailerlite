#!/usr/bin/python

import os
import unittest
import mailerlite


try:
    API_KEY = os.environ['PYML_TEST_API_KEY']
except KeyError as e:
    print('You need to configure a PYML_TEST_API_KEY in your env variables. '
          '{0}'.format(e))


class ApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._api = mailerlite.Api(API_KEY)

        # Check if any campaigns exist and grab one to test against.
        try:
            # If the all_campaigns method is busted it is still tested,
            # so this failing for that reason will be reported later.
            cls._all_campaigns = cls._api.all_campaigns()
            cls._campaign_id = cls._all_campaigns['Results'][0]['id']
        except:
            cls._campaign_id = None
            print('No campaigns found, skipping tests that require one.')

        # # Try to make a list for testing against.
        # try:
        #     cls._test_list = cls._api.create_list(
        #         'pyml_test_list_{0}'.format(random.randint(100000, 999999))
        #     )
        #     cls._test_list_id = cls._test_list['id']
        # except:
        #     cls._test_list_id = None
        #     print('Something went wrong making a new list, skipping tests '
        #           'that require a test list.')

        print 'Running integration tests on the API class.'

    def test_all_campaigns(self):
        response = self._api.all_campaigns()
        expected = ('Page', 'Limit', 'RecordsOnPage', 'Results')

        self.assertItemsEqual(response, expected)

    def test_campaign_details(self):
        if self._campaign_id is None:
            self.skipTest('No campaigns found to test campaign_details.')

        response = self._api.campaign_details(self._campaign_id)
        expected = (
            'unsubscribes',
            'uniqueOpens',
            'url',
            'bounces',
            'junk',
            'clicks',
            'started',
            'done',
            'total',
            'id',
            'opens',
            'subject'
        )

        self.assertItemsEqual(response, expected)

    def test_campaign_recipients(self):
        if self._campaign_id is None:
            self.skipTest('No campaigns found to test campaign_recipients.')

        response = self._api.campaign_recipients(self._campaign_id)
        expected = (
            'RecordsOnPage',
            'Limit',
            'Results',
            'Page'
        )

        self.assertItemsEqual(response, expected)

    def test_campaign_opens(self):
        if self._campaign_id is None:
            self.skipTest('No campaigns found to test campaign_opens.')

        response = self._api.campaign_opens(self._campaign_id)
        expected = (
            'RecordsOnPage',
            'Limit',
            'Results',
            'Page'
        )

        self.assertItemsEqual(response, expected)

    def test_campaign_clicks(self):
        if self._campaign_id is None:
            self.skipTest('No campaigns found to test campaign_clicks.')

        response = self._api.campaign_clicks(self._campaign_id)
        expected = (
            'RecordsOnPage',
            'Limit',
            'Results',
            'Page'
        )

        self.assertItemsEqual(response, expected)

    def test_campaign_unsubscribes(self):
        if self._campaign_id is None:
            self.skipTest('No campaigns found to test campaign_unsubscribes.')

        response = self._api.campaign_unsubscribes(self._campaign_id)
        expected = (
            'RecordsOnPage',
            'Limit',
            'Results',
            'Page'
        )

        self.assertItemsEqual(response, expected)

    def test_campaign_bounces(self):
        if self._campaign_id is None:
            self.skipTest('No campaigns found to test campaign_bounces.')

        response = self._api.campaign_bounces(self._campaign_id)
        expected = (
            'RecordsOnPage',
            'Limit',
            'Results',
            'Page'
        )

        self.assertItemsEqual(response, expected)

    def test_campaign_spam_complaints(self):
        if self._campaign_id is None:
            self.skipTest(
                'No campaigns found to test campaign_spam_complaints.'
            )

        response = self._api.campaign_spam_complaints(self._campaign_id)
        expected = (
            'RecordsOnPage',
            'Limit',
            'Results',
            'Page'
        )

        self.assertItemsEqual(response, expected)

    def test_all_lists(self):
        response = self._api.all_lists()
        expected = (
            'RecordsOnPage',
            'Limit',
            'Results',
            'Page'
        )

        self.assertItemsEqual(response, expected)

    def test_create_list(self):
        response = self._api.create_list('pyml_test_list')
        expected = ('id', 'name')

        try:
            self._test_list_id = response['id']
        except:
            self._test_list_id = None
            print(
                'Something went wrong making a new list, skipping tests '
                'that require a test list.'
            )

        self.assertItemsEqual(response, expected)

    def test_list_details(self):
        if self._test_list_id is None:
            self.skipTest(
                'No test list found to test list_details.'
            )

        response = self._api.list_details(self._test_list_id)
        expected = (
            'updated',
            'bounced',
            'name',
            'unsubscribed',
            'date',
            'total',
            'id'
        )

        self.assertItemsEqual(response, expected)

    def test_update_list(self):
        if self._test_list_id is None:
            self.skipTest(
                'No test list found to test update_list.'
            )

        response = self._api.update_list(self._test_list_id, 'updated_name')
        expected = {u'id': 2186293, u'name': u'updated_name'}

        self.assertEqual(response, expected)

    def test_delete_list(self):
        if self._test_list_id is None:
            self.skipTest(
                'No test list found to test delete_list.'
            )

        response = self._api.delete_list(self._test_list_id)
        expected = (
            []
        )

        self.assertEquals(response, expected)
