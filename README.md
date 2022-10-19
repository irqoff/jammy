# Ansible for Jammy Jellyfish

Just execute `jammy.sh`:
```
./jammy.sh
```

For run without `jammy.sh`, execute `sudo true && export ANSIBLE_PYTHON_INTERPRETER=${PYENV_VIRTUAL_ENV}/bin/python3` and then `ansible-playbook jammy.yml`

## GPD Pocket 3

![gpd_pocket3](./images/gpd_pocket3.jpg)

Steps:
 * `./jammy.sh`
 * `sudo true && export ANSIBLE_PYTHON_INTERPRETER=${PYENV_VIRTUAL_ENV}/bin/python3`
 * `ansible-playbook jammy.yml -t pocket3 -e pocket3=yes`
 * `reboot`
 * `ansible-playbook jammy.yml -t pocket3 -e pocket3=yes -e pocket3_after_reboot=yes`
