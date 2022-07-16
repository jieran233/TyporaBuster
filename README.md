# TyporaBuster

[=> Here are the README in English](https://github.com/jieran233/TyporaBuster/blob/main/README-EN.md)

一个简单的Python脚本，能使Typora试用期永不结束，也许会奏效。

[![State-of-the-art Shitcode](https://img.shields.io/static/v1?label=State-of-the-art&message=114514Code&color=7B5804)](https://github.com/trekhleb/state-of-the-art-shitcode)

## Features

- **仅支持Windows平台**

- 基于 **Typora 1.3.8** 编写，无法保证其他版本能用，如果你没有安装对应版本，可以在这里下载，[typora-setup-x64.exe](https://jieran233.lanzouy.com/in6Bn07viduf)

- **依靠修改注册表实现无限试用**，不修改程序文件
- 支持写入hosts以屏蔽typora更新（可选，但强烈推荐使用）
- 支持删除`profile.data` `typora.log` `typora-old.log`以绝后患

## Usage

#### Running from python script

注意：请在运行脚本前至少运行过一次新安装的Typora，且请以管理员身份运行脚本

```
git clone --depth=1 https://github.com/jieran233/TyporaBuster
cd TyporaBuster
python typorabuster.py
```

#### ~~Running from binary executable file packed by pyinstaller~~

~~See Releases of this repo.~~

### CLI parameters

```
typorabuster.py <操作>

无参数: 一般运行

操作:
reg  修改注册表，无限试用
rm   删除 ['profile.data', 'typora.log', 'typora-old.log']
```

