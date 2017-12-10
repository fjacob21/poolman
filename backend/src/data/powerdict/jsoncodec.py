import json
from .powerdict import PowerDict
import sys


class PowerDictEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, PowerDict):
            result = obj.data
            result['__objectname__'] = type(obj).__name__
            return result
        return json.JSONEncoder.default(self, obj)


class PowerDictDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        self._pack =  sys.modules[__name__]
        if 'pack' in kwargs:
            self._pack = kwargs['pack']
        json.JSONDecoder.__init__(self, object_hook=self.object_hook)  # ,
        # *args, **kwargs)

    def object_hook(self, obj):
        if '__objectname__' not in obj:
            return obj
        type = obj['__objectname__']
        newobjclass = getattr(self._pack, type)  # globals()[type]()
        newobj = newobjclass()
        newobj._data = obj
        del newobj._data['__objectname__']
        return newobj
