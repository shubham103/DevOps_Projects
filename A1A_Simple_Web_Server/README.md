# Commands used
- sudo yum update -y
- sudo yum install docker -y
- sudo usermod -aG docker ec2-user
- sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
- sudo chmod +x /usr/local/bin/docker-compose
- sudo yum install git -y
- git clone https://github.com/shubham103/DevOps_Projects.git
- cd repo
- docker build -t mywebapp .
- docker run -d -p --name testbuild 5000:5000 mywebapp

## installing and congifuring nginx
- sudo yum install nginx -y
- sudo rm /etc/nginx/nginx.conf
- sudo vim /etc/nginx/nginx.conf  // paste the content from config dir in this repo
- sudo vim /etc/nginx/conf.d/mywebapp.conf // paste the content from config dir in this repo
- sudo systemctl restart nginx

## Installing and configuring Prometheus and Graffana
- wget https://github.com/prometheus/prometheus/releases/download/v2.37.0/prometheus-2.37.0.linux-amd64.tar.gz
- tar xvfz prometheus-2.37.0.linux-amd64.tar.gz
- cd prome*
- vim prometheus.yml   // paste the content from congig dir
- ./prometheus --config.file=prometheus.yml

- wget https://dl.grafana.com/oss/release/grafana-10.0.2.linux-amd64.tar.gz
- tar xvfz grafana-10.0.2.linux-amd64.tar.gz
- cd grafana-10.0.2/
- ./bin/grafana-server

