from aws_cdk import (
    CfnOutput,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cpactions,
    aws_codebuild as codebuild,
    pipelines,
    SecretValue,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()
        source_action=cpactions.GitHubSourceAction(
            action_name='GitHub',
            output=source_artifact,
            oauth_token=SecretValue.secrets_manager('github-amit-pat'),
            owner='amitkbrillio',
            repo='cdk_github_pipeline',
            trigger=cpactions.GitHubTrigger.POLL)

        pipeline=codepipeline.Pipeline(self,'LambdaPipeline',
         pipeline_name='LambdaPipeline',
         stages=[
            codepipeline.StageProps(stage_name="Source",actions=[source_action]),
            codepipeline.StageProps(
                stage_name="Build",
                actions=[
                    cpactions.CodeBuildAction(
                        action_name="Build",
                        project=codebuild.PipelineProject(self,"MyProject"),
                        input=source_artifact,
                    )
                ],
            ),


         ],
        #  synth=pipelines.CodeBuildStep('Synth',
        #     input=source_artifact,
        #     install_commands=["npm install -g aws-cdk","python3 -m pip install -r requirements.txt"],
        #     commands=["cdk synth",]
            
         )
