elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
            "helium": {"number": 2,
                       "weight": 4.002602,
                       "symbol": "He"}}
helium = elements["helium"]
hydrogen_weight = elements["hydrogen"]["weight"]
print(hydrogen_weight)
oxygen = {"number": 8, "weight": 15.999, "symbol": "O"}
elements["oxygen"] = oxygen
print('elements =', elements)

# Data Structure	Ordered 	Mutable 	Constructor 	Example
# List	            Yes	        Yes	        [ ] or list()	[5.7, 4, 'yes', 5.7]
# Tuple	            Yes	        No	        ( ) or tuple()	(5.7, 4, 'yes', 5.7)
# Set	            No	        Yes	        {}* or set()	{5.7, 4, 'yes'}
# Dictionary	    No	        No**	    { } or dict()	{'Jun': 75, 'Jul': 89}
