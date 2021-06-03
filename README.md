# Python RESTful Server
A sample application that demonstrates how to build a RESTful service using Python 3

### Helpful Notes
*Install Virtual Environment*
`py -m venv .venv`

*DOSKEY marcos*
`doskey /macros` - show all of the current macros
`doskey aws=docker run --rm -it -v %userprofile%\.aws:/root/.aws -v %cd%\aws amazon/aws-cli $*`

*Get required libraries*
`pip install -r requirements.txt`

*Zip a local folder*
`jar -cfM {yourfile.zip} {yourfolder}`

### SAM Commands
*Deploy Lambda Function*
`sam deploy --template-file sam-template.yml --stack-name om-lambda-stack --capabilities CAPABILITY_IAM`