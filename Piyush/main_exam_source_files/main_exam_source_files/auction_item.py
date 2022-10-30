"""Auction Item class."""


class AuctionItem:
    """Auction Item class for storing details of a Auction Item."""

    def __init__(self, name="", bid_price=0, is_vintage=False):
        """Initialise an Auction Item."""
        self.name = name
        self.bid_price = bid_price
        self.is_vintage = is_vintage

    def __str__(self):
        """Return a string representation of a Auction Item."""
        return "{} with highest bid of ${:,.2f} ({})".format(self.name, self.bid_price, "Vintage"
            if self.is_vintage else "Common")

    def __lt__(self, other):
        """Less than, used for sorting Auction Items."""
        return self.bid_price < other.bid_price

    def __repr__(self):
        return f"<<{self.__str__()}>>"
