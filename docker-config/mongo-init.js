connection = new Mongo();
db = connection.getDB("popular_articles");
db.createCollection("init");
db.createUser({
    user: "user",
    pwd: "pwd",
    roles: [
        {
            role: "readWrite",
            db: "popular_articles"
        }
    ]
});
connection.close();