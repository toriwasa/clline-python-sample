# README
## Introduction
- Python を使ってバックエンドのプログラム開発を行う際のサンプルリポジトリ

## How To Use
- 以下のディレクトリおよびファイルをプロジェクトディレクトリにコピーする
  - .devcontainer
  - .vscode
  - .clinerules
  - .clineignore
  - .gitignore
  - .python-version
  - pyproject.toml
- 空の memory-bank ディレクトリを作成する
- 開発内容に応じて .devcontainer および pyproject.toml の内容を書き換える
- .devcontainer の内容を元に開発コンテナをビルドして起動する
- .clinerules のプロジェクト内容に応じて書き換える
- .clinerules にプロジェクトで実現したいシステムの概要を追記する
- Cline の設定で利用するAPIを指定する。 claude-3.5-sonnet や claude-3.7-sonnet など
- Cline の設定で Read files, Edit files のAuto-Approveを有効にする
- Cline で "initialize memory bank" をActモードで実行する
- domain/models ディレクトリ配下に処理で利用するデータクラスファイルを作成する
- Cline のPlanモードで公開関数1つの作成を依頼する。結果を見つつ要件に合わせて設計の修正を依頼する
- 要件の詳細が確定したら Start new Taskを実行する
- Cline のPlanモードで詳細化された要件を元に公開関数の実装を依頼する
- Planモードの結果が要件に合致していればActモードに切り替える。実装が開始されるので待機する
- Actモードで出力されたコードを確認して、コメントの追記など細部を修正する

## 公開関数の設計および実装順序
- 以下の順序で公開関数を設計および実装する
  - usecase層のビジネスロジック関数-バリデーションチェック処理
  - usecase層のビジネスロジック関数-正常系データ加工処理
  - infrastructure層のデータ読み込み関数
  - infrastructure層のデータ書き込み関数
- ビジネスロジック関数を先に設計、実装することで、データや前提条件の過不足を確認することができる
- バリデーションチェックやエラーハンドリングなど、ビジネスロジックの正常系が想定していないデータや実行結果が出力されることが分かった場合は、正常系の処理フローに入る前にコントローラー層で早期リターンするように実装する

## ライブラリ運用

```bash
# プロダクトコードで利用するライブラリのインストール
uv add [library_name]
# Linter, Formatter, Type Checker, 単体テストなど開発用に利用するライブラリのインストール
uv add --dev [library_name]
```

## Linterの実行方法

```bash
uv run ruff check --fix
```

## Formatterの実行方法

```bash
uv run ruff format
```

## Type Checkerの実行方法

```bash
uv run pyright
```

## 単体テストの実行方法

```bash
PYTHONPATH=src uv run pytest
```

## ややこしい部分
- .venv をワークスペース配下に作ってしまうとuvコマンド実行時にファイルのハードコピーが作れずエラーが発生する
- エラーが発生してもuvは動作するが速度が犠牲になるらしい
- そのため /home/vscode/.venv に作成するようにしている
