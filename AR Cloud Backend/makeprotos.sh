#!/bin/sh

src_dir=./protos
dst_dir=./src
all=*

python -m grpc_tools.protoc -I=$src_dir --python_out=$dst_dir --grpc_python_out=$dst_dir $src_dir/*
