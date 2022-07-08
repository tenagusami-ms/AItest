"""
main
"""
from __future__ import annotations

import asyncio


async def main() -> None:
    """
    main program
    """
    try:
        pass

    except Error as err:
        print(err.args)
        exit(1)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    asyncio.run(main())
