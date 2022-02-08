#!/usr/bin/env python3
import os
from speedtest import Speedtest
import sheets

def run_speedtest():
    s = Speedtest()

    s.get_best_server()
    s.download()
    s.upload()

    return s.results

print("Running speedtest...")
test = run_speedtest()
print("Speedtest finished.")
print("Download: {}\nUpload: {}\nPing: {}\n".format(test.download, test.upload, test.ping))
print("Inserting into Google Docs Spreadsheet...")
sheets.insert_speedtest_result(test, os.environ['SPREADSHEET_ID'])
