# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stake.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stake.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0bstake.proto\"O\n\x05Stake\x12\r\n\x05nonce\x18\x01 \x01(\x03\x12\x13\n\x0bownerPubKey\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x02\x12\x13\n\x0b\x62lockNumber\x18\x04 \x01(\x03\"p\n\tStakeList\x12*\n\x08stakeMap\x18\x01 \x03(\x0b\x32\x18.StakeList.StakeMapEntry\x1a\x37\n\rStakeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x15\n\x05value\x18\x02 \x01(\x0b\x32\x06.Stake:\x02\x38\x01\x42\x1b\n\x17sawtooth.stake.protobufP\x01\x62\x06proto3')
)




_STAKE = _descriptor.Descriptor(
  name='Stake',
  full_name='Stake',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='Stake.nonce', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ownerPubKey', full_name='Stake.ownerPubKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Stake.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blockNumber', full_name='Stake.blockNumber', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=94,
)


_STAKELIST_STAKEMAPENTRY = _descriptor.Descriptor(
  name='StakeMapEntry',
  full_name='StakeList.StakeMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='StakeList.StakeMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='StakeList.StakeMapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=208,
)

_STAKELIST = _descriptor.Descriptor(
  name='StakeList',
  full_name='StakeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stakeMap', full_name='StakeList.stakeMap', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STAKELIST_STAKEMAPENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=208,
)

_STAKELIST_STAKEMAPENTRY.fields_by_name['value'].message_type = _STAKE
_STAKELIST_STAKEMAPENTRY.containing_type = _STAKELIST
_STAKELIST.fields_by_name['stakeMap'].message_type = _STAKELIST_STAKEMAPENTRY
DESCRIPTOR.message_types_by_name['Stake'] = _STAKE
DESCRIPTOR.message_types_by_name['StakeList'] = _STAKELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Stake = _reflection.GeneratedProtocolMessageType('Stake', (_message.Message,), dict(
  DESCRIPTOR = _STAKE,
  __module__ = 'stake_pb2'
  # @@protoc_insertion_point(class_scope:Stake)
  ))
_sym_db.RegisterMessage(Stake)

StakeList = _reflection.GeneratedProtocolMessageType('StakeList', (_message.Message,), dict(

  StakeMapEntry = _reflection.GeneratedProtocolMessageType('StakeMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _STAKELIST_STAKEMAPENTRY,
    __module__ = 'stake_pb2'
    # @@protoc_insertion_point(class_scope:StakeList.StakeMapEntry)
    ))
  ,
  DESCRIPTOR = _STAKELIST,
  __module__ = 'stake_pb2'
  # @@protoc_insertion_point(class_scope:StakeList)
  ))
_sym_db.RegisterMessage(StakeList)
_sym_db.RegisterMessage(StakeList.StakeMapEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027sawtooth.stake.protobufP\001'))
_STAKELIST_STAKEMAPENTRY.has_options = True
_STAKELIST_STAKEMAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)