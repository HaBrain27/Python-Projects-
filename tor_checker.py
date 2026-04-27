import re
from urllib.parse import urlparse

def check_onion_format(url: str) -> bool:
    parsed = urlparse(url if "://" in url else "http://" + url)
    host = parsed.hostname or ""

    # v3 onion addresses are 56 chars, base32-looking, ending in .onion
    pattern = r"^[a-z2-7]{56}\.onion$"
    return bool(re.match(pattern, host))

test = input("Enter .onion URL: ").strip()

if check_onion_format(test):
    print("Looks like a valid v3 .onion address format.")
else:
    print("Not a valid v3 .onion address format.")
