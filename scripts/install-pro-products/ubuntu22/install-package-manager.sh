#!/bin/bash

# Usage:
# chmod u+x install-package-manager.sh
# sudo ./install-package-manager.sh

export DEBIAN_FRONTEND="noninteractive"

R_VERSION="4.2.2"
PACKAGE_MANAGER_VERSION="rstudio-pm_2022.11.2-18_amd64.deb"

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
echo "# Installing Package Manager"
echo "# ------------------------------------------------------------------------"
curl -O https://cdn.rstudio.com/package-manager/ubuntu22/amd64/${PACKAGE_MANAGER_VERSION}
gdebi -n $PACKAGE_MANAGER_VERSION
rm $PACKAGE_MANAGER_VERSION

# Configure Package Manager
cp /etc/rstudio-pm/rstudio-pm.gcfg /etc/rstudio-pm/default-rstudio-pm.gcfg

cat <<EOF > /etc/rstudio-pm/rstudio-pm.gcfg
[Server]
Address = 
RVersion = /opt/R/${R_VERSION}

[HTTP]
Listen = :4242
EOF

echo "# ------------------------------------------------------------------------"
echo "# Installation Complete!"
echo "# ------------------------------------------------------------------------"