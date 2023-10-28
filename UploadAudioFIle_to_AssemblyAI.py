import requests
import json
import time
import assemblyai as aai

aai.settings.api_key = f"11795e4483f34fcbafe7fc315900ad36"

transcriber = aai.Transcriber()

audio_url = "C:\\Users\\haris\\Downloads\\Revflac.flac"

#transcript = transcriber.transcribe(audio_url)
base_url = "https://api.assemblyai.com/v2"

headers = {
    "authorization": "11795e4483f34fcbafe7fc315900ad36"
}

with open(audio_url , "rb") as f:
  response = requests.post(base_url + "/upload",
                          headers=headers,
                          data=f)

upload_url = response.json()["upload_url"]
print(upload_url)

'''if transcript.error:
   print(transcript.error)
print(transcript.text)'''
#################################

'''transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
# request parameters where Sentiment Analysis has been enabled
data = {
  "audio_url": audio_url,
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
print(response)

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
'''
