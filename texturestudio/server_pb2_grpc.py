# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from texturestudio import server_pb2 as texturestudio_dot_server__pb2


class TextureStudioServerServiceStub(object):
  """Service to manage texture studio server.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StartServer = channel.unary_unary(
        '/texture_studio.TextureStudioServerService/StartServer',
        request_serializer=texturestudio_dot_server__pb2.StartServerRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.StartServerResponse.FromString,
        )
    self.StopServer = channel.unary_unary(
        '/texture_studio.TextureStudioServerService/StopServer',
        request_serializer=texturestudio_dot_server__pb2.StopServerRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.StopServerResponse.FromString,
        )
    self.RestartServer = channel.unary_unary(
        '/texture_studio.TextureStudioServerService/RestartServer',
        request_serializer=texturestudio_dot_server__pb2.RestartServerRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.RestartServerResponse.FromString,
        )
    self.ServerStatus = channel.unary_unary(
        '/texture_studio.TextureStudioServerService/ServerStatus',
        request_serializer=texturestudio_dot_server__pb2.ServerStatusRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.ServerStatusResponse.FromString,
        )
    self.UploadProject = channel.unary_unary(
        '/texture_studio.TextureStudioServerService/UploadProject',
        request_serializer=texturestudio_dot_server__pb2.UploadProjectRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.UploadProjectResponse.FromString,
        )
    self.GetProject = channel.unary_unary(
        '/texture_studio.TextureStudioServerService/GetProject',
        request_serializer=texturestudio_dot_server__pb2.GetProjectRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.GetProjectResponse.FromString,
        )
    self.GetProjects = channel.unary_unary(
        '/texture_studio.TextureStudioServerService/GetProjects',
        request_serializer=texturestudio_dot_server__pb2.GetProjectsRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.GetProjectsResponse.FromString,
        )
    self.SubscribeToProjectsChanges = channel.unary_stream(
        '/texture_studio.TextureStudioServerService/SubscribeToProjectsChanges',
        request_serializer=texturestudio_dot_server__pb2.SubscribeToProjectsChangesRequest.SerializeToString,
        response_deserializer=texturestudio_dot_server__pb2.SubscribeToProjectsChangesResponse.FromString,
        )


class TextureStudioServerServiceServicer(object):
  """Service to manage texture studio server.
  """

  def StartServer(self, request, context):
    """Start a texture studio server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopServer(self, request, context):
    """Stop a texture studio server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RestartServer(self, request, context):
    """Restart a texture studio server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServerStatus(self, request, context):
    """Get texture studio server status.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadProject(self, request, context):
    """Upload project to texture studio.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProject(self, request, context):
    """Get texture-studio objects project.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProjects(self, request, context):
    """Get all projects.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeToProjectsChanges(self, request, context):
    """Listen for project changes - if texture studio project has been created or modified, this will trigger an event.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TextureStudioServerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StartServer': grpc.unary_unary_rpc_method_handler(
          servicer.StartServer,
          request_deserializer=texturestudio_dot_server__pb2.StartServerRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.StartServerResponse.SerializeToString,
      ),
      'StopServer': grpc.unary_unary_rpc_method_handler(
          servicer.StopServer,
          request_deserializer=texturestudio_dot_server__pb2.StopServerRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.StopServerResponse.SerializeToString,
      ),
      'RestartServer': grpc.unary_unary_rpc_method_handler(
          servicer.RestartServer,
          request_deserializer=texturestudio_dot_server__pb2.RestartServerRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.RestartServerResponse.SerializeToString,
      ),
      'ServerStatus': grpc.unary_unary_rpc_method_handler(
          servicer.ServerStatus,
          request_deserializer=texturestudio_dot_server__pb2.ServerStatusRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.ServerStatusResponse.SerializeToString,
      ),
      'UploadProject': grpc.unary_unary_rpc_method_handler(
          servicer.UploadProject,
          request_deserializer=texturestudio_dot_server__pb2.UploadProjectRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.UploadProjectResponse.SerializeToString,
      ),
      'GetProject': grpc.unary_unary_rpc_method_handler(
          servicer.GetProject,
          request_deserializer=texturestudio_dot_server__pb2.GetProjectRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.GetProjectResponse.SerializeToString,
      ),
      'GetProjects': grpc.unary_unary_rpc_method_handler(
          servicer.GetProjects,
          request_deserializer=texturestudio_dot_server__pb2.GetProjectsRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.GetProjectsResponse.SerializeToString,
      ),
      'SubscribeToProjectsChanges': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeToProjectsChanges,
          request_deserializer=texturestudio_dot_server__pb2.SubscribeToProjectsChangesRequest.FromString,
          response_serializer=texturestudio_dot_server__pb2.SubscribeToProjectsChangesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'texture_studio.TextureStudioServerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
