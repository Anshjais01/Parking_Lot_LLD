# Patch the PaymentStatus module: ensure PaymentStatus exists and has PENDING
from . import PaymentStatus as _ps_mod
if hasattr(_ps_mod, 'PaymentaMode') and not hasattr(_ps_mod, 'PaymentStatus'):
    _ps_mod.PaymentStatus = _ps_mod.PaymentaMode

_ps_class = getattr(_ps_mod, 'PaymentStatus', None) or getattr(_ps_mod, 'PaymentaMode', None)
if _ps_class and not hasattr(_ps_class, 'PENDING'):
    _ps_class.PENDING = getattr(_ps_class, 'PENDIG', 'PENDING')

from . import GateType as _gate_mod
_gate_mod.GateType.ENTRY = "ENTRY"

from . import PricingStrategyType as _pst_mod
_pst_mod.PricingStrategyType = _pst_mod.PriceStrategyType

from . import PaymentMode as _pm_mod
if not hasattr(_pm_mod.PaymentMode, 'NETBANKING'):
    _pm_mod.PaymentMode.NETBANKING = "NETBANKING"

# Re-export enum classes so `from ..enums import VehicleType` gets the CLASS
# (not the module), matching the import pattern used in Car.py, Bike.py, etc.
from .VehicleType import VehicleType
from .GateType import GateType
from .PaymentMode import PaymentMode
PaymentStatus = _ps_class
from .PricingStrategyType import PriceStrategyType, PriceStrategyType as PricingStrategyType
