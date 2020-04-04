# subd.py

# Tutorial had subdomains text document just live in the same directory as script.
# I chose to store it some where else, which meant pulling it in differently.
# I decided to use pathlib and hard code the full path.

import requests
import sys
import pathlib

subd_file = pathlib.Path("E:\Documents\Python\subdomains-1000.txt")

sub_list = open(subd_file).read()
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_to_check)

    except requests.ConnectionError:
        pass

    else:
        print(f"Valid domain: {url_to_check}")