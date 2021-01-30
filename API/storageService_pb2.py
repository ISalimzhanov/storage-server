# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storageService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='storageService.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14storageService.proto\"\x10\n\x0e\x43ontrolRequest\".\n\x0c\x43ontrolReply\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"/\n\rUpdateRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"?\n\x0bUpdateReply\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61pacity\x18\x02 \x01(\x05\"\x1e\n\nGetRequest\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\"8\n\x08GetReply\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"\"\n\rDeleteRequest\x12\x11\n\tfilenames\x18\x01 \x03(\t2\x84\x02\n\x0eStorageService\x12(\n\x04Ping\x12\x0f.ControlRequest\x1a\r.ControlReply\"\x00\x12(\n\x06\x43reate\x12\x0e.UpdateRequest\x1a\x0c.UpdateReply\"\x00\x12\'\n\x05Write\x12\x0e.UpdateRequest\x1a\x0c.UpdateReply\"\x00\x12 \n\x04Read\x12\x0b.GetRequest\x1a\t.GetReply\"\x00\x12(\n\x06\x44\x65lete\x12\x0e.DeleteRequest\x1a\x0c.UpdateReply\"\x00\x12)\n\x05\x43lear\x12\x0f.ControlRequest\x1a\r.ControlReply\"\x00'
)




_CONTROLREQUEST = _descriptor.Descriptor(
  name='ControlRequest',
  full_name='ControlRequest',
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=40,
)


_CONTROLREPLY = _descriptor.Descriptor(
  name='ControlReply',
  full_name='ControlReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ControlReply.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='ControlReply.error', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=88,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='UpdateRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='UpdateRequest.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=137,
)


_UPDATEREPLY = _descriptor.Descriptor(
  name='UpdateReply',
  full_name='UpdateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='UpdateReply.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='UpdateReply.error', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='UpdateReply.capacity', index=2,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=202,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='GetRequest.filename', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=234,
)


_GETREPLY = _descriptor.Descriptor(
  name='GetReply',
  full_name='GetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='GetReply.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='GetReply.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='GetReply.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=292,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filenames', full_name='DeleteRequest.filenames', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=328,
)

DESCRIPTOR.message_types_by_name['ControlRequest'] = _CONTROLREQUEST
DESCRIPTOR.message_types_by_name['ControlReply'] = _CONTROLREPLY
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateReply'] = _UPDATEREPLY
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetReply'] = _GETREPLY
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlRequest = _reflection.GeneratedProtocolMessageType('ControlRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLREQUEST,
  '__module__' : 'storageService_pb2'
  # @@protoc_insertion_point(class_scope:ControlRequest)
  })
_sym_db.RegisterMessage(ControlRequest)

ControlReply = _reflection.GeneratedProtocolMessageType('ControlReply', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLREPLY,
  '__module__' : 'storageService_pb2'
  # @@protoc_insertion_point(class_scope:ControlReply)
  })
_sym_db.RegisterMessage(ControlReply)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'storageService_pb2'
  # @@protoc_insertion_point(class_scope:UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateReply = _reflection.GeneratedProtocolMessageType('UpdateReply', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREPLY,
  '__module__' : 'storageService_pb2'
  # @@protoc_insertion_point(class_scope:UpdateReply)
  })
_sym_db.RegisterMessage(UpdateReply)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'storageService_pb2'
  # @@protoc_insertion_point(class_scope:GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)

GetReply = _reflection.GeneratedProtocolMessageType('GetReply', (_message.Message,), {
  'DESCRIPTOR' : _GETREPLY,
  '__module__' : 'storageService_pb2'
  # @@protoc_insertion_point(class_scope:GetReply)
  })
_sym_db.RegisterMessage(GetReply)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'storageService_pb2'
  # @@protoc_insertion_point(class_scope:DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)



_STORAGESERVICE = _descriptor.ServiceDescriptor(
  name='StorageService',
  full_name='StorageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=331,
  serialized_end=591,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='StorageService.Ping',
    index=0,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='StorageService.Create',
    index=1,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='StorageService.Write',
    index=2,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_UPDATEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='StorageService.Read',
    index=3,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='StorageService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_UPDATEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Clear',
    full_name='StorageService.Clear',
    index=5,
    containing_service=None,
    input_type=_CONTROLREQUEST,
    output_type=_CONTROLREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STORAGESERVICE)

DESCRIPTOR.services_by_name['StorageService'] = _STORAGESERVICE

# @@protoc_insertion_point(module_scope)