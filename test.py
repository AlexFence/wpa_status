import wpa_status

client = wpa_status.Client("/tmp/wifi-chan.sok")

print(wpa_status.ping(client).serialize())

print(wpa_status.list_networks(client).serialize())

print(wpa_status.status(client).serialize())
