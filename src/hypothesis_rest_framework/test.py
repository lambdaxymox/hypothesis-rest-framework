import hypothesis

import rest_framework.test as rf_test


class APITestCase(hypothesis.extra.django.TestCase):
    client_class = rf_test.APIClient

