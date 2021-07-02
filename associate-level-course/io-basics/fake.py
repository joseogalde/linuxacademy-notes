import errno
import os

try:
    f = open("fake.txt", 'r')
except OSError as err:
    print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")

