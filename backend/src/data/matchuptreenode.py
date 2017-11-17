from .powerdict import PowerDict


STATE_UNITIALIZED = 1
STATE_NOT_STARTED = 2
STATE_STARTED = 3
STATE_FINISHED = 4


class MatchupTreeNode(PowerDict):

    def __init__(self, id, round, right=None, left=None, next=None,
                 matchup=None, state=STATE_UNITIALIZED):
        node = {}
        node['id'] = id
        node['round'] = round
        node['state'] = state
        node['right'] = right
        node['left'] = left
        node['next'] = next
        node['matchup'] = matchup
        self._data = node
