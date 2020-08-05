from random import (
    choice,
    randrange,
    sample,
)
from numpy import arange
from datetime import datetime, timedelta
import pytz

utc = pytz.UTC


def create_mock_profile():
    currency = "$"
    account_balance = 0

    credit_card_balance = {}
    transaction_history = {"spend": {}, "deposit": {}}

    mock_profile = {}
    
    return mock_profile
