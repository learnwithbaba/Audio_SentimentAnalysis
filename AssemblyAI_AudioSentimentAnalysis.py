import requests
import json
import time

# replace with your API token
YOUR_API_TOKEN = "11795e4483f34fcbafe7fc315900ad36"

# URL of the file to transcribe
FILE_URL = "https://cdn.assemblyai.com/upload/bb7ee17a-6b24-4ce1-9215-55d67401a957"
#FILE_URL = "gs://audiotranscription_pib/Rev(1).mp3"

# AssemblyAI transcript endpoint (where we submit the file)
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

# request parameters where Sentiment Analysis has been enabled
data = {
  "audio_url": FILE_URL,
  "sentiment_analysis": True
}

# HTTP request headers
headers={
  "Authorization": '11795e4483f34fcbafe7fc315900ad36',
  "Content-Type": "application/json"
}

# submit for transcription via HTTP request
response = requests.post(transcript_endpoint,
                         json=data,
                         headers=headers)

# polling for transcription completion
polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{response.json()['id']}"

while True:
    transcription_result = requests.get(polling_endpoint, headers=headers).json()

    if transcription_result['status'] == 'completed':
        # print the results
        print(json.dumps(transcription_result, indent=2))
        break
    elif transcription_result['status'] == 'error':
        raise RuntimeError(f"Transcription failed: {transcription_result['error']}")
    else:
        time.sleep(3)