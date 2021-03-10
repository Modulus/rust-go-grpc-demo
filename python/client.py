import logging
import asyncio
import grpc
import say_pb2_grpc
import say_pb2

async def run() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = say_pb2_grpc.SayerStub(channel)
        response = await stub.Send(say_pb2.SayerRequest(name='Tonic', comment="I know nothing!"))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())