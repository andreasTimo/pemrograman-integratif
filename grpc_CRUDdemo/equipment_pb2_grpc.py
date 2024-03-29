# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import equipment_pb2 as equipment__pb2


class EquipmentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEquipment = channel.unary_unary(
                '/equipment.EquipmentService/CreateEquipment',
                request_serializer=equipment__pb2.Equipment.SerializeToString,
                response_deserializer=equipment__pb2.Equipment.FromString,
                )
        self.ReadEquipment = channel.unary_unary(
                '/equipment.EquipmentService/ReadEquipment',
                request_serializer=equipment__pb2.Equipment.SerializeToString,
                response_deserializer=equipment__pb2.Equipment.FromString,
                )
        self.UpdateEquipment = channel.unary_unary(
                '/equipment.EquipmentService/UpdateEquipment',
                request_serializer=equipment__pb2.Equipment.SerializeToString,
                response_deserializer=equipment__pb2.Equipment.FromString,
                )
        self.DeleteEquipment = channel.unary_unary(
                '/equipment.EquipmentService/DeleteEquipment',
                request_serializer=equipment__pb2.Equipment.SerializeToString,
                response_deserializer=equipment__pb2.Equipment.FromString,
                )


class EquipmentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateEquipment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadEquipment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEquipment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEquipment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EquipmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateEquipment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEquipment,
                    request_deserializer=equipment__pb2.Equipment.FromString,
                    response_serializer=equipment__pb2.Equipment.SerializeToString,
            ),
            'ReadEquipment': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadEquipment,
                    request_deserializer=equipment__pb2.Equipment.FromString,
                    response_serializer=equipment__pb2.Equipment.SerializeToString,
            ),
            'UpdateEquipment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEquipment,
                    request_deserializer=equipment__pb2.Equipment.FromString,
                    response_serializer=equipment__pb2.Equipment.SerializeToString,
            ),
            'DeleteEquipment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEquipment,
                    request_deserializer=equipment__pb2.Equipment.FromString,
                    response_serializer=equipment__pb2.Equipment.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'equipment.EquipmentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EquipmentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateEquipment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/equipment.EquipmentService/CreateEquipment',
            equipment__pb2.Equipment.SerializeToString,
            equipment__pb2.Equipment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadEquipment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/equipment.EquipmentService/ReadEquipment',
            equipment__pb2.Equipment.SerializeToString,
            equipment__pb2.Equipment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEquipment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/equipment.EquipmentService/UpdateEquipment',
            equipment__pb2.Equipment.SerializeToString,
            equipment__pb2.Equipment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEquipment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/equipment.EquipmentService/DeleteEquipment',
            equipment__pb2.Equipment.SerializeToString,
            equipment__pb2.Equipment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
