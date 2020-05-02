import asyncio



async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
    print("Done w/ nums in range {} divisible by {}".format(inrange,div_by))
    return located


async def main():
    div1 = loop.create_task(find_divisibles(885585,279))
    div2 = loop.create_task(find_divisibles(58798,278))
    div3 = loop.create_task(find_divisibles(58987,642))
    await asyncio.wait([div1,div2,div3])
    return div1,div2,div3

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        pass
    finally:
        loop.close()