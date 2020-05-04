"""Websockets."""
import json

import websockets


def connection(funct, self=None):
    """Connection."""
    async def wrapper(self, *args, **kwargs):
        async with websockets.connect(self._uri) as websocket:
            command = funct(self, *args, **kwargs)
            await websocket.send(json.dumps(command, cls=self._encoder))
            return self._decode(await websocket.recv())

    async def wrapper_no_self(*args, **kwargs):
        async with websockets.connect(self._uri) as websocket:
            print(args, kwargs)
            command = funct(self, *args, **kwargs)
            await websocket.send(json.dumps(command, cls=self._encoder))
            return self._decode(await websocket.recv())
    if self:
        return wrapper_no_self
    return wrapper
