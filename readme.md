# LLMs workshop - University of New York, Tirana

## Installations

There are few pre-requisites for installations. 

- Python3
- Node.js
- Ollama

## Python3 & Conda

### MAC

#### Python

```
brew install python@3.10

echo 'export PATH="/usr/local/opt/python@3.10/bin:$PATH"' >> ~/.zshrc

source ~/.zshrc

python3.10 --version

echo 'alias python=python3.10' >> ~/.zshrc

source ~/.zshrc

python --version
```

#### Conda

```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

chmod +x Miniconda3-latest-MacOSX-x86_64.sh

./Miniconda3-latest-MacOSX-x86_64.sh

source ~/.zshrc

conda --version

```

### Windows 

Make sure you have chocolatey package manager installed [chocolatey](https://chocolatey.org/)

#### Python

```
choco install python --version=3.10.0

python --version
```

#### Conda 

```
choco install miniconda3

conda --version

```

### Linux (Ubuntu)

#### Python 

```
sudo apt update

sudo apt install software-properties-common -y

sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

sudo apt install python3.10 python3.10-venv python3.10-dev -y

python3.10 --version

echo 'alias python=python3.10' >> ~/.bashrc

source ~/.bashrc

python --version
```

#### Conda 

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

chmod +x Miniconda3-latest-Linux-x86_64.sh

./Miniconda3-latest-Linux-x86_64.sh

source ~/.bashrc

conda --version

```

## Node.js & nvm 

### MAC

```
brew install node@22

echo 'export PATH="/usr/local/opt/node@22/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

node --version 

##### For installing exact version (v22.14.0)

brew install nvm
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.zshrc
echo '[ -s "/usr/local/opt/nvm/nvm.sh" ] && . "/usr/local/opt/nvm/nvm.sh"' >> ~/.zshrc
source ~/.zshrc
nvm install 22.14.0
nvm use 22.14.0

node --version
```
### Windows

```
choco install nodejs-lts

node --version
```

### Ubuntu 

```
sudo apt update
sudo apt install curl -y

curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -

sudo apt install -y nodejs

node --version  # Should show v22.x.x

#####  For exact version (v22.14.0)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

nvm install 22.14.0
nvm use 22.14.0

node --version

```

## Ollama

Ollama is an open-source tool that makes it easy to run large language models (LLMs) locally on your computer.

### MAC

```
brew install ollama

ollama --version
```

### Windows

```
Download and Install exe from here https://ollama.com/download/windows
```

### Ubuntu 

```
curl -fsSL https://ollama.com/install.sh | sh
```
 
Once Ollama is installed, we should install a few models beforehand as they need to be downloaded. 

```

ollama run llama3.2:3b

```
This will be almost 2GB model that would need to be downloaded. 

```

ollama run deepseek-r1:7b

```

This is almost 4.7GB model. 

You can explore other models here [https://ollama.com/search](https://ollama.com/search) and download whichever you prefer. 

