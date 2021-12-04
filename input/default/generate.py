#!/usr/bin/env python3

# This script generates the same codeplug as generate.sh
# by running dzcb via the python API

# First round of updates for OR centric codeplug, did not update generate.sh
# K7WXW 12.03.21
# Changes to CodePlugRecipe - set seattledmr to False, add prox.csv, add order.csv

from pathlib import Path
import os

from dzcb.recipe import CodeplugRecipe

cp_dir = Path(__file__).parent
output = Path(os.environ.get("OUTPUT") or (cp_dir / ".." / ".." / "OUTPUT"))

CodeplugRecipe(
    source_pnwdigital=True,
# changed, was True
    source_seattledmr=False,
    source_default_k7abd=True,
# added
    source_k7abd=[(cp_dir / "k7abd")],
#added
    source_repeaterbook_proximity=cp_dir / "prox.csv",
    scanlists_json=cp_dir / "scanlists.json",
#added
    exclude=cp_dir / "exclude.csv",
#added
    order=cp_dir / "order.csv",
    output_farnsworth=cp_dir.glob("md3?0-?hf.json"),
).generate(output / cp_dir.name)
