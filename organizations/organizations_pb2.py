# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: organizations/organizations.proto

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
  name='organizations/organizations.proto',
  package='mruv.organizations',
  syntax='proto3',
  serialized_options=_b('Z+github.com/MruV-RP/mruv-pb-go/organizations'),
  serialized_pb=_b('\n!organizations/organizations.proto\x12\x12mruv.organizations\x1a\x1cgoogle/api/annotations.proto\"\x1b\n\x19\x43reateOrganizationRequest\"\x1c\n\x1a\x43reateOrganizationResponse\"$\n\x16GetOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x19\n\x17GetOrganizationResponse\"\'\n\x19UpdateOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x1c\n\x1aUpdateOrganizationResponse\"\'\n\x19\x44\x65leteOrganizationRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x1c\n\x1a\x44\x65leteOrganizationResponse\"!\n\x13\x41ssignLeaderRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x16\n\x14\x41ssignLeaderResponse\"#\n\x15UnassignLeaderRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x18\n\x16UnassignLeaderResponse2\x80\x07\n\x18MruVOrganizationsService\x12\x8e\x01\n\x12\x43reateOrganization\x12-.mruv.organizations.CreateOrganizationRequest\x1a..mruv.organizations.CreateOrganizationResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x11/v1/organizations\x12\x8a\x01\n\x0fGetOrganization\x12*.mruv.organizations.GetOrganizationRequest\x1a+.mruv.organizations.GetOrganizationResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/organizations/{id}\x12\x93\x01\n\x12UpdateOrganization\x12-.mruv.organizations.UpdateOrganizationRequest\x1a..mruv.organizations.UpdateOrganizationResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x32\x16/v1/organizations/{id}\x12\x93\x01\n\x12\x44\x65leteOrganization\x12-.mruv.organizations.DeleteOrganizationRequest\x1a..mruv.organizations.DeleteOrganizationResponse\"\x1e\x82\xd3\xe4\x93\x02\x18*\x16/v1/organizations/{id}\x12\x88\x01\n\x0c\x41ssignLeader\x12\'.mruv.organizations.AssignLeaderRequest\x1a(.mruv.organizations.AssignLeaderResponse\"%\x82\xd3\xe4\x93\x02\x1f\x1a\x1d/v1/organizations/{id}/leader\x12\x8e\x01\n\x0eUnassignLeader\x12).mruv.organizations.UnassignLeaderRequest\x1a*.mruv.organizations.UnassignLeaderResponse\"%\x82\xd3\xe4\x93\x02\x1f*\x1d/v1/organizations/{id}/leaderB-Z+github.com/MruV-RP/mruv-pb-go/organizationsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CREATEORGANIZATIONREQUEST = _descriptor.Descriptor(
  name='CreateOrganizationRequest',
  full_name='mruv.organizations.CreateOrganizationRequest',
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
  serialized_start=87,
  serialized_end=114,
)


_CREATEORGANIZATIONRESPONSE = _descriptor.Descriptor(
  name='CreateOrganizationResponse',
  full_name='mruv.organizations.CreateOrganizationResponse',
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
  serialized_start=116,
  serialized_end=144,
)


_GETORGANIZATIONREQUEST = _descriptor.Descriptor(
  name='GetOrganizationRequest',
  full_name='mruv.organizations.GetOrganizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.organizations.GetOrganizationRequest.id', index=0,
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
  serialized_start=146,
  serialized_end=182,
)


_GETORGANIZATIONRESPONSE = _descriptor.Descriptor(
  name='GetOrganizationResponse',
  full_name='mruv.organizations.GetOrganizationResponse',
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
  serialized_start=184,
  serialized_end=209,
)


_UPDATEORGANIZATIONREQUEST = _descriptor.Descriptor(
  name='UpdateOrganizationRequest',
  full_name='mruv.organizations.UpdateOrganizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.organizations.UpdateOrganizationRequest.id', index=0,
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
  serialized_start=211,
  serialized_end=250,
)


_UPDATEORGANIZATIONRESPONSE = _descriptor.Descriptor(
  name='UpdateOrganizationResponse',
  full_name='mruv.organizations.UpdateOrganizationResponse',
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
  serialized_start=252,
  serialized_end=280,
)


_DELETEORGANIZATIONREQUEST = _descriptor.Descriptor(
  name='DeleteOrganizationRequest',
  full_name='mruv.organizations.DeleteOrganizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.organizations.DeleteOrganizationRequest.id', index=0,
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
  serialized_start=282,
  serialized_end=321,
)


_DELETEORGANIZATIONRESPONSE = _descriptor.Descriptor(
  name='DeleteOrganizationResponse',
  full_name='mruv.organizations.DeleteOrganizationResponse',
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
  serialized_start=323,
  serialized_end=351,
)


_ASSIGNLEADERREQUEST = _descriptor.Descriptor(
  name='AssignLeaderRequest',
  full_name='mruv.organizations.AssignLeaderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.organizations.AssignLeaderRequest.id', index=0,
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
  serialized_start=353,
  serialized_end=386,
)


_ASSIGNLEADERRESPONSE = _descriptor.Descriptor(
  name='AssignLeaderResponse',
  full_name='mruv.organizations.AssignLeaderResponse',
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
  serialized_start=388,
  serialized_end=410,
)


_UNASSIGNLEADERREQUEST = _descriptor.Descriptor(
  name='UnassignLeaderRequest',
  full_name='mruv.organizations.UnassignLeaderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.organizations.UnassignLeaderRequest.id', index=0,
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
  serialized_start=412,
  serialized_end=447,
)


_UNASSIGNLEADERRESPONSE = _descriptor.Descriptor(
  name='UnassignLeaderResponse',
  full_name='mruv.organizations.UnassignLeaderResponse',
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
  serialized_start=449,
  serialized_end=473,
)

DESCRIPTOR.message_types_by_name['CreateOrganizationRequest'] = _CREATEORGANIZATIONREQUEST
DESCRIPTOR.message_types_by_name['CreateOrganizationResponse'] = _CREATEORGANIZATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetOrganizationRequest'] = _GETORGANIZATIONREQUEST
DESCRIPTOR.message_types_by_name['GetOrganizationResponse'] = _GETORGANIZATIONRESPONSE
DESCRIPTOR.message_types_by_name['UpdateOrganizationRequest'] = _UPDATEORGANIZATIONREQUEST
DESCRIPTOR.message_types_by_name['UpdateOrganizationResponse'] = _UPDATEORGANIZATIONRESPONSE
DESCRIPTOR.message_types_by_name['DeleteOrganizationRequest'] = _DELETEORGANIZATIONREQUEST
DESCRIPTOR.message_types_by_name['DeleteOrganizationResponse'] = _DELETEORGANIZATIONRESPONSE
DESCRIPTOR.message_types_by_name['AssignLeaderRequest'] = _ASSIGNLEADERREQUEST
DESCRIPTOR.message_types_by_name['AssignLeaderResponse'] = _ASSIGNLEADERRESPONSE
DESCRIPTOR.message_types_by_name['UnassignLeaderRequest'] = _UNASSIGNLEADERREQUEST
DESCRIPTOR.message_types_by_name['UnassignLeaderResponse'] = _UNASSIGNLEADERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateOrganizationRequest = _reflection.GeneratedProtocolMessageType('CreateOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGANIZATIONREQUEST,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.CreateOrganizationRequest)
  })
_sym_db.RegisterMessage(CreateOrganizationRequest)

CreateOrganizationResponse = _reflection.GeneratedProtocolMessageType('CreateOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGANIZATIONRESPONSE,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.CreateOrganizationResponse)
  })
_sym_db.RegisterMessage(CreateOrganizationResponse)

GetOrganizationRequest = _reflection.GeneratedProtocolMessageType('GetOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONREQUEST,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.GetOrganizationRequest)
  })
_sym_db.RegisterMessage(GetOrganizationRequest)

GetOrganizationResponse = _reflection.GeneratedProtocolMessageType('GetOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORGANIZATIONRESPONSE,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.GetOrganizationResponse)
  })
_sym_db.RegisterMessage(GetOrganizationResponse)

UpdateOrganizationRequest = _reflection.GeneratedProtocolMessageType('UpdateOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORGANIZATIONREQUEST,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.UpdateOrganizationRequest)
  })
_sym_db.RegisterMessage(UpdateOrganizationRequest)

UpdateOrganizationResponse = _reflection.GeneratedProtocolMessageType('UpdateOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORGANIZATIONRESPONSE,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.UpdateOrganizationResponse)
  })
_sym_db.RegisterMessage(UpdateOrganizationResponse)

DeleteOrganizationRequest = _reflection.GeneratedProtocolMessageType('DeleteOrganizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEORGANIZATIONREQUEST,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.DeleteOrganizationRequest)
  })
_sym_db.RegisterMessage(DeleteOrganizationRequest)

DeleteOrganizationResponse = _reflection.GeneratedProtocolMessageType('DeleteOrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEORGANIZATIONRESPONSE,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.DeleteOrganizationResponse)
  })
_sym_db.RegisterMessage(DeleteOrganizationResponse)

AssignLeaderRequest = _reflection.GeneratedProtocolMessageType('AssignLeaderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNLEADERREQUEST,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.AssignLeaderRequest)
  })
_sym_db.RegisterMessage(AssignLeaderRequest)

AssignLeaderResponse = _reflection.GeneratedProtocolMessageType('AssignLeaderResponse', (_message.Message,), {
  'DESCRIPTOR' : _ASSIGNLEADERRESPONSE,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.AssignLeaderResponse)
  })
_sym_db.RegisterMessage(AssignLeaderResponse)

UnassignLeaderRequest = _reflection.GeneratedProtocolMessageType('UnassignLeaderRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNASSIGNLEADERREQUEST,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.UnassignLeaderRequest)
  })
_sym_db.RegisterMessage(UnassignLeaderRequest)

UnassignLeaderResponse = _reflection.GeneratedProtocolMessageType('UnassignLeaderResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNASSIGNLEADERRESPONSE,
  '__module__' : 'organizations.organizations_pb2'
  # @@protoc_insertion_point(class_scope:mruv.organizations.UnassignLeaderResponse)
  })
_sym_db.RegisterMessage(UnassignLeaderResponse)


DESCRIPTOR._options = None

_MRUVORGANIZATIONSSERVICE = _descriptor.ServiceDescriptor(
  name='MruVOrganizationsService',
  full_name='mruv.organizations.MruVOrganizationsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=476,
  serialized_end=1372,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateOrganization',
    full_name='mruv.organizations.MruVOrganizationsService.CreateOrganization',
    index=0,
    containing_service=None,
    input_type=_CREATEORGANIZATIONREQUEST,
    output_type=_CREATEORGANIZATIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\"\021/v1/organizations'),
  ),
  _descriptor.MethodDescriptor(
    name='GetOrganization',
    full_name='mruv.organizations.MruVOrganizationsService.GetOrganization',
    index=1,
    containing_service=None,
    input_type=_GETORGANIZATIONREQUEST,
    output_type=_GETORGANIZATIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\030\022\026/v1/organizations/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateOrganization',
    full_name='mruv.organizations.MruVOrganizationsService.UpdateOrganization',
    index=2,
    containing_service=None,
    input_type=_UPDATEORGANIZATIONREQUEST,
    output_type=_UPDATEORGANIZATIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\0302\026/v1/organizations/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteOrganization',
    full_name='mruv.organizations.MruVOrganizationsService.DeleteOrganization',
    index=3,
    containing_service=None,
    input_type=_DELETEORGANIZATIONREQUEST,
    output_type=_DELETEORGANIZATIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002\030*\026/v1/organizations/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='AssignLeader',
    full_name='mruv.organizations.MruVOrganizationsService.AssignLeader',
    index=4,
    containing_service=None,
    input_type=_ASSIGNLEADERREQUEST,
    output_type=_ASSIGNLEADERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\037\032\035/v1/organizations/{id}/leader'),
  ),
  _descriptor.MethodDescriptor(
    name='UnassignLeader',
    full_name='mruv.organizations.MruVOrganizationsService.UnassignLeader',
    index=5,
    containing_service=None,
    input_type=_UNASSIGNLEADERREQUEST,
    output_type=_UNASSIGNLEADERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\037*\035/v1/organizations/{id}/leader'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVORGANIZATIONSSERVICE)

DESCRIPTOR.services_by_name['MruVOrganizationsService'] = _MRUVORGANIZATIONSSERVICE

# @@protoc_insertion_point(module_scope)