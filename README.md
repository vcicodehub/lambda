# Python RESTful Server
A sample application that demonstrates how to build a AWS Lambda function using Python 3

### Helpful Notes
*Install Virtual Environment*
`py -m venv .venv`

*Get required libraries*
`pip install -r requirements.txt`

*Zip a local folder*
`jar -cfM {yourfile.zip} {yourfolder}`

### SAM Commands
*Deploy Lambda Function*
`sam deploy --template-file sam-template.yml --stack-name om-lambda-stack --capabilities CAPABILITY_IAM`
`sam deploy --template-file /codebuild/output/src086628328/src/packaged-template.yml --stack-name <YOUR STACK NAME>`

## Recent Error Message
> Application metadata not found in the SAM template: 'missing AWS::ServerlessRepo::Application section in template Metadata'
