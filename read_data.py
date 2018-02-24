#!/usr/bin/env python

import pandas as pd
from simpledbf import Dbf5

dbf = Dbf5('test.dbf')
df = dbf.to_dataframe()
