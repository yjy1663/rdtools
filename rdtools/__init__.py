from normalization import normalize_with_sapm
from normalization import normalize_with_pvwatts
from degradation import degradation_ols
from degradation import degradation_classical_decomposition
from degradation import degradation_year_on_year
from aggregation import aggregation_insol
from clearsky_temperature import get_clearsky_tamb
from filtering import csi_filter

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
