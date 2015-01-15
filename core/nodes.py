from neomodel import StructuredNode, StringProperty, DateTimeProperty, \
    ArrayProperty, BooleanProperty, RelationshipTo, Relationship, \
    RelationshipFrom
from core import rel_types
from core.relationships import Contains, IsNeighbourOf, TradesIn


class Commodity(StructuredNode):
    """
    Defines goods that can be sold or bought from Stations.

    Note: Not all commodities can be found at all Stations.
    """
    name = StringProperty()
    category = StringProperty()
    updated_at = DateTimeProperty()
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

    system = RelationshipFrom('System', rel_type=rel_types.CONTAINS,
                              model=Contains)
    market = RelationshipTo('Commodity', rel_type=rel_types.TRADES_IN,
                            model=TradesIn)


class System(StructuredNode):
    """
    Represents a star system. We only need the name and date/time that it was
    created

    NEIGHBOURS System objects
    CONTAINS Station objects
    """
    name = StringProperty()
    created_at = DateTimeProperty()

    stations = RelationshipTo('Station', rel_type=rel_types.CONTAINS,
                              model=Contains)
    neighbours = Relationship('System', rel_type=rel_types.IS_NEIGHBOUR_OF,
                              model=IsNeighbourOf)

