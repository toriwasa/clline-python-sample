from pyspark.sql import SparkSession


def get_spark_session(app_name: str = "ClinerSampleApp") -> SparkSession:
    """SparkSession インスタンスを取得する

    Args:
        app_name (str, optional): Sparkアプリケーション名. デフォルトは "ClinerSampleApp"

    Returns:
        SparkSession: SparkSession インスタンス
    """
    return SparkSession.builder.appName(app_name).getOrCreate()
