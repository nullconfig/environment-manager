# If not running interactively, don't do anything
[[ $- == *i* ]] || return

[ -n "$PS1" ] && source ~/.bash_profile;

alias ansible='/usr/bin/docker run --rm -it -v ~/.ssh/keys:/root/.ssh/keys -v ${PWD}:/opt/ansible ansible-docker'
