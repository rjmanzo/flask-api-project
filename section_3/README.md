# Section 3

In this section we implement five API endpoints for a store. We don't use any database, only a List of stores.

## List Structure

Structure of the stores

``` json

Stores = [

	{
		"name": "the_store",
		"items": [
			"name": "item_1",
			"price": 9.5		
		]
	}
]

## Endpoints 

* GET/store --> Get all the stores. 

* GET/<string:name> --> Get a particular store. The request recive the name as a parameter.

* GET/<string:name/item --> Get all the items from a particular store. The request recive the name as a parameter.

* POST/<string:name> --> Insert a new store. The request recive the name as a parameter.

* POST/<string:name/item --> Insert an Item in a particular store. The request recive the name_store, name_item and the price of the item. 
