#!/usr/bin/env python3

'''
This script creates symlinks from the home directory 
to any desired dotfiles in homedir/dotfiles, 
and also installs Homebrew Packages.
'''
import argparse, os
from os import path

from environment_manager import PackageManager as pm
from environment_manager import DotfileManager as dm

HERE = path.abspath(path.dirname(__file__))
HOMEDIR = os.environ.get("HOME")
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
                      help="Linux package manager", 
                      required=False)

  return parser.parse_args()

def main():
  arguments = cmd_parser()
  os.system(f"rsync -avr {HERE}/../dotfiles {HOMEDIR}")

  if arguments.package_manager:
    pm.install_packages(vars(arguments)["package_manager"])
  if arguments.homedir:
    dm(HOMEDIR, FILES)

if __name__ == "__main__":
  main()