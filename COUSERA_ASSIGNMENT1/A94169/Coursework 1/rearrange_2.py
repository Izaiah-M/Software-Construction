#!/usr/bin/env python3

import re

def rearrange_name(name):
    # Regular expression to match the 'Last, First' pattern
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    # Check if the pattern was not found
    if result == None:
        # Return the original name if the pattern is not matched
        return name
    # Rearrange the name to 'First Last' format
    return "{} {}".format(result[2], result[1])