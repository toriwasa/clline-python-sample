from infrastructure.file import read_user_action_tsv_as_df
from usecase.get_latest_user_actions import get_latest_user_actions


def main():
    try:
        # TSVファイルからユーザーアクションのデータを読み込む
        user_action_df = read_user_action_tsv_as_df()

        # ユーザーアクションの最新データを取得する
        latest_df = get_latest_user_actions(user_action_df)

        latest_df.df.show()

    except ValueError as e:
        print(f"Error reading user action data: {e}")


if __name__ == "__main__":
    main()
