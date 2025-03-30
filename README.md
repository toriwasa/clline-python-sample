# README
## Introduction
- Python を使ってバックエンドのプログラム開発を行う際のサンプルリポジトリ

## 技術スタック
- プログラミング言語: Python
- パッケージマネージャ: uv
- DataFrame ライブラリ: Spark
- Formatter: Ruff
- Linter: Ruff
- Type Checker: pyright
- 単体テストフレームワーク: pytest

## ディレクトリ構成

```txt
.
├── README.md  このファイル
├── .devcontainer  開発コンテナ定義ファイル置き場
│   ├── devcontainer.json
│   ├── docker-compose.dev.yml
│   ├── postCreateCommand.sh
│   └── Dockerfile
├── .vscode
│   ├── launch.json  デバッグタスクの設定ファイル
│   └── settings.json  VSCodeのプロジェクト固有設定ファイル
├── .clinerules  Clineのルールファイル
├── .clineignore  Clineの無視ファイル
├── .gitignore  Gitの無視ファイル
├── .python-version  pyenvのバージョン指定ファイル
├── .env  開発用に環境変数を定義するファイル
├── pyproject.toml  Pythonのプロジェクト固有設定ファイル
├── src  プロダクトコード置き場
│   └── cline_sample  開発対象のパッケージディレクトリ
│       ├── main.py  処理のエントリーポイント
│       ├── domain  ドメイン層
│       │   └── models  データクラス置き場
│       ├── usecase  ユースケース層 ビジネスロジック置き場
│       ├── infrastructure  インフラ層 データアクセス処理置き場
│       ├── handler  ユーザーインターフェース層  WebAPIやCLIなどのユーザーインターフェース処理置き場
│       └── controller  コントローラー層  usecase層やinfrastructure層を呼び出す
├── tests  テストコード置き場
│   └── cline_sample  開発対象のパッケージディレクトリ
│       └── usecase  ユースケース層のテストコード置き場
├ tool  開発用ツール置き場
├ data  開発用テストデータ置き場
└ memory-bank  Clineのメモリバンク置き場
```

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

## VSCodeデバッグ機能の使い方
- launch.json でmain.pyを任意の引数で実行する起動タスクを定義している
- 開発コードの任意の場所にブレークポイントを設定する
- Ctrl + Shift + D で "実行とデバッグ" タブを開く
- Python: Debug main.py を選択して実行する
- ブレークポイントで停止したら、デバッグコンソールで変数の値を確認したり、ステップ実行を行う
- launch.json の設定を変更することで、実行するPythonファイルや引数を変更することができる

## VSCodeのテスト機能の使い方
- Ctrl + Shift + P でコマンドパレットを開く
- "テスト: カバレッジを使用してすべてのテストを実行" を実行する
- テスト結果が "テスト" タブに表示される
- ファイル一覧の右側にテストのカバレッジが表示される
- ウィンドウ左側のテストタブやウィンドウ下側のテスト結果タブでテストケースごとの結果を確認することもできる

## 開発コンテナの .venv について
- .venv をワークスペース配下に作ってしまうとuvコマンド実行時にファイルのハードコピーが作れずエラーが発生する
- エラーが発生してもuvは動作するが速度が犠牲になるらしい
- そのため /home/vscode/.venv に作成するようにしている
- 上記の構成だと使い勝手が悪くなるため .venv のシンボリックリンクをワークスペース直下に作成している
