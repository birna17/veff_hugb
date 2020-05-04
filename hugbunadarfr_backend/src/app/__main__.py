"""Run woofer's backend."""
import websockets
import asyncio
from src.app.repository.service import interface as rinterface
from src.app.controller.service import interface as cinterface


url = "localhost"
repo_port = 8765
controller_port = 8766


def repository():
    """Get repository websocket server."""
    start_server = websockets.serve(
        rinterface.repository_service, url, repo_port)
    return start_server


def controller():
    """Get controller websocket server."""
    start_server = websockets.serve(
        cinterface.controller_service, url, controller_port)
    return start_server


def main():
    """Start both the repository and controller services."""
    print("Starting backend...")
    repository_uri = f"ws://{url}:{repo_port}"
    future = asyncio.gather(
        repository(),
        cinterface.repository_context.connect(repository_uri),
    )
    asyncio.get_event_loop().run_until_complete(future)

    future = asyncio.gather(
        future, controller()
    )
    asyncio.get_event_loop().run_until_complete(future)

    print(f"Listening on ws://{url}:{controller_port}")

    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
