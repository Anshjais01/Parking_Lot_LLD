# Patch CardPayment module: class is named CashPayment in CardPayment.py
from . import CardPayment as _card_mod
if hasattr(_card_mod, 'CashPayment') and not hasattr(_card_mod, 'CardPayment'):
    _card_mod.CardPayment = _card_mod.CashPayment
# Patch CardPayment module: class is named CashPayment in CardPayment.py
from . import CardPayment as _card_mod
if hasattr(_card_mod, 'CashPayment') and not hasattr(_card_mod, 'CardPayment'):
    _card_mod.CardPayment = _card_mod.CashPayment

from .PaymentStrategy import PaymentStrategy
from .CashPayment import CashPayment
from .CardPayment import CashPayment as CardPayment
from .UpiPayment import UpiPayment
from .NetBankingPayment import NetBankingPayment
from .PaymentStrategy import PaymentStrategy
from .CashPayment import CashPayment
from .CardPayment import CashPayment as CardPayment
from .UpiPayment import UpiPayment
from .NetBankingPayment import NetBankingPayment

