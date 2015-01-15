from neomodel import StructuredRel, FloatProperty, DateTimeProperty, \
    IntegerProperty


class IsNeighbourOf(StructuredRel):
    """
    Defines the relationship between two ``<System>`` objects.

    Attributes:
    distance Float required
        the distance between the two systems in light years
    updated_at DateTime required
        the date/time the relationship was last saved.
    created_at DateTime required
        the date/time the relationship was created. After creation this
        should treated as read-only
    """
    distance = FloatProperty()
    updated_at = DateTimeProperty()
    created_at = DateTimeProperty()


class TradesIn(StructuredRel):
    """
    Defines the relationship between a ``<Station>`` and ``<Commodity>`` object

    Note the sell and buy attributes are named poorly but that's because
    that's the way they're listed in-game.

    The `<sell_price>` attribute is the price the ``<Station>`` will buy the
    ``<Commodity>`` for from a trader. Conversely, The ``buy_price``
    attribute is the price a trader may buy a ``<Commodity>`` from the
    ``<Station>`` at.

    Attributes:
    sell_price (0.0) Float required
        the price the ``<Station>`` will buy the ``<Commodity>`` for
    buy_price (0.0) Float required
        the price the ``<Station>`` will sell the ``<Commodity>`` for
    supply_level (0) Integer required
        the number of units of ``<Commodity>`` the ``<Station>`` has to sell
    demand_level (0) Integer required
        the number of units of ``<Commodity>`` the ``<Station>`` wants to buy
    supply_flag String
        must contain one of 'HIGH', 'MED', 'LOW'
    demand_flag String
        must contain one of 'HIGH', 'MED', 'LOW'
    updated_at DateTime
        the date/time the relationship was last saved
    created_at DateTime required
        the date/time the relationship was created. After creation this
        should treated as read-only
    """
    sell_price = FloatProperty()
    buy_price = FloatProperty()
    supply_level = IntegerProperty()
    demand_level = IntegerProperty()
    updated_at = DateTimeProperty()
    created_at = DateTimeProperty()


class Contains(StructuredRel):
    """
    Defines the relationship between ``<System>`` and ``<Commodity>`` objects

    Attributes:
    created_at DateTime required
        the date/time the relationship was created. After creation this
        should treated as read-only
    """
    created_at = DateTimeProperty()
