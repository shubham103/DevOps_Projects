#Problem Statement:

Create a Git repository, upload a open source GOLANG project, create a  script which will create instance of jenkins pipeline and perform the deployment steps and upload the binaries in s3.


Conversations on requirements:

 - create a repo in github and try to add people with proper accecss rights
 - need to install jenkins in ec2
 - our go code will take some x amount of time to build.. so as per the time need to choose the aws machine
 - pipeline should have three steps 
      - checkout the branch
      - test the code
      - build the binaries
      - upload the binaries in aws s3
      - archive the logs
      - create a tag in github for that commit
      - clean the workspace

     Post build actions: 
      - OnSuccess: mail the developers about the success
      - OnFailure: mail the developers about the failure with the error logs
 - I have to upload the build artifacts in aws s3

