#!/usr/bin/env python
# -*- coding: utf-8 -*-
from chain import Chain


def main():
    block_chain = Chain()
    for i in range(1, 20):
        block_chain.append_next_block(i)
    print(block_chain)


if __name__ == "__main__":
    main()
