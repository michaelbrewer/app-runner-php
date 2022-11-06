import aws_cdk as cdk

from stack.app_stack import AppRunnerStack


app = cdk.App()
AppRunnerStack(app, "app-runner")
app.synth()
