# Author: O98K

"""
    步骤：
        1.爬取
        2.去重
        3.入库

"""
import asyncio
import re
import aiohttp
import aiomysql
from pyquery import PyQuery


base_url = "http://www.jobbole.com/"

