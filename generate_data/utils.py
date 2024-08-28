import os
import json


def write_config(args, save_dir):
  out_fn = "config.json"
  out_fp = os.path.join(save_dir, out_fn)
  with open(out_fp, 'w') as fh:
    json.dump(vars(args), fh)
