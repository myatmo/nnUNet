import neptune.new as neptune

PROJECT_NAME = "UMN-RC-1/Fatchecker"
API_TOKEN = "eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiIzOGFiYmZkMS1jY2VmLTQ1YWYtYjJjZC0xMjc0MTI4MzNiZTAifQ=="

def config_run(id=None):
    if id is None:
        run = neptune.init_run(
                project=PROJECT_NAME,
                api_token=API_TOKEN,
            )

    else:
        run = neptune.init_run(
                project=PROJECT_NAME,
                api_token=API_TOKEN,
                with_id = id,
            )

    return run
