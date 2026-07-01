from app.domain.signals import (
    ContextSignals,
    CustomerSignals,
    MerchantSignals,
    TriggerSignals,
)


class ContextBuilder:

    def build(self, merchant, trigger, customer):

        merchant_signal = MerchantSignals()

        sales = merchant.raw_data.get("sales_change", 0)

        if sales < -10:
            merchant_signal.sales_health = "declining"
        elif sales > 10:
            merchant_signal.sales_health = "growing"
        else:
            merchant_signal.sales_health = "stable"

        if merchant.raw_data.get("active_offer", False):
            merchant_signal.offer_quality = "good"
        else:
            merchant_signal.offer_quality = "poor"

        trigger_signal = TriggerSignals(
            seasonal=trigger.raw_data.get("seasonal", False),
            urgency=trigger.raw_data.get("urgency", "medium"),
        )

        customer_signal = CustomerSignals(
            is_repeat=customer.raw_data.get("repeat_customer", False),
            days_since_last_visit=customer.raw_data.get(
                "days_since_last_visit",
                0,
            ),
            consent=customer.raw_data.get("consent", False),
        )

        return ContextSignals(
            merchant=merchant_signal,
            trigger=trigger_signal,
            customer=customer_signal,
        )