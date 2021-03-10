from concurrent import futures
import logging

import grpc

import say_pb2
import say_pb2_grpc


class Sayer(say_pb2_grpc.SayerServicer):

    def Send(self, request, context):
        logger = logging.getLogger("Sayer")
        logger.setLevel(logging.INFO)
        logger.info(f"Got name {request.name} and comment: {request.comment}")
        logger.info("Sending response")
        return say_pb2.SayerResponse(message='Hello, %s!' % request.name, comment=request.comment, id=123)


def serve():
    logger = logging.getLogger("Server")
    logger.setLevel(logging.INFO)
    logger.info("Server running on port :50051")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    say_pb2_grpc.add_SayerServicer_to_server(Sayer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()