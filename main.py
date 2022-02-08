#!/usr/bin/env python3
import speedtest

s = speedtest.Speedtest()

s.get_best_server()
s.download()
s.upload()

print(s.results.json())
