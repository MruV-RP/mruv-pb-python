# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estates/estates.proto

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
  name='estates/estates.proto',
  package='mruv.estates',
  syntax='proto3',
  serialized_options=_b('Z%github.com/MruV-RP/mruv-pb-go/estates'),
  serialized_pb=_b('\n\x15\x65states/estates.proto\x12\x0cmruv.estates\x1a\x1cgoogle/api/annotations.proto\"|\n\x06\x45state\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tentrances\x18\x04 \x03(\r\x12\r\n\x05gates\x18\x05 \x03(\r\x12\r\n\x05rooms\x18\x06 \x03(\r\x12\x12\n\nproduct_id\x18\x07 \x01(\r\"8\n\x13\x43reateEstateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\"\n\x14\x43reateEstateResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\x1e\n\x10GetEstateRequest\x12\n\n\x02id\x18\x01 \x01(\r\"D\n\x13UpdateEstateRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\x16\n\x14UpdateEstateResponse\"!\n\x13\x44\x65leteEstateRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x16\n\x14\x44\x65leteEstateResponse\"\x1f\n\x11GetEstatesRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x14\n\x12GetEstatesResponse\"4\n\x0e\x41\x64\x64GateRequest\x12\x11\n\testate_id\x18\x01 \x01(\r\x12\x0f\n\x07gate_id\x18\x02 \x01(\r\"%\n\x0f\x41\x64\x64GateResponse\x12\x12\n\ngate_count\x18\x01 \x01(\r\"7\n\x11\x44\x65leteGateRequest\x12\x11\n\testate_id\x18\x01 \x01(\r\x12\x0f\n\x07gate_id\x18\x02 \x01(\r\"(\n\x12\x44\x65leteGateResponse\x12\x12\n\ngate_count\x18\x01 \x01(\r\"*\n\x15GetEstateGatesRequest\x12\x11\n\testate_id\x18\x01 \x01(\r\"\x18\n\x16GetEstateGatesResponse\"<\n\x12\x41\x64\x64\x45ntranceRequest\x12\x11\n\testate_id\x18\x01 \x01(\r\x12\x13\n\x0b\x65ntrance_id\x18\x02 \x01(\r\"-\n\x13\x41\x64\x64\x45ntranceResponse\x12\x16\n\x0e\x65ntrance_count\x18\x01 \x01(\r\"?\n\x15RemoveEntranceRequest\x12\x11\n\testate_id\x18\x01 \x01(\r\x12\x13\n\x0b\x65ntrance_id\x18\x02 \x01(\r\"0\n\x16RemoveEntranceResponse\x12\x16\n\x0e\x65ntrance_count\x18\x01 \x01(\r\".\n\x19GetEstateEntrancesRequest\x12\x11\n\testate_id\x18\x01 \x01(\r\"\x1c\n\x1aGetEstateEntrancesResponse2\xc4\n\n\x11MruVEstateService\x12j\n\x0c\x43reateEstate\x12!.mruv.estates.CreateEstateRequest\x1a\".mruv.estates.CreateEstateResponse\"\x13\x82\xd3\xe4\x93\x02\r\"\x0b/v1/estates\x12[\n\tGetEstate\x12\x1e.mruv.estates.GetEstateRequest\x1a\x14.mruv.estates.Estate\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/estates/{id}\x12o\n\x0cUpdateEstate\x12!.mruv.estates.UpdateEstateRequest\x1a\".mruv.estates.UpdateEstateResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x32\x10/v1/estates/{id}\x12o\n\x0c\x44\x65leteEstate\x12!.mruv.estates.DeleteEstateRequest\x1a\".mruv.estates.DeleteEstateResponse\"\x18\x82\xd3\xe4\x93\x02\x12*\x10/v1/estates/{id}\x12\x64\n\nGetEstates\x12\x1f.mruv.estates.GetEstatesRequest\x1a .mruv.estates.GetEstatesResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/estates\x12m\n\x07\x41\x64\x64Gate\x12\x1c.mruv.estates.AddGateRequest\x1a\x1d.mruv.estates.AddGateResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1d/v1/estates/{estate_id}/gates\x12\x80\x01\n\nDeleteGate\x12\x1f.mruv.estates.DeleteGateRequest\x1a .mruv.estates.DeleteGateResponse\"/\x82\xd3\xe4\x93\x02)*\'/v1/estates/{estate_id}/gates/{gate_id}\x12\x81\x01\n\x0eGetEstateGates\x12#.mruv.estates.GetEstateGatesRequest\x1a$.mruv.estates.GetEstateGatesResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/estate/{estate_id}/gates\x12}\n\x0b\x41\x64\x64\x45ntrance\x12 .mruv.estates.AddEntranceRequest\x1a!.mruv.estates.AddEntranceResponse\")\x82\xd3\xe4\x93\x02#\"!/v1/estates/{estate_id}/entrances\x12\x94\x01\n\x0eRemoveEntrance\x12#.mruv.estates.RemoveEntranceRequest\x1a$.mruv.estates.RemoveEntranceResponse\"7\x82\xd3\xe4\x93\x02\x31*//v1/estates/{estate_id}/entrances/{entrance_id}\x12\x91\x01\n\x12GetEstateEntrances\x12\'.mruv.estates.GetEstateEntrancesRequest\x1a(.mruv.estates.GetEstateEntrancesResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/estate/{estate_id}/entrancesB\'Z%github.com/MruV-RP/mruv-pb-go/estatesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ESTATE = _descriptor.Descriptor(
  name='Estate',
  full_name='mruv.estates.Estate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.estates.Estate.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.estates.Estate.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.estates.Estate.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entrances', full_name='mruv.estates.Estate.entrances', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gates', full_name='mruv.estates.Estate.gates', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rooms', full_name='mruv.estates.Estate.rooms', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='mruv.estates.Estate.product_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=69,
  serialized_end=193,
)


_CREATEESTATEREQUEST = _descriptor.Descriptor(
  name='CreateEstateRequest',
  full_name='mruv.estates.CreateEstateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.estates.CreateEstateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.estates.CreateEstateRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=195,
  serialized_end=251,
)


_CREATEESTATERESPONSE = _descriptor.Descriptor(
  name='CreateEstateResponse',
  full_name='mruv.estates.CreateEstateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.estates.CreateEstateResponse.id', index=0,
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
  serialized_start=253,
  serialized_end=287,
)


_GETESTATEREQUEST = _descriptor.Descriptor(
  name='GetEstateRequest',
  full_name='mruv.estates.GetEstateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.estates.GetEstateRequest.id', index=0,
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
  serialized_start=289,
  serialized_end=319,
)


_UPDATEESTATEREQUEST = _descriptor.Descriptor(
  name='UpdateEstateRequest',
  full_name='mruv.estates.UpdateEstateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.estates.UpdateEstateRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.estates.UpdateEstateRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.estates.UpdateEstateRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=321,
  serialized_end=389,
)


_UPDATEESTATERESPONSE = _descriptor.Descriptor(
  name='UpdateEstateResponse',
  full_name='mruv.estates.UpdateEstateResponse',
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
  serialized_start=391,
  serialized_end=413,
)


_DELETEESTATEREQUEST = _descriptor.Descriptor(
  name='DeleteEstateRequest',
  full_name='mruv.estates.DeleteEstateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.estates.DeleteEstateRequest.id', index=0,
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
  serialized_start=415,
  serialized_end=448,
)


_DELETEESTATERESPONSE = _descriptor.Descriptor(
  name='DeleteEstateResponse',
  full_name='mruv.estates.DeleteEstateResponse',
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
  serialized_start=450,
  serialized_end=472,
)


_GETESTATESREQUEST = _descriptor.Descriptor(
  name='GetEstatesRequest',
  full_name='mruv.estates.GetEstatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.estates.GetEstatesRequest.id', index=0,
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
  serialized_start=474,
  serialized_end=505,
)


_GETESTATESRESPONSE = _descriptor.Descriptor(
  name='GetEstatesResponse',
  full_name='mruv.estates.GetEstatesResponse',
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
  serialized_start=507,
  serialized_end=527,
)


_ADDGATEREQUEST = _descriptor.Descriptor(
  name='AddGateRequest',
  full_name='mruv.estates.AddGateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='estate_id', full_name='mruv.estates.AddGateRequest.estate_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gate_id', full_name='mruv.estates.AddGateRequest.gate_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=529,
  serialized_end=581,
)


_ADDGATERESPONSE = _descriptor.Descriptor(
  name='AddGateResponse',
  full_name='mruv.estates.AddGateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gate_count', full_name='mruv.estates.AddGateResponse.gate_count', index=0,
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
  serialized_start=583,
  serialized_end=620,
)


_DELETEGATEREQUEST = _descriptor.Descriptor(
  name='DeleteGateRequest',
  full_name='mruv.estates.DeleteGateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='estate_id', full_name='mruv.estates.DeleteGateRequest.estate_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gate_id', full_name='mruv.estates.DeleteGateRequest.gate_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=622,
  serialized_end=677,
)


_DELETEGATERESPONSE = _descriptor.Descriptor(
  name='DeleteGateResponse',
  full_name='mruv.estates.DeleteGateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gate_count', full_name='mruv.estates.DeleteGateResponse.gate_count', index=0,
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
  serialized_start=679,
  serialized_end=719,
)


_GETESTATEGATESREQUEST = _descriptor.Descriptor(
  name='GetEstateGatesRequest',
  full_name='mruv.estates.GetEstateGatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='estate_id', full_name='mruv.estates.GetEstateGatesRequest.estate_id', index=0,
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
  serialized_start=721,
  serialized_end=763,
)


_GETESTATEGATESRESPONSE = _descriptor.Descriptor(
  name='GetEstateGatesResponse',
  full_name='mruv.estates.GetEstateGatesResponse',
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
  serialized_start=765,
  serialized_end=789,
)


_ADDENTRANCEREQUEST = _descriptor.Descriptor(
  name='AddEntranceRequest',
  full_name='mruv.estates.AddEntranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='estate_id', full_name='mruv.estates.AddEntranceRequest.estate_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entrance_id', full_name='mruv.estates.AddEntranceRequest.entrance_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=791,
  serialized_end=851,
)


_ADDENTRANCERESPONSE = _descriptor.Descriptor(
  name='AddEntranceResponse',
  full_name='mruv.estates.AddEntranceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entrance_count', full_name='mruv.estates.AddEntranceResponse.entrance_count', index=0,
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
  serialized_start=853,
  serialized_end=898,
)


_REMOVEENTRANCEREQUEST = _descriptor.Descriptor(
  name='RemoveEntranceRequest',
  full_name='mruv.estates.RemoveEntranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='estate_id', full_name='mruv.estates.RemoveEntranceRequest.estate_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entrance_id', full_name='mruv.estates.RemoveEntranceRequest.entrance_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=900,
  serialized_end=963,
)


_REMOVEENTRANCERESPONSE = _descriptor.Descriptor(
  name='RemoveEntranceResponse',
  full_name='mruv.estates.RemoveEntranceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entrance_count', full_name='mruv.estates.RemoveEntranceResponse.entrance_count', index=0,
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
  serialized_start=965,
  serialized_end=1013,
)


_GETESTATEENTRANCESREQUEST = _descriptor.Descriptor(
  name='GetEstateEntrancesRequest',
  full_name='mruv.estates.GetEstateEntrancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='estate_id', full_name='mruv.estates.GetEstateEntrancesRequest.estate_id', index=0,
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
  serialized_start=1015,
  serialized_end=1061,
)


_GETESTATEENTRANCESRESPONSE = _descriptor.Descriptor(
  name='GetEstateEntrancesResponse',
  full_name='mruv.estates.GetEstateEntrancesResponse',
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
  serialized_start=1063,
  serialized_end=1091,
)

DESCRIPTOR.message_types_by_name['Estate'] = _ESTATE
DESCRIPTOR.message_types_by_name['CreateEstateRequest'] = _CREATEESTATEREQUEST
DESCRIPTOR.message_types_by_name['CreateEstateResponse'] = _CREATEESTATERESPONSE
DESCRIPTOR.message_types_by_name['GetEstateRequest'] = _GETESTATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateEstateRequest'] = _UPDATEESTATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateEstateResponse'] = _UPDATEESTATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteEstateRequest'] = _DELETEESTATEREQUEST
DESCRIPTOR.message_types_by_name['DeleteEstateResponse'] = _DELETEESTATERESPONSE
DESCRIPTOR.message_types_by_name['GetEstatesRequest'] = _GETESTATESREQUEST
DESCRIPTOR.message_types_by_name['GetEstatesResponse'] = _GETESTATESRESPONSE
DESCRIPTOR.message_types_by_name['AddGateRequest'] = _ADDGATEREQUEST
DESCRIPTOR.message_types_by_name['AddGateResponse'] = _ADDGATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteGateRequest'] = _DELETEGATEREQUEST
DESCRIPTOR.message_types_by_name['DeleteGateResponse'] = _DELETEGATERESPONSE
DESCRIPTOR.message_types_by_name['GetEstateGatesRequest'] = _GETESTATEGATESREQUEST
DESCRIPTOR.message_types_by_name['GetEstateGatesResponse'] = _GETESTATEGATESRESPONSE
DESCRIPTOR.message_types_by_name['AddEntranceRequest'] = _ADDENTRANCEREQUEST
DESCRIPTOR.message_types_by_name['AddEntranceResponse'] = _ADDENTRANCERESPONSE
DESCRIPTOR.message_types_by_name['RemoveEntranceRequest'] = _REMOVEENTRANCEREQUEST
DESCRIPTOR.message_types_by_name['RemoveEntranceResponse'] = _REMOVEENTRANCERESPONSE
DESCRIPTOR.message_types_by_name['GetEstateEntrancesRequest'] = _GETESTATEENTRANCESREQUEST
DESCRIPTOR.message_types_by_name['GetEstateEntrancesResponse'] = _GETESTATEENTRANCESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Estate = _reflection.GeneratedProtocolMessageType('Estate', (_message.Message,), {
  'DESCRIPTOR' : _ESTATE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.Estate)
  })
_sym_db.RegisterMessage(Estate)

CreateEstateRequest = _reflection.GeneratedProtocolMessageType('CreateEstateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEESTATEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.CreateEstateRequest)
  })
_sym_db.RegisterMessage(CreateEstateRequest)

CreateEstateResponse = _reflection.GeneratedProtocolMessageType('CreateEstateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEESTATERESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.CreateEstateResponse)
  })
_sym_db.RegisterMessage(CreateEstateResponse)

GetEstateRequest = _reflection.GeneratedProtocolMessageType('GetEstateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETESTATEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.GetEstateRequest)
  })
_sym_db.RegisterMessage(GetEstateRequest)

UpdateEstateRequest = _reflection.GeneratedProtocolMessageType('UpdateEstateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEESTATEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.UpdateEstateRequest)
  })
_sym_db.RegisterMessage(UpdateEstateRequest)

UpdateEstateResponse = _reflection.GeneratedProtocolMessageType('UpdateEstateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEESTATERESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.UpdateEstateResponse)
  })
_sym_db.RegisterMessage(UpdateEstateResponse)

DeleteEstateRequest = _reflection.GeneratedProtocolMessageType('DeleteEstateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEESTATEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.DeleteEstateRequest)
  })
_sym_db.RegisterMessage(DeleteEstateRequest)

DeleteEstateResponse = _reflection.GeneratedProtocolMessageType('DeleteEstateResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEESTATERESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.DeleteEstateResponse)
  })
_sym_db.RegisterMessage(DeleteEstateResponse)

GetEstatesRequest = _reflection.GeneratedProtocolMessageType('GetEstatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETESTATESREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.GetEstatesRequest)
  })
_sym_db.RegisterMessage(GetEstatesRequest)

GetEstatesResponse = _reflection.GeneratedProtocolMessageType('GetEstatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETESTATESRESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.GetEstatesResponse)
  })
_sym_db.RegisterMessage(GetEstatesResponse)

AddGateRequest = _reflection.GeneratedProtocolMessageType('AddGateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDGATEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.AddGateRequest)
  })
_sym_db.RegisterMessage(AddGateRequest)

AddGateResponse = _reflection.GeneratedProtocolMessageType('AddGateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDGATERESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.AddGateResponse)
  })
_sym_db.RegisterMessage(AddGateResponse)

DeleteGateRequest = _reflection.GeneratedProtocolMessageType('DeleteGateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGATEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.DeleteGateRequest)
  })
_sym_db.RegisterMessage(DeleteGateRequest)

DeleteGateResponse = _reflection.GeneratedProtocolMessageType('DeleteGateResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGATERESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.DeleteGateResponse)
  })
_sym_db.RegisterMessage(DeleteGateResponse)

GetEstateGatesRequest = _reflection.GeneratedProtocolMessageType('GetEstateGatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETESTATEGATESREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.GetEstateGatesRequest)
  })
_sym_db.RegisterMessage(GetEstateGatesRequest)

GetEstateGatesResponse = _reflection.GeneratedProtocolMessageType('GetEstateGatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETESTATEGATESRESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.GetEstateGatesResponse)
  })
_sym_db.RegisterMessage(GetEstateGatesResponse)

AddEntranceRequest = _reflection.GeneratedProtocolMessageType('AddEntranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDENTRANCEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.AddEntranceRequest)
  })
_sym_db.RegisterMessage(AddEntranceRequest)

AddEntranceResponse = _reflection.GeneratedProtocolMessageType('AddEntranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDENTRANCERESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.AddEntranceResponse)
  })
_sym_db.RegisterMessage(AddEntranceResponse)

RemoveEntranceRequest = _reflection.GeneratedProtocolMessageType('RemoveEntranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEENTRANCEREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.RemoveEntranceRequest)
  })
_sym_db.RegisterMessage(RemoveEntranceRequest)

RemoveEntranceResponse = _reflection.GeneratedProtocolMessageType('RemoveEntranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEENTRANCERESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.RemoveEntranceResponse)
  })
_sym_db.RegisterMessage(RemoveEntranceResponse)

GetEstateEntrancesRequest = _reflection.GeneratedProtocolMessageType('GetEstateEntrancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETESTATEENTRANCESREQUEST,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.GetEstateEntrancesRequest)
  })
_sym_db.RegisterMessage(GetEstateEntrancesRequest)

GetEstateEntrancesResponse = _reflection.GeneratedProtocolMessageType('GetEstateEntrancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETESTATEENTRANCESRESPONSE,
  '__module__' : 'estates.estates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.estates.GetEstateEntrancesResponse)
  })
_sym_db.RegisterMessage(GetEstateEntrancesResponse)


DESCRIPTOR._options = None

_MRUVESTATESERVICE = _descriptor.ServiceDescriptor(
  name='MruVEstateService',
  full_name='mruv.estates.MruVEstateService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1094,
  serialized_end=2442,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateEstate',
    full_name='mruv.estates.MruVEstateService.CreateEstate',
    index=0,
    containing_service=None,
    input_type=_CREATEESTATEREQUEST,
    output_type=_CREATEESTATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\r\"\013/v1/estates'),
  ),
  _descriptor.MethodDescriptor(
    name='GetEstate',
    full_name='mruv.estates.MruVEstateService.GetEstate',
    index=1,
    containing_service=None,
    input_type=_GETESTATEREQUEST,
    output_type=_ESTATE,
    serialized_options=_b('\202\323\344\223\002\022\022\020/v1/estates/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateEstate',
    full_name='mruv.estates.MruVEstateService.UpdateEstate',
    index=2,
    containing_service=None,
    input_type=_UPDATEESTATEREQUEST,
    output_type=_UPDATEESTATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\0222\020/v1/estates/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteEstate',
    full_name='mruv.estates.MruVEstateService.DeleteEstate',
    index=3,
    containing_service=None,
    input_type=_DELETEESTATEREQUEST,
    output_type=_DELETEESTATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\022*\020/v1/estates/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetEstates',
    full_name='mruv.estates.MruVEstateService.GetEstates',
    index=4,
    containing_service=None,
    input_type=_GETESTATESREQUEST,
    output_type=_GETESTATESRESPONSE,
    serialized_options=_b('\202\323\344\223\002\r\022\013/v1/estates'),
  ),
  _descriptor.MethodDescriptor(
    name='AddGate',
    full_name='mruv.estates.MruVEstateService.AddGate',
    index=5,
    containing_service=None,
    input_type=_ADDGATEREQUEST,
    output_type=_ADDGATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\037\"\035/v1/estates/{estate_id}/gates'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteGate',
    full_name='mruv.estates.MruVEstateService.DeleteGate',
    index=6,
    containing_service=None,
    input_type=_DELETEGATEREQUEST,
    output_type=_DELETEGATERESPONSE,
    serialized_options=_b('\202\323\344\223\002)*\'/v1/estates/{estate_id}/gates/{gate_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetEstateGates',
    full_name='mruv.estates.MruVEstateService.GetEstateGates',
    index=7,
    containing_service=None,
    input_type=_GETESTATEGATESREQUEST,
    output_type=_GETESTATEGATESRESPONSE,
    serialized_options=_b('\202\323\344\223\002\036\022\034/v1/estate/{estate_id}/gates'),
  ),
  _descriptor.MethodDescriptor(
    name='AddEntrance',
    full_name='mruv.estates.MruVEstateService.AddEntrance',
    index=8,
    containing_service=None,
    input_type=_ADDENTRANCEREQUEST,
    output_type=_ADDENTRANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002#\"!/v1/estates/{estate_id}/entrances'),
  ),
  _descriptor.MethodDescriptor(
    name='RemoveEntrance',
    full_name='mruv.estates.MruVEstateService.RemoveEntrance',
    index=9,
    containing_service=None,
    input_type=_REMOVEENTRANCEREQUEST,
    output_type=_REMOVEENTRANCERESPONSE,
    serialized_options=_b('\202\323\344\223\0021*//v1/estates/{estate_id}/entrances/{entrance_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetEstateEntrances',
    full_name='mruv.estates.MruVEstateService.GetEstateEntrances',
    index=10,
    containing_service=None,
    input_type=_GETESTATEENTRANCESREQUEST,
    output_type=_GETESTATEENTRANCESRESPONSE,
    serialized_options=_b('\202\323\344\223\002\"\022 /v1/estate/{estate_id}/entrances'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVESTATESERVICE)

DESCRIPTOR.services_by_name['MruVEstateService'] = _MRUVESTATESERVICE

# @@protoc_insertion_point(module_scope)
