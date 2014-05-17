
function die()
{
    echo "${@}"
    exit 1
}

# Install MPD, Alsa, and dependencies
sudo apt-get -y update && sudo apt-get -y upgrade || die "CLI FAIL WHALE"
sudo apt-get -y install mpd || die "Could not install mpd"

sudo apt-get -y install libfaad2 libfaad-dev libflac8 libflac-dev libogg0 libogg-dev \
libvorbis0a libvorbis-dev libid3tag0 libid3tag0-dev libmad0 libmad0-dev \
libcue-dev libcue1 libasound2 libasound-dev libasound2-dev \
libao-dev libwavpack-dev libwavpack1 libsamplerate0 \
libsamplerate-dev libmikmod2-dev libmikmod2 libmikmod-dev \
libshout-dev libavformat-dev libavcodec-dev libavutil-dev \
libcurl4-openssl-dev libmms-dev libmms0 alsa-utils \
libtwolame-dev libtwolame0 libmp3lame-dev  ||  die "Could not install dependencies"
  
# Clone soundatron and mpd-configure repos
git clone https://github.com/foundatron/soundatron.git || die "Could not clone soundatron"    
cd soundatron || die "Could not enter directory"
git submodule init && git submodule update || die "Could not add submodule"

#Get python requirements
sudo apt-get -y install python 
virtualenv sound_env  && source sound_env/bin/activate || die "Had trouble setting up the virtualenv"
pip install -r requirements.txt || die "Failed during pip install of requirements"

echo "Success!! To start server, run:" 
echo "'cd soundatron && source sound_env/bin/activate && python manage.py runserver -h 0.0.0.0'"
