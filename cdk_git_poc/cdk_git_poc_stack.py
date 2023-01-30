from os import path
from aws_cdk import (
    CfnOutput,
    aws_lambda as lmb,
    aws_apigateway as apigw,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkGitPocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        this_dir=path.dirname(__file__)
        handler=lmb.Function(
            self,'Handler',
            runtime=lmb.Runtime.PYTHON_3_7,
            code=lmb.Code.from_asset(path.join(this_dir,'lambda_code')),
            handler='handler.handler'
        )
        gw=apigw.LambdaRestApi(
            self,'Endpoint',
            description='Endpoint for a simple lambda-powered web service.',
            handler=handler.current_version
        )
        self.url_output=CfnOutput(self,'Url',value=gw.url
        
        )

