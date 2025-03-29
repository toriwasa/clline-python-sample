from datetime import datetime
from typing import Iterator
import sqlite3

from domain.models.user_action import UserAction


def read_user_action_table(db_path: str) -> Iterator[UserAction]:
    """UserActionテーブルからデータを読み込みUserActionオブジェクトのイテレータを返す

    Args:
        db_path: SQLiteデータベースのパス

    Yields:
        UserAction: 各レコードのUserActionオブジェクト
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, username, user_machine_id, action_name, action_time FROM UserAction"
        )

        for row in cursor:
            yield UserAction(
                id=row[0],
                username=row[1],
                user_machine_id=row[2],
                action_name=row[3],
                action_time=datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S"),
            )
