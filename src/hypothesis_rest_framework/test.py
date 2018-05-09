import hypothesis

import rest_framework.test as rf_test
hypothesis.extra.django.TestCase


class APITransactionTestCase(hypothesis.extra.django.TransactionTestCase):
    client_class = APIClient


class APITestCase(hypothesis.extra.django.TestCase):
    client_class = APIClient

