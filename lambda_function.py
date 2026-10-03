
def lambda_handler(event, context):
    # 1. Extract the slots from the Lex V2 event
    slots = event['sessionState']['intent']['slots']
    
    room_type = slots['RoomType']['value']['interpretedValue']
    check_in = slots['CheckInDate']['value']['interpretedValue']
    # Convert nights to an integer for math calculation
    nights = int(slots['Nights']['value']['interpretedValue'])
    
    # 2. Define the room prices dictionary
    prices = {
        "classic": 1000,
        "deluxe": 2000,
        "duplex": 3500,
        "suite": 5000
    }
    
    # 3. Calculate total price (default to 1000 if room type isn't matched)
    base_price = prices.get(room_type.lower(), 1000)
    total_price = base_price * nights
    
    # 4. Create the final fulfillment message fulfilling your project requirements
    message = f"Success! Your {room_type} room is confirmed for {nights} night(s) starting on {check_in}. Your total price to be paid at the hotel is ₹{total_price}."
    
    # 5. Return the exact JSON format Amazon Lex V2 expects
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": event['sessionState']['intent']['name'],
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message
            }
        ]
    }
