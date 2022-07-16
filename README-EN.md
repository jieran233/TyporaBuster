# TyporaBuster

A simple script that makes typora's trial period never end, maybe it works.

[![State-of-the-art Shitcode](https://img.shields.io/static/v1?label=State-of-the-art&message=114514Code&color=7B5804)](https://github.com/trekhleb/state-of-the-art-shitcode)

## Features

- **For Windows only**

- Written for **Typora 1.3.8**, There is no guarantee that other versions will work. If you do not have the corresponding version installed, you can download it here: [typora-setup-x64.exe](https://jieran233.lanzouy.com/in6Bn07viduf)

- Rely on **modifying the registry** to achieve unlimited trial, not modify the program file
- Support writing hosts to block Typora updates (optional, but highly recommended)
- Delete 'profile.data' 'typora.log' 'typora-old.log' to avoid future problems

## Usage

#### Running from python script

- **Note: Please run the newly installed Typora at least once before running the script, and run the script as Administrator**

```
git clone --depth=1 https://github.com/jieran233/TyporaBuster
cd TyporaBuster
python typorabuster.py
```

### CLI parameters

```
fucktypora.py <Operation>

No parameter    run normally

Operation:
reg   modify registry value, try-out forever.
rm    delete files: ['profile.data', 'typora.log', 'typora-old.log']
```

