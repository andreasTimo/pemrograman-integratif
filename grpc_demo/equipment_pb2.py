# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: equipment.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x65quipment.proto\x12\tequipment\"9\n\tEquipment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x32\x94\x02\n\x10\x45quipmentService\x12?\n\x0f\x43reateEquipment\x12\x14.equipment.Equipment\x1a\x14.equipment.Equipment\"\x00\x12=\n\rReadEquipment\x12\x14.equipment.Equipment\x1a\x14.equipment.Equipment\"\x00\x12?\n\x0fUpdateEquipment\x12\x14.equipment.Equipment\x1a\x14.equipment.Equipment\"\x00\x12?\n\x0f\x44\x65leteEquipment\x12\x14.equipment.Equipment\x1a\x14.equipment.Equipment\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'equipment_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EQUIPMENT._serialized_start=30
  _EQUIPMENT._serialized_end=87
  _EQUIPMENTSERVICE._serialized_start=90
  _EQUIPMENTSERVICE._serialized_end=366
# @@protoc_insertion_point(module_scope)