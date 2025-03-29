from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

from domain.models.user_action import UserActionDataFrame


def read_user_action_tsv_as_df(file_path: str = "data/tsv/user_action.tsv") -> UserActionDataFrame:
    """TSVファイルからユーザーアクションのデータを読み込みUserActionDataFrameを返却する

    Args:
        file_path (str, optional): 読み込むTSVファイルのパス. デフォルトは "data/tsv/user_action.tsv"

    Returns:
        UserActionDataFrame: 読み込んだユーザーアクションのDataFrame

    Raises:
        ValueError: DataFrameのスキーマが不正な場合に発生
    """
    # SparkSessionの作成
    spark = SparkSession.builder \
        .appName("UserActionReader") \
        .getOrCreate()

    # スキーマの定義
    schema = StructType([
        StructField("id", StringType(), True),  # 一時的にStringTypeとして読み込み
        StructField("username", StringType(), True),
        StructField("user_machine_id", StringType(), True),
        StructField("action_name", StringType(), True),
        StructField("action_time", StringType(), True)  # 一時的にStringTypeとして読み込み
    ])

    try:
        # TSVファイルの読み込み
        df = spark.read \
            .option("header", "true") \
            .option("delimiter", "\t") \
            .schema(schema) \
            .csv(file_path)

        # データ型の変換
        df = df.withColumn("id", df["id"].cast(IntegerType())) \
            .withColumn("action_time", df["action_time"].cast(TimestampType()))

        # UserActionDataFrameに変換して返却
        return UserActionDataFrame(df)

    except Exception as e:
        raise ValueError(f"Failed to read TSV file: {str(e)}")
    finally:
        # SparkSessionの終了
        spark.stop()
