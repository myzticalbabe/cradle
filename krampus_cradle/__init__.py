"""CRADLE -- the whole chain behind one command.

The five parts (FLAMING SWORD, defender, REAPER/sentinel, GRIMOIRE/memory, server) ship
inside this package in `tools/`, because cradle.py loads each of them from a real file
path and then calls it. A wheel that carried only `cradle.py` would install a command
whose --doctor reported all five parts absent -- measured on the first build of this
package, which is why the parts live here rather than in a sibling directory.
"""

from .cradle import main

__all__ = ["main"]
__version__ = "0.1.0"
