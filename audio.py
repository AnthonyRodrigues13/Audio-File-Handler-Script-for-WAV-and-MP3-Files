#!/usr/bin/python3

import cgi
import os
import sys
import base64

# Set the path to the audio file
audio_file_path = "path"

# Check if the audio file is not present
if (audio_file_path == "File Not Present"):
    print("Content-type: text/html\r\n\r\n")
    print("Status: \n")
    print("Recording Not Available.")

else:
    # Extract file name and extension
    fn = os.path.basename(audio_file_path)
    ex = fn.split('.')

    # Check if the file exists
    if os.path.exists(audio_file_path):
        # Check the file extension
        if ex[-1] == 'wav':
            # If it's a WAV file
            with open(audio_file_path, 'rb') as wav_file:
                audio_content = wav_file.read()

            # Check if the file is a valid WAV file
            if audio_content.startswith(b'RIFF') and b'WAVEfmt' in audio_content:
                sys.stdout.buffer.write(f"Content-Type: audio/wav\r\n".encode())
                # sys.stdout.buffer.write(f"Content-Disposition: attachment; filename=\"audio-{userid}.wav\"\r\n".encode())
                sys.stdout.buffer.write(f"Content-Disposition: inline; filename=\"audio-{userid}.wav\"\r\n".encode())
                sys.stdout.buffer.write(f"Content-Length: {len(audio_content)}\r\n".encode())
                sys.stdout.buffer.write(b"\r\n")
                sys.stdout.buffer.write(audio_content)
            else:
                print("Content-type: text/html\r\n\r\n")
                print("Status: 500 Internal Server Error\n")
                print("Invalid WAV file format.")
        elif ex[-1] == "mp3":
            # If it's an MP3 file
            with open(audio_file_path, 'rb') as mp3_file:
                audio_content = mp3_file.read()

            sys.stdout.buffer.write(f"Content-Type: audio/mpeg3\r\n".encode())
            sys.stdout.buffer.write(f"Content-Disposition: attachment; filename=\"audio-{userid}.mp3\"\r\n".encode())
            sys.stdout.buffer.write(f"Content-Length: {len(audio_content)}\r\n".encode())
            sys.stdout.buffer.write(b"\r\n")
            sys.stdout.buffer.write(audio_content)
        else:
            print("Content-type: text/html\r\n\r\n")
            print(f"Status: 500 Internal Server Error No file {fn} \n")
            print("Invalid file format.")
    else:
        print("Content-type: text/html\r\n\r\n")
        print("Status: \n")
        print("Recording Not Available.")

