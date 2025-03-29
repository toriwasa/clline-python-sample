from dataclasses import dataclass
from datetime import datetime
from pyspark.sql import DataFrame
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    TimestampType,
)


@dataclass
class UserAction:
    """ユーザーがアプリ上で実行したアクションを表すデータクラス

    Attributes:
        id (int): ユーザーアクションのID
        username (str): ユーザー名
        user_machine_id (str): ユーザーのマシンID
        action_name (str): アクション名
        action_time (datetime): アクションが実行された日時
    """

    id: int
    username: str
    user_machine_id: str
    action_name: str
    action_time: datetime


class UserActionDataFrame:
    """ユーザーアクションのデータフレームを表すクラス

    Fields:
        id (IntegerType): ユーザーアクションのID
        username (StringType): ユーザー名
        user_machine_id (StringType): ユーザーのマシンID
        action_name (StringType): アクション名
        action_time (TimestampType): アクションが実行された日時
    """

    _df: DataFrame
    SCHEMA = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("username", StringType(), True),
            StructField("user_machine_id", StringType(), True),
            StructField("action_name", StringType(), True),
            StructField("action_time", TimestampType(), True),
        ]
    )

    def __init__(self, df: DataFrame):
        if df.schema != self.SCHEMA:  # pragma: no cover
            raise ValueError(
                f"DataFrame schema does not match expected schema. Expected: {self.SCHEMA}, but got: {df.schema}"
            )

        self._df = df

    @property
    def df(self) -> DataFrame:
        """DataFrameを返す"""
        return self._df
