#!/bin/bash

# remove unwanted VSCode extension(s)
sudo code --uninstall-extension eamodio.gitlens

# change default git config to ignore chmod changes and symbolic links
git config core.fileMode false

# change pull to alway rebase to eliminate common git error
git config pull.rebase true

# set up first-run-notice
cp .devcontainer/first-run-notice.txt /workspaces/.codespaces/shared/first-run-notice.txt

# set up dircolors and aliases for consistent terminal experience
cp .devcontainer/.dircolors ~
cp .devcontainer/.bash_aliases ~

# upgrade pip and install required packages
pip install --upgrade pip
pip install pytest
pip install pytest-subtests
pip install pytest-timeout
pip install pylint
