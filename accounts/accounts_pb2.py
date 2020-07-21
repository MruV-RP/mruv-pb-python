# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts/accounts.proto

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
  name='accounts/accounts.proto',
  package='mruv',
  syntax='proto3',
  serialized_options=_b('Z&github.com/MruV-RP/mruv-pb-go/accounts'),
  serialized_pb=_b('\n\x17\x61\x63\x63ounts/accounts.proto\x12\x04mruv\x1a\x1cgoogle/api/annotations.proto\"H\n\x16RegisterAccountRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\">\n\x17RegisterAccountResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\naccount_id\x18\x02 \x01(\r\"/\n\x0cLogInRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"4\n\rLogInResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\naccount_id\x18\x02 \x01(\r\"\"\n\x11GetAccountRequest\x12\r\n\x05login\x18\x01 \x01(\t\"2\n\x12GetAccountResponse\x12\r\n\x05login\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\",\n\x1bGetAccountCharactersRequest\x12\r\n\x05login\x18\x01 \x01(\t\"5\n\x1cGetAccountCharactersResponse\x12\x15\n\rcharacter_ids\x18\x01 \x03(\r\"&\n\x15IsAccountExistRequest\x12\r\n\x05login\x18\x01 \x01(\t\"4\n\x16IsAccountExistResponse\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\r2\xb0\x04\n\x13MruVAccountsService\x12m\n\x0fRegisterAccount\x12\x1c.mruv.RegisterAccountRequest\x1a\x1d.mruv.RegisterAccountResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/v1/accounts/register\x12L\n\x05LogIn\x12\x12.mruv.LogInRequest\x1a\x13.mruv.LogInResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x12/v1/accounts/login\x12t\n\x0eIsAccountExist\x12\x1b.mruv.IsAccountExistRequest\x1a\x1c.mruv.IsAccountExistResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/accounts/{login}/registered\x12]\n\nGetAccount\x12\x17.mruv.GetAccountRequest\x1a\x18.mruv.GetAccountResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/accounts/{login}\x12\x86\x01\n\x14GetAccountCharacters\x12!.mruv.GetAccountCharactersRequest\x1a\".mruv.GetAccountCharactersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/accounts/{login}/charactersB(Z&github.com/MruV-RP/mruv-pb-go/accountsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_REGISTERACCOUNTREQUEST = _descriptor.Descriptor(
  name='RegisterAccountRequest',
  full_name='mruv.RegisterAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='mruv.RegisterAccountRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='mruv.RegisterAccountRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='mruv.RegisterAccountRequest.email', index=2,
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
  serialized_start=63,
  serialized_end=135,
)


_REGISTERACCOUNTRESPONSE = _descriptor.Descriptor(
  name='RegisterAccountResponse',
  full_name='mruv.RegisterAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='mruv.RegisterAccountResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='mruv.RegisterAccountResponse.account_id', index=1,
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
  serialized_start=137,
  serialized_end=199,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LogInRequest',
  full_name='mruv.LogInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='mruv.LogInRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='mruv.LogInRequest.password', index=1,
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
  serialized_start=201,
  serialized_end=248,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LogInResponse',
  full_name='mruv.LogInResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='mruv.LogInResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='mruv.LogInResponse.account_id', index=1,
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
  serialized_start=250,
  serialized_end=302,
)


_GETACCOUNTREQUEST = _descriptor.Descriptor(
  name='GetAccountRequest',
  full_name='mruv.GetAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='mruv.GetAccountRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=304,
  serialized_end=338,
)


_GETACCOUNTRESPONSE = _descriptor.Descriptor(
  name='GetAccountResponse',
  full_name='mruv.GetAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='mruv.GetAccountResponse.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='mruv.GetAccountResponse.email', index=1,
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
  serialized_start=340,
  serialized_end=390,
)


_GETACCOUNTCHARACTERSREQUEST = _descriptor.Descriptor(
  name='GetAccountCharactersRequest',
  full_name='mruv.GetAccountCharactersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='mruv.GetAccountCharactersRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=392,
  serialized_end=436,
)


_GETACCOUNTCHARACTERSRESPONSE = _descriptor.Descriptor(
  name='GetAccountCharactersResponse',
  full_name='mruv.GetAccountCharactersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='character_ids', full_name='mruv.GetAccountCharactersResponse.character_ids', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=438,
  serialized_end=491,
)


_ISACCOUNTEXISTREQUEST = _descriptor.Descriptor(
  name='IsAccountExistRequest',
  full_name='mruv.IsAccountExistRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login', full_name='mruv.IsAccountExistRequest.login', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=493,
  serialized_end=531,
)


_ISACCOUNTEXISTRESPONSE = _descriptor.Descriptor(
  name='IsAccountExistResponse',
  full_name='mruv.IsAccountExistResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exists', full_name='mruv.IsAccountExistResponse.exists', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.IsAccountExistResponse.id', index=1,
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
  serialized_start=533,
  serialized_end=585,
)

DESCRIPTOR.message_types_by_name['RegisterAccountRequest'] = _REGISTERACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['RegisterAccountResponse'] = _REGISTERACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['LogInRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LogInResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['GetAccountRequest'] = _GETACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['GetAccountResponse'] = _GETACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['GetAccountCharactersRequest'] = _GETACCOUNTCHARACTERSREQUEST
DESCRIPTOR.message_types_by_name['GetAccountCharactersResponse'] = _GETACCOUNTCHARACTERSRESPONSE
DESCRIPTOR.message_types_by_name['IsAccountExistRequest'] = _ISACCOUNTEXISTREQUEST
DESCRIPTOR.message_types_by_name['IsAccountExistResponse'] = _ISACCOUNTEXISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterAccountRequest = _reflection.GeneratedProtocolMessageType('RegisterAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERACCOUNTREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.RegisterAccountRequest)
  })
_sym_db.RegisterMessage(RegisterAccountRequest)

RegisterAccountResponse = _reflection.GeneratedProtocolMessageType('RegisterAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERACCOUNTRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.RegisterAccountResponse)
  })
_sym_db.RegisterMessage(RegisterAccountResponse)

LogInRequest = _reflection.GeneratedProtocolMessageType('LogInRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.LogInRequest)
  })
_sym_db.RegisterMessage(LogInRequest)

LogInResponse = _reflection.GeneratedProtocolMessageType('LogInResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.LogInResponse)
  })
_sym_db.RegisterMessage(LogInResponse)

GetAccountRequest = _reflection.GeneratedProtocolMessageType('GetAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.GetAccountRequest)
  })
_sym_db.RegisterMessage(GetAccountRequest)

GetAccountResponse = _reflection.GeneratedProtocolMessageType('GetAccountResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.GetAccountResponse)
  })
_sym_db.RegisterMessage(GetAccountResponse)

GetAccountCharactersRequest = _reflection.GeneratedProtocolMessageType('GetAccountCharactersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTCHARACTERSREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.GetAccountCharactersRequest)
  })
_sym_db.RegisterMessage(GetAccountCharactersRequest)

GetAccountCharactersResponse = _reflection.GeneratedProtocolMessageType('GetAccountCharactersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTCHARACTERSRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.GetAccountCharactersResponse)
  })
_sym_db.RegisterMessage(GetAccountCharactersResponse)

IsAccountExistRequest = _reflection.GeneratedProtocolMessageType('IsAccountExistRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISACCOUNTEXISTREQUEST,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.IsAccountExistRequest)
  })
_sym_db.RegisterMessage(IsAccountExistRequest)

IsAccountExistResponse = _reflection.GeneratedProtocolMessageType('IsAccountExistResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISACCOUNTEXISTRESPONSE,
  '__module__' : 'accounts.accounts_pb2'
  # @@protoc_insertion_point(class_scope:mruv.IsAccountExistResponse)
  })
_sym_db.RegisterMessage(IsAccountExistResponse)


DESCRIPTOR._options = None

_MRUVACCOUNTSSERVICE = _descriptor.ServiceDescriptor(
  name='MruVAccountsService',
  full_name='mruv.MruVAccountsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=588,
  serialized_end=1148,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterAccount',
    full_name='mruv.MruVAccountsService.RegisterAccount',
    index=0,
    containing_service=None,
    input_type=_REGISTERACCOUNTREQUEST,
    output_type=_REGISTERACCOUNTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\"\025/v1/accounts/register'),
  ),
  _descriptor.MethodDescriptor(
    name='LogIn',
    full_name='mruv.MruVAccountsService.LogIn',
    index=1,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINRESPONSE,
    serialized_options=_b('\202\323\344\223\002\024\"\022/v1/accounts/login'),
  ),
  _descriptor.MethodDescriptor(
    name='IsAccountExist',
    full_name='mruv.MruVAccountsService.IsAccountExist',
    index=2,
    containing_service=None,
    input_type=_ISACCOUNTEXISTREQUEST,
    output_type=_ISACCOUNTEXISTRESPONSE,
    serialized_options=_b('\202\323\344\223\002!\022\037/v1/accounts/{login}/registered'),
  ),
  _descriptor.MethodDescriptor(
    name='GetAccount',
    full_name='mruv.MruVAccountsService.GetAccount',
    index=3,
    containing_service=None,
    input_type=_GETACCOUNTREQUEST,
    output_type=_GETACCOUNTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\022\024/v1/accounts/{login}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetAccountCharacters',
    full_name='mruv.MruVAccountsService.GetAccountCharacters',
    index=4,
    containing_service=None,
    input_type=_GETACCOUNTCHARACTERSREQUEST,
    output_type=_GETACCOUNTCHARACTERSRESPONSE,
    serialized_options=_b('\202\323\344\223\002!\022\037/v1/accounts/{login}/characters'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVACCOUNTSSERVICE)

DESCRIPTOR.services_by_name['MruVAccountsService'] = _MRUVACCOUNTSSERVICE

# @@protoc_insertion_point(module_scope)