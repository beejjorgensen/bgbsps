# Beej's Guide Build System for Python-Sphinx

Dependencies:

* xelatex (can be found in TeXLive)
* python-sphinx
* python3

## Example Usage

In the Guide directory, add the following files. Modify the variables to
suit.

**Makefile**

```
TODO
```

**src/Makefile**

```
GUIDE_ID=bggit
BGBSPS_DIR?=../../bgbsps  # where this build system lives

export BGBSPS_DIR
export BGBSPS_DIR

include $(BGBSPS_DIR)/source.make
```
**src/conf.py**

```
project = "Beej's Guide to Git"
copyright = 'Copyright © July 9, 2024'
author = 'Brian "Beej Jorgensen" Hall'
release = '0.0.5'

import os
with open(os.sep.join((os.getenv('BGBSPS_DIR'), 'common-conf.py'))) as f: exec(f.read(), globals())
```

