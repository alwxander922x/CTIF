

import os

def get_base_url():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://demostore.supersqa.com'
    elif env.lower() =='prod':
        return 'http://localhost/prod/quicksite'
    else:
        raise Exception(f"Unknown environment: {env}")
