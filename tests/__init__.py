import unittest
import pandas as pd
from datetime import datetime, timedelta

from connectors.s3 import S3Connector
from connectors.chatgpt import ChatGPTConnector
from actions.create_new_product import run

import settings

s3_connector = S3Connector("fictive-company")
chatgpt_connector = ChatGPTConnector()


class ConnectorsTest(unittest.TestCase):

    def test_s3_data_fetch(self):
        res = s3_connector.fetch_data("products", settings.S3_FETCH_WINDOW)

    def test_run(self):
        res = run()


if __name__ == "__main__":
    unittest.main()
