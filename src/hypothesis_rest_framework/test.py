import hypothesis
import rest_framework.test as rf_test
import django.test         as dt


class APITransactionTestCase(hypothesis.extra.django.TransactionTestCase):
    client_class = APIClient


class APITestCase(hypothesis.extra.django.TestCase):
    client_class = APIClient


class APISimpleTestCase(hypothesis.extra.django.HypothesisTestCase, dt.SimpleTestCase):
    client_class = APIClient


class APILiveServerTestCase(hypothesis.extra.django.HypothesisTestCase, dt.LiveServerTestCase):
    client_class = APIClient

