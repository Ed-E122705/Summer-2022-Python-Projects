# AD1 Systems - Internet Speed Checker

# This project uses the speedtest package to output your internet's download and upload speeds and the ping

import speedtest

spdtest = speedtest.Speedtest()

print("Waiting...")

dload = spdtest.download()
uload = spdtest.upload()
pload = spdtest.results.ping

print(f"Download speed: {dload/1024/1024:.1f} Mb/s")
print(f"Upload speed: {uload/1024/1024:.1f} Mb/s")
print(f"Ping: {pload:.1f} ms")