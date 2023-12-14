
import urllib.request
import os


def fetch_input(url, sid: str = str(os.environ.get('AOC_SID'))) -> str:
    print(sid)
    this_request = urllib.request.Request(url)
    this_request.add_header('Cookie','session='+sid)
    with urllib.request.urlopen(this_request) as response:
        return response.read().decode('utf-8')


def split_by_line(input_string) -> list:
    return input_string[:-1].split("\n")