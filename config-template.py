config = {}
USERNAME = ''
PASSWORD = ''
DB_NAME = 'music'
SOCKET_PATH = '/tmp/cloudsql'
PROJECT_ID=''
INSTANCE_NAME = ''

if not USERNAME:
    raise ValueError("Change USERNAME = '' line to assign a username.")
if not PASSWORD:
    raise ValueError("Change PASSWORD = '' line to assign a password.")


config['DB_URL'] = r'mysql+mysqldb://{}:{}@/{}?unix_socket={}/google.com:{}:{}'.format(
    USERNAME, PASSWORD, DB_NAME, SOCKET_PATH, PROJECT_ID, INSTANCE_NAME)
