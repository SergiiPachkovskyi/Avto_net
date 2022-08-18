from api import create_app
from api.config.config import config_dict

if __name__ == '__main__':
    dev_app = create_app(config_dict['production'])
    dev_app.run()
