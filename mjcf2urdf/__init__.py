# flake8: noqa

import pkg_resources


__version__ = pkg_resources.get_distribution("mjcf2urdf").version


from mjcf2urdf.makedirs import makedirs
from mjcf2urdf.core import convert_mjcf_to_urdf
