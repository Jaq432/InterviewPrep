# Task: Parse the given input list of strings and output them formatted as shown below

# Input
routes = [
    '/home',
    '/account/account',
    '/account/payments',
    '/account/payments/details',
    '/subscriptions/details',
    '/subscriptions/status'
]

# Output Structure
# 
# - home
# - account
#     - account
#     - payments
#         - details
# - subscriptions
#     - details
#     - status

# This is the data structure we are trying to create
'''
{
    'home': {},
    'account': {
        "account": {}, 
        "payment": {
            "details": {}
            }
        },
    'subscriptions':{
        "details": {},
        "status": {}
    }
}
'''

def routeFormatter(routesList):
    directoryDict = {}
    
    for route in routesList:
        print("Route: " + str(route))
        routeArray = route.split("/")[1:]
        
        current_dict = directoryDict
        
        for subroute in routeArray:
            print("Subroute: " + str(subroute))
            if subroute not in current_dict:
                current_dict[subroute] = {}
            # If the uppermost directory is in the dictionary
            # we want to add subdirectories into its values as a dict
            current_dict = current_dict[subroute]
    
    return directoryDict
    
    
def dictPrint(routes_dict): 
    pass
    
output = routeFormatter(routes)
print(output)

#{'home': {}, 'account': {'account': {}, 'payments': {'details': {}}}, 'subscriptions': {'details': {}, 'status': {}}}




