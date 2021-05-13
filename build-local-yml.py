#!/usr/bin/env python3

import yaml

with open("_config.yml") as f:
    cfg = yaml.safe_load(f)

# change config to be local
cfg["url"] = "http://127.0.0.1:4000"

with open("_config.local.yml", "w") as f:
    yaml.dump(cfg, f)
