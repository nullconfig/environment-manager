#!/usr/bin/env python3

'''
This script creates symlinks from the home directory 
to any desired dotfiles in homedir/dotfiles, 
and also installs Homebrew Packages.
'''
import argparse, os
from os import path

from environment_manager.environment_manager import PackageManager as pm
from environment_manager.environment_manager import DotfileManager as dm

# ensure the files in this list are relevant your shell
FILES = [
  "aliases",
  "zshrc",
  "bashrc",
  "bash_profile",
  "bash_prompt"
]

def cmd_parser():
  ''' parse command line arguments passed in '''
  parser = argparse.ArgumentParser(description='Dotfile installer and shell configuration tool')

  parser.add_argument('-hd', '--homedir', 
                      help="Full path to your home directory", 
                      required=True)

  parser.add_argument('-pm', '--package-manager', 
                      help="package manager relevant to your operating system", 
                      required=True)

  return parser.parse_args()

def main():
  arguments = cmd_parser()

  if arguments.package_manager:
    pm.install_packages(vars(arguments)["package_manager"])
    # If your user requires sudo access to install packages
    # you'll need to rerun this without sudo to correct the 
    # owner of the dotfiles in your home directory
    dm(arguments.homedir, FILES)

if __name__ == "__main__":
  main()
