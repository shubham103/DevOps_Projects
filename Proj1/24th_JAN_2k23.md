# Using Github actions


![workflow](https://user-images.githubusercontent.com/26185774/214270953-5b2d0cfc-408e-4e4c-8d45-a0cc941e761f.png)




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
