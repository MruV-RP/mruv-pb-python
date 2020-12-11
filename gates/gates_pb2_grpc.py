# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gates import gates_pb2 as gates_dot_gates__pb2


class MruVGatesServiceStub(object):
    """The MruV gates service provides procedures for managing gates and moving objects groups.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateGate = channel.unary_unary(
                '/mruv.gates.MruVGatesService/CreateGate',
                request_serializer=gates_dot_gates__pb2.CreateGateRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.CreateGateResponse.FromString,
                )
        self.GetGate = channel.unary_unary(
                '/mruv.gates.MruVGatesService/GetGate',
                request_serializer=gates_dot_gates__pb2.GetGateRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.GetGateResponse.FromString,
                )
        self.UpdateGate = channel.unary_unary(
                '/mruv.gates.MruVGatesService/UpdateGate',
                request_serializer=gates_dot_gates__pb2.UpdateGateRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.UpdateGateResponse.FromString,
                )
        self.DeleteGate = channel.unary_unary(
                '/mruv.gates.MruVGatesService/DeleteGate',
                request_serializer=gates_dot_gates__pb2.DeleteGateRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.DeleteGateResponse.FromString,
                )
        self.Lock = channel.unary_unary(
                '/mruv.gates.MruVGatesService/Lock',
                request_serializer=gates_dot_gates__pb2.LockRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.LockResponse.FromString,
                )
        self.Unlock = channel.unary_unary(
                '/mruv.gates.MruVGatesService/Unlock',
                request_serializer=gates_dot_gates__pb2.UnlockRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.UnlockResponse.FromString,
                )
        self.Open = channel.unary_unary(
                '/mruv.gates.MruVGatesService/Open',
                request_serializer=gates_dot_gates__pb2.OpenRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.OpenResponse.FromString,
                )
        self.Close = channel.unary_unary(
                '/mruv.gates.MruVGatesService/Close',
                request_serializer=gates_dot_gates__pb2.CloseRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.CloseResponse.FromString,
                )
        self.FindNearestGate = channel.unary_unary(
                '/mruv.gates.MruVGatesService/FindNearestGate',
                request_serializer=gates_dot_gates__pb2.FindNearestGateRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.FindNearestGateResponse.FromString,
                )
        self.FetchAll = channel.unary_stream(
                '/mruv.gates.MruVGatesService/FetchAll',
                request_serializer=gates_dot_gates__pb2.FetchAllGatesRequest.SerializeToString,
                response_deserializer=gates_dot_gates__pb2.FetchAllGatesResponse.FromString,
                )


class MruVGatesServiceServicer(object):
    """The MruV gates service provides procedures for managing gates and moving objects groups.
    """

    def CreateGate(self, request, context):
        """Create a gate or a moving objects objects group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGate(self, request, context):
        """Get a gate or a moving objects objects group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateGate(self, request, context):
        """Update a gate or a moving objects objects group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGate(self, request, context):
        """Delete a gate or a moving objects objects group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Lock(self, request, context):
        """Lock a gate. Locked gate cannot be opened.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unlock(self, request, context):
        """Unload a gate, so it can be open.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Open(self, request, context):
        """Opens a gate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Close a gate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindNearestGate(self, request, context):
        """Find gate that is closest to a specific position.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchAll(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MruVGatesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateGate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGate,
                    request_deserializer=gates_dot_gates__pb2.CreateGateRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.CreateGateResponse.SerializeToString,
            ),
            'GetGate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGate,
                    request_deserializer=gates_dot_gates__pb2.GetGateRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.GetGateResponse.SerializeToString,
            ),
            'UpdateGate': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateGate,
                    request_deserializer=gates_dot_gates__pb2.UpdateGateRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.UpdateGateResponse.SerializeToString,
            ),
            'DeleteGate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGate,
                    request_deserializer=gates_dot_gates__pb2.DeleteGateRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.DeleteGateResponse.SerializeToString,
            ),
            'Lock': grpc.unary_unary_rpc_method_handler(
                    servicer.Lock,
                    request_deserializer=gates_dot_gates__pb2.LockRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.LockResponse.SerializeToString,
            ),
            'Unlock': grpc.unary_unary_rpc_method_handler(
                    servicer.Unlock,
                    request_deserializer=gates_dot_gates__pb2.UnlockRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.UnlockResponse.SerializeToString,
            ),
            'Open': grpc.unary_unary_rpc_method_handler(
                    servicer.Open,
                    request_deserializer=gates_dot_gates__pb2.OpenRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.OpenResponse.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=gates_dot_gates__pb2.CloseRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.CloseResponse.SerializeToString,
            ),
            'FindNearestGate': grpc.unary_unary_rpc_method_handler(
                    servicer.FindNearestGate,
                    request_deserializer=gates_dot_gates__pb2.FindNearestGateRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.FindNearestGateResponse.SerializeToString,
            ),
            'FetchAll': grpc.unary_stream_rpc_method_handler(
                    servicer.FetchAll,
                    request_deserializer=gates_dot_gates__pb2.FetchAllGatesRequest.FromString,
                    response_serializer=gates_dot_gates__pb2.FetchAllGatesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mruv.gates.MruVGatesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MruVGatesService(object):
    """The MruV gates service provides procedures for managing gates and moving objects groups.
    """

    @staticmethod
    def CreateGate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/CreateGate',
            gates_dot_gates__pb2.CreateGateRequest.SerializeToString,
            gates_dot_gates__pb2.CreateGateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/GetGate',
            gates_dot_gates__pb2.GetGateRequest.SerializeToString,
            gates_dot_gates__pb2.GetGateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateGate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/UpdateGate',
            gates_dot_gates__pb2.UpdateGateRequest.SerializeToString,
            gates_dot_gates__pb2.UpdateGateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteGate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/DeleteGate',
            gates_dot_gates__pb2.DeleteGateRequest.SerializeToString,
            gates_dot_gates__pb2.DeleteGateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Lock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/Lock',
            gates_dot_gates__pb2.LockRequest.SerializeToString,
            gates_dot_gates__pb2.LockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/Unlock',
            gates_dot_gates__pb2.UnlockRequest.SerializeToString,
            gates_dot_gates__pb2.UnlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Open(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/Open',
            gates_dot_gates__pb2.OpenRequest.SerializeToString,
            gates_dot_gates__pb2.OpenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/Close',
            gates_dot_gates__pb2.CloseRequest.SerializeToString,
            gates_dot_gates__pb2.CloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindNearestGate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.gates.MruVGatesService/FindNearestGate',
            gates_dot_gates__pb2.FindNearestGateRequest.SerializeToString,
            gates_dot_gates__pb2.FindNearestGateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mruv.gates.MruVGatesService/FetchAll',
            gates_dot_gates__pb2.FetchAllGatesRequest.SerializeToString,
            gates_dot_gates__pb2.FetchAllGatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
