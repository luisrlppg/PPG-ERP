# Initialize and update submodules if the repo is already cloned
git submodule init
# git submodule update

# Clone the repository with submodules if not already cloned
git clone --recurse-submodules --depth 1 git@github.com:luisrlppg/PPG-ERP.git

# to pull new changes from a sub module
# git submodule update --init --depth 10

