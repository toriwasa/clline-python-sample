from datetime import datetime, timedelta
from faker import Faker
import random
from pathlib import Path

ACTION_NAMES = [
    "login",
    "logout",
    "view_dashboard",
    "edit_profile",
    "send_message",
    "delete_file",
    "upload_file",
    "create_document",
    "share_content",
    "change_settings",
]


def create_sample_data() -> None:
    """
    ユーザーアクションのサンプルデータを生成してTSVファイルに出力する関数

    Generated Fields:
        id(int): アクションID
        username(str): ユーザー名
        user_machine_id(str): ユーザーのマシンID
        action_name(str): アクション名
        action_time(str): アクション実行時間 (ISO format)
    """
    fake = Faker()

    # 出力パスの設定
    output_path = Path("data/tsv/user_action.tsv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 現在時刻から過去30日分のデータを生成
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)

    # サンプルデータの生成
    data = []
    unique_users = [fake.user_name() for _ in range(20)]  # 20人のユーザーを生成

    for i in range(100):
        username = random.choice(unique_users)
        user_machine_id = f"MACHINE-{random.randint(1000, 9999)}"
        action_name = random.choice(ACTION_NAMES)
        action_time = start_time + timedelta(
            seconds=random.randint(0, int((end_time - start_time).total_seconds()))
        )

        data.append(
            {
                "id": i + 1,
                "username": username,
                "user_machine_id": user_machine_id,
                "action_name": action_name,
                "action_time": action_time.isoformat(),
            }
        )

    # TSVファイルへの出力
    with output_path.open("w", encoding="utf-8") as f:
        # ヘッダーの書き込み
        f.write("id\tusername\tuser_machine_id\taction_name\taction_time\n")

        # データの書き込み
        for row in sorted(data, key=lambda x: x["action_time"]):
            f.write(
                f"{row['id']}\t{row['username']}\t{row['user_machine_id']}\t{row['action_name']}\t{row['action_time']}\n"
            )


if __name__ == "__main__":
    create_sample_data()
