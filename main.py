from loader import app
from handlers import register_handlers

register_handlers(app)

if __name__ == "__main__":
    app.run_polling()
