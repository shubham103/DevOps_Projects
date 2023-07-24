
## Start

- Clone the repo
- git clone https://github.com/shubham103/DevOps_Projects.git
- git clone https://github.com/uditsaurabh/go-crud-api.git
- cd DevOps_Projects/A3B-Go_RestAPI
- chmod 700 prepare.sh
- ./prepare.sh
- echo "export PATH=$PATH:/usr/local/go/bin" >> .profile
- source .profile
- go version

- cd ../go-crud-api
- go get .
- go mod download
- sudo -u postgres psql
- ALTER USER postgres WITH PASSWORD 'test123';
- \q
- sed -i 's/password=password/password=test123/' db-connection.go
- go run .
