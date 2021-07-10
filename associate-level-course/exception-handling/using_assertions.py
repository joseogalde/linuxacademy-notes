import sys

from cliassertions import main
from cliassertions import ArgumentError

try:
    main()
except (ArgumentError, AssertionError) as err:
    print(f"Error: {err}")
    sys.exit(1)
