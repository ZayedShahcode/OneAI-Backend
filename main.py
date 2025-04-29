from dotenv import load_dotenv
from app import create_app
import os
load_dotenv()

app = create_app()
port = os.getenv('PORT', 5000)

if __name__== '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(port)) 