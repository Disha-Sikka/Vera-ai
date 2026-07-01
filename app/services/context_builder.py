from app.domain.signals import (
    ContextSignals,
    CustomerSignals,
    MerchantSignals,
    TriggerSignals,
)


class ContextBuilder:

    def build(self, merchant, trigger, customer):

        merchant_signals = MerchantSignals()

        trigger_signals = TriggerSignals()

        customer_signals = CustomerSignals()

        return ContextSignals(
            merchant=merchant_signals,
            trigger=trigger_signals,
            customer=customer_signals,
        )