import requests
import base64
import argparse

url = 'https://texttospeech.googleapis.com/v1/text:synthesize?key='

request = {'audioConfig': {
    'audioEncoding': 'LINEAR16',
    'pitch': 0,
    "speakingRate": 1.1,
    },
    'input': {
        'text': 'Default text'
        },
    'voice': {
        'languageCode': 'en-GB',
        'name': 'en-GB-Wavenet-F'
        }
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', required=True)
    parser.add_argument('--text', '-t', required=True)
    parser.add_argument('--out', '-o', default="output.mp3")
    args = parser.parse_args()
    request["input"]["text"] = args.text
    response = requests.post(url + args.key ,json=request)
    with open(args.out, "wb") as f:
        f.write(base64.b64decode(response.json()["audioContent"]))
