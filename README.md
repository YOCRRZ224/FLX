# FLX - Host your own project manager

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) 
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/) 
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)] 
[![Version](https://img.shields.io/badge/version-0.9.0-orange)] 
[![Plugin Ready](https://img.shields.io/badge/plugin-system-blueviolet)] 

---

## What is FLX?

FLX is a **lightweight Git alternative** for developers who want **full snapshot versioning**, **human-readable logs**, **plugin support**, and **AI-powered project enrichment**.  

Think of it as **Git, but fast, minimal, and enriched with plugins + AI magic**.

---

## Features

- **Full Snapshot Versioning** — Not diffs, full project snapshots.  
- **Human-Readable History** — `flx log` shows versions & commit messages.  
- **Project Status** — `flx status` to see **New / Modified / Deleted** files.  
- **Plugin System** — Add plugins under `plugins/` and run `flx -p
- <plugin_name>`  
- **.flxignore Support** — Ignore files/folders during snapshots.  
- **Server-Client Mode** — Push & pull from your personal home lab or server.  

---
## Uses 
- **To manage** - easy than git
- **Self host** - host your own
- **Create** - create your own plugins
- **Fast** - using python will be fast
- **Management** - manage your projects easily.

---
## All commands
- `flx log` - check logs
- `flx store` - see plugins
- `flx init` - intialize repo
- `flx push -v <version name> -c "commit"` - push an repo
- `flx pull <version name>` - pull an version
- `flx status` - like diff but beta
- `flx install <plugin name>` - install a plugin.
- `flx list` - list version that are pushed
- `flx plugins` - show installed plugins
- `flx -p <plugin name>` - use an plugin

---
## What you get
- **pre installed** - 5 pre installed plugins in store run `flx store` to see plugins available.
- **create own** - create your own plugins and save in the plugins folder.
- **management** - your own server and management.

---
## install
- **RUN THIS ONE LINER** =>
- ```bash
  git clone https://github.com/YOCRRZ224/FLX.git && cd FLX
## How
- **Run main.py** - server run
- **To use FLX command globally and ready for use just one line**
- on termux =>
- ```bash
  cd && cd FLX && mv flx /data/data/com.termux/files/usr/bin && chmod +x /data/data/com.termux/files/usr/bin/flx && cd && mkdir /data/data/com.termux/files/usr/bin/plugins

- on any other device put it in usr/bin folder

runt the python file
