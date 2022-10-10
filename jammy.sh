#!/bin/bash

set -o errexit -o nounset -o xtrace

source ~/jammy/ansible.sh

cd ~/jammy && ansible-playbook jammy.yml --skip-tags linuxbrew_packages

set +o nounset
source "${HOME}/.bashrc_${USER}"
set -o nounset

ansible-playbook jammy.yml -t linuxbrew_packages

set +o errexit +o nounset +o xtrace
