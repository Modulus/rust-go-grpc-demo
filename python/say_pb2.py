# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: say.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='say.proto',
  package='say',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tsay.proto\x12\x03say\"-\n\x0cSayerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\"=\n\rSayerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\x05\x32\x36\n\x05Sayer\x12-\n\x04Send\x12\x11.say.SayerRequest\x1a\x12.say.SayerResponseb\x06proto3'
)




_SAYERREQUEST = _descriptor.Descriptor(
  name='SayerRequest',
  full_name='say.SayerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='say.SayerRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment', full_name='say.SayerRequest.comment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=18,
  serialized_end=63,
)


_SAYERRESPONSE = _descriptor.Descriptor(
  name='SayerResponse',
  full_name='say.SayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='say.SayerResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment', full_name='say.SayerResponse.comment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='say.SayerResponse.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=65,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['SayerRequest'] = _SAYERREQUEST
DESCRIPTOR.message_types_by_name['SayerResponse'] = _SAYERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SayerRequest = _reflection.GeneratedProtocolMessageType('SayerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAYERREQUEST,
  '__module__' : 'say_pb2'
  # @@protoc_insertion_point(class_scope:say.SayerRequest)
  })
_sym_db.RegisterMessage(SayerRequest)

SayerResponse = _reflection.GeneratedProtocolMessageType('SayerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAYERRESPONSE,
  '__module__' : 'say_pb2'
  # @@protoc_insertion_point(class_scope:say.SayerResponse)
  })
_sym_db.RegisterMessage(SayerResponse)



_SAYER = _descriptor.ServiceDescriptor(
  name='Sayer',
  full_name='say.Sayer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=128,
  serialized_end=182,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='say.Sayer.Send',
    index=0,
    containing_service=None,
    input_type=_SAYERREQUEST,
    output_type=_SAYERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SAYER)

DESCRIPTOR.services_by_name['Sayer'] = _SAYER

# @@protoc_insertion_point(module_scope)
