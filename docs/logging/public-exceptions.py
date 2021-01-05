# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""
Sample use of Public* exception types.
"""

from confidential_ml_utils.exceptions import prefix_stack_trace, PublicValueError


def divide(a, b):
    if not b:
        raise PublicValueError("Second argument cannot be null or zero.")
    return a / b


# Output will be:
# SystemLog: Traceback (most recent call last):
# SystemLog:   File ".\docs\logging\public-exceptions.py", line 24, in main
# SystemLog:     divide(1, 0)
# SystemLog:   File ".\docs\logging\public-exceptions.py", line 13, in divide
# SystemLog:     raise PublicValueError("Second argument cannot be null or zero.")
# SystemLog: confidential_ml_utils.exceptions.PublicValueError: SystemLog:Second argument cannot be null or zero.
@prefix_stack_trace()
def main():
    divide(1, 0)


if __name__ == "__main__":
    main()
