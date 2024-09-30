# 1
GET /index HTTP/1.0
Host: yourdomain.com

# 2
POST /api/login HTTP/1.0
Host: yourdomain.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
username=Alice&password=secret

# 3
GET http://example.com/home HTTP/1.1
Host: example.com

# 4
GET http://example.com/data HTTP/1.1
Host: example.com
Accept: application/json

# 5
POST http://example.com/api/messages HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 37

{"username": "Alice", "msg": "Hello"}

# 6
PUT http://example.com/api/messages/42 HTTP/1.1
Host: example.com
Content-Type: text/plain
Content-Length: 17

Updated message

# 7
DELETE http://example.com/api/messages/42 HTTP/1.1
Host: example.com