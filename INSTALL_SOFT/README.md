## Docker


## golang specific version
- sudo apt update
- sudo apt upgrade -y
- curl -OL https://golang.org/dl/go1.18.linux-amd64.tar.gz
- sudo tar -C /usr/local -xvf go1.18.linux-amd64.tar.gz
- echo "export PATH=$PATH:/usr/local/go/bin" >> .profile
- source .profile
- go verison

## install postgresql
- sudo apt install postgresql postgresql-contrib -y
- sudo systemctl start postgresql.service
