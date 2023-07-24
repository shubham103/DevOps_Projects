## Docker


## golang specific version
- sudo apt update
- sudo apt upgrade -y
- curl -OL https://golang.org/dl/go1.16.7.linux-amd64.tar.gz
- sudo tar -C /usr/local -xvf go1.16.7.linux-amd64.tar.gz
- go verison
- echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile
- source ~/.profile

## install postgresql
- sudo apt install postgresql postgresql-contrib
- sudo systemctl start postgresql.service
