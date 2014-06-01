#!/usr/bin/env bash
## `soundatron-bootstrap' is a bash script that tries to ease the
## installation of soundatron.
##
##  Copyright (C) 2014 Ryan Small <e.ryan.small@gmail.com>
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
## The script and documentation are published at 
## https://github.com/foundatron/soundatron


## user adaptable paths 
## root directory to store the virtualenv and git repository in
dir_build=$(pwd)
## directory name to store the python virtualenv
dir_virtualenv="sound_env"

## do not change below this
projectname="soundatron"
git_url="https://github.com/foundatron/${projectname}.git"
git_mpdconfigure="mpd-configure"
git_pacapt="pacapt"

path_gitrepo=${dir_build}/${projectname}
path_virtualenv=${dir_build}/${dir_virtualenv}

path_scripts="$(dirname $0)/scripts"
pacapt_path="${path_scripts}/pacapt/pacapt"
cmd_updatepackageslist="${pacapt_path} -Sy"
cmd_install="${pacapt_path} -S"

packageslist_updated=""

function die() {
    printf "error: %s.\n" "$@" 1>&2; 
    printf "will now exit ...\n"  1>&2; 
    exit 1
}

function inform() {
    printf "%s\n" "$@" 1>&2; 
}

function inform_inline() {
    printf "%s" "$@" 1>&2; 
}

function inform_done() {
    printf "done.\n" 1>&2; 
}

function install_package()  {
    ## install package $1
    ## ref: https://wiki.archlinux.org/index.php/Pacman_Rosetta

    package="$1"

    ## update packageslist if needed
    if [[ ! -z ${packageslist_updated} ]]; then
	inform_inline "updating packages list using \`${cmd_updatepackageslist}\` ... "
	res=$(${cmd_updatepackageslist})
	if [[ $? -ne 0 ]]; then
	    die "\`${res}\`"
	else
	    inform_done
	    packageslist_updated=True
	fi 
    fi 

    ## install the package
    inform_inline " - installing package using \`${cmd_install} ${package}\` ... "
    if [[ ${EUID} -ne 0 ]];
	## user is not root; use sudo
	res=$(${cmd_sudo} ${cmd_install} ${package} &>/dev/null)
    else
	## user is root
	res=$(${cmd_install} ${package} &>/dev/null)
    fi 
    if [[ $? -ne 0 ]]; then
	die "\`${res}\`"
    else
	inform_done
    fi

}

function command_not_found() {
    ## install package $2 and check if that resulted in command $1

    cmd="$1"
    package="$2"

	    
    ## cmd was not found, first install package
    res=$(install_package "${package}")
    
    ## check if that worked
    inform_inline " - rechecking for \`${cmd}\` ... "
    cmd=$(which cmd)

    if [[ $? -ne 0 ]]; then
	## command still does not exist, exit with error
	die "still not present"
    else
	## return the command (with path)
	printf "${cmd}"
    fi
}

function init_update_gitsubmodule() {
    ## git init submodule $1 and update it

    ## initialize the git submodule
    git_submodule="${1}"
    inform_inline " - initializing git submodule \`${git_submodule}\` ... "
    res=$(cd ${path_gitrepo} && \
	${cmd_git} submodule init ${git_submodule} &>/dev/null) 
    if [[ $? -ne 0 ]]; then
	die "\`${res}\`"
    else 
	inform_done
    fi 
    
    ## update the git submodule
    inform_inline " - updating git submodule \`${git_submodule}\` ..."
    res=$(cd ${path_gitrepo} && \
	${cmd_git} submodule update ${git_submodule} &>/dev/null)
    if [[ $? -ne 0 ]]; then
	die "\`${res}\`"
    else
	inform_done
    fi 

}

inform "starting $0 ..."

## create the output directory if it does not exit
if [[ ! -d ${dir_build} ]]; then
    inform "creating output directory \`${dir_build}\` ... "
    res=$(mkdir -p ${dir_build})
    [[ $? -ne 0 ]] && \
	die "\`${res}\`" || \
	inform_done
fi 

## exit if directories already exist
if [[ -d ${path_gitrepo} ]]; then
    die "target directory \`${path_gitrepo}\` for git repository already exists"
fi

if [[ -d ${path_virtualenv} ]]; then
    die "target directory \`${path_virtualenv}\` for python virtualenv already exists"
fi

## check for necessary commands and handle approriately

## check if user is root
if [[ ${EUID} -ne 0 ]];
    ## user isn't root, check for sudo
    cmd_sudo=$(which sudo || die "this script assumes you have sudo")
    ## activate sudo in session
    res="$(${cmd_sudo} ls) &>/dev/null"
fi

## aplay is needed for mpd-configure, we might as well check its presense now
cmd_aplay=$(which aplay || command_not_found "aplay" "alsa-utils")

## TODO: mpd is not needed locally when it runs on a different host?
cmd_mpd=$(which mpd || command_not_found "mpd" "mpd")
[[ $? -ne 0 ]] && exit 1;

## TODO: catch 22: no git > no pacapt
cmd_git=$(which git || command_not_found "git" "git")
[[ $? -ne 0 ]] && exit 1;

cmd_virtualenv=$(which virtualenv || \
    command_not_found "virtualenv" "python-virtualenv")
[[ $? -ne 0 ]] && exit 1;

## clone soundatron git repo
inform_inline " - cloning git repository \`${projectname}\` in \`${path_gitrepo}\` ... "
res=$(${cmd_git} clone ${git_url} &>/dev/null)
if [[ $? -ne 0 ]]; then
    die "\`${res}\`"
else
    inform_done
fi

## initialize the mpd-configure git submodule
init_update_gitsubmodule "${git_mpdconfigure}"
## initialize the pacapt git submodule
init_update_gitsubmodule "${git_pacapt}"


## create python virtualenv
inform_inline " - creating python virtualenv \`${dir_virtualenv}\` ... " 
res=$(${cmd_virtualenv} ${dir_virtualenv} &>/dev/null)
if [[ $? -ne 0 ]]; then
    die "\`${res}\`"
else
    inform_done
fi 

## activate the virtualenv by sourcing its activate script
cmd_activate=${dir_virtualenv}/bin/activate
inform_inline " - activating it by sourcing \`${cmd_activate}\` ... "
res=$(source ${cmd_activate})
if [[ $? -ne 0 ]]; then
    die "\`${res}\`"
else
    inform_done
fi 

## install python packages in virtualenv based on requirements in git repo
cmd_pip=${dir_virtualenv}/bin/pip
file_requirements=${projectname}/requirements.txt
inform_inline " - installing \`${file_requirements}\` in virtualenv \`${dir_virtualenv}\` using pip ... "
res=$(${cmd_pip} install -r ${file_requirements} &>/dev/null)
if [[ $? -ne 0 ]]; then
    die "\`${res}\`"
else
    inform_done
fi

inform " * all done, summary:"
inform "   - git repository stored in   : \`${path_gitrepo}\`."
inform "   - web framework installed in : \`${path_virtualenv}\`."
inform "   - to start the web application run the following commands:" 
inform "cd ${path_gitrepo} &&  
source ${path_virtualenv}/bin/activate && 
python manage.py runserver -h 0.0.0.0"

