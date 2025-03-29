from datetime import datetime

import pytest
from pyspark.sql import Row, SparkSession
from pyspark.testing import assertDataFrameEqual
from schema import USER_ACTIONS_SCHEMA

from cline_sample.domain.models.user_action import UserActionDataFrame
from cline_sample.usecase.get_latest_user_actions import get_latest_user_actions


@pytest.fixture(scope="session")
def spark():
    """テストで使用する SparkSession を提供する fixture"""
    spark = (
        SparkSession.builder.appName("TestSparkSession")  # type: ignore
        .master("local[*]")
        .getOrCreate()
    )
    yield spark
    spark.stop()


def test_同一ユーザーの場合最新のレコードのみが残る(spark: SparkSession):
    """同一ユーザーで複数レコードがある場合、action_timeが最新のレコードのみが抽出されることを確認するテスト"""

    class ConstantsHelper:
        USERNAME = "test_user"
        USER_MACHINE_ID = "machine_1"
        ACTION_NAME = "test_action"
        OLD_TIME = datetime(2024, 1, 1, 10, 0, 0)
        NEW_TIME = datetime(2024, 1, 1, 11, 0, 0)

    # Arrange
    input_df = spark.createDataFrame(
        [
            Row(
                id=1,
                username=ConstantsHelper.USERNAME,
                user_machine_id=ConstantsHelper.USER_MACHINE_ID,
                action_name=ConstantsHelper.ACTION_NAME,
                action_time=ConstantsHelper.OLD_TIME,
            ),
            Row(
                id=2,
                username=ConstantsHelper.USERNAME,
                user_machine_id=ConstantsHelper.USER_MACHINE_ID,
                action_name=ConstantsHelper.ACTION_NAME,
                action_time=ConstantsHelper.NEW_TIME,
            ),
        ],
        schema=USER_ACTIONS_SCHEMA,
    )
    user_actions = UserActionDataFrame(input_df)

    expected_df = spark.createDataFrame(
        [
            Row(
                id=2,
                username=ConstantsHelper.USERNAME,
                user_machine_id=ConstantsHelper.USER_MACHINE_ID,
                action_name=ConstantsHelper.ACTION_NAME,
                action_time=ConstantsHelper.NEW_TIME,
            ),
        ],
        schema=USER_ACTIONS_SCHEMA,
    )

    # Act
    result = get_latest_user_actions(user_actions)

    # Assert
    assertDataFrameEqual(result.df, expected_df)


def test_複数ユーザーの場合各ユーザーの最新レコードが残る(spark: SparkSession):
    """複数ユーザーで複数レコードがある場合、各ユーザーのaction_timeが最新のレコードが抽出されることを確認するテスト"""

    class ConstantsHelper:
        USER1 = "user1"
        USER2 = "user2"
        MACHINE1 = "machine1"
        MACHINE2 = "machine2"
        ACTION = "test_action"
        USER1_OLD_TIME = datetime(2024, 1, 1, 10, 0, 0)
        USER1_NEW_TIME = datetime(2024, 1, 1, 11, 0, 0)
        USER2_OLD_TIME = datetime(2024, 1, 1, 12, 0, 0)
        USER2_NEW_TIME = datetime(2024, 1, 1, 13, 0, 0)

    # Arrange
    input_df = spark.createDataFrame(
        [
            # User1のレコード
            Row(
                id=1,
                username=ConstantsHelper.USER1,
                user_machine_id=ConstantsHelper.MACHINE1,
                action_name=ConstantsHelper.ACTION,
                action_time=ConstantsHelper.USER1_OLD_TIME,
            ),
            Row(
                id=2,
                username=ConstantsHelper.USER1,
                user_machine_id=ConstantsHelper.MACHINE1,
                action_name=ConstantsHelper.ACTION,
                action_time=ConstantsHelper.USER1_NEW_TIME,
            ),
            # User2のレコード
            Row(
                id=3,
                username=ConstantsHelper.USER2,
                user_machine_id=ConstantsHelper.MACHINE2,
                action_name=ConstantsHelper.ACTION,
                action_time=ConstantsHelper.USER2_OLD_TIME,
            ),
            Row(
                id=4,
                username=ConstantsHelper.USER2,
                user_machine_id=ConstantsHelper.MACHINE2,
                action_name=ConstantsHelper.ACTION,
                action_time=ConstantsHelper.USER2_NEW_TIME,
            ),
        ],
        schema=USER_ACTIONS_SCHEMA,
    )
    user_actions = UserActionDataFrame(input_df)

    expected_df = spark.createDataFrame(
        [
            # User1の最新レコード
            Row(
                id=2,
                username=ConstantsHelper.USER1,
                user_machine_id=ConstantsHelper.MACHINE1,
                action_name=ConstantsHelper.ACTION,
                action_time=ConstantsHelper.USER1_NEW_TIME,
            ),
            # User2の最新レコード
            Row(
                id=4,
                username=ConstantsHelper.USER2,
                user_machine_id=ConstantsHelper.MACHINE2,
                action_name=ConstantsHelper.ACTION,
                action_time=ConstantsHelper.USER2_NEW_TIME,
            ),
        ],
        schema=USER_ACTIONS_SCHEMA,
    )

    # Act
    result = get_latest_user_actions(user_actions)

    # Assert
    assertDataFrameEqual(result.df, expected_df)


def test_単一レコードの場合そのレコードが残る(spark: SparkSession):
    """単一レコードの場合、そのレコードが抽出されることを確認するテスト"""

    class ConstantsHelper:
        ID = 1
        USERNAME = "test_user"
        USER_MACHINE_ID = "machine_1"
        ACTION_NAME = "test_action"
        ACTION_TIME = datetime(2024, 1, 1, 10, 0, 0)

    # Arrange
    input_df = spark.createDataFrame(
        [
            Row(
                id=ConstantsHelper.ID,
                username=ConstantsHelper.USERNAME,
                user_machine_id=ConstantsHelper.USER_MACHINE_ID,
                action_name=ConstantsHelper.ACTION_NAME,
                action_time=ConstantsHelper.ACTION_TIME,
            ),
        ],
        schema=USER_ACTIONS_SCHEMA,
    )
    user_actions = UserActionDataFrame(input_df)

    expected_df = spark.createDataFrame(
        [
            Row(
                id=ConstantsHelper.ID,
                username=ConstantsHelper.USERNAME,
                user_machine_id=ConstantsHelper.USER_MACHINE_ID,
                action_name=ConstantsHelper.ACTION_NAME,
                action_time=ConstantsHelper.ACTION_TIME,
            ),
        ],
        schema=USER_ACTIONS_SCHEMA,
    )

    # Act
    result = get_latest_user_actions(user_actions)

    # Assert
    assertDataFrameEqual(result.df, expected_df)
