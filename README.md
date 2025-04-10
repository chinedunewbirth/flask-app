# Flask-App-CICD-AWS-GitHub-Action-2
Continuously Build &amp; Deploy a Python Flask App (with SQLite) on AWS EC2 using GitHub Actions, and execute it via WSGI (Gunicorn) - great job ---

🔧 Tech Stack

Flask (Python micro web framework)

SQLite (lightweight DB)

WSGI via Gunicorn

AWS EC2 (Ubuntu instance)

GitHub Actions (CI/CD)

Nginx (optional, for reverse proxy)

🧱 Project Structure

flask-app/
│
├── app.py
├── requirements.txt
├── database.db
├── .github/
│   └── workflows/
│       └── deploy.yml
├── wsgi.py
└── templates/
    └── index.html

Create EC2 Instance on AWS

-> Launch a Ubuntu instance.

-> SSH into it.

-> Install dependencies

Add GitHub Secrets

EC2_HOST → public IP of EC2

EC2_USER → usually ubuntu

EC2_SSH_KEY → private key content (from ~/.ssh/id_rsa)

Optional: Setup Nginx as Reverse Proxy

sudo nano /etc/nginx/sites-available/flask
server {
    listen 80;
    server_name your_ec2_public_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

⚙️ If you're using a Systemd service (gunicorn.service)

sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/flask-app
Environment="PATH=/home/ubuntu/flask-app/venv/bin"
ExecStart=/home/ubuntu/flask-app/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 wsgi:app

[Install]
WantedBy=multi-user.target

then run

sudo systemctl daemon-reexec       # Refresh systemd
sudo systemctl daemon-reload
sudo systemctl restart gunicorn    # 🔁 Restart Gunicorn
sudo systemctl status gunicorn     # ✅ Check status

after which try this

sudo systemctl stop gunicorn

sudo systemctl start gunicorn

sudo systemctl enable gunicorn (auto-start on reboot)
