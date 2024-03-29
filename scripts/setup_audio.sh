#!/bin/bash

# install MPEG-4 AAC decoder to play mp3s
apt install -y gstreamer1.0-plugins-bad

# ensure the system audio settings match the user audio settings
ln -s ~/.asoundrc /etc/asound.conf

# Install mopidy
mkdir -p /etc/apt/keyrings
wget -q -O /etc/apt/keyrings/mopidy-archive-keyring.gpg https://apt.mopidy.com/mopidy.gpg
wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/bullseye.list
apt update
apt install -y mopidy

# install mpd + client
apt install -y mopidy-mpd mpc

# configure mopidy (audio out and media folder)
echo "[audio]
output = alsasink

[file]
media_dirs =
  /home/pi/pixiebox/data/audio/
" > /etc/mopidy/mopidy.conf

# enable mopidy to run as a service, start it and print status
systemctl enable mopidy
systemctl start mopidy
systemctl status mopidy

# set volume to 65%
amixer set PCM 65%
