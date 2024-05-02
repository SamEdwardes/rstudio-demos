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
# Python - Applications
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/applications/dash-multi-page-penguins/using-dash-pages"
heading "$(pwd)"
create_venv "requirements.txt"
.venv/bin/rsconnect deploy dash --new --title "Python App - Dash - Multipage (using Dash pages)" --python .venv/bin/python --entrypoint app:app .

cd "$PROJECT_ROOT/applications/dash-multi-page-penguins/using-dcc-location"
heading "$(pwd)"
create_venv "requirements.txt"
.venv/bin/rsconnect deploy dash --new --title "Python App - Dash Multipage (using dcc)" --python .venv/bin/python --entrypoint app:app .

cd "$PROJECT_ROOT/applications/dash-penguins"
heading "$(pwd)"
create_venv "app/requirements.txt"
.venv/bin/rsconnect deploy dash --new --title "Python App - Dash - Pengins" --python .venv/bin/python --entrypoint app:app app


cd "$PROJECT_ROOT/applications/streamlit-penguins"
heading "$(pwd)"
create_venv "app/requirements.txt"
.venv/bin/rsconnect deploy streamlit --new --title "Python App - Streamlit - Penguins" --python .venv/bin/python --entrypoint app app

# ------------------------------------------------------------------------------
# R - Applications
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/applications/shiny-for-r-with-reticulate"
heading "$(pwd)"
create_venv "requirements.txt"
Rscript -e 'rsconnect::deployApp(appFiles = c("app.R", "requirements.txt"), forceUpdate = TRUE, appTitle = "R App - Reticulate Shiny App")'

cd "$PROJECT_ROOT/applications/shiny-penguins"
heading "$(pwd)"
Rscript -e 'rsconnect::deployApp(appDir = "app", appFiles = c("app.R"), forceUpdate = TRUE, appTitle = "R App - Shiny - Penguins")'

# ------------------------------------------------------------------------------
# Python - Dcouments
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/documents/jupyter-python-penguins"
heading "$(pwd)"
create_venv "requirements.txt"
.venv/bin/rsconnect deploy notebook --new --title "Python Notebook - Jupyter Notebook - Penguins" --python .venv/bin/python notebook.ipynb

# cd "$PROJECT_ROOT/documents/jupyter-using-ray"
# heading "$(pwd)"
# create_venv "requirements.txt"

# ------------------------------------------------------------------------------
# R - Dcouments
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/documents/quarto-colorado-report"
heading "$(pwd)"
Rscript -e 'renv::restore(repos = "https://packagemanager.posit.co/cran/__linux__/jammy/latest")'
# Rscript -e 'renv::install("rsconnect"); rsconnect::deployApp(appDir = ".", appPrimaryDoc = "colorado-report.qmd")'

# ------------------------------------------------------------------------------
# Python - APIs
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/apis/fastapi-penguins"
heading "$(pwd)"
create_venv "requirements.txt"
.venv/bin/rsconnect deploy fastapi --new --title "Python API - Fast API - Penguins" --python .venv/bin/python --entrypoint app:app .

cd "$PROJECT_ROOT/apis/fastapi-whoami"
heading "$(pwd)"
create_venv "requirements.txt"
.venv/bin/rsconnect deploy fastapi --new --title "Python API - Fast API - whoami" --python .venv/bin/python --entrypoint app:app .

cd "$PROJECT_ROOT/apis/flask-webapp"
heading "$(pwd)"
create_venv "requirements.txt"
.venv/bin/rsconnect deploy api --new --title "Python App - Flask - Web App" --entrypoint "app.app:app" --python ".venv/bin/python" .

# cd "$PROJECT_ROOT/apis/vetiver-train-and-deploy-python"
# heading "$(pwd)"
# create_venv "requirements.txt"

# ------------------------------------------------------------------------------
# R - APIs
# ------------------------------------------------------------------------------
cd "$PROJECT_ROOT/apis/plumber-penguins"
heading "$(pwd)"
Rscript -e 'renv::restore(repos = "https://packagemanager.posit.co/cran/__linux__/jammy/latest")'
Rscript -e 'renv::install("rsconnect"); rsconnect::deployAPI(api = "app", appFiles = c("plumber.R"), appTitle = "R API - Plumber - Penguins Data", forceUpdate = TRUE)'