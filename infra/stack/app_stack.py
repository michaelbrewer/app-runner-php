from constructs import Construct
from aws_cdk import Stack
import aws_cdk.aws_apprunner_alpha as apprunner


class AppRunnerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        apprunner.Service(
            self,
            "AppRunnerDemo",
            source=apprunner.Source.from_git_hub(
                repository_url="https://github.com/michaelbrewer/app-runner-php",
                branch="main",
                configuration_source=apprunner.ConfigurationSourceType.REPOSITORY,
                connection=apprunner.GitHubConnection.from_connection_arn(
                    "arn:aws:apprunner:us-east-2:254688924456:connection/personal/19f5f17f173846a88abd163c3bdf6fa1"
                ),
            ),
        )
