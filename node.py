"""
Author: ZR000X
Dated: 2021-08-03
License: MIT
Source: https://github.com/ZR000X/Nodes
"""

from ordinal import Ordinal


class Node(Ordinal):
    """
    A node is an application of the Ordinal class that adds reasonable features
    """
    def __init__(self, name=None, subordinates=None, calc_rank_on_init=False) -> None:
        super().__init__(subordinates=subordinates, calc_rank_on_init=calc_rank_on_init)
        self.name = name

    # TODO: 
    # - Add the ability for Node to find its roots
    # - Add the ability for Node to derive paths from a Nodes that lead to it (e.g. each of its roots)
    # - Add the ability for Node to save/load itself
    # - Think about the Node using data in interesting ways
    # - Think about the Node having customisable relationships with its subordinates/superiors
    # - Think about what properties should exist on the Ordinal level, which on the Node level