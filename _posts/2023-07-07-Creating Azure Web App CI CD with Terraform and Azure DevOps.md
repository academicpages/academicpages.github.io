# Step-by-Step Guide: Creating Azure Web App CI/CD with Terraform and Azure DevOps

![Kunal Das, Author](https://miro.medium.com/v2/resize:fill:44:44/1*kfaefcgQPHrPsNobjuiiSg.jpeg)

Read on : 
 
<a href="https://kunaldaskd.medium.com/?source=post_page-----986bb257ea4--------------------------------">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Medium_%28website%29_logo.svg/798px-Medium_%28website%29_logo.svg.png" alt="Medium Logo" width="200"/>
</a>



![](https://miro.medium.com/v2/resize:fit:700/1*hj3ezml_2bs9uDUssU4oLQ.png)



Introduction:  
In today’s fast-paced development environment, implementing Continuous Integration and Continuous Deployment (CI/CD) is crucial for efficient software delivery. In this tutorial, we will walk through the process of setting up a CI/CD pipeline for an Azure web app using Terraform and Azure DevOps. By following these steps, you can automate the deployment process and ensure high-quality code reaches your production environment.

Prerequisites:  
Before we begin, make sure you have the following prerequisites in place:  
\- An Azure DevOps account  
\- Access to an Azure subscription  
\- Basic knowledge of Terraform and Docker

Step 1: Creating Infrastructure with Terraform  
To ensure a consistent and repeatable infrastructure setup, we will use Terraform. Terraform allows us to define our infrastructure as code and manage it through version control. Follow these steps to create the necessary infrastructure for your Azure web app:

1\. Set up a new Azure DevOps project.  
2\. Create a new repository within your project and clone it to your local machine.  
3\. Create a folder structure for your Terraform code, such as “infra/environment1” and “infra/environment2” for two environments.  
4\. Within each environment folder, create a main.tf file and define the necessary Azure resources, such as resource groups, app services, and databases. Use Terraform modules to ensure a modular and reusable infrastructure setup.  
5\. Define input variables in a separate variable.tf file to make your infrastructure code dynamic and easily configurable.  
6\. Initialize Terraform within each environment folder by running the \`terraform init\` command. This will download the required providers and modules.  
7\. Create a build pipeline in Azure DevOps to trigger the Terraform deployment. Use the “Terraform CLI” task to execute Terraform commands, passing the appropriate input variables for each environment.

Step 2: CI Steps  
In this step, we will set up Continuous Integration (CI) to ensure code quality and generate artifacts for deployment.

1\. Configure your source code repository in Azure DevOps to trigger the CI pipeline on code changes.  
2\. Set up a build pipeline in Azure DevOps with the following steps:  
a. Use a task to install the required dependencies for your application, such as Python packages.  
b. Run unit tests using your preferred testing framework (e.g., pytest) to ensure code functionality.  
c. Use linters (flake8, black) and formatters (isort) to enforce code style consistency.  
d. Generate a code coverage report using coverage.py to track the percentage of code covered by tests.  
e. Integrate with SonarQube for static code analysis and maintain code quality.  
f. Build a Docker image containing your application code and dependencies.  
g. Push the Docker image to an Azure Container Registry (ACR) for later use in deployment.

Step 3: CD — Continuous Deployment  
Now that we have our infrastructure in place and a reliable CI process, we can proceed to set up Continuous Deployment (CD) to automate the deployment process.

1\. Determine the deployment strategy based on your requirements. For example:  
— Two environments (dev and prod) can follow a simple deployment flow where the code is deployed to dev first and then promoted to prod after successful testing.  
— Three environments (dev, test, and prod) can follow a more complex deployment flow where code moves through each environment sequentially.  
2\. Create release pipelines in Azure DevOps for each environment, using the appropriate deployment strategy.  
3\. Configure post-deployment tests specific to each environment to ensure the deployed application is functioning as expected.  
4\. Add performance testing steps after the deployment to the dev environment to validate system

performance under real-world conditions. Use tools like Apache JMeter or Azure Application Insights to conduct performance tests.

Certainly! Below are the code snippets for each step, following a generic parameterized approach and best practices:

Step 1: Creating Infrastructure with Terraform

1\. Set up Azure DevOps pipeline:  
— Create a new pipeline in Azure DevOps and select your repository.  
— Choose the appropriate trigger for your pipeline, such as a repository branch or pull request.

2\. Configure Terraform backend:  
— Create an Azure Storage Account to store Terraform state.  
— Add the following code to your \`main.tf\` file within each environment folder:

```tf
terraform {
 backend “azurerm” {
 storage_account_name = “<storage_account_name>”
 container_name = “<container_name>”
 key = “<environment>.tfstate”
 }
}
```

3\. Define variables:  
```tf
variable "environment" {
 type = string
 description = "Environment name"
}
variable "resource_group_name" {
 type = string
 description = "Name of the resource group"
}
# Add more variables as per your infrastructure requirements
```
— Create a \`variables.tf\` file within each environment folder to define input variables. Here’s an example:

4\. Create infrastructure resources:  
```tf
resource "azurerm_resource_group" "rg" {
 name = var.resource_group_name
 location = "West US"
}
resource "azurerm_app_service_plan" "app_service_plan" {
 name = "${var.environment}-app-service-plan"
 location = azurerm_resource_group.rg.location
 resource_group_name = azurerm_resource_group.rg.name
 kind = "Linux"
 reserved = true
sku {
 tier = "Basic"
 size = "B1"
 }
}
# Add more resources as per your infrastructure requiremen
```
Add the following code to create a resource group and app service plan in the \`main.tf\` file within each environment folder:
```tf
- task: UsePythonVersion@0
 inputs:
 versionSpec: '3.x'
 addToPath: true
- task: TerraformInstaller@0
 inputs:
 terraformVersion: 'latest'
- task: TerraformCLI@0
 inputs:
 command: 'init'
 workingDirectory: 'infra/environment1'
- task: TerraformCLI@0
 inputs:
 command: 'apply'
 workingDirectory: 'infra/environment1'
 environmentServiceNameAzureRM: '<connection_name>'
 commandOptions: '-auto-approve'
```
5\. Execute Terraform commands in Azure DevOps pipeline:

Add the following steps to your Azure DevOps pipeline YAML file:

Step 2: CI Steps

1\. Configure CI pipeline triggers and variables:  
— Define your pipeline triggers and variables in the Azure DevOps YAML file, as per your requirements.

2\. Set up build steps:  
— Use appropriate task names and commands based on your specific needs. Here’s an example:
```yaml
- task: UsePythonVersion@0
 inputs:
 versionSpec: '3.x'
 addToPath: true
- task: PythonScript@0
 inputs:
 scriptSource: 'filePath'
 scriptPath: 'scripts/install_dependencies.py'
- task: PythonScript@0
 inputs:
 scriptSource: 'filePath'
 scriptPath: 'scripts/run_unit_tests.py'
- task: CmdLine@2
 inputs:
 script: |
 pip install coverage
 coverage run - source=src -m pytest
 coverage xml -o coverage.xml
- task: SonarQubePrepare@4
 inputs:
 SonarQube: '<SonarQube_connection_name>'
 scannerMode: 'CLI'
 cliProjectKey: '<project_key>'
 cliProjectName: '<project_name>'
 cliSources: 'src'
 extraProperties: |
 sonar.coverage.reportPaths=coverage.x
```
3\. Build and push Docker image:  
— Use the appropriate task names and commands based on your specific needs. Here’s an example:
```yaml
- task: Docker@2
 inputs:
 containerRegistry: '<container_registry_connection_name>'
 repository: '<image_repository_name>'
 command: 'buildAndPush'
 Dockerfile: 'Dockerfile'
 tags: '$(Build.BuildId)'
```
Step 3: CD — Continuous Deployment

1\. Determine deployment strategy and set up release pipelines:  
— Based on your deployment strategy, define the release pipelines in Azure DevOps with appropriate stages and triggers.

2\. Configure post-deployment tests:  
— Use the appropriate tasks and scripts to run post-deployment tests. Here’s an example:

```yaml  
- task: PythonScript@0  
inputs:  
scriptSource: ‘filePath’  
scriptPath: ‘scripts/post\_deployment\_tests.py’  
arguments: ‘-e $(environment)’

- task: PublishTestResults@2  
inputs:  
testResultsFormat: ‘JUnit’  
testResultsFiles: ‘\*\*/test-results.xml’  
searchFolder: ‘$(System.DefaultWorkingDirectory)’  
```

3\. Perform performance testing:  
— Use the appropriate tasks and scripts to perform performance testing. Here’s an example using Apache JMeter:

```yaml
- task: DownloadFile@1  
inputs:  
sourceUrl: ‘[https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-5.4.1.tgz'](https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-5.4.1.tgz')  
targetPath: ‘$(Pipeline.Workspace)/jmeter/apache-jmeter-5.4.1.tgz’

- task: ExtractFiles@1  
inputs:  
archiveFilePatterns: ‘$(Pipeline.Workspace)/jmeter/apache-jmeter-5.4.1.tgz’  
destinationFolder: ‘$(Pipeline.Workspace)/jmeter/’

- task: CmdLine@2  
inputs:  
script: |  
$(Pipeline.Workspace)/jmeter/apache-jmeter-5.4.1/bin/jmeter -n -t $(Pipeline.Workspace)/jmeter/performance\_test.jmx -l $(Pipeline.Workspace)/jmeter/results.jtl  
```

Note: The provided code snippets serve as examples and may require modifications based on your specific application, environment, and tools being used.

Remember to update the connection names, resource names, and specific command arguments according to your project setup and requirements.