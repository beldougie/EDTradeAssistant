from neomodel import StructuredNode, StringProperty, DateTimeProperty, \
    ArrayProperty, BooleanProperty


class Commodity(StructuredNode):
    """
    Represents a commodity that can be sold at any Station

    Note: Not all commodities can be found at all stations.
    """
    name = StringProperty()
    category = StringProperty()
    created_at = DateTimeProperty()


class Station(StructuredNode):
    """
    Represents a station within a System.

    TRADES_IN Commodity objects
    """
    name = StringProperty()
    imports = ArrayProperty()
    exports = ArrayProperty()
    prohibited = ArrayProperty()
    black_market = BooleanProperty()
    rare_goods = BooleanProperty()
    updated_at = DateTimeProperty()
    created_at = DateTimeProperty()


class System(StructuredNode):
    """
    Represents a star system. We only need the name and date/time that it was
    created

    NEIGHBOURS System objects
    CONTAINS Station objects
    """
    name = StringProperty()
    created_at = DateTimeProperty()

