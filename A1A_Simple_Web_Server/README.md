# Commands used
- sudo yum update -y
- sudo amazon-linux-extras install docker -y
- sudo usermod -aG docker ec2-user
- sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
- sudo chmod +x /usr/local/bin/docker-compose
- sudo yum install git -y
- git clone <repository_url>
- cd repo
- docker build -t mywebapp .
- docker run -d -p 5000:5000 mywebapp

