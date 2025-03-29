from pyspark.sql import Window
from pyspark.sql.functions import col, row_number

from cline_sample.domain.models.user_action import UserActionDataFrame


def get_latest_user_actions(user_actions: UserActionDataFrame) -> UserActionDataFrame:
    """ユーザー名ごとに最新のアクションレコードを抽出する

    Args:
        user_actions (UserActionDataFrame): ユーザーアクションのデータフレーム

    Returns:
        UserActionDataFrame: ユーザー名ごとに最新のアクションレコードだけを含むデータフレーム
    """
    df = user_actions.df

    window_spec = Window.partitionBy("username").orderBy(col("action_time").desc())
    df_with_row_number = df.withColumn("row_number", row_number().over(window_spec))

    df_latest_actions = df_with_row_number.filter(col("row_number") == 1).drop(
        col("row_number")
    )

    return UserActionDataFrame(df_latest_actions)
