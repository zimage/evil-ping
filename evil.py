#!/usr/bin/env python
from scapy.all import *
import time
import arguably

@arguably.command
def ping(destination, *, evil = False, count = 5, ttl = 64, timeout = 1.0, interval = 1.0, size = 56):
    """
    send ICMP ECHO_REQUEST to network hosts
    Args:
        destination:  DNS name or IP address
        count: [-c] stop after {count} replies
        evil: [-E] send evil packets
        interval: [-i] seconds between sending each packet
        size: [-s] use {size} as number of data bytes to be sent
        ttl: [-t] define time to live
        timeout: [-W] time to wait for response
    """
    kwargs = {"dst": destination, "ttl": ttl}
    if evil:
        kwargs["flags"] = "evil"

    #data = 'A' * 100
    print(f"PING {destination} ({destination}) {size}({size+28}) bytes of data.")
    for i in range(count):
        packet = IP(**kwargs)/ICMP(seq=i)/("X"*size)
        reply = sr1(packet, timeout=timeout, verbose=0)
        if reply:
             print(f"{reply.len} bytes from {reply.src}: icmp_seq={reply.seq} ttl={reply.ttl} time=x.xxx ms")
        else:
             print("Timeout waiting for %s" % packet[IP].dst)
        time.sleep(interval)

if __name__ == "__main__":
    arguably.run()
