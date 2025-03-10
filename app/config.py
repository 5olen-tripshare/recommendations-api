#MONGO_URI = "mongodb://host.docker.internal:27017/"
MONGO_URI = "mongodb://mongodb-0.mongodb-service:27017,mongodb-1.mongodb-service:27017,mongodb-2.mongodb-service:27017/TripShare?replicaSet=rs0&authSource=admin"
DB_NAME = "TripShare"
