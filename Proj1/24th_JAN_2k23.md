# Using Github actions


![new_workflow drawio](https://user-images.githubusercontent.com/26185774/214272440-d7f71e85-83b4-4a0f-b67d-473dcbe7dbd4.png)




#####  GitHub Main branch
- In this main branch is protected.
- No one can directly push to main branch
- Pull request required atleat one owner approval

- There are two workflows
   - one when someone push some commit in develop branch
      - This will test the code, run the code, build the binaries and upload the binary in AWS S3 bucket. 
   - second when some PR for main branch get approves.
      - This will create a new release tag in master branch

##### S3 policies

- only "shubham" user can upload the files
- versioning is on
- More than 3 months old data will automatically move to AWS S3 Glacier.
