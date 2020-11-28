import time

from yaspin import yaspin

with yaspin() as sp:
    sp.text = "processed 1"
    time.sleep(1)
    sp.text = "processed 2"
    time.sleep(1)
    sp.text = "processed 3"
    time.sleep(1)
    sp.text = "processed 4"

print("done!")
