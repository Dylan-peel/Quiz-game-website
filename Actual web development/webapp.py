from app import app
from app.models import User
from config import Config
u = User(username='test', password='test')
print(u)

if __name__ == '__main__':
    app.config.from_object(Config)
    app.run('localhost', 5555)

