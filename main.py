#!/usr/bin/env python3
"""Works on My Machine — entry for Fortune Cookie Funnies for Engineers on make.fun.

Prints exactly one line (at most 120 characters): a fortune cookie
message aimed at a software engineer.
"""

LINE = "You will find the bug exactly one minute after telling everyone it cannot be reproduced. Lucky numbers: 200, 404, 500."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 120
    print(LINE)


if __name__ == "__main__":
    main()
