
# Declaring the Python Function lambda_handler with event paramater
def lambda_handler(event, context):
    message = 'Amigo {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }
