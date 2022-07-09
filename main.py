"""
main
"""
from __future__ import annotations

import asyncio

from modules.Section1_6 import section1_6
from modules.lower_layer_modules.Exceptions import Error


async def main() -> None:
    """
    main program
    """
    try:
        section1_6()

    except Error as err:
        print(err.args)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    asyncio.run(main())
