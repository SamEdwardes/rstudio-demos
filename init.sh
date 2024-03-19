#!/bin/env bash
#
# A shell script to bootstrap the environments for demos.
#
# Usage:
# /bin/bash bootstrap.sh

export DEBIAN_FRONTEND='noninteractive'
set -o nounset
set -e
PROJECT_ROOT=$(pwd)

heading() {
    echo ""
    echo "====================================================================="
    echo "# $1"
    echo "====================================================================="
}

create_venv() {
    REQUIREMENTS_TXT="$1"
    uv venv
    uv pip install -r "$REQUIREMENTS_TXT"
}

install_pipx() {
    /opt/python/3.11.6/bin/python -m pip install pipx
    ~/.local/bin/pipx ensurepath
}

install_uv() {
    heading "Installing uv"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
}

install_zsh() {
    heading "Installing zsh"
    wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
    mkdir zsh && unxz zsh.tar.xz && tar -xvf zsh.tar -C zsh --strip-components 1
    cd zsh
}

install_starship () {
    heading "Installing starship"
    wget --no-verbose --directory-prefix '/tmp' https://github.com/starship/starship/releases/download/v1.17.1/starship-x86_64-unknown-linux-musl.tar.gz
    tar --directory ~/.local/bin -zxf /tmp/starship-x86_64-unknown-linux-musl.tar.gz
    echo 'eval "$(~/.local/bin/starship init bash)"' >> ~/.bashrc
}


# ------------------------------------------------------------------------------
# Install CLI tools
# ------------------------------------------------------------------------------
mkdir -p ~/.local/bin

install_pipx
install_uv
install_starship


# ------------------------------------------------------------------------------
# Applications
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/applications/dash-multi-page-penguins/using-dash-pages"
heading "$(pwd)"
create_venv "requirements.txt"

cd "$PROJECT_ROOT/applications/dash-multi-page-penguins/using-dcc-location"
heading "$(pwd)"
create_venv "requirements.txt"

cd "$PROJECT_ROOT/applications/dash-penguins"
heading "$(pwd)"
create_venv "app/requirements.txt"

cd "$PROJECT_ROOT/applications/shiny-for-r-with-reticulate"
heading "$(pwd)"
create_venv "requirements.txt"

cd "$PROJECT_ROOT/applications/streamlit-penguins"
heading "$(pwd)"
create_venv "app/requirements.txt"

# ------------------------------------------------------------------------------
# Dcouments
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/documents/jupyter-python-penguins"
heading "$(pwd)"
create_venv "requirements.txt"

# cd "$PROJECT_ROOT/documents/jupyter-using-ray"
# heading "$(pwd)"
# create_venv "requirements.txt"

# ------------------------------------------------------------------------------
# APIs
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/apis/fastapi-penguins"
heading "$(pwd)"
create_venv "app/requirements.txt"

cd "$PROJECT_ROOT/apis/fastapi-whoami"
heading "$(pwd)"
create_venv "requirements.txt"

cd "$PROJECT_ROOT/apis/flask-webapp"
heading "$(pwd)"
create_venv "requirements.txt"

# cd "$PROJECT_ROOT/apis/vetiver-train-and-deploy-python"
# heading "$(pwd)"
# create_venv "requirements.txt"