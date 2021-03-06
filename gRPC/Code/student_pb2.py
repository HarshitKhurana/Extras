# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: student.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='student.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstudent.proto\"$\n\x07student\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x63ls\x18\x02 \x01(\x05\"\x1e\n\tstudentId\x12\x11\n\tstudentId\x18\x01 \x01(\x05\x32\x86\x01\n\x0fStudentRegistry\x12$\n\naddStudent\x12\x08.student\x1a\n.studentId\"\x00\x12$\n\ngetStudent\x12\n.studentId\x1a\x08.student\"\x00\x12\'\n\rremoveStudent\x12\n.studentId\x1a\x08.student\"\x00\x62\x06proto3'
)




_STUDENT = _descriptor.Descriptor(
  name='student',
  full_name='student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='student.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cls', full_name='student.cls', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=53,
)


_STUDENTID = _descriptor.Descriptor(
  name='studentId',
  full_name='studentId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='studentId', full_name='studentId.studentId', index=0,
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
  serialized_start=55,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['student'] = _STUDENT
DESCRIPTOR.message_types_by_name['studentId'] = _STUDENTID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

student = _reflection.GeneratedProtocolMessageType('student', (_message.Message,), {
  'DESCRIPTOR' : _STUDENT,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:student)
  })
_sym_db.RegisterMessage(student)

studentId = _reflection.GeneratedProtocolMessageType('studentId', (_message.Message,), {
  'DESCRIPTOR' : _STUDENTID,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:studentId)
  })
_sym_db.RegisterMessage(studentId)



_STUDENTREGISTRY = _descriptor.ServiceDescriptor(
  name='StudentRegistry',
  full_name='StudentRegistry',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=88,
  serialized_end=222,
  methods=[
  _descriptor.MethodDescriptor(
    name='addStudent',
    full_name='StudentRegistry.addStudent',
    index=0,
    containing_service=None,
    input_type=_STUDENT,
    output_type=_STUDENTID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getStudent',
    full_name='StudentRegistry.getStudent',
    index=1,
    containing_service=None,
    input_type=_STUDENTID,
    output_type=_STUDENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='removeStudent',
    full_name='StudentRegistry.removeStudent',
    index=2,
    containing_service=None,
    input_type=_STUDENTID,
    output_type=_STUDENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STUDENTREGISTRY)

DESCRIPTOR.services_by_name['StudentRegistry'] = _STUDENTREGISTRY

# @@protoc_insertion_point(module_scope)
