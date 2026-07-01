class ContextStore:
    """
    Stores merchant, trigger and customer contexts.
    """

    def __init__(self):
        self.categories = {}
        self.merchants = {}
        self.customers = {}
        self.triggers = {}

    def reset(self):
        self.categories.clear()
        self.merchants.clear()
        self.customers.clear()
        self.triggers.clear()