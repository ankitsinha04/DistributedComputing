# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cloud_pb2 as cloud__pb2


class CloudAPIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterFogNode = channel.unary_unary(
        '/cloudapi.CloudAPI/RegisterFogNode',
        request_serializer=cloud__pb2.RequestRegisterFog.SerializeToString,
        response_deserializer=cloud__pb2.ResponseRegisterFog.FromString,
        )
    self.Tag = channel.unary_unary(
        '/cloudapi.CloudAPI/Tag',
        request_serializer=cloud__pb2.RequestTag.SerializeToString,
        response_deserializer=cloud__pb2.Error.FromString,
        )
    self.Fetch = channel.unary_unary(
        '/cloudapi.CloudAPI/Fetch',
        request_serializer=cloud__pb2.RequestFetch.SerializeToString,
        response_deserializer=cloud__pb2.ResponseFetch.FromString,
        )


class CloudAPIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RegisterFogNode(self, request, context):
    """For fog nodes to register themselves with cloud
    params :: ip: string, coordinates: pair(lat, long)
    return :: stream regionalFogs: list(ip)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Tag(self, request, context):
    """// For fog nodes to leave
    // params :: ip: string
    // return :: None
    rpc RemoveFogNode;

    // For users to register
    // params :: ip: string, coordinates: pair(lat, long)
    // return :: stream localFogs: list(list(ip))
    rpc RegisterUser;

    For fog to tag images with their locations
    params :: imageId: int32, address: string
    return :: None
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Fetch(self, request, context):
    """// For fog to lookup a location for images
    // params :: isUserFog: bool, coordinates: pair(l,l), (optional) image
    // return :: images: list(image)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CloudAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterFogNode': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterFogNode,
          request_deserializer=cloud__pb2.RequestRegisterFog.FromString,
          response_serializer=cloud__pb2.ResponseRegisterFog.SerializeToString,
      ),
      'Tag': grpc.unary_unary_rpc_method_handler(
          servicer.Tag,
          request_deserializer=cloud__pb2.RequestTag.FromString,
          response_serializer=cloud__pb2.Error.SerializeToString,
      ),
      'Fetch': grpc.unary_unary_rpc_method_handler(
          servicer.Fetch,
          request_deserializer=cloud__pb2.RequestFetch.FromString,
          response_serializer=cloud__pb2.ResponseFetch.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cloudapi.CloudAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
