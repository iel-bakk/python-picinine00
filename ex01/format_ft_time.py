import time
from time import gmtime, strftime

timestamp = time.time()

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
print(strftime("%b %d %Y", gmtime()))