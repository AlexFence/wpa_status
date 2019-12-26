from wpa_status.client import Client
from wpa_status.protocol import Method


def ping(client: Client):
    return client.request(Method.PING)


def status(client: Client):
    return client.request(Method.STATUS)


def list_networks(client: Client):
    return client.request(Method.LIST_NETWORKS)


def is_supplicant_running(client: Client):
    return client.request(Method.SUPPLICANT_RUNNING)
