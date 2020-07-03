# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehicles/vehicles.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vehicles/vehicles.proto',
  package='mruv.vehicles',
  syntax='proto3',
  serialized_options=_b('Z&github.com/MruV-RP/mruv-pb-go/vehicles'),
  serialized_pb=_b('\n\x17vehicles/vehicles.proto\x12\rmruv.vehicles\x1a\x1cgoogle/api/annotations.proto\"\x16\n\x14\x43reateVehicleRequest\"\x17\n\x15\x43reateVehicleResponse\"\x1f\n\x11GetVehicleRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x14\n\x12GetVehicleResponse\"\"\n\x14UpdateVehicleRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x17\n\x15UpdateVehicleResponse\"\"\n\x14\x44\x65leteVehicleRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x17\n\x15\x44\x65leteVehicleResponse2\xe3\x03\n\x13MruVVehiclesService\x12p\n\rCreateVehicle\x12#.mruv.vehicles.CreateVehicleRequest\x1a$.mruv.vehicles.CreateVehicleResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\"\x0c/v1/vehicles\x12l\n\nGetVehicle\x12 .mruv.vehicles.GetVehicleRequest\x1a!.mruv.vehicles.GetVehicleResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/vehicles/{id}\x12u\n\rUpdateVehicle\x12#.mruv.vehicles.UpdateVehicleRequest\x1a$.mruv.vehicles.UpdateVehicleResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x32\x11/v1/vehicles/{id}\x12u\n\rDeleteVehicle\x12#.mruv.vehicles.DeleteVehicleRequest\x1a$.mruv.vehicles.DeleteVehicleResponse\"\x19\x82\xd3\xe4\x93\x02\x13*\x11/v1/vehicles/{id}B(Z&github.com/MruV-RP/mruv-pb-go/vehiclesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CREATEVEHICLEREQUEST = _descriptor.Descriptor(
  name='CreateVehicleRequest',
  full_name='mruv.vehicles.CreateVehicleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=94,
)


_CREATEVEHICLERESPONSE = _descriptor.Descriptor(
  name='CreateVehicleResponse',
  full_name='mruv.vehicles.CreateVehicleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=119,
)


_GETVEHICLEREQUEST = _descriptor.Descriptor(
  name='GetVehicleRequest',
  full_name='mruv.vehicles.GetVehicleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.vehicles.GetVehicleRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=152,
)


_GETVEHICLERESPONSE = _descriptor.Descriptor(
  name='GetVehicleResponse',
  full_name='mruv.vehicles.GetVehicleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=174,
)


_UPDATEVEHICLEREQUEST = _descriptor.Descriptor(
  name='UpdateVehicleRequest',
  full_name='mruv.vehicles.UpdateVehicleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.vehicles.UpdateVehicleRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=210,
)


_UPDATEVEHICLERESPONSE = _descriptor.Descriptor(
  name='UpdateVehicleResponse',
  full_name='mruv.vehicles.UpdateVehicleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=235,
)


_DELETEVEHICLEREQUEST = _descriptor.Descriptor(
  name='DeleteVehicleRequest',
  full_name='mruv.vehicles.DeleteVehicleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.vehicles.DeleteVehicleRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=271,
)


_DELETEVEHICLERESPONSE = _descriptor.Descriptor(
  name='DeleteVehicleResponse',
  full_name='mruv.vehicles.DeleteVehicleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=296,
)

DESCRIPTOR.message_types_by_name['CreateVehicleRequest'] = _CREATEVEHICLEREQUEST
DESCRIPTOR.message_types_by_name['CreateVehicleResponse'] = _CREATEVEHICLERESPONSE
DESCRIPTOR.message_types_by_name['GetVehicleRequest'] = _GETVEHICLEREQUEST
DESCRIPTOR.message_types_by_name['GetVehicleResponse'] = _GETVEHICLERESPONSE
DESCRIPTOR.message_types_by_name['UpdateVehicleRequest'] = _UPDATEVEHICLEREQUEST
DESCRIPTOR.message_types_by_name['UpdateVehicleResponse'] = _UPDATEVEHICLERESPONSE
DESCRIPTOR.message_types_by_name['DeleteVehicleRequest'] = _DELETEVEHICLEREQUEST
DESCRIPTOR.message_types_by_name['DeleteVehicleResponse'] = _DELETEVEHICLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateVehicleRequest = _reflection.GeneratedProtocolMessageType('CreateVehicleRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVEHICLEREQUEST,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.CreateVehicleRequest)
  })
_sym_db.RegisterMessage(CreateVehicleRequest)

CreateVehicleResponse = _reflection.GeneratedProtocolMessageType('CreateVehicleResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVEHICLERESPONSE,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.CreateVehicleResponse)
  })
_sym_db.RegisterMessage(CreateVehicleResponse)

GetVehicleRequest = _reflection.GeneratedProtocolMessageType('GetVehicleRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVEHICLEREQUEST,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.GetVehicleRequest)
  })
_sym_db.RegisterMessage(GetVehicleRequest)

GetVehicleResponse = _reflection.GeneratedProtocolMessageType('GetVehicleResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVEHICLERESPONSE,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.GetVehicleResponse)
  })
_sym_db.RegisterMessage(GetVehicleResponse)

UpdateVehicleRequest = _reflection.GeneratedProtocolMessageType('UpdateVehicleRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVEHICLEREQUEST,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.UpdateVehicleRequest)
  })
_sym_db.RegisterMessage(UpdateVehicleRequest)

UpdateVehicleResponse = _reflection.GeneratedProtocolMessageType('UpdateVehicleResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVEHICLERESPONSE,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.UpdateVehicleResponse)
  })
_sym_db.RegisterMessage(UpdateVehicleResponse)

DeleteVehicleRequest = _reflection.GeneratedProtocolMessageType('DeleteVehicleRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVEHICLEREQUEST,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.DeleteVehicleRequest)
  })
_sym_db.RegisterMessage(DeleteVehicleRequest)

DeleteVehicleResponse = _reflection.GeneratedProtocolMessageType('DeleteVehicleResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVEHICLERESPONSE,
  '__module__' : 'vehicles.vehicles_pb2'
  # @@protoc_insertion_point(class_scope:mruv.vehicles.DeleteVehicleResponse)
  })
_sym_db.RegisterMessage(DeleteVehicleResponse)


DESCRIPTOR._options = None

_MRUVVEHICLESSERVICE = _descriptor.ServiceDescriptor(
  name='MruVVehiclesService',
  full_name='mruv.vehicles.MruVVehiclesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=299,
  serialized_end=782,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateVehicle',
    full_name='mruv.vehicles.MruVVehiclesService.CreateVehicle',
    index=0,
    containing_service=None,
    input_type=_CREATEVEHICLEREQUEST,
    output_type=_CREATEVEHICLERESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\"\014/v1/vehicles'),
  ),
  _descriptor.MethodDescriptor(
    name='GetVehicle',
    full_name='mruv.vehicles.MruVVehiclesService.GetVehicle',
    index=1,
    containing_service=None,
    input_type=_GETVEHICLEREQUEST,
    output_type=_GETVEHICLERESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\022\021/v1/vehicles/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateVehicle',
    full_name='mruv.vehicles.MruVVehiclesService.UpdateVehicle',
    index=2,
    containing_service=None,
    input_type=_UPDATEVEHICLEREQUEST,
    output_type=_UPDATEVEHICLERESPONSE,
    serialized_options=_b('\202\323\344\223\002\0232\021/v1/vehicles/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteVehicle',
    full_name='mruv.vehicles.MruVVehiclesService.DeleteVehicle',
    index=3,
    containing_service=None,
    input_type=_DELETEVEHICLEREQUEST,
    output_type=_DELETEVEHICLERESPONSE,
    serialized_options=_b('\202\323\344\223\002\023*\021/v1/vehicles/{id}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVVEHICLESSERVICE)

DESCRIPTOR.services_by_name['MruVVehiclesService'] = _MRUVVEHICLESSERVICE

# @@protoc_insertion_point(module_scope)
