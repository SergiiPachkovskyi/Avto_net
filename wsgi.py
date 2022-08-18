from api import create_app
from api.config.config import config_dict


app = create_app(config_dict['prod'])

if __name__ == '__main__':
    app.run(host='164.92.211.61', port=88)
