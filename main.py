#!/usr/bin/env python3
import os
from speedtest import Speedtest
import sheets
from time import sleep


def run_speedtest():
    s = Speedtest()

    s.get_best_server()
    s.download()
    s.upload()

    return s.results


def try_speedtest():
    print("Running speedtest...")
    test = run_speedtest()
    print("Speedtest finished.")
    print("Download: {}\nUpload: {}\nPing: {}\n".format(
        test.download, test.upload, test.ping))
    print("Inserting into Google Docs Spreadsheet...")
    sheets.insert_speedtest_result(test, os.environ['SPREADSHEET_ID'])


retries = 0

while retries <= 3:
    try:
        retries = retries + 1
        try_speedtest()
        break
    except:
        delay = retries * 10
        print("Speedtest failed. Retrying in {} seconds.".format(delay))
        sleep(delay)
