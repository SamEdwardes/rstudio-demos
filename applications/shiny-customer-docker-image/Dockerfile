FROM ubuntu:18.04

LABEL maintainer="Sam Edwardes <sam.edwardes@posit.co>"

ARG DEBIAN_FRONTEND=noninteractive

# Locale configuration --------------------------------------------------------#
RUN apt-get update \
    && apt-get install -y --no-install-recommends locales \
    && localedef -i en_US -f UTF-8 en_US.UTF-8 \
    && rm -rf /var/lib/apt/lists/*
	
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ARG DEBIAN_FRONTEND=noninteractive

# Installation prerequisites --------------------------------------------------#
# curl is used to download things.
# libev-dev is required for most interactive Python applications.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      curl \
      libev-dev \
    && rm -rf /var/lib/apt/lists/*

# System dependencies needed by popular R packages ----------------------------#
# https://docs.rstudio.com/rsc/post-setup-tool/#install-system-dependencies
# Now, install the system requirements for R packages.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      default-jdk \
      gdal-bin \
      git \
      gsfonts \
      imagemagick \
      libcairo2-dev \
      libcurl4-openssl-dev \
      libfontconfig1-dev \
      libfreetype6-dev \
      libfribidi-dev \
      libgdal-dev \
      libgeos-dev \
      libgl1-mesa-dev \
      libglpk-dev \
      libglu1-mesa-dev \
      libgmp3-dev \
      libharfbuzz-dev \
      libicu-dev \
      libjpeg-dev \
      libmagick++-dev \
      libmysqlclient-dev \
      libpng-dev \
      libpq-dev \
      libproj-dev \
      libsodium-dev \
      libssh2-1-dev \
      libssl-dev \
      libtiff-dev \
      libudunits2-dev \
      libv8-dev \
      libicu-dev \
      libxml2-dev \
      make \
      perl \
      tcl \
      tk \
      tk-dev \
      tk-table \
      unixodbc-dev \
      zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install R -------------------------------------------------------------------#
# Reference: https://docs.rstudio.com/resources/install-r/
# We are NOT linking one of these R versions into the PATH.
ARG R_DISTRIBUTION=ubuntu-1804
ARG R_VERSION=4.1.3
ARG R_INSTALLER=r-${R_VERSION}_1_amd64.deb

RUN curl -fsSL -O https://cdn.rstudio.com/r/${R_DISTRIBUTION}/pkgs/${R_INSTALLER} \
    && apt-get update \
    && apt-get install -f -y --no-install-recommends ./${R_INSTALLER} \
    && rm ${R_INSTALLER} \
    && rm -rf /var/lib/apt/lists/*

# Install the pdftools system dependencies ------------------------------------#
# https://docs.ropensci.org/pdftools/
RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository -y ppa:cran/poppler \
  && apt-get update \
  && apt-get install -y libpoppler-cpp-dev \
  && rm -rf /var/lib/apt/lists/*
  