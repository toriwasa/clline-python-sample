from pyspark.sql import Window
from pyspark.sql.functions import row_number

from cline_sample.domain.models.user_action import UserActionDataFrame


def get_latest_user_actions(user_actions: UserActionDataFrame) -> UserActionDataFrame:
    """ユーザー名ごとに最新のアクションレコードを抽出する

    Args:
        user_actions (UserActionDataFrame): ユーザーアクションのデータフレーム

    Returns:
        UserActionDataFrame: ユーザー名ごとに最新のアクションレコードだけを含むデータフレーム
    """
    window_spec = Window.partitionBy("username").orderBy("action_time", ascending=False)

    latest_actions_df = (
        user_actions.df.withColumn("row_number", row_number().over(window_spec))
        .filter("row_number = 1")
        .drop("row_number")
    )

    return UserActionDataFrame(latest_actions_df)
