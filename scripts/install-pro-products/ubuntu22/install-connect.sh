#!/bin/bash

# Usage:
# chmod u+x install-connect.sh
# sudo ./install-connect.sh

export DEBIAN_FRONTEND="noninteractive"

R_VERSION="4.2.2"
PYTHON_VERSION="3.11.2"
QUARTO_VERSION="1.2.262"
CONNECT_VERSION="rstudio-connect_2023.01.1~ubuntu22_amd64.deb"

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

echo "# ------------------------------------------------------------------------"
echo "# Installing Python"
echo "# ------------------------------------------------------------------------"
# Install Python
curl -O https://cdn.rstudio.com/python/ubuntu-2204/pkgs/python-${PYTHON_VERSION}_1_amd64.deb
gdebi -n python-${PYTHON_VERSION}_1_amd64.deb
rm python-${PYTHON_VERSION}_1_amd64.deb

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
echo "# Installing Connect"
echo "# ------------------------------------------------------------------------"
curl -O https://cdn.rstudio.com/connect/2023.01/${CONNECT_VERSION}
gdebi -n "$CONNECT_VERSION"
rm "$CONNECT_VERSION"

# Configure Connect
cp /etc/rstudio-connect/rstudio-connect.gcfg /etc/rstudio-connect/default-rstudio-connect.gcfg

cat <<EOF > /etc/rstudio-connect/rstudio-connect.gcfg
[HTTP]
Listen = ":3939"

[Authentication]
Provider = "password"

[RPackageRepository "CRAN"]
URL = "https://packagemanager.rstudio.com/cran/__linux__/jammy/latest"

[RPackageRepository "RSPM"]
URL = "https://packagemanager.rstudio.com/cran/__linux__/jammy/latest"

[R]
Enabled = true
ExecutableScanning = false
Executable = /shared/R/${R_VERSION}/bin/R

[Python]
Enabled = true
Executable = /shared/Python/${PYTHON_VERSION}/bin/python3

[Quarto]
Enabled = true
Executable = "/usr/local/bin/quarto"
EOF

echo "# ------------------------------------------------------------------------"
echo "# Installation Complete!"
echo "# ------------------------------------------------------------------------"