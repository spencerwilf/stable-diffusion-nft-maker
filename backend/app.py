from flask import Flask, request, jsonify
import os
import requests

key = '2nsKyD5rYUNqxzdYDBsgnLWcgdECi8Yh3ld5pz0Q7cWcF8Ychs1dOShs6tcE'
app = Flask(__name__)


@app.route('/create-art', methods=['POST'])
def create_art():

    # Retrieve the user's input from the request

    api_url = 'https://stablediffusionapi.com/api/v3/text2img'
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}

    data = {'key': key,
            'prompt': request.json['prompt'],
            'negative-prompt': None,
            'width': '512',
            'height': '512',
            'samples': '1',
            "num_inference_steps": "20",
            "seed": None,
            "guidance_scale": 7.5,
            "webhook": None,
            "track_id": None
            }
    
    print(data)

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        result = response.json()
        # Process the response as needed
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        return(f"Error: {e}")


if __name__ == '__main__':
    app.run(debug=True)