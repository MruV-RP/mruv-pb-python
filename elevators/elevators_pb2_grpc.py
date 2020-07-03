# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from elevators import elevators_pb2 as elevators_dot_elevators__pb2


class MruVElevatorsServiceStub(object):
  """The MruV entrances service provides procedures for managing an elevators.
  Elevators allow all players in the elevator area to move between building floors.
  Floor change is processed in following steps:
  1. Someone chooses a floor
  1. Doors closing event is fired
  2. Doors closed event is fired.
  3. Everyone in a elevator are registered as players, that will be teleported to chosen floor.
  4. X seconds delay (elevator is moving)
  5. Teleport players to other floor elevator
  6. Doors opening
  7. Doors opened - end
  You can define a one-man pseudo-elevator where only point 5 is executed.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateElevator = channel.unary_unary(
        '/mruv.elevators.MruVElevatorsService/CreateElevator',
        request_serializer=elevators_dot_elevators__pb2.CreateElevatorRequest.SerializeToString,
        response_deserializer=elevators_dot_elevators__pb2.CreateElevatorResponse.FromString,
        )
    self.GetElevator = channel.unary_unary(
        '/mruv.elevators.MruVElevatorsService/GetElevator',
        request_serializer=elevators_dot_elevators__pb2.GetElevatorRequest.SerializeToString,
        response_deserializer=elevators_dot_elevators__pb2.GetElevatorResponse.FromString,
        )
    self.UpdateElevator = channel.unary_unary(
        '/mruv.elevators.MruVElevatorsService/UpdateElevator',
        request_serializer=elevators_dot_elevators__pb2.UpdateElevatorRequest.SerializeToString,
        response_deserializer=elevators_dot_elevators__pb2.UpdateElevatorResponse.FromString,
        )
    self.DeleteElevator = channel.unary_unary(
        '/mruv.elevators.MruVElevatorsService/DeleteElevator',
        request_serializer=elevators_dot_elevators__pb2.DeleteElevatorRequest.SerializeToString,
        response_deserializer=elevators_dot_elevators__pb2.DeleteElevatorResponse.FromString,
        )
    self.GetElevatorFloors = channel.unary_unary(
        '/mruv.elevators.MruVElevatorsService/GetElevatorFloors',
        request_serializer=elevators_dot_elevators__pb2.GetElevatorFloorsRequest.SerializeToString,
        response_deserializer=elevators_dot_elevators__pb2.GetElevatorFloorsResponse.FromString,
        )


class MruVElevatorsServiceServicer(object):
  """The MruV entrances service provides procedures for managing an elevators.
  Elevators allow all players in the elevator area to move between building floors.
  Floor change is processed in following steps:
  1. Someone chooses a floor
  1. Doors closing event is fired
  2. Doors closed event is fired.
  3. Everyone in a elevator are registered as players, that will be teleported to chosen floor.
  4. X seconds delay (elevator is moving)
  5. Teleport players to other floor elevator
  6. Doors opening
  7. Doors opened - end
  You can define a one-man pseudo-elevator where only point 5 is executed.
  """

  def CreateElevator(self, request, context):
    """Create an elevator.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetElevator(self, request, context):
    """Get an elevator.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateElevator(self, request, context):
    """Update an elevator.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteElevator(self, request, context):
    """Delete an elevator.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetElevatorFloors(self, request, context):
    """Get available elevator floors.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MruVElevatorsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateElevator': grpc.unary_unary_rpc_method_handler(
          servicer.CreateElevator,
          request_deserializer=elevators_dot_elevators__pb2.CreateElevatorRequest.FromString,
          response_serializer=elevators_dot_elevators__pb2.CreateElevatorResponse.SerializeToString,
      ),
      'GetElevator': grpc.unary_unary_rpc_method_handler(
          servicer.GetElevator,
          request_deserializer=elevators_dot_elevators__pb2.GetElevatorRequest.FromString,
          response_serializer=elevators_dot_elevators__pb2.GetElevatorResponse.SerializeToString,
      ),
      'UpdateElevator': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateElevator,
          request_deserializer=elevators_dot_elevators__pb2.UpdateElevatorRequest.FromString,
          response_serializer=elevators_dot_elevators__pb2.UpdateElevatorResponse.SerializeToString,
      ),
      'DeleteElevator': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteElevator,
          request_deserializer=elevators_dot_elevators__pb2.DeleteElevatorRequest.FromString,
          response_serializer=elevators_dot_elevators__pb2.DeleteElevatorResponse.SerializeToString,
      ),
      'GetElevatorFloors': grpc.unary_unary_rpc_method_handler(
          servicer.GetElevatorFloors,
          request_deserializer=elevators_dot_elevators__pb2.GetElevatorFloorsRequest.FromString,
          response_serializer=elevators_dot_elevators__pb2.GetElevatorFloorsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mruv.elevators.MruVElevatorsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
