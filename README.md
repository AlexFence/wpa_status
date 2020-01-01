# Wpa_status
Client library for [wpa_statusd](https://github.com/AlexFence/wpa_statusd).

## Example
```python
import wpa_status

client = wpa_status.Client()
status = wpa_status.status(client)
ssid = status.result["Status"]["ssid"]
print(ssid)
```
