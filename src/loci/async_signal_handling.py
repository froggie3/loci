import asyncio
import signal
import sys


async def main_loop():
    print("Running async main loop...")
    while True:
        await asyncio.sleep(1)


def cleanup():
    print("Caught signal. Cleaning up...")
    sys.exit(0)


def async_main():
    loop = asyncio.get_event_loop()

    # adding signal handlers
    loop.add_signal_handler(signal.SIGINT, cleanup)  # Ctrl+C
    loop.add_signal_handler(signal.SIGHUP, cleanup)  # HUP

    try:
        loop.run_until_complete(main_loop())
    except KeyboardInterrupt:
        cleanup()


def main():
    asyncio.run(async_main())
