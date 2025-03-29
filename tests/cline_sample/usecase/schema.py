"""単体テストに利用するスキーマを定義するモジュール"""

from pyspark.sql.types import (
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

USER_ACTIONS_SCHEMA = StructType(
        [
            StructField("id", IntegerType(), True),
            StructField("username", StringType(), True),
            StructField("user_machine_id", StringType(), True),
            StructField("action_name", StringType(), True),
            StructField("action_time", TimestampType(), True),
        ]
    )
