import sys
import importlib
import json
import base64
import os

if int(sys.argv[1]) == 0:
    # bytecode
    import cloudpickle as pickleModule
elif int(sys.argv[1]) == 1:
    # srccode
    import codepickle as pickleModule
else:
    exit("Incorrect input")

dir_path = os.path.dirname(os.path.realpath(__file__))
d_folder = os.path.join(dir_path, "deserialize")
sys.path.append(d_folder)
target_mod_str = (sys.argv[2])[:-3] if (sys.argv[2]).endswith('.py') else None
assert(target_mod_str != None)
target_mod = importlib.import_module("deserialize." + target_mod_str)
assert(target_mod != None)
target_classes = dict([(name, cls) for name, cls in target_mod.__dict__.items() if isinstance(cls, type) and name.startswith('Test')])

pickled_file = os.path.join(dir_path, ".tmp/%s.tmp" % (target_mod_str))
with open(pickled_file) as f:
    pickled_obj = json.load(f)

for target_class, cls in target_classes.items():
    o = cls()
    pickled = base64.b64decode(pickled_obj[target_class])
    pickled_func = pickleModule.loads(pickled)
    o.testObj(pickled_func)