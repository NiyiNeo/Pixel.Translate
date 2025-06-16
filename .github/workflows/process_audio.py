import boto3 
import os
import wave
import time
import json
from pydub import AudioSegment

#Environment Variables for GitHub Secrets
s3_bucket = os.environ['S3_BUCKET']
 

#AWS Clients from GitHub Secrets
session = boto3.session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    region_name=os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')
)
s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')
polly = boto3.client('polly')
translate = boto3.client('translate')


#Call Amazon Transcribe to generate a transcript

#Assign files
input_files = ["pixel.greeting.mp3", "pixel.language.mp3"]
output_files = ["pixel.greeting.wav", "pixel.language.wav"]

for mp3, wav in zip(input_files, output_files):
    sound = AudioSegment.from_mp3(mp3)
    sound.export(wav, format="wav")
    print(f"Converted {mp3} to {wav}")


#Call Amazon Translate to translate Text to target language

#Call Amazon Polly to synthesize translated speech into an audio file


#Upload Objects in S3


