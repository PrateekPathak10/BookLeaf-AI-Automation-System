import pandas as pd
from datetime import datetime

LOG_FILE = "query_logs.csv"


def log_query(query, response, confidence, escalation):

    data = {
        "timestamp": [datetime.now()],
        "query": [query],
        "response": [response],
        "confidence": [confidence],
        "escalation": [escalation]
    }

    df = pd.DataFrame(data)

    try:
        old_df = pd.read_csv(LOG_FILE)
        df = pd.concat([old_df, df])
    except:
        pass

    df.to_csv(LOG_FILE, index=False)