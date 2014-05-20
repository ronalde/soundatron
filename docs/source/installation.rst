 Requirements/Dependencies 
 =========================

1. Debian/Ubuntu. 
2. A sound device/card 
3. Installed: `MPD <http://www.musicpd.org/>`_
4. Installed: `ALSA <http://www.alsa-project.org/>`_
5. Installed: `MPD-Configure <https://github.com/ronalde/mpd-configure>`_

Installation 
=====================

The Easy Way
----------------------
Execute the this line and get some coffee.::

    curl -Lo- https://bit.ly/soundatron-bootstrap | bash


Oh god! What did that just do? The bootstrap script...

1. Installs MPD, Alsa and related dependencies
2. Clones the Soundatron, and Mpd-Configure repos
3. Creates a virtualenv
4. Installs the python dependencies from the requirements.txt.

Hard Way
---------------------
Want to all that by hand? Here you go, step by step.

1.  Install the lastest mpd package::

    sudo apt-get install mpd


2. Install the dependencies::

    sudo apt-get install libfaad2 libfaad-dev libflac8 libflac-dev libogg0 libogg-dev \
    libvorbis0a libvorbis-dev libid3tag0 libid3tag0-dev libmad0 libmad0-dev \
    libcue-dev libcue1 libasound2 libasound-dev libasound2-dev \
    libao-dev libwavpack-dev libwavpack1 libsamplerate0 \
    libsamplerate-dev libmikmod2-dev libmikmod2 libmikmod-dev \
    libshout-dev libavformat-dev libavcodec-dev libavutil-dev \
    libcurl4-openssl-dev libmms-dev libmms0 alsa-utils \
    libtwolame-dev libtwolame0 libmp3lame-dev 
   

3. Clone the Soundatron repo to somewhere in your user's home folder::

    git clone https://github.com/foundatron/soundatron.git

     
4. Get the mpd-configure sub-repo set up::

    cd soundatron
    git submodule init
    git submodule update

5. Create and enter a python virtualenv for Soundatron::

    cp virtualenv soundatron_env
    source soundatron_env/bin/activate

6. Install the python requirements::

    pip install -r requirements


7. Start Soundatron::

    python manage.py runserver -h 0.0.0.0 

8. In a browser navigate to that computer's ip address, and the specified port.