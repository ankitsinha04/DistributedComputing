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


def add_CloudAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterFogNode': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterFogNode,
          request_deserializer=cloud__pb2.RequestRegisterFog.FromString,
          response_serializer=cloud__pb2.ResponseRegisterFog.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cloudapi.CloudAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))