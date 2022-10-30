"""CP1404 Auctions Question."""

from auction_item import AuctionItem
from random import choice

def main():
    with open("./auction_data.txt", "r", encoding="utf-8") as auction_data:
        data = []
        vintage_count = 0
        for auction_item in auction_data.readlines():
            is_vintage = False
            if auction_item.strip().endswith('+'):
                vintage_count+=1
                auction_item = auction_item[: len(auction_item)-2]
                is_vintage = True

            name, bid = auction_item.split(",")
            auction_item_obj = AuctionItem(name = name.strip(), \
                bid_price=int(bid.strip()), is_vintage=is_vintage)

            data.append(auction_item_obj)
    print(f"You have {len(data)} auction items ({vintage_count} vintage).")
    print(f"The highest bid for your items is ${round(max(data).bid_price, 2)}")
    print("Today's random auction item starred is:")
    print(choice(data))

main()