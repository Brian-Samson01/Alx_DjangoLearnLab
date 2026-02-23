# HTTPS Deployment Configuration

This project enforces HTTPS to ensure secure communication between clients and the server.

## SSL/TLS Setup (Example using Nginx)

1. Obtain an SSL certificate (e.g., via Let's Encrypt).
2. Configure Nginx with SSL enabled:

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/private/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

3. Redirect all HTTP traffic to HTTPS:

server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

## Notes
- Django security settings enforce HTTPS at the application level.
- SSL termination is handled by the web server.