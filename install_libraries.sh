#!/usr/bin/env bash

setupBackend() {
  # Crear directorio si no existe
  mkdir -p "$HOME/mineria/UNIVAP/omni"
  cd "$HOME/mineria/UNIVAP/omni" || exit 1

  echo "--------------------------- Creating virtual environment ----------------------"
  python3 -m venv --clear entorno_omni || {
    echo "Failed to create virtual environment";
    exit 1;
  }

  echo "--------------------------- Activating environment ---------------------------"
  source entorno_omni/bin/activate || {
    echo "Failed to activate virtual environment";
    exit 1;
  }

  echo "--------------------------- Upgrading pip ------------------------------------"
  python -m ensurepip --upgrade
  python -m pip install --upgrade pip --user || {
    echo "Failed to upgrade pip";
    exit 1;
  }

  echo "----------------------- Installing dependencies ------------------------------"
  python -m pip install -r requirements.txt --user || {
    echo "Failed to install dependencies";
    exit 1;
  }

  echo "----------------------- Running Omni Data Retrieve -------------------------"
  python omni_data_downloader.py
}

setupBackend
