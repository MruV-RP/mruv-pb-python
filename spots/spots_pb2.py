# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spots/spots.proto

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
  name='spots/spots.proto',
  package='mruv.spots',
  syntax='proto3',
  serialized_options=_b('Z#github.com/MruV-RP/mruv-pb-go/spots'),
  serialized_pb=_b('\n\x11spots/spots.proto\x12\nmruv.spots\x1a\x1cgoogle/api/annotations.proto\"\x8a\x01\n\x11\x43reateSpotRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\x05\x12\x0e\n\x06marker\x18\x04 \x01(\x05\x12\t\n\x01x\x18\x05 \x01(\x02\x12\t\n\x01y\x18\x06 \x01(\x02\x12\t\n\x01z\x18\x07 \x01(\x02\x12\n\n\x02vw\x18\x08 \x01(\x05\x12\x0b\n\x03int\x18\t \x01(\x05\" \n\x12\x43reateSpotResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\x1c\n\x0eGetSpotRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x88\x01\n\x0fGetSpotResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\x05\x12\x0e\n\x06marker\x18\x04 \x01(\x05\x12\t\n\x01x\x18\x05 \x01(\x02\x12\t\n\x01y\x18\x06 \x01(\x02\x12\t\n\x01z\x18\x07 \x01(\x02\x12\n\n\x02vw\x18\x08 \x01(\x05\x12\x0b\n\x03int\x18\t \x01(\x05\"\x96\x01\n\x11UpdateSpotRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\x05\x12\x0e\n\x06marker\x18\x05 \x01(\x05\x12\t\n\x01x\x18\x06 \x01(\x02\x12\t\n\x01y\x18\x07 \x01(\x02\x12\t\n\x01z\x18\x08 \x01(\x02\x12\n\n\x02vw\x18\t \x01(\x05\x12\x0b\n\x03int\x18\n \x01(\x05\"\x14\n\x12UpdateSpotResponse\"\x1f\n\x11\x44\x65leteSpotRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x14\n\x12\x44\x65leteSpotResponse2\x98\x03\n\x10MruVSpotsService\x12^\n\nCreateSpot\x12\x1d.mruv.spots.CreateSpotRequest\x1a\x1e.mruv.spots.CreateSpotResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\"\t/v1/spots\x12Z\n\x07GetSpot\x12\x1a.mruv.spots.GetSpotRequest\x1a\x1b.mruv.spots.GetSpotResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/spots/{id}\x12\x63\n\nUpdateSpot\x12\x1d.mruv.spots.UpdateSpotRequest\x1a\x1e.mruv.spots.UpdateSpotResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x32\x0e/v1/spots/{id}\x12\x63\n\nDeleteSpot\x12\x1d.mruv.spots.DeleteSpotRequest\x1a\x1e.mruv.spots.DeleteSpotResponse\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/v1/spots/{id}B%Z#github.com/MruV-RP/mruv-pb-go/spotsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CREATESPOTREQUEST = _descriptor.Descriptor(
  name='CreateSpotRequest',
  full_name='mruv.spots.CreateSpotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.spots.CreateSpotRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='mruv.spots.CreateSpotRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='mruv.spots.CreateSpotRequest.icon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marker', full_name='mruv.spots.CreateSpotRequest.marker', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='mruv.spots.CreateSpotRequest.x', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mruv.spots.CreateSpotRequest.y', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='mruv.spots.CreateSpotRequest.z', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vw', full_name='mruv.spots.CreateSpotRequest.vw', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int', full_name='mruv.spots.CreateSpotRequest.int', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=64,
  serialized_end=202,
)


_CREATESPOTRESPONSE = _descriptor.Descriptor(
  name='CreateSpotResponse',
  full_name='mruv.spots.CreateSpotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.spots.CreateSpotResponse.id', index=0,
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
  serialized_start=204,
  serialized_end=236,
)


_GETSPOTREQUEST = _descriptor.Descriptor(
  name='GetSpotRequest',
  full_name='mruv.spots.GetSpotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.spots.GetSpotRequest.id', index=0,
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
  serialized_start=238,
  serialized_end=266,
)


_GETSPOTRESPONSE = _descriptor.Descriptor(
  name='GetSpotResponse',
  full_name='mruv.spots.GetSpotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.spots.GetSpotResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='mruv.spots.GetSpotResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='mruv.spots.GetSpotResponse.icon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marker', full_name='mruv.spots.GetSpotResponse.marker', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='mruv.spots.GetSpotResponse.x', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mruv.spots.GetSpotResponse.y', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='mruv.spots.GetSpotResponse.z', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vw', full_name='mruv.spots.GetSpotResponse.vw', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int', full_name='mruv.spots.GetSpotResponse.int', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=269,
  serialized_end=405,
)


_UPDATESPOTREQUEST = _descriptor.Descriptor(
  name='UpdateSpotRequest',
  full_name='mruv.spots.UpdateSpotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.spots.UpdateSpotRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.spots.UpdateSpotRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='mruv.spots.UpdateSpotRequest.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='mruv.spots.UpdateSpotRequest.icon', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marker', full_name='mruv.spots.UpdateSpotRequest.marker', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='mruv.spots.UpdateSpotRequest.x', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mruv.spots.UpdateSpotRequest.y', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='mruv.spots.UpdateSpotRequest.z', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vw', full_name='mruv.spots.UpdateSpotRequest.vw', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int', full_name='mruv.spots.UpdateSpotRequest.int', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=408,
  serialized_end=558,
)


_UPDATESPOTRESPONSE = _descriptor.Descriptor(
  name='UpdateSpotResponse',
  full_name='mruv.spots.UpdateSpotResponse',
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
  serialized_start=560,
  serialized_end=580,
)


_DELETESPOTREQUEST = _descriptor.Descriptor(
  name='DeleteSpotRequest',
  full_name='mruv.spots.DeleteSpotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.spots.DeleteSpotRequest.id', index=0,
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
  serialized_start=582,
  serialized_end=613,
)


_DELETESPOTRESPONSE = _descriptor.Descriptor(
  name='DeleteSpotResponse',
  full_name='mruv.spots.DeleteSpotResponse',
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
  serialized_start=615,
  serialized_end=635,
)

DESCRIPTOR.message_types_by_name['CreateSpotRequest'] = _CREATESPOTREQUEST
DESCRIPTOR.message_types_by_name['CreateSpotResponse'] = _CREATESPOTRESPONSE
DESCRIPTOR.message_types_by_name['GetSpotRequest'] = _GETSPOTREQUEST
DESCRIPTOR.message_types_by_name['GetSpotResponse'] = _GETSPOTRESPONSE
DESCRIPTOR.message_types_by_name['UpdateSpotRequest'] = _UPDATESPOTREQUEST
DESCRIPTOR.message_types_by_name['UpdateSpotResponse'] = _UPDATESPOTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteSpotRequest'] = _DELETESPOTREQUEST
DESCRIPTOR.message_types_by_name['DeleteSpotResponse'] = _DELETESPOTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateSpotRequest = _reflection.GeneratedProtocolMessageType('CreateSpotRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESPOTREQUEST,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.CreateSpotRequest)
  })
_sym_db.RegisterMessage(CreateSpotRequest)

CreateSpotResponse = _reflection.GeneratedProtocolMessageType('CreateSpotResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESPOTRESPONSE,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.CreateSpotResponse)
  })
_sym_db.RegisterMessage(CreateSpotResponse)

GetSpotRequest = _reflection.GeneratedProtocolMessageType('GetSpotRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSPOTREQUEST,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.GetSpotRequest)
  })
_sym_db.RegisterMessage(GetSpotRequest)

GetSpotResponse = _reflection.GeneratedProtocolMessageType('GetSpotResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSPOTRESPONSE,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.GetSpotResponse)
  })
_sym_db.RegisterMessage(GetSpotResponse)

UpdateSpotRequest = _reflection.GeneratedProtocolMessageType('UpdateSpotRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESPOTREQUEST,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.UpdateSpotRequest)
  })
_sym_db.RegisterMessage(UpdateSpotRequest)

UpdateSpotResponse = _reflection.GeneratedProtocolMessageType('UpdateSpotResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESPOTRESPONSE,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.UpdateSpotResponse)
  })
_sym_db.RegisterMessage(UpdateSpotResponse)

DeleteSpotRequest = _reflection.GeneratedProtocolMessageType('DeleteSpotRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESPOTREQUEST,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.DeleteSpotRequest)
  })
_sym_db.RegisterMessage(DeleteSpotRequest)

DeleteSpotResponse = _reflection.GeneratedProtocolMessageType('DeleteSpotResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESPOTRESPONSE,
  '__module__' : 'spots.spots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.spots.DeleteSpotResponse)
  })
_sym_db.RegisterMessage(DeleteSpotResponse)


DESCRIPTOR._options = None

_MRUVSPOTSSERVICE = _descriptor.ServiceDescriptor(
  name='MruVSpotsService',
  full_name='mruv.spots.MruVSpotsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=638,
  serialized_end=1046,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateSpot',
    full_name='mruv.spots.MruVSpotsService.CreateSpot',
    index=0,
    containing_service=None,
    input_type=_CREATESPOTREQUEST,
    output_type=_CREATESPOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\013\"\t/v1/spots'),
  ),
  _descriptor.MethodDescriptor(
    name='GetSpot',
    full_name='mruv.spots.MruVSpotsService.GetSpot',
    index=1,
    containing_service=None,
    input_type=_GETSPOTREQUEST,
    output_type=_GETSPOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/spots/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateSpot',
    full_name='mruv.spots.MruVSpotsService.UpdateSpot',
    index=2,
    containing_service=None,
    input_type=_UPDATESPOTREQUEST,
    output_type=_UPDATESPOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\0202\016/v1/spots/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSpot',
    full_name='mruv.spots.MruVSpotsService.DeleteSpot',
    index=3,
    containing_service=None,
    input_type=_DELETESPOTREQUEST,
    output_type=_DELETESPOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020*\016/v1/spots/{id}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVSPOTSSERVICE)

DESCRIPTOR.services_by_name['MruVSpotsService'] = _MRUVSPOTSSERVICE

# @@protoc_insertion_point(module_scope)