from __future__ import unicode_literals
from .version import __version__
import pyximport
pyximport.install()
from .quicksectx import Interval, IntervalNode, IntervalTree, distancex
