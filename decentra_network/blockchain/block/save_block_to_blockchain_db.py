#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from decentra_network.accounts.get_accounts import GetAccounts
from decentra_network.accounts.save_accounts import SaveAccounts
from decentra_network.blockchain.block.save_block import SaveBlock
from decentra_network.blockchain.block.blocks_hash import GetBlockshash
from decentra_network.blockchain.block.blocks_hash import SaveBlockshash
from decentra_network.blockchain.block.blocks_hash import GetBlockshash_part
from decentra_network.blockchain.block.blocks_hash import SaveBlockshash_part
from decentra_network.config import BLOCKS_PATH
from decentra_network.wallet.wallet_import import wallet_import


def SaveBlockstoBlockchainDB(
    block,
    custom_BLOCKS_PATH=None,
    custom_TEMP_ACCOUNTS_PATH=None,
    custom_TEMP_BLOCKSHASH_PATH=None,
    custom_TEMP_BLOCKSHASH_PART_PATH=None,
):
    """
    Adds the block to the blockchain database
    at BLOCKS_PATH.
    """

    my_public_key = "".join(
        [
            l.strip()
            for l in wallet_import(-1, 0).splitlines()
            if l and not l.startswith("-----")
        ]
    )
    my_address = wallet_import(-1, 3)
    our_tx = any(
        (validated_transaction.fromUser == my_public_key)
        or (validated_transaction.toUser == my_address)
        for validated_transaction in block.validating_list
    )

    # If the block is our transaction, then add it to the blockchain database.
    if our_tx:
        the_BLOCKS_PATH = (
            BLOCKS_PATH if custom_BLOCKS_PATH is None else custom_BLOCKS_PATH
        )
        SaveBlock(block, (the_BLOCKS_PATH + str(block.sequance_number) + ".block.json"))
        SaveAccounts(
            GetAccounts(custom_TEMP_ACCOUNTS_PATH=custom_TEMP_ACCOUNTS_PATH),
            (the_BLOCKS_PATH + str(block.sequance_number) + ".accounts.json"),
        )
        SaveBlockshash(
            GetBlockshash(custom_TEMP_BLOCKSHASH_PATH=custom_TEMP_BLOCKSHASH_PATH),
            (the_BLOCKS_PATH + str(block.sequance_number) + ".blockshash.json"),
        )
        SaveBlockshash_part(
            GetBlockshash_part(
                custom_TEMP_BLOCKSHASH_PART_PATH=custom_TEMP_BLOCKSHASH_PART_PATH
            ),
            (the_BLOCKS_PATH + str(block.sequance_number) + ".blockshashpart.json"),
        )

    else:
        False