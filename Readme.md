# Programming Test

## Objective

Write a pre-commit hook for Mercurial that checks the commit message for the presence of an issue ID (e.g. `#1234`).  
If it's missing, warn the user and ask if they want to commit anyway.  
Send in a single .py file and mention in a comment what line should be added to repository's `.hg`/`hgrc` file to use the hook.  

Documentation: https://www.mercurial-scm.org/wiki/MercurialApi

In TortoiseHg (we use it on Windows, but Ubuntu packs it too now), the warning should look something like this:

![GUI Image](https://media.discordapp.net/attachments/977884486555541544/979086569841496084/unknown.png)

In the terminal, it would look something like

![Terminal Image](https://media.discordapp.net/attachments/977884486555541544/979086821491363860/unknown.png)

(Ignore the "Missing timeCreated".)


There is no hard time limit on the test, but seeing how long you take to complete tasks is part of the test.

After you send in your solution, we'll have a call to discuss it and your role on the project.

Ah, on compatibility: we're still on the Python 2.7 flavor of Mercurial.


# getting started

## Install mercurial's TortoiseHg

See https://foss.heptapod.net/mercurial/tortoisehg/thg/-/wikis/developers/MacOSX#install-via-homebrew

```bash
brew install --cask tortoisehg
```

## Install virtualenv/venv
```bash
$ brew update

$ brew install pyenv
$ echo 'echo "# loading python environment"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc

$ brew install pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ echo 'if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi' >> ~/.bashrc
```

## Install old Python 2.7
```bash
pyenv install --list | grep 2.7
# highest as time of writing is 2.7.18
# the installed one of TortoiseHg is 2.7.17 

# See https://github.com/pyenv/pyenv/issues/640#issuecomment-560081065
brew unlink binutils

env PYTHON_CONFIGURE_OPTS="--enable-shared" AR=/usr/bin/ar pyenv install -v 2.7.17

# See https://github.com/pyenv/pyenv/issues/640#issuecomment-560081065, restore "before".
brew link binutils
```

## Install virtual environment for this project
```bash
NAME="overmare-ashes-programming-test" && PYTHON_VERSION="2.7.17" && pyenv virtualenv ${PYTHON_VERSION} ${NAME}-${PYTHON_VERSION} && pyenv local ${NAME}-${PYTHON_VERSION}

# cleanup would be: 
# $ pyenv virtualenv-delete ${NAME}-${PYTHON_VERSION}
```



## Register with Mercurial
Source: https://github.com/jrburke/dvcs_jslint/#mercurial

https://mercurial.selenic.com/wiki/HookExamples


## Run tests

Using doctests (the function comments starting with ">>>").

```bash
pip install -r requirements-dev.txt

python -m doctest -v hello-hg.py
```


## Do a commit
```bash
cd 'test repo'
/Applications/TortoiseHg.app/Contents/MacOS/hg commit
```




