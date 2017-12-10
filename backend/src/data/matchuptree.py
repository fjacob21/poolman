from .matchuptreenode import MatchupTreeNode, STATE_UNITIALIZED
from .powerdict import PowerDict


def create_matchup_tree():
    return MatchupTree()


class MatchupTree(PowerDict):

    def __init__(self):
        self._data = {}
        self._on_matchup_finished = None
        self._on_round_finished = None

    def create_node(self, id, round, right=None, left=None, next=None,
                    matchup=None, state=STATE_UNITIALIZED):
        self._data[id] = MatchupTreeNode(id, round, right, left, next,
                                         matchup, state)

    def update_node_links(self, id, right=None, left=None, next=None):
        if right:
            self._data[id]['right'] = right
        if left:
            self._data[id]['left'] = left
        if next:
            self._data[id]['next'] = next

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        raise AttributeError("Invalid node id: '" + key + "'")

    def __contains__(self, key):
        return key in self._data

    def __getattr__(self, key):
        return self._data[key]

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            raise AttributeError("Invalid node id: '" + name + "'")
        else:
            return object.__setattr__(self, name, value)
