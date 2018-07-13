#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as date
import hashlib as hasher


class Block:
    def __init__(self, block_header, block_body):
        self.block_header = block_header
        self.block_body = block_body

    def str_block(self):
        return '''%s
---------------------------
''' % (self.block_header.str_lock_header() + self.block_body.str_block_body())

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(bytes(self.str_block()))
        return sha.hexdigest()

    def generate_next_block(self, data):
        index = self.block_header.index + 1
        time_stamp = date.datetime.now()
        previous_hash = self.hash_block()
        this_block_header = BlockHeader(index, time_stamp, previous_hash)
        this_block_body = BlockBody(data)
        return Block(this_block_header, this_block_body)

    @classmethod
    def create_genesis_block(cls):
        return Block(
            BlockHeader(0, date.datetime.now(), "Genesis Block"),
            BlockBody("Genesis Block")
        )


class BlockHeader:
    def __init__(self, index, time_stamp, previous_hash):
        self.index = index
        self.time_stamp = time_stamp
        self.previous_hash = previous_hash

    def str_lock_header(self):
        return '''区块头：
    编号：%s
    时间戳：%s
    第一个区块的Hash值：%s
''' % (str(self.index), str(self.time_stamp), str(self.previous_hash))


class BlockBody:
    def __init__(self, data):
        self.data = data

    def str_block_body(self):
        return '''区块数据：
    %s''' % str(self.data)
