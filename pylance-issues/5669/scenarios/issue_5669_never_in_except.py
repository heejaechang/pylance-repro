# Issue 5669: A local variable is being treated as type 'Never' in an except handler
# https://github.com/microsoft/pylance-release/issues/5669
#
# When an async method has no return type annotation (simulating an untyped library),
# a variable annotated as `T | None` that is assigned from `await untyped_method()`
# inside a try block gets narrowed to `Never` after an `is not None` guard in the
# except handler.
#
# Expected: deviceConnection should be `DeviceConnection` (not `Never`) after the
# `if deviceConnection is not None` guard in the except block.

class DeviceConnection:
    async def disconnect(self) -> None: ...


class Device:
    # No return annotation — simulates untyped third-party library (e.g. aioble)
    async def connect(self): ...


async def do_connect(device: Device) -> None:
    deviceConnection: DeviceConnection | None = None
    try:
        deviceConnection = await device.connect()
        if not deviceConnection:
            return
        # doing stuff with deviceConnection
    except Exception as ex:
        if deviceConnection is not None:
            await deviceConnection.disconnect()  # BUG: Pylance reports "Never" is not awaitable
