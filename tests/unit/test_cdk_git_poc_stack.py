import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_git_poc.cdk_git_poc_stack import CdkGitPocStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_git_poc/cdk_git_poc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkGitPocStack(app, "cdk-git-poc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
