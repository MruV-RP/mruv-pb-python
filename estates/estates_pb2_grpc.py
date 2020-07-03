# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from estates import estates_pb2 as estates_dot_estates__pb2


class MruVEstateServiceStub(object):
  """The MruV estate service provides procedures for managing buildings and other estates.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateEstate = channel.unary_unary(
        '/mruv.estates.MruVEstateService/CreateEstate',
        request_serializer=estates_dot_estates__pb2.CreateEstateRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.CreateEstateResponse.FromString,
        )
    self.GetEstate = channel.unary_unary(
        '/mruv.estates.MruVEstateService/GetEstate',
        request_serializer=estates_dot_estates__pb2.GetEstateRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.Estate.FromString,
        )
    self.UpdateEstate = channel.unary_unary(
        '/mruv.estates.MruVEstateService/UpdateEstate',
        request_serializer=estates_dot_estates__pb2.UpdateEstateRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.UpdateEstateResponse.FromString,
        )
    self.DeleteEstate = channel.unary_unary(
        '/mruv.estates.MruVEstateService/DeleteEstate',
        request_serializer=estates_dot_estates__pb2.DeleteEstateRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.DeleteEstateResponse.FromString,
        )
    self.GetEstates = channel.unary_unary(
        '/mruv.estates.MruVEstateService/GetEstates',
        request_serializer=estates_dot_estates__pb2.GetEstatesRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.GetEstatesResponse.FromString,
        )
    self.AddGate = channel.unary_unary(
        '/mruv.estates.MruVEstateService/AddGate',
        request_serializer=estates_dot_estates__pb2.AddGateRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.AddGateResponse.FromString,
        )
    self.DeleteGate = channel.unary_unary(
        '/mruv.estates.MruVEstateService/DeleteGate',
        request_serializer=estates_dot_estates__pb2.DeleteGateRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.DeleteGateResponse.FromString,
        )
    self.GetEstateGates = channel.unary_unary(
        '/mruv.estates.MruVEstateService/GetEstateGates',
        request_serializer=estates_dot_estates__pb2.GetEstateGatesRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.GetEstateGatesResponse.FromString,
        )
    self.AddEntrance = channel.unary_unary(
        '/mruv.estates.MruVEstateService/AddEntrance',
        request_serializer=estates_dot_estates__pb2.AddEntranceRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.AddEntranceResponse.FromString,
        )
    self.RemoveEntrance = channel.unary_unary(
        '/mruv.estates.MruVEstateService/RemoveEntrance',
        request_serializer=estates_dot_estates__pb2.RemoveEntranceRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.RemoveEntranceResponse.FromString,
        )
    self.GetEstateEntrances = channel.unary_unary(
        '/mruv.estates.MruVEstateService/GetEstateEntrances',
        request_serializer=estates_dot_estates__pb2.GetEstateEntrancesRequest.SerializeToString,
        response_deserializer=estates_dot_estates__pb2.GetEstateEntrancesResponse.FromString,
        )


class MruVEstateServiceServicer(object):
  """The MruV estate service provides procedures for managing buildings and other estates.
  """

  def CreateEstate(self, request, context):
    """Create real estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEstate(self, request, context):
    """Get real estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateEstate(self, request, context):
    """Update real estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteEstate(self, request, context):
    """Delete real estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEstates(self, request, context):
    """Get all created real estates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddGate(self, request, context):
    """Add a gate to an estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteGate(self, request, context):
    """Delete a gate from estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEstateGates(self, request, context):
    """Get all estate gates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddEntrance(self, request, context):
    """Add an entrance to estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveEntrance(self, request, context):
    """Remove an entrance from estate.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEstateEntrances(self, request, context):
    """Get all estate entrances.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MruVEstateServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateEstate': grpc.unary_unary_rpc_method_handler(
          servicer.CreateEstate,
          request_deserializer=estates_dot_estates__pb2.CreateEstateRequest.FromString,
          response_serializer=estates_dot_estates__pb2.CreateEstateResponse.SerializeToString,
      ),
      'GetEstate': grpc.unary_unary_rpc_method_handler(
          servicer.GetEstate,
          request_deserializer=estates_dot_estates__pb2.GetEstateRequest.FromString,
          response_serializer=estates_dot_estates__pb2.Estate.SerializeToString,
      ),
      'UpdateEstate': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateEstate,
          request_deserializer=estates_dot_estates__pb2.UpdateEstateRequest.FromString,
          response_serializer=estates_dot_estates__pb2.UpdateEstateResponse.SerializeToString,
      ),
      'DeleteEstate': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteEstate,
          request_deserializer=estates_dot_estates__pb2.DeleteEstateRequest.FromString,
          response_serializer=estates_dot_estates__pb2.DeleteEstateResponse.SerializeToString,
      ),
      'GetEstates': grpc.unary_unary_rpc_method_handler(
          servicer.GetEstates,
          request_deserializer=estates_dot_estates__pb2.GetEstatesRequest.FromString,
          response_serializer=estates_dot_estates__pb2.GetEstatesResponse.SerializeToString,
      ),
      'AddGate': grpc.unary_unary_rpc_method_handler(
          servicer.AddGate,
          request_deserializer=estates_dot_estates__pb2.AddGateRequest.FromString,
          response_serializer=estates_dot_estates__pb2.AddGateResponse.SerializeToString,
      ),
      'DeleteGate': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteGate,
          request_deserializer=estates_dot_estates__pb2.DeleteGateRequest.FromString,
          response_serializer=estates_dot_estates__pb2.DeleteGateResponse.SerializeToString,
      ),
      'GetEstateGates': grpc.unary_unary_rpc_method_handler(
          servicer.GetEstateGates,
          request_deserializer=estates_dot_estates__pb2.GetEstateGatesRequest.FromString,
          response_serializer=estates_dot_estates__pb2.GetEstateGatesResponse.SerializeToString,
      ),
      'AddEntrance': grpc.unary_unary_rpc_method_handler(
          servicer.AddEntrance,
          request_deserializer=estates_dot_estates__pb2.AddEntranceRequest.FromString,
          response_serializer=estates_dot_estates__pb2.AddEntranceResponse.SerializeToString,
      ),
      'RemoveEntrance': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveEntrance,
          request_deserializer=estates_dot_estates__pb2.RemoveEntranceRequest.FromString,
          response_serializer=estates_dot_estates__pb2.RemoveEntranceResponse.SerializeToString,
      ),
      'GetEstateEntrances': grpc.unary_unary_rpc_method_handler(
          servicer.GetEstateEntrances,
          request_deserializer=estates_dot_estates__pb2.GetEstateEntrancesRequest.FromString,
          response_serializer=estates_dot_estates__pb2.GetEstateEntrancesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mruv.estates.MruVEstateService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
