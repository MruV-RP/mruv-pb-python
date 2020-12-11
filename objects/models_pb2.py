# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: objects/models.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='objects/models.proto',
  package='mruv.objects',
  syntax='proto3',
  serialized_options=b'Z%github.com/MruV-RP/mruv-pb-go/objects',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14objects/models.proto\x12\x0cmruv.objects\x1a\x1cgoogle/api/annotations.proto\"\xa3\x02\n\x0bObjectModel\x12\r\n\x05model\x18\x01 \x01(\x05\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\x0e\n\x06length\x18\x05 \x01(\x01\x12\r\n\x05width\x18\x06 \x01(\x01\x12\x0e\n\x06height\x18\x07 \x01(\x01\x12\x0c\n\x04size\x18\x08 \x01(\x01\x12\x0c\n\x04tags\x18\t \x03(\t\x12\x15\n\rhas_collision\x18\n \x01(\x08\x12\x15\n\rbreaks_on_hit\x18\x0b \x01(\x08\x12\x15\n\rhas_animation\x18\x0c \x01(\x08\x12\x17\n\x0fvisible_by_time\x18\x10 \x01(\x08\x12\x14\n\x0cvisible_from\x18\x11 \x01(\r\x12\x12\n\nvisible_to\x18\x12 \x01(\r\"J\n\x18\x43reateObjectModelRequest\x12.\n\x0bobject_type\x18\x01 \x01(\x0b\x32\x19.mruv.objects.ObjectModel\"\'\n\x19\x43reateObjectModelResponse\x12\n\n\x02id\x18\x01 \x01(\r\"&\n\x15GetObjectModelRequest\x12\r\n\x05model\x18\x01 \x01(\x05\"H\n\x16GetObjectModelResponse\x12.\n\x0bobject_type\x18\x01 \x01(\x0b\x32\x19.mruv.objects.ObjectModel\"J\n\x18UpdateObjectModelRequest\x12.\n\x0bobject_type\x18\x01 \x01(\x0b\x32\x19.mruv.objects.ObjectModel\"\x1b\n\x19UpdateObjectModelResponse\")\n\x18\x44\x65leteObjectModelRequest\x12\r\n\x05model\x18\x01 \x01(\x05\"\x1b\n\x19\x44\x65leteObjectModelResponse\"+\n\x15\x46\x65tchAllModelsRequest\x12\x12\n\nchunk_size\x18\x01 \x01(\r\"\xa4\x01\n\x16\x46\x65tchAllModelsResponse\x12@\n\x06models\x18\x01 \x03(\x0b\x32\x30.mruv.objects.FetchAllModelsResponse.ModelsEntry\x1aH\n\x0bModelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.mruv.objects.ObjectModel:\x02\x38\x01\x32\xb1\x05\n\x17MruVObjectModelsService\x12\x80\x01\n\x11\x43reateObjectModel\x12&.mruv.objects.CreateObjectModelRequest\x1a\'.mruv.objects.CreateObjectModelResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/objectTypes:\x01*\x12|\n\x0eGetObjectModel\x12#.mruv.objects.GetObjectModelRequest\x1a$.mruv.objects.GetObjectModelResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/objectTypes/{model}\x12\x94\x01\n\x11UpdateObjectModel\x12&.mruv.objects.UpdateObjectModelRequest\x1a\'.mruv.objects.UpdateObjectModelResponse\".\x82\xd3\xe4\x93\x02(2#/v1/objectTypes/{object_type.model}:\x01*\x12\x85\x01\n\x11\x44\x65leteObjectModel\x12&.mruv.objects.DeleteObjectModelRequest\x1a\'.mruv.objects.DeleteObjectModelResponse\"\x1f\x82\xd3\xe4\x93\x02\x19*\x17/v1/objectTypes/{model}\x12v\n\x0e\x46\x65tchAllModels\x12#.mruv.objects.FetchAllModelsRequest\x1a$.mruv.objects.FetchAllModelsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/objectTypes0\x01\x42\'Z%github.com/MruV-RP/mruv-pb-go/objectsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_OBJECTMODEL = _descriptor.Descriptor(
  name='ObjectModel',
  full_name='mruv.objects.ObjectModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='mruv.objects.ObjectModel.model', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='mruv.objects.ObjectModel.model_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.objects.ObjectModel.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='mruv.objects.ObjectModel.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='mruv.objects.ObjectModel.length', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='mruv.objects.ObjectModel.width', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='mruv.objects.ObjectModel.height', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='mruv.objects.ObjectModel.size', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='mruv.objects.ObjectModel.tags', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_collision', full_name='mruv.objects.ObjectModel.has_collision', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='breaks_on_hit', full_name='mruv.objects.ObjectModel.breaks_on_hit', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_animation', full_name='mruv.objects.ObjectModel.has_animation', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visible_by_time', full_name='mruv.objects.ObjectModel.visible_by_time', index=12,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visible_from', full_name='mruv.objects.ObjectModel.visible_from', index=13,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visible_to', full_name='mruv.objects.ObjectModel.visible_to', index=14,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=360,
)


_CREATEOBJECTMODELREQUEST = _descriptor.Descriptor(
  name='CreateObjectModelRequest',
  full_name='mruv.objects.CreateObjectModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_type', full_name='mruv.objects.CreateObjectModelRequest.object_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=362,
  serialized_end=436,
)


_CREATEOBJECTMODELRESPONSE = _descriptor.Descriptor(
  name='CreateObjectModelResponse',
  full_name='mruv.objects.CreateObjectModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.objects.CreateObjectModelResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=477,
)


_GETOBJECTMODELREQUEST = _descriptor.Descriptor(
  name='GetObjectModelRequest',
  full_name='mruv.objects.GetObjectModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='mruv.objects.GetObjectModelRequest.model', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=479,
  serialized_end=517,
)


_GETOBJECTMODELRESPONSE = _descriptor.Descriptor(
  name='GetObjectModelResponse',
  full_name='mruv.objects.GetObjectModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_type', full_name='mruv.objects.GetObjectModelResponse.object_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=519,
  serialized_end=591,
)


_UPDATEOBJECTMODELREQUEST = _descriptor.Descriptor(
  name='UpdateObjectModelRequest',
  full_name='mruv.objects.UpdateObjectModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_type', full_name='mruv.objects.UpdateObjectModelRequest.object_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=593,
  serialized_end=667,
)


_UPDATEOBJECTMODELRESPONSE = _descriptor.Descriptor(
  name='UpdateObjectModelResponse',
  full_name='mruv.objects.UpdateObjectModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=669,
  serialized_end=696,
)


_DELETEOBJECTMODELREQUEST = _descriptor.Descriptor(
  name='DeleteObjectModelRequest',
  full_name='mruv.objects.DeleteObjectModelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='mruv.objects.DeleteObjectModelRequest.model', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=698,
  serialized_end=739,
)


_DELETEOBJECTMODELRESPONSE = _descriptor.Descriptor(
  name='DeleteObjectModelResponse',
  full_name='mruv.objects.DeleteObjectModelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=741,
  serialized_end=768,
)


_FETCHALLMODELSREQUEST = _descriptor.Descriptor(
  name='FetchAllModelsRequest',
  full_name='mruv.objects.FetchAllModelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_size', full_name='mruv.objects.FetchAllModelsRequest.chunk_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=770,
  serialized_end=813,
)


_FETCHALLMODELSRESPONSE_MODELSENTRY = _descriptor.Descriptor(
  name='ModelsEntry',
  full_name='mruv.objects.FetchAllModelsResponse.ModelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mruv.objects.FetchAllModelsResponse.ModelsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='mruv.objects.FetchAllModelsResponse.ModelsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=908,
  serialized_end=980,
)

_FETCHALLMODELSRESPONSE = _descriptor.Descriptor(
  name='FetchAllModelsResponse',
  full_name='mruv.objects.FetchAllModelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='models', full_name='mruv.objects.FetchAllModelsResponse.models', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FETCHALLMODELSRESPONSE_MODELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=816,
  serialized_end=980,
)

_CREATEOBJECTMODELREQUEST.fields_by_name['object_type'].message_type = _OBJECTMODEL
_GETOBJECTMODELRESPONSE.fields_by_name['object_type'].message_type = _OBJECTMODEL
_UPDATEOBJECTMODELREQUEST.fields_by_name['object_type'].message_type = _OBJECTMODEL
_FETCHALLMODELSRESPONSE_MODELSENTRY.fields_by_name['value'].message_type = _OBJECTMODEL
_FETCHALLMODELSRESPONSE_MODELSENTRY.containing_type = _FETCHALLMODELSRESPONSE
_FETCHALLMODELSRESPONSE.fields_by_name['models'].message_type = _FETCHALLMODELSRESPONSE_MODELSENTRY
DESCRIPTOR.message_types_by_name['ObjectModel'] = _OBJECTMODEL
DESCRIPTOR.message_types_by_name['CreateObjectModelRequest'] = _CREATEOBJECTMODELREQUEST
DESCRIPTOR.message_types_by_name['CreateObjectModelResponse'] = _CREATEOBJECTMODELRESPONSE
DESCRIPTOR.message_types_by_name['GetObjectModelRequest'] = _GETOBJECTMODELREQUEST
DESCRIPTOR.message_types_by_name['GetObjectModelResponse'] = _GETOBJECTMODELRESPONSE
DESCRIPTOR.message_types_by_name['UpdateObjectModelRequest'] = _UPDATEOBJECTMODELREQUEST
DESCRIPTOR.message_types_by_name['UpdateObjectModelResponse'] = _UPDATEOBJECTMODELRESPONSE
DESCRIPTOR.message_types_by_name['DeleteObjectModelRequest'] = _DELETEOBJECTMODELREQUEST
DESCRIPTOR.message_types_by_name['DeleteObjectModelResponse'] = _DELETEOBJECTMODELRESPONSE
DESCRIPTOR.message_types_by_name['FetchAllModelsRequest'] = _FETCHALLMODELSREQUEST
DESCRIPTOR.message_types_by_name['FetchAllModelsResponse'] = _FETCHALLMODELSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectModel = _reflection.GeneratedProtocolMessageType('ObjectModel', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMODEL,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.ObjectModel)
  })
_sym_db.RegisterMessage(ObjectModel)

CreateObjectModelRequest = _reflection.GeneratedProtocolMessageType('CreateObjectModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOBJECTMODELREQUEST,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.CreateObjectModelRequest)
  })
_sym_db.RegisterMessage(CreateObjectModelRequest)

CreateObjectModelResponse = _reflection.GeneratedProtocolMessageType('CreateObjectModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOBJECTMODELRESPONSE,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.CreateObjectModelResponse)
  })
_sym_db.RegisterMessage(CreateObjectModelResponse)

GetObjectModelRequest = _reflection.GeneratedProtocolMessageType('GetObjectModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTMODELREQUEST,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.GetObjectModelRequest)
  })
_sym_db.RegisterMessage(GetObjectModelRequest)

GetObjectModelResponse = _reflection.GeneratedProtocolMessageType('GetObjectModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTMODELRESPONSE,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.GetObjectModelResponse)
  })
_sym_db.RegisterMessage(GetObjectModelResponse)

UpdateObjectModelRequest = _reflection.GeneratedProtocolMessageType('UpdateObjectModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEOBJECTMODELREQUEST,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.UpdateObjectModelRequest)
  })
_sym_db.RegisterMessage(UpdateObjectModelRequest)

UpdateObjectModelResponse = _reflection.GeneratedProtocolMessageType('UpdateObjectModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEOBJECTMODELRESPONSE,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.UpdateObjectModelResponse)
  })
_sym_db.RegisterMessage(UpdateObjectModelResponse)

DeleteObjectModelRequest = _reflection.GeneratedProtocolMessageType('DeleteObjectModelRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOBJECTMODELREQUEST,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.DeleteObjectModelRequest)
  })
_sym_db.RegisterMessage(DeleteObjectModelRequest)

DeleteObjectModelResponse = _reflection.GeneratedProtocolMessageType('DeleteObjectModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOBJECTMODELRESPONSE,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.DeleteObjectModelResponse)
  })
_sym_db.RegisterMessage(DeleteObjectModelResponse)

FetchAllModelsRequest = _reflection.GeneratedProtocolMessageType('FetchAllModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHALLMODELSREQUEST,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.FetchAllModelsRequest)
  })
_sym_db.RegisterMessage(FetchAllModelsRequest)

FetchAllModelsResponse = _reflection.GeneratedProtocolMessageType('FetchAllModelsResponse', (_message.Message,), {

  'ModelsEntry' : _reflection.GeneratedProtocolMessageType('ModelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FETCHALLMODELSRESPONSE_MODELSENTRY,
    '__module__' : 'objects.models_pb2'
    # @@protoc_insertion_point(class_scope:mruv.objects.FetchAllModelsResponse.ModelsEntry)
    })
  ,
  'DESCRIPTOR' : _FETCHALLMODELSRESPONSE,
  '__module__' : 'objects.models_pb2'
  # @@protoc_insertion_point(class_scope:mruv.objects.FetchAllModelsResponse)
  })
_sym_db.RegisterMessage(FetchAllModelsResponse)
_sym_db.RegisterMessage(FetchAllModelsResponse.ModelsEntry)


DESCRIPTOR._options = None
_FETCHALLMODELSRESPONSE_MODELSENTRY._options = None

_MRUVOBJECTMODELSSERVICE = _descriptor.ServiceDescriptor(
  name='MruVObjectModelsService',
  full_name='mruv.objects.MruVObjectModelsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=983,
  serialized_end=1672,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateObjectModel',
    full_name='mruv.objects.MruVObjectModelsService.CreateObjectModel',
    index=0,
    containing_service=None,
    input_type=_CREATEOBJECTMODELREQUEST,
    output_type=_CREATEOBJECTMODELRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\"\017/v1/objectTypes:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetObjectModel',
    full_name='mruv.objects.MruVObjectModelsService.GetObjectModel',
    index=1,
    containing_service=None,
    input_type=_GETOBJECTMODELREQUEST,
    output_type=_GETOBJECTMODELRESPONSE,
    serialized_options=b'\202\323\344\223\002\031\022\027/v1/objectTypes/{model}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateObjectModel',
    full_name='mruv.objects.MruVObjectModelsService.UpdateObjectModel',
    index=2,
    containing_service=None,
    input_type=_UPDATEOBJECTMODELREQUEST,
    output_type=_UPDATEOBJECTMODELRESPONSE,
    serialized_options=b'\202\323\344\223\002(2#/v1/objectTypes/{object_type.model}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteObjectModel',
    full_name='mruv.objects.MruVObjectModelsService.DeleteObjectModel',
    index=3,
    containing_service=None,
    input_type=_DELETEOBJECTMODELREQUEST,
    output_type=_DELETEOBJECTMODELRESPONSE,
    serialized_options=b'\202\323\344\223\002\031*\027/v1/objectTypes/{model}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchAllModels',
    full_name='mruv.objects.MruVObjectModelsService.FetchAllModels',
    index=4,
    containing_service=None,
    input_type=_FETCHALLMODELSREQUEST,
    output_type=_FETCHALLMODELSRESPONSE,
    serialized_options=b'\202\323\344\223\002\021\022\017/v1/objectTypes',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVOBJECTMODELSSERVICE)

DESCRIPTOR.services_by_name['MruVObjectModelsService'] = _MRUVOBJECTMODELSSERVICE

# @@protoc_insertion_point(module_scope)
