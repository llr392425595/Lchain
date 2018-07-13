#!/usr/bin/env python
# -*- coding: utf-8 -*-
from block import Block, BlockHeader


class Chain:
    def __init__(self):
        self.genesis_block = Block.create_genesis_block()
        self.block_list = [self.genesis_block]

    def __str__(self):
        return ''.join(i.str_block() for i in self.block_list)

    def append_next_block(self, data):
        last_block = self.block_list[-1]
        self.block_list.append(last_block.generate_next_block(data))
