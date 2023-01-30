#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_git_poc.cdk_git_poc_stack import CdkGitPocStack
from cdk_git_poc.pipeline_stack import PipelineStack


app = cdk.App()
env = cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"])
)
CdkGitPocStack(app, "CdkGitPocStack",env=env)
PipelineStack(app, "PipelineStack",env=env)
app.synth()
