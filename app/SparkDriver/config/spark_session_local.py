# -*- coding: utf-8 -*-
from pathlib import Path
import os
import sys

_PROJECT_HOME = Path(os.path.dirname(__file__)).parent.parent.parent
SPARK_WAREHOUSE_HOME = str(_PROJECT_HOME / "hive-db" / "spark-warehouse")
HIVE_METASTORE_DB_HOME = str(_PROJECT_HOME / "hive-db" )

appName = "local-test"
master = "local[*]"
conf_list = [    # TMP
        ["spark.sql.execution.arrow.enabled", "true"],
        ["spark.memory.offHeap.enabled", "true"],
        ["spark.memory.offHeap.size", "4096"],
        ["spark.driver.memory", "2g"],
        ["spark.executor.memory", "6g"],
        #["spark.eventLog.enabled", "true"],
        ["spark.serializer", "org.apache.spark.serializer.KryoSerializer"],
        ["spark.sql.warehouse.dir", SPARK_WAREHOUSE_HOME],
        ["spark.driver.extraJavaOptions", f"-Dderby.system.home='{HIVE_METASTORE_DB_HOME}'"],
        ]
