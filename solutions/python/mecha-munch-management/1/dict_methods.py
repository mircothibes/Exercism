"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    if not recipe_updates:
        return ideas
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment = {}
    for item in sorted(cart.keys(), reverse=True):
        qty = cart[item]
        info = aisle_mapping.get(item)

        if isinstance(info, (list, tuple)) and len(info) >= 2:
            aisle, refrigerated = info[0], bool(info[1])
        elif isinstance(info, dict):
            aisle = info.get("aisle")
            refrigerated = bool(info.get("refrigerated", False))
        else:
            aisle, refrigerated = None, False

        fulfillment[item] = [qty, aisle, refrigerated]

    return fulfillment


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, info in fulfillment_cart.items():
        if isinstance(info, (list, tuple)) and len(info) >= 1:
            order_qty = int(info[0])
            order_aisle = info[1] if len(info) > 1 else None
            order_refrig = bool(info[2]) if len(info) > 2 else False
        else:
            order_qty = int(info.get("quantity", 0))
            order_aisle = info.get("aisle")
            order_refrig = bool(info.get("refrigerated", False))

        entry = store_inventory.get(item)
        if entry is None:
            store_inventory[item] = [0, order_aisle, order_refrig]
            entry = store_inventory[item]

        current_qty = entry[0]
        current_qty = int(current_qty) if not isinstance(current_qty, str) else 0  # trata "Out of Stock" como 0

        new_qty = current_qty - order_qty
        if new_qty <= 0:
            entry[0] = "Out of Stock"
        else:
            entry[0] = new_qty


    return store_inventory
      
