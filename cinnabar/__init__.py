"""
cinnabar
Report results for free energy simualtions
"""


# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions

# import 
from .plotlying import *
from .plotting import *
from .stats import *
from .wrangle import *