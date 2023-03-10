#!/bin/bash

# Usage:
# chmod u+x install-workbench.sh
# sudo ./install-workbench.sh

export DEBIAN_FRONTEND="noninteractive"

R_VERSION="4.2.2"
PYTHON_VERSION="3.11.2"
QUARTO_VERSION="1.2.262"
WORKBENCH_VERSION="rstudio-workbench-2022.12.0-353.pro20-amd64.deb"

echo "# ------------------------------------------------------------------------"
echo "# Installing System Dependencies"
echo "# ------------------------------------------------------------------------"
apt-get update
# Required
apt-get install -y gdebi-core
# Nice to have
apt-get install -y \
    vim \
    tree

echo "# ------------------------------------------------------------------------"
echo "# Installing R"
echo "# ------------------------------------------------------------------------"
curl -O https://cdn.rstudio.com/r/ubuntu-2204/pkgs/r-${R_VERSION}_1_amd64.deb
gdebi -n r-${R_VERSION}_1_amd64.deb
rm r-${R_VERSION}_1_amd64.deb

# Symlink R
ln -s /opt/R/${R_VERSION}/bin/R /usr/local/bin/R
ln -s /opt/R/${R_VERSION}/bin/Rscript /usr/local/bin/Rscript

# Configure R
cat <<EOF > /opt/R/${R_VERSION}/lib/R/etc/Rprofile.site
options(
  repos = c(
    CRAN = "https://packagemanager.rstudio.com/cran/__linux__/jammy/latest",
    RSPM = "https://packagemanager.rstudio.com/cran/__linux__/jammy/latest"
  )
)
EOF

# Install desired packages that will be available everyone
/opt/R/${R_VERSION}/bin/Rscript -e "install.packages(c('pak'))"

echo "# ------------------------------------------------------------------------"
echo "# Installing Python"
echo "# ------------------------------------------------------------------------"
# Install Python
curl -O https://cdn.rstudio.com/python/ubuntu-2204/pkgs/python-${PYTHON_VERSION}_1_amd64.deb
gdebi -n python-${PYTHON_VERSION}_1_amd64.deb
rm python-${PYTHON_VERSION}_1_amd64.deb

# Add python to the PATH
cat <<EOF > /etc/profile.d/python.sh
PATH=/opt/python/${PYTHON_VERSION}/bin:\$PATH
EOF

echo "# ------------------------------------------------------------------------"
echo "# Installing Jupyter"
echo "# ------------------------------------------------------------------------"
/opt/python/${PYTHON_VERSION}/bin/python -m pip install --upgrade pip wheel setuptools
/opt/python/${PYTHON_VERSION}/bin/python -m pip install \
    jupyter \
    jupyterlab \
    rsp_jupyter \
    rsconnect_jupyter \
    workbench_jupyterlab
/opt/python/${PYTHON_VERSION}/bin/jupyter-nbextension install --sys-prefix --py rsp_jupyter
/opt/python/${PYTHON_VERSION}/bin/jupyter-nbextension enable --sys-prefix --py rsp_jupyter
/opt/python/${PYTHON_VERSION}/bin/jupyter-nbextension install --sys-prefix --py rsconnect_jupyter
/opt/python/${PYTHON_VERSION}/bin/jupyter-nbextension enable --sys-prefix --py rsconnect_jupyter
/opt/python/${PYTHON_VERSION}/bin/jupyter-serverextension enable --sys-prefix --py rsconnect_jupyter

echo "# ------------------------------------------------------------------------"
echo "# Installing Quarto"
echo "# ------------------------------------------------------------------------"
mkdir -p /opt/quarto/${QUARTO_VERSION}
curl -o quarto.tar.gz -L https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz
tar -zxvf quarto.tar.gz -C "/opt/quarto/${QUARTO_VERSION}" --strip-components=1
rm quarto.tar.gz

# Symlink quarto
ln -s /opt/quarto/${QUARTO_VERSION}/bin/quarto /usr/local/bin/quarto

echo "# ------------------------------------------------------------------------"
echo "# Installing Workbench"
echo "# ------------------------------------------------------------------------"
curl -O https://download2.rstudio.org/server/jammy/amd64/${WORKBENCH_VERSION}
gdebi -n "$WORKBENCH_VERSION"
rm "$WORKBENCH_VERSION"

# Configure Workbench
cp /etc/rstudio/jupyter.conf /etc/rstudio/default-jupyter.conf

cat << EOF > /etc/rstudio/jupyter.conf
jupyter-exe=/opt/python/${PYTHON_VERSION}/bin/jupyter
notebooks-enabled=1
labs-enabled=1
default-session-cluster=Local
EOF

echo "# ------------------------------------------------------------------------"
echo "# Installation Complete!"
echo "# ------------------------------------------------------------------------"