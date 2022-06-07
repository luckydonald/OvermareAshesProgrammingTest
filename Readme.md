# Programming Test

Programming test for you:  
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

```
brew install --cask tortoisehg
```

