from infrastructure.file import read_user_action_tsv_as_df


def main():
    try:
        # TSVファイルからユーザーアクションのデータを読み込む
        user_action_df = read_user_action_tsv_as_df()

        # 読み込んだデータを表示
        print("Successfully read user action data:")
        user_action_df.df.show()

    except ValueError as e:
        print(f"Error reading user action data: {e}")


if __name__ == "__main__":
    main()
