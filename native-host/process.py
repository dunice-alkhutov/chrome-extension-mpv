from subprocess import Popen, DEVNULL

def play(data):
    if data['type'] in ['youtube', 'twitch']:
        Popen(['mpv', data['url']], stdout=DEVNULL, stderr=DEVNULL)
