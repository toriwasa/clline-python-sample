from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

from domain.models.user_action import UserActionDataFrame

def read_user_action_tsv_as_df(spark: SparkSession, file_path: str = "data/tsv/user_action.tsv") -> UserActionDataFrame:
    """TSVファイルからユーザーアクションのデータを読み込みUserActionDataFrameを返却する

    Args:
        spark (SparkSession): Sparkセッション
        file_path (str, optional): 読み込むTSVファイルのパス. デフォルトは "data/tsv/user_action.tsv"

    Returns:
        UserActionDataFrame: 読み込んだユーザーアクションのDataFrame

    Raises:
        ValueError: DataFrameのスキーマが不正な場合に発生
    """
    # スキーマの定義
    schema = StructType([
        StructField("id", IntegerType(), True),  # 一時的にStringTypeとして読み込み
        StructField("username", StringType(), True),
        StructField("user_machine_id", StringType(), True),
        StructField("action_name", StringType(), True),
        StructField("action_time", TimestampType(), True)  # 一時的にStringTypeとして読み込み
    ])

    try:
        # TSVファイルの読み込み
        df = spark.read.csv(file_path, schema=schema, sep="\t", header=True)

        # UserActionDataFrameに変換して返却
        return UserActionDataFrame(df)

    except Exception as e:
        raise ValueError(f"Failed to read TSV file: {str(e)}")
