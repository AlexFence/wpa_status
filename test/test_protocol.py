from wpa_status.protocol import Request, Method


def test_request():
    req = Request("PING")
    assert req.method.__class__ is Method
    # rqeust generates a fresh uuid upon creation
    id = req.id
    assert req.serialize() == {
        "id": id,
        "type": "Request",
        "method": "PING",
        "params": None
    }
