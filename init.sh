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
    python -m venv .venv
    .venv/bin/python3 -m pip install --upgrade pip wheel setuptools
    .venv/bin/python3 -m pip install -r "$REQUIREMENTS_TXT"
}

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