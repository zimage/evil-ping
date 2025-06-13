# evil-ping

```bash
usage: evil.py [-h] [-E] [-c COUNT] [-t TTL] [-W TIMEOUT] [-i INTERVAL] [-s SIZE] destination

send ICMP ECHO_REQUEST to network hosts

positional arguments:
  destination               DNS name or IP address (type: str)

optional arguments:
  -h, --help               show this help message and exit
  -E, --evil               send evil packets (type: bool, default: False)
  -c, --count COUNT        stop after count replies (type: int, default: 5)
  -t, --ttl TTL            define time to live (type: int, default: 64)
  -W, --timeout TIMEOUT    time to wait for response (type: float, default: 1.0)
  -i, --interval INTERVAL  seconds between sending each packet (type: float, default: 1.0)
  -s, --size SIZE          use size as number of data bytes to be sent (type: int, default: 56)
```
