#!/usr/bin/env python3

# This script generates the same codeplug as generate.sh
# by running dzcb via the python API

# First round of updates for OR centric codeplug,
# K7WXW 12.03.21
# Changes to CodePlugRecipe - add exclude, comment out seattledmr, default_k7abd,
# repeaterbook_proximity, scanlists, order.  This should product a codeplug based 
# only on pnwdigital and the exclude list

from pathlib import Path
import os

from dzcb.recipe import CodeplugRecipe

cp_dir = Path(__file__).parent
output = Path(os.environ.get("OUTPUT") or (cp_dir / ".." / ".." / "OUTPUT"))

CodeplugRecipe(
    source_pnwdigital=True,
#   source_seattledmr=True,
#   source_default_k7abd=True,
#   source_k7abd=[(cp_dir / "k7abd")],
#   source_repeaterbook_proximity=cp_dir / "prox.csv",
#   scanlists_json=cp_dir / "scanlists.json",
#added
    exclude=cp_dir / "exclude.csv",
#   order=cp_dir / "order.csv",
    output_farnsworth=cp_dir.glob("md3?0-?hf.json"),
).generate(output / cp_dir.name)
