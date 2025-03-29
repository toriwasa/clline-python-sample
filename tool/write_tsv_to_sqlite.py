#!/usr/bin/env python3
import argparse
import sqlite3

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

# Constants
TABLE_NAME = "UserAction"
TSV_COLUMNS = ["id", "username", "user_machine_id",
               "action_name", "action_time"]
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def _create_spark_session() -> SparkSession:
    """SparkSessionを作成する"""
    return SparkSession.builder.appName("TSVtoSQLite").getOrCreate()


def _create_table(conn: sqlite3.Connection) -> None:
    """UserActionテーブルを作成する

    Args:
        conn: SQLite接続オブジェクト
    """
    conn.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            user_machine_id TEXT NOT NULL,
            action_name TEXT NOT NULL,
            action_time TIMESTAMP NOT NULL
        )
        """
    )


def _read_tsv(spark: SparkSession, file_path: str) -> pd.DataFrame:
    """TSVファイルを読み込みDataFrameに変換する

    Args:
        spark: SparkSession
        file_path: TSVファイルのパス

    Returns:
        pd.DataFrame: 読み込んだデータ
    """
    schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("username", StringType(), True),
        StructField("user_machine_id", StringType(), True),
        StructField("action_name", StringType(), True),
        StructField("action_time", TimestampType(), True)
    ])

    df = spark.read.csv(file_path, schema=schema, sep="\t", header=True)
    return df.toPandas()


def _write_to_sqlite(df: pd.DataFrame, conn: sqlite3.Connection) -> None:
    """DataFrameをSQLiteに書き込む

    Args:
        df: 書き込むデータ
        conn: SQLite接続オブジェクト
    """
    df.to_sql(TABLE_NAME, conn, if_exists="append", index=False)


def write_tsv_to_sqlite(tsv_path: str, sqlite_path: str) -> None:
    """TSVファイルの内容をSQLiteのUserActionテーブルに書き込む

    Args:
        tsv_path: TSVファイルのパス
        sqlite_path: SQLiteデータベースのパス
    """
    spark = _create_spark_session()

    try:
        # TSVファイルを読み込む
        df = _read_tsv(spark, tsv_path)

        # SQLiteに接続してテーブルを作成し、データを書き込む
        with sqlite3.connect(sqlite_path) as conn:
            _create_table(conn)
            _write_to_sqlite(df, conn)
    finally:
        spark.stop()


def main():
    parser = argparse.ArgumentParser(
        description="TSVファイルの内容をSQLiteのUserActionテーブルに書き込むツール")
    parser.add_argument("tsv_path", help="入力TSVファイルのパス")
    parser.add_argument("sqlite_path", help="出力SQLiteデータベースのパス")

    args = parser.parse_args()
    write_tsv_to_sqlite(args.tsv_path, args.sqlite_path)


if __name__ == "__main__":
    main()
