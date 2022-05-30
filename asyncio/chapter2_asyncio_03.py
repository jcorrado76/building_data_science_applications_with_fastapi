import asyncio


async def printer(name: str, times: int) -> None:
    for _ in range(times):
        print(name)
        # await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        printer("Coroutine A", 3),
        printer("Coroutine B", 2)
    )

if __name__ == "__main__":
    asyncio.run(main())

