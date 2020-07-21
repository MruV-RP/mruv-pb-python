# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: items/items_model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='items/items_model.proto',
  package='mruv',
  syntax='proto3',
  serialized_options=_b('Z#github.com/MruV-RP/mruv-pb-go/items'),
  serialized_pb=_b('\n\x17items/items_model.proto\x12\x04mruv\"\x8b\x01\n\x08ItemType\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x13\n\x0b\x62\x61se_weight\x18\x04 \x01(\x02\x12\x13\n\x0b\x62\x61se_volume\x18\x05 \x01(\x02\x12\x12\n\nmodel_name\x18\x06 \x01(\t\x12\x12\n\nmodel_hash\x18\x07 \x01(\x05\"\x18\n\nItemTypeID\x12\n\n\x02id\x18\x01 \x01(\r\"H\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\r\x12\x14\n\x0citem_type_id\x18\x02 \x01(\r\x12\x0e\n\x06weight\x18\x03 \x01(\x02\x12\x0e\n\x06volume\x18\x04 \x01(\x02\"\x14\n\x06ItemID\x12\n\n\x02id\x18\x01 \x01(\r\"\x91\x01\n\rContainerType\x12\n\n\x02id\x18\x01 \x01(\r\x12\x1e\n\x16\x63ontainer_item_type_id\x18\x02 \x01(\r\x12\x12\n\nmax_number\x18\x03 \x01(\r\x12\x12\n\nmax_volume\x18\x04 \x01(\x02\x12\x12\n\nmax_weight\x18\x05 \x01(\x02\x12\x18\n\x10valid_item_types\x18\x08 \x03(\x03\"\x1d\n\x0f\x43ontainerTypeID\x12\n\n\x02id\x18\x01 \x01(\r\"p\n\tContainer\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0f\n\x07type_id\x18\x02 \x01(\r\x12\x0f\n\x07item_id\x18\x03 \x01(\r\x12\x14\n\x0citems_inside\x18\x04 \x01(\r\x12\x1f\n\x05items\x18\x05 \x03(\x0b\x32\x10.mruv.InsideItem\"\x19\n\x0b\x43ontainerID\x12\n\n\x02id\x18\x01 \x01(\r\"q\n\nInsideItem\x12\x14\n\x0c\x63ontainer_id\x18\x01 \x01(\r\x12\x11\n\x07item_id\x18\x02 \x01(\rH\x00\x12\x1a\n\x04item\x18\x03 \x01(\x0b\x32\n.mruv.ItemH\x00\x12\x10\n\x08position\x18\x04 \x01(\x05\x42\x0c\n\nitem_or_id*\\\n\x0bSortingMode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bWEIGHT_DESC\x10\x01\x12\x0e\n\nWEIGHT_ASC\x10\x02\x12\x0f\n\x0bVOLUME_DESC\x10\x03\x12\x0e\n\nVOLUME_ASC\x10\x04\x42%Z#github.com/MruV-RP/mruv-pb-go/itemsb\x06proto3')
)

_SORTINGMODE = _descriptor.EnumDescriptor(
  name='SortingMode',
  full_name='mruv.SortingMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIGHT_DESC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIGHT_ASC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_DESC', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_ASC', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=732,
  serialized_end=824,
)
_sym_db.RegisterEnumDescriptor(_SORTINGMODE)

SortingMode = enum_type_wrapper.EnumTypeWrapper(_SORTINGMODE)
UNKNOWN = 0
WEIGHT_DESC = 1
WEIGHT_ASC = 2
VOLUME_DESC = 3
VOLUME_ASC = 4



_ITEMTYPE = _descriptor.Descriptor(
  name='ItemType',
  full_name='mruv.ItemType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.ItemType.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.ItemType.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.ItemType.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_weight', full_name='mruv.ItemType.base_weight', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_volume', full_name='mruv.ItemType.base_volume', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='mruv.ItemType.model_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_hash', full_name='mruv.ItemType.model_hash', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=34,
  serialized_end=173,
)


_ITEMTYPEID = _descriptor.Descriptor(
  name='ItemTypeID',
  full_name='mruv.ItemTypeID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.ItemTypeID.id', index=0,
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
  serialized_start=175,
  serialized_end=199,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='mruv.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.Item.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_type_id', full_name='mruv.Item.item_type_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='mruv.Item.weight', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='mruv.Item.volume', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_end=273,
)


_ITEMID = _descriptor.Descriptor(
  name='ItemID',
  full_name='mruv.ItemID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.ItemID.id', index=0,
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
  serialized_start=275,
  serialized_end=295,
)


_CONTAINERTYPE = _descriptor.Descriptor(
  name='ContainerType',
  full_name='mruv.ContainerType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.ContainerType.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='container_item_type_id', full_name='mruv.ContainerType.container_item_type_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_number', full_name='mruv.ContainerType.max_number', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_volume', full_name='mruv.ContainerType.max_volume', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_weight', full_name='mruv.ContainerType.max_weight', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_item_types', full_name='mruv.ContainerType.valid_item_types', index=5,
      number=8, type=3, cpp_type=2, label=3,
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
  serialized_start=298,
  serialized_end=443,
)


_CONTAINERTYPEID = _descriptor.Descriptor(
  name='ContainerTypeID',
  full_name='mruv.ContainerTypeID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.ContainerTypeID.id', index=0,
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
  serialized_start=445,
  serialized_end=474,
)


_CONTAINER = _descriptor.Descriptor(
  name='Container',
  full_name='mruv.Container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.Container.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type_id', full_name='mruv.Container.type_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='mruv.Container.item_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items_inside', full_name='mruv.Container.items_inside', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='mruv.Container.items', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=476,
  serialized_end=588,
)


_CONTAINERID = _descriptor.Descriptor(
  name='ContainerID',
  full_name='mruv.ContainerID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.ContainerID.id', index=0,
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
  serialized_start=590,
  serialized_end=615,
)


_INSIDEITEM = _descriptor.Descriptor(
  name='InsideItem',
  full_name='mruv.InsideItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_id', full_name='mruv.InsideItem.container_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='mruv.InsideItem.item_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item', full_name='mruv.InsideItem.item', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='mruv.InsideItem.position', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
    _descriptor.OneofDescriptor(
      name='item_or_id', full_name='mruv.InsideItem.item_or_id',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=617,
  serialized_end=730,
)

_CONTAINER.fields_by_name['items'].message_type = _INSIDEITEM
_INSIDEITEM.fields_by_name['item'].message_type = _ITEM
_INSIDEITEM.oneofs_by_name['item_or_id'].fields.append(
  _INSIDEITEM.fields_by_name['item_id'])
_INSIDEITEM.fields_by_name['item_id'].containing_oneof = _INSIDEITEM.oneofs_by_name['item_or_id']
_INSIDEITEM.oneofs_by_name['item_or_id'].fields.append(
  _INSIDEITEM.fields_by_name['item'])
_INSIDEITEM.fields_by_name['item'].containing_oneof = _INSIDEITEM.oneofs_by_name['item_or_id']
DESCRIPTOR.message_types_by_name['ItemType'] = _ITEMTYPE
DESCRIPTOR.message_types_by_name['ItemTypeID'] = _ITEMTYPEID
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['ItemID'] = _ITEMID
DESCRIPTOR.message_types_by_name['ContainerType'] = _CONTAINERTYPE
DESCRIPTOR.message_types_by_name['ContainerTypeID'] = _CONTAINERTYPEID
DESCRIPTOR.message_types_by_name['Container'] = _CONTAINER
DESCRIPTOR.message_types_by_name['ContainerID'] = _CONTAINERID
DESCRIPTOR.message_types_by_name['InsideItem'] = _INSIDEITEM
DESCRIPTOR.enum_types_by_name['SortingMode'] = _SORTINGMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ItemType = _reflection.GeneratedProtocolMessageType('ItemType', (_message.Message,), {
  'DESCRIPTOR' : _ITEMTYPE,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.ItemType)
  })
_sym_db.RegisterMessage(ItemType)

ItemTypeID = _reflection.GeneratedProtocolMessageType('ItemTypeID', (_message.Message,), {
  'DESCRIPTOR' : _ITEMTYPEID,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.ItemTypeID)
  })
_sym_db.RegisterMessage(ItemTypeID)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.Item)
  })
_sym_db.RegisterMessage(Item)

ItemID = _reflection.GeneratedProtocolMessageType('ItemID', (_message.Message,), {
  'DESCRIPTOR' : _ITEMID,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.ItemID)
  })
_sym_db.RegisterMessage(ItemID)

ContainerType = _reflection.GeneratedProtocolMessageType('ContainerType', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERTYPE,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.ContainerType)
  })
_sym_db.RegisterMessage(ContainerType)

ContainerTypeID = _reflection.GeneratedProtocolMessageType('ContainerTypeID', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERTYPEID,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.ContainerTypeID)
  })
_sym_db.RegisterMessage(ContainerTypeID)

Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINER,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.Container)
  })
_sym_db.RegisterMessage(Container)

ContainerID = _reflection.GeneratedProtocolMessageType('ContainerID', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERID,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.ContainerID)
  })
_sym_db.RegisterMessage(ContainerID)

InsideItem = _reflection.GeneratedProtocolMessageType('InsideItem', (_message.Message,), {
  'DESCRIPTOR' : _INSIDEITEM,
  '__module__' : 'items.items_model_pb2'
  # @@protoc_insertion_point(class_scope:mruv.InsideItem)
  })
_sym_db.RegisterMessage(InsideItem)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)