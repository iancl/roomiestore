from roomiestore import Application
from roomiestore.config import config


def main():
    level = True if config['server']['debugmode'] == 'True' else False
    app = Application(config)
    app.setup_logging()
    app.mount_routes()
    app.server.run(debug=level, port=config['server']['port'])

if __name__ == '__main__':
    main()