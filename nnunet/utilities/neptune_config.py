import os
import neptune.new as neptune

NEPTUNE_PROJECT = os.getenv("NEPTUNE_PROJECT")
#NEPTUNE_API_TOKEN = os.getenv("NEPTUNE_API_TOKEN")

def config_run(id=None):
    if id is None:
        run = neptune.init_run(
                project=NEPTUNE_PROJECT,
                #api_token=NEPTUNE_API_TOKEN,
            )

    else:
        run = neptune.init_run(
                project=NEPTUNE_PROJECT,
                #api_token=NEPTUNE_API_TOKEN,
                with_id = id
            )
    
    return run