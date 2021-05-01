# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cai/pb/im/msg/msg/msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cai.pb.im.msg.common import common_pb2 as cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2
from cai.pb.im.msg.msg_body import msg_body_pb2 as cai_dot_pb_dot_im_dot_msg_dot_msg__body_dot_msg__body__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cai/pb/im/msg/msg/msg.proto',
  package='im.msg.msg',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x63\x61i/pb/im/msg/msg/msg.proto\x12\nim.msg.msg\x1a!cai/pb/im/msg/common/common.proto\x1a%cai/pb/im/msg/msg_body/msg_body.proto\"\x7f\n\x03\x43\x32\x43\x12#\n\x06sender\x18\x01 \x01(\x0b\x32\x13.im.msg.common.User\x12%\n\x08receiver\x18\x02 \x01(\x0b\x32\x13.im.msg.common.User\x12,\n\x0b\x63\x32\x43Relation\x18\x03 \x01(\x0b\x32\x17.im.msg.msg.C2CRelation\"p\n\x0b\x43\x32\x43Relation\x12\x0f\n\x07\x63\x32\x43Type\x18\x01 \x01(\r\x12+\n\tgroupInfo\x18\x02 \x01(\x0b\x32\x18.im.msg.common.GroupInfo\x12#\n\x05token\x18\x03 \x01(\x0b\x32\x14.im.msg.common.Token\"\xb2\x01\n\x0b\x43ontentHead\x12\x0e\n\x06pkgNum\x18\x01 \x01(\r\x12\x10\n\x08pkgIndex\x18\x02 \x01(\r\x12\x0b\n\x03seq\x18\x03 \x01(\r\x12\x10\n\x08\x64\x61teTime\x18\x04 \x01(\r\x12\x0c\n\x04type\x18\x05 \x01(\r\x12\x0e\n\x06\x64ivSeq\x18\x06 \x01(\r\x12\x10\n\x08msgdbUin\x18\x07 \x01(\x04\x12\x10\n\x08msgdbSeq\x18\x08 \x01(\r\x12\x12\n\nwordMsgSeq\x18\t \x01(\r\x12\x0c\n\x04rand\x18\n \x01(\r\"\x80\x01\n\x05Group\x12#\n\x06sender\x18\x01 \x01(\x0b\x32\x13.im.msg.common.User\x12%\n\x08receiver\x18\x02 \x01(\x0b\x32\x13.im.msg.common.User\x12+\n\tgroupInfo\x18\x03 \x01(\x0b\x32\x18.im.msg.common.GroupInfo\"P\n\x03Msg\x12!\n\x04head\x18\x01 \x01(\x0b\x32\x13.im.msg.msg.MsgHead\x12&\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x18.im.msg.msg_body.MsgBody\"|\n\x07MsgHead\x12,\n\x0broutingHead\x18\x01 \x01(\x0b\x32\x17.im.msg.msg.RoutingHead\x12,\n\x0b\x63ontentHead\x18\x02 \x01(\x0b\x32\x17.im.msg.msg.ContentHead\x12\x15\n\rgbkTmpMsgBody\x18\x03 \x01(\x0c\"n\n\nMsgSendReq\x12\x1c\n\x03msg\x18\x01 \x01(\x0b\x32\x0f.im.msg.msg.Msg\x12\r\n\x05\x62uMsg\x18\x02 \x01(\x0c\x12\x0e\n\x06tailId\x18\x03 \x01(\r\x12\x13\n\x0b\x63onnMsgFlag\x18\x04 \x01(\r\x12\x0e\n\x06\x63ookie\x18\x05 \x01(\x0c\"\r\n\x0bMsgSendResp\"M\n\x0bRoutingHead\x12\x1c\n\x03\x63\x32\x43\x18\x01 \x01(\x0b\x32\x0f.im.msg.msg.C2C\x12 \n\x05group\x18\x02 \x01(\x0b\x32\x11.im.msg.msg.Group'
  ,
  dependencies=[cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2.DESCRIPTOR,cai_dot_pb_dot_im_dot_msg_dot_msg__body_dot_msg__body__pb2.DESCRIPTOR,])




_C2C = _descriptor.Descriptor(
  name='C2C',
  full_name='im.msg.msg.C2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='im.msg.msg.C2C.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='im.msg.msg.C2C.receiver', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='c2CRelation', full_name='im.msg.msg.C2C.c2CRelation', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=244,
)


_C2CRELATION = _descriptor.Descriptor(
  name='C2CRelation',
  full_name='im.msg.msg.C2CRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2CType', full_name='im.msg.msg.C2CRelation.c2CType', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupInfo', full_name='im.msg.msg.C2CRelation.groupInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='im.msg.msg.C2CRelation.token', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=358,
)


_CONTENTHEAD = _descriptor.Descriptor(
  name='ContentHead',
  full_name='im.msg.msg.ContentHead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pkgNum', full_name='im.msg.msg.ContentHead.pkgNum', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pkgIndex', full_name='im.msg.msg.ContentHead.pkgIndex', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seq', full_name='im.msg.msg.ContentHead.seq', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dateTime', full_name='im.msg.msg.ContentHead.dateTime', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='im.msg.msg.ContentHead.type', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='divSeq', full_name='im.msg.msg.ContentHead.divSeq', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msgdbUin', full_name='im.msg.msg.ContentHead.msgdbUin', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msgdbSeq', full_name='im.msg.msg.ContentHead.msgdbSeq', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wordMsgSeq', full_name='im.msg.msg.ContentHead.wordMsgSeq', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rand', full_name='im.msg.msg.ContentHead.rand', index=9,
      number=10, type=13, cpp_type=3, label=1,
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
  serialized_start=361,
  serialized_end=539,
)


_GROUP = _descriptor.Descriptor(
  name='Group',
  full_name='im.msg.msg.Group',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='im.msg.msg.Group.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='im.msg.msg.Group.receiver', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupInfo', full_name='im.msg.msg.Group.groupInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=670,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='im.msg.msg.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='head', full_name='im.msg.msg.Msg.head', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='im.msg.msg.Msg.body', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=672,
  serialized_end=752,
)


_MSGHEAD = _descriptor.Descriptor(
  name='MsgHead',
  full_name='im.msg.msg.MsgHead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='routingHead', full_name='im.msg.msg.MsgHead.routingHead', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contentHead', full_name='im.msg.msg.MsgHead.contentHead', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gbkTmpMsgBody', full_name='im.msg.msg.MsgHead.gbkTmpMsgBody', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=754,
  serialized_end=878,
)


_MSGSENDREQ = _descriptor.Descriptor(
  name='MsgSendReq',
  full_name='im.msg.msg.MsgSendReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='im.msg.msg.MsgSendReq.msg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buMsg', full_name='im.msg.msg.MsgSendReq.buMsg', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tailId', full_name='im.msg.msg.MsgSendReq.tailId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connMsgFlag', full_name='im.msg.msg.MsgSendReq.connMsgFlag', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cookie', full_name='im.msg.msg.MsgSendReq.cookie', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=880,
  serialized_end=990,
)


_MSGSENDRESP = _descriptor.Descriptor(
  name='MsgSendResp',
  full_name='im.msg.msg.MsgSendResp',
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
  serialized_start=992,
  serialized_end=1005,
)


_ROUTINGHEAD = _descriptor.Descriptor(
  name='RoutingHead',
  full_name='im.msg.msg.RoutingHead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2C', full_name='im.msg.msg.RoutingHead.c2C', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='im.msg.msg.RoutingHead.group', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1007,
  serialized_end=1084,
)

_C2C.fields_by_name['sender'].message_type = cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2._USER
_C2C.fields_by_name['receiver'].message_type = cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2._USER
_C2C.fields_by_name['c2CRelation'].message_type = _C2CRELATION
_C2CRELATION.fields_by_name['groupInfo'].message_type = cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2._GROUPINFO
_C2CRELATION.fields_by_name['token'].message_type = cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2._TOKEN
_GROUP.fields_by_name['sender'].message_type = cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2._USER
_GROUP.fields_by_name['receiver'].message_type = cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2._USER
_GROUP.fields_by_name['groupInfo'].message_type = cai_dot_pb_dot_im_dot_msg_dot_common_dot_common__pb2._GROUPINFO
_MSG.fields_by_name['head'].message_type = _MSGHEAD
_MSG.fields_by_name['body'].message_type = cai_dot_pb_dot_im_dot_msg_dot_msg__body_dot_msg__body__pb2._MSGBODY
_MSGHEAD.fields_by_name['routingHead'].message_type = _ROUTINGHEAD
_MSGHEAD.fields_by_name['contentHead'].message_type = _CONTENTHEAD
_MSGSENDREQ.fields_by_name['msg'].message_type = _MSG
_ROUTINGHEAD.fields_by_name['c2C'].message_type = _C2C
_ROUTINGHEAD.fields_by_name['group'].message_type = _GROUP
DESCRIPTOR.message_types_by_name['C2C'] = _C2C
DESCRIPTOR.message_types_by_name['C2CRelation'] = _C2CRELATION
DESCRIPTOR.message_types_by_name['ContentHead'] = _CONTENTHEAD
DESCRIPTOR.message_types_by_name['Group'] = _GROUP
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['MsgHead'] = _MSGHEAD
DESCRIPTOR.message_types_by_name['MsgSendReq'] = _MSGSENDREQ
DESCRIPTOR.message_types_by_name['MsgSendResp'] = _MSGSENDRESP
DESCRIPTOR.message_types_by_name['RoutingHead'] = _ROUTINGHEAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2C = _reflection.GeneratedProtocolMessageType('C2C', (_message.Message,), {
  'DESCRIPTOR' : _C2C,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.C2C)
  })
_sym_db.RegisterMessage(C2C)

C2CRelation = _reflection.GeneratedProtocolMessageType('C2CRelation', (_message.Message,), {
  'DESCRIPTOR' : _C2CRELATION,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.C2CRelation)
  })
_sym_db.RegisterMessage(C2CRelation)

ContentHead = _reflection.GeneratedProtocolMessageType('ContentHead', (_message.Message,), {
  'DESCRIPTOR' : _CONTENTHEAD,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.ContentHead)
  })
_sym_db.RegisterMessage(ContentHead)

Group = _reflection.GeneratedProtocolMessageType('Group', (_message.Message,), {
  'DESCRIPTOR' : _GROUP,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.Group)
  })
_sym_db.RegisterMessage(Group)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.Msg)
  })
_sym_db.RegisterMessage(Msg)

MsgHead = _reflection.GeneratedProtocolMessageType('MsgHead', (_message.Message,), {
  'DESCRIPTOR' : _MSGHEAD,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.MsgHead)
  })
_sym_db.RegisterMessage(MsgHead)

MsgSendReq = _reflection.GeneratedProtocolMessageType('MsgSendReq', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDREQ,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.MsgSendReq)
  })
_sym_db.RegisterMessage(MsgSendReq)

MsgSendResp = _reflection.GeneratedProtocolMessageType('MsgSendResp', (_message.Message,), {
  'DESCRIPTOR' : _MSGSENDRESP,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.MsgSendResp)
  })
_sym_db.RegisterMessage(MsgSendResp)

RoutingHead = _reflection.GeneratedProtocolMessageType('RoutingHead', (_message.Message,), {
  'DESCRIPTOR' : _ROUTINGHEAD,
  '__module__' : 'cai.pb.im.msg.msg.msg_pb2'
  # @@protoc_insertion_point(class_scope:im.msg.msg.RoutingHead)
  })
_sym_db.RegisterMessage(RoutingHead)


# @@protoc_insertion_point(module_scope)
