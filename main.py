"""
main
"""
from __future__ import annotations

import asyncio

from modules.Section1_6 import section1_6
from modules.lower_layer_modules.Exceptions import Error
from modules.section2_3 import section2_3


async def main() -> None:
    """
    main program
    """
    try:
        # section1_6()
        section2_3()

    except Error as err:
        print(err.args)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    asyncio.run(main())
