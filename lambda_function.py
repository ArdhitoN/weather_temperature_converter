import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):
    
    request_body = json.loads(event.get('body'))

    city = request_body['city']
    ec2_url = os.environ.get("WEATHER_SERVICE_API")
    response = requests.post(ec2_url, json={"city": city})
    data = response.json()

    celsius = float(data['temperature'].replace("°C", ""))
    fahrenheit = (celsius * 9/5) + 32
    
    return {
        "city": data['city'],
        "temperature": f"{fahrenheit}°F",
        "condition": data['condition']
    }
    
    