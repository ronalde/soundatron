# Soundatron 

Soundatron is a small flask app that helps you configure your bit perfect MPD server. Soundatron is targeted at little arm computers like the [RaspberyPi](http://www.raspberrypi.org/) and [BeagleBone Black](http://beagleboard.org/Products/BeagleBone%20Black) boards, but will probably run on anything that meets the [requirements](#requirements).

Soundatron has been tested on the following device OS combos:

1. Beaglebone Black - [Debian Wheezy 7.4](http://beagleboard.org/latest-images)
1. Raspberry PI - [Raspian](http://www.raspberrypi.org/downloads/)
1. And my laptop, a Lenovo E220s - Ubuntu 13.10

Soundatron works because [mpd-configure](https://github.com/ronalde/mpd-configure) works. Check it out.


## What does Soundatron do?
Not much! and that's the way we like it. 

Soundatron does two things:

1. It allows you to configure a small subset of MPD settings.
  * Sound device
  * Music directory
  * Zeroconf Name

2. It creates and applies a new mpd.conf with settings that enable your device to be a bit perfect music server.

![screenshot](https://raw.githubusercontent.com/foundatron/soundatron/master/soundatron.png)

## What it isn't...
1. It isn't a MPD client. You will stell need one those to use your server. [Link](http://www.musicpd.org/clients/)
1. It isn't ready for prime time. Don't run this on a machine that has anything on it that you love or hold dear.
1. It isn't secure. Soundatron does some pretty funny stuff with your password right now. Only use it behind a firewall and don't tell anyone about it.

## Requirements/Dependencies 
1. Debian/Ubuntu. 
2. A sound device/card 
3. Installed: [MPD](http://www.musicpd.org/) 
4. Installed: [Alsa](http://www.alsa-project.org/)
5. Installed: [MPD-Configure](https://github.com/ronalde/mpd-configure)

## Installation 

### The Easy Way
Execute the this line and get some coffee.

```bash
curl -Lo- https://bit.ly/soundatron-bootstrap | bash
```

Oh god! What did that just do? The bootstrap script...

1. Installs MPD, Alsa and related dependencies
2. Clones the Soundatron, and Mpd-Configure repos
3. Creates a virtualenv
4. Installs the python dependencies from the requirements.txt.

### Hard Way
Want to all that by hand? Here you go, step by step.

1.  Install the lastest mpd package.

   ```bash
   sudo apt-get install mpd
   ```

2. Install the dependencies

   ```bash
   sudo apt-get install libfaad2 libfaad-dev libflac8 libflac-dev libogg0 libogg-dev \
   libvorbis0a libvorbis-dev libid3tag0 libid3tag0-dev libmad0 libmad0-dev \
   libcue-dev libcue1 libasound2 libasound-dev libasound2-dev \
   libao-dev libwavpack-dev libwavpack1 libsamplerate0 \
   libsamplerate-dev libmikmod2-dev libmikmod2 libmikmod-dev \
   libshout-dev libavformat-dev libavcodec-dev libavutil-dev \
   libcurl4-openssl-dev libmms-dev libmms0 alsa-utils \
   libtwolame-dev libtwolame0 libmp3lame-dev 
   ```

3. Clone the Soundatron repo to somewhere in your user's home folder

    ```bash
    git clone https://github.com/foundatron/soundatron.git
    ```
     
4. Get the mpd-configure sub-repo set up

    ```bash
    cd soundatron
    git submodule init
    git submodule update
    ```
5. Create and enter a python virtualenv for Soundatron

   ```bash
   virtualenv soundatron_env
   source soundatron_env/bin/activate
   ````

6. Install the python requirements

   ```bash
   pip install -r requirements
   ```

7. Start Soundatron 

   ```bash
   python manage.py runserver -h 0.0.0.0 
   ```

8. In a browser navigate to that computer's ip address, and the specified port.
