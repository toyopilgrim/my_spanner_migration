import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SRC_INSTANCE_ID = os.environ.get("SRC_INSTANCE_ID")
DST_INSTANCE_ID = os.environ.get("DST_INSTANCE_ID")
SRC_DATABASE = os.environ.get("SRC_DATABASE")
DST_DATABASE = os.environ.get("DST_DATABASE")
TBL_NAME = os.environ.get("TBL_NAME")