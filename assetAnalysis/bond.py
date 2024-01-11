from asset import Asset
import datetime

'''
Bonds: Loans that can be obtained from the market.

Characteristics:
- Periodic Interest Payments
- Principal Amount (amount borrowed)

Quotes Include:
- Coupon rate
- Maturity Date
- YTM
'''

class Bond(Asset):
    def __init__(self, name):
        # super constructor
        super().__init__(name)
        # fields
        self.principal = 0.00
        self.coupon_rate = 0.00
        self.interest_payment = 0.00
        self.purchase_date = datetime.date.now()
        self.maturity_date = datetime.datetime.now()

    # calculate interest_payment
    def set_principal(new_amount):
        self.principal = new_amount