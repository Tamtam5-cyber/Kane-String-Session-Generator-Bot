from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "25811007"))
API_HASH = environ.get("API_HASH", "72cc7062951f56abb5240994690e49de")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7789014828:AAHCFG1-ZswdY8nJUAC4HAwnUrT3O0GWxjE")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7240555847")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002271972643")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://nguyenkhactam5:q1231234@cluster0.srj0a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
