#!/usr/bin/env python3
import struct
import sys
import json
from process import play

# Function to send a message to chrome.


def send_message(msg):
    # Converts dictionary into string containing JSON format.I
    msg_json = json.dumps(msg, separators=(",", ":"))
    # Encodes string with UTF-8.
    msg_json_utf8 = msg_json.encode("utf-8")
    # Writes the message size. (Writing to buffer because writing bytes
    # object.)
    sys.stdout.buffer.write(struct.pack("i", len(msg_json_utf8)))
    # Writes the message itself. (Writing to buffer because writing bytes
    # object.)
    sys.stdout.buffer.write(msg_json_utf8)


# Function to read a message from Chrome.
def read_message():
    f = open('debug.log', 'w')
    # Reads the first 4 bytes of the message (which designates message length).
    text_length_bytes = sys.stdin.buffer.read(4)
    f.write('readed 4 bytes: {}'.format(text_length_bytes))
    # Unpacks the first 4 bytes that are the message length. [0] required
    # because unpack returns tuple with required data at index 0.
    text_length = struct.unpack("i", text_length_bytes)[0]
    # Reads and decodes the text (which is JSON) of the message.
    text_decoded = sys.stdin.buffer.read(text_length).decode("utf-8")
    f.write('decoded {}'.format(text_decoded))
    # Converts the message string into a dictionary.
    text_dict = json.loads(text_decoded)
    f.write('parsed {}'.format(text_dict))
    # Returns the dictionary.
    f.close()
    return text_dict


if __name__ == '__main__':
    data = read_message()
    resp = dict(msg='not finished', code=-1)
    if data.get('type') and data.get('url'):
        play(data)
        resp = dict(msg='ok', code=1)
    send_message(resp)
