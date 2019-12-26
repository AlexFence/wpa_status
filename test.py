import wpa_status

client = wpa_status.Client("/tmp/wifi-chan.sok")


def ping(client):
    response = client.request(wpa_status.Method.PING)
    return response


def status(client):
    response = client.request(wpa_status.Method.STATUS)
    return response


def list_n(client):
    response = client.request(wpa_status.Method.LIST_NETWORKS)
    return response


print(ping(client).serialize())


client = wpa_status.Client("/tmp/wifi-chan.sok")

print(list_n(client).serialize())


client = wpa_status.Client("/tmp/wifi-chan.sok")
print(status(client).serialize())
