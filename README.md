# Elite Dangerous Trading Assistant

This application is an experiment with the graph database [Neo4j][1]. It is not
intended for any serious use but if you are an enthusiast of the game and either
want to help develop it or use it yourself, then please feel free.

At some point, I will add a how-to to this README to demonstrate how to install
the system.

## TO DO

### Code

* decide on neo4j framework - no point in reinventing blah blah...
* add node definitions
    * System
        * name - the name of the system
        * created_at - date/time when the system was added to the database
    * Station
        * name - the name of the station
        * imports - a list of names of commodities that the station imports
        * exports - a list of names of commodities that the station exports
        * prohibited - a list of names of commodities that the station prohibits
        * black_market - boolean whether the station offers a black market
        * rare_goods - boolean whether the station deals in rare goods
        * updated_at date/time when the station was last saved
        * created_at date/time when the station was added to the database
    * Commodity
        * name - the name of the commodity
        * category - the category in which the commodity lies
* add relationship definitions
    * <System> IS_NEIGHBOUR_OF <System>
        * distance - float representing the distance between the two systems in light years
    * <System> CONTAINS <Station>
    * <Station> TRADES_IN <Commodity>
        * sell_price property - the price the <Station> will pay for <Commodity>
        * buy_price property - the price the <Station> will sell <Commodity> for (I know... but as player you can *sell* at the `sell_price` and buy at the `buy_price`)
        * supply_level - how many units of <Commodity> the <Station> has in stock
        * demand_level - how many units of <Commodity> the <Station> wants
        * supply_flag - string containing 'HIGH', 'MED' or 'LOW', or Null
        * demand_flag - string containing 'HIGH', 'MED' or 'LOW', or Null
        * updated_at - date/time updated when saved
        * created_at - date/time set during creation


### Docs

* List Requirements
* Installation
* Usage
* Sphinx API docs


[1]: http://neo4j.com/ "Neo4j website"