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
    sys.exit("Incorrect input")

pickled_obj = {}

dir_path = os.path.dirname(os.path.realpath(__file__))
s_folder = os.path.join(dir_path, "serialize")
sys.path.append(s_folder)
target_mod_str = (sys.argv[2])[:-3] if (sys.argv[2]).endswith('.py') else None
assert(target_mod_str != None)
target_mod = importlib.import_module("serialize." + target_mod_str)
assert(target_mod != None)
target_classes = dict([(name, cls) for name, cls in target_mod.__dict__.items() if isinstance(cls, type) and name.startswith('Test')])

pickled_file = os.path.join(dir_path, ".tmp/%s.tmp" % (target_mod_str))
open(pickled_file, "w+").close() # Clear the file

for target_class, cls in target_classes.items():
    o = cls()
    target_function = o.getFunction()
    bin_obj = pickleModule.dumps(target_function)
    pickled_obj[target_class] = base64.b64encode(bin_obj).decode("utf-8")
    # Test after serialization to prevent alterting of global variables.
    o.testObj(target_function)

with open(pickled_file, 'w') as f:
    json.dump(pickled_obj, f)