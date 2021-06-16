echo off
echo Building Lambda zip...
mkdir .build
xcopy /seqy .\.venv\Lib\site-packages\* .\.build
rmdir /Q /S .\.build\psycopg2
xcopy .\aws-psycopg2\* .\.build\psycopg2\
xcopy .\*.py .\.build\
7z a lambda.zip -r .\.build\*
rmdir /Q /S .\.build
