# uv の実行バイナリを保持するコンテナ
FROM ghcr.io/astral-sh/uv:latest AS uv

# サービスのビルド環境および実行環境のコンテナ
FROM mcr.microsoft.com/vscode/devcontainers/python:3.11-bookworm
WORKDIR /workspace

# uvの実行バイナリを開発コンテナにコピーする
COPY --from=uv --chown=vscode: /uv /uvx /bin/

# 作業ディレクトリ配下をコンテナ側の作業用ディレクトリにコピーする
COPY ./ .
