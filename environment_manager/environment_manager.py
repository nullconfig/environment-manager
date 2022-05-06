import os
# pulled from a list inside of the packages
# directory. Update these lists to match
# the applications you want to install or 
# match the pattern and add the package manager
# relevant to your operating system
from packages import apt_packages
from packages import brew_packages

install_once = {
    "tunnelblick": {"mac_app": "Tunnelblick.app"},
    "visual-studio-code": {"mac_app": "Visual\ Studio\ Code.app"},
    "google-chrome": {"mac_app": "Google\ Chrome.app"},
    "firefox": {"mac_app": "Firefox.app"}
}

class PackageManager:
  '''
  Installs packages based on the provided list that matches
  the given package manager, and creates symlinks for all 
  dotfiles in the dotfiles directory to the home directory
  '''
  def install_packages(package_manager):
    if package_manager == "brew":
      for package in brew_packages.apps:
        if package in install_once.keys() and os.system(f"ls /Applications/{install_once[package]['mac_app']} > /dev/null") == 0:
          pass
        else:
          os.system(f"{package_manager} install {package}")
    else:
      for package in apt_packages.apps:
        os.system(f"{package_manager} install {package}")

class DotfileManager:
  def __init__(self, homedir, files) -> None:
    self.homedir = homedir
    self.files = files

    if self.homedir:
      dotfiledir = f"{self.homedir}/dotfiles"

      for file in files:
        try:
          os.symlink(f"{dotfiledir}/.{file}", f"{self.homedir}/.{file}")
          print(f"Symlink created {dotfiledir}/.{file} -> {self.homedir}/.{file}")
        except FileExistsError:
          print("Symlink exist updating with current dotfile")
          os.remove(f"{self.homedir}/.{file}")
          os.symlink(f"{dotfiledir}/.{file}", f"{self.homedir}/.{file}")
          print(f"{dotfiledir}/.{file} -> {self.homedir}/.{file}")
          print()
