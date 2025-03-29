#!/bin/bash

# 開発用ディレクトリの所有者を Dev Container のデフォルトユーザーである vscode ユーザーに変更する
sudo chown -R vscode:vscode /workspace

# pip の代わりにパッケージ管理ツール uv をインストールする
curl -LsSf https://astral.sh/uv/install.sh | sh

# uv のインストール先を PATH に追加する
source /home/vscode/.local/bin/env

# プロジェクトに必要な Python パッケージをインストールする
uv sync
