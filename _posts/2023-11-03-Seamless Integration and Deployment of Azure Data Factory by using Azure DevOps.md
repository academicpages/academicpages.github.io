# Seamless Integration and Deployment of Azure Data Factory by using Azure DevOps

![Kunal Das, Author](https://miro.medium.com/v2/resize:fill:44:44/1*kfaefcgQPHrPsNobjuiiSg.jpeg)



- [Seamless Integration and Deployment of Azure Data Factory by using Azure DevOps](#seamless-integration-and-deployment-of-azure-data-factory-by-using-azure-devops)
  - [Introduction](#introduction)
  - [Embracing Source Control in ADF](#embracing-source-control-in-adf)
  - [Advantages of Git Integration with Azure Data Factory](#advantages-of-git-integration-with-azure-data-factory)
  - [**Architecture Flow diagram**](#architecture-flow-diagram)
  - [Connecting to a Git Repository](#connecting-to-a-git-repository)
  - [Implementing the Pipeline Template](#implementing-the-pipeline-template)


## Introduction

Azure Data Factory (ADF) offers a robust platform for data integration and transformation, and when combined with continuous integration and delivery (CI/CD), it becomes a powerhouse. CI/CD in ADF context is the seamless transition of data pipelines across different environments like development, testing, and production. ADF leverages Azure Resource Manager (ARM) templates to encapsulate the configurations of its entities, such as pipelines, datasets, and data flows. There are primarily two recommended ways to transition a data factory across environments:

1.  Leveraging Azure Pipelines for an automated deployment.
2.  Manually uploading an ARM template through the Data Factory user interface integrated with Azure Resource Manager.

## Embracing Source Control in ADF

Azure Data Factory’s integration with ARM templates facilitates the deployment of pipelines. Notably, there’s a distinct ADF Publish branch and a collaboration branch.

Steps for Integrating Source Control with Branching Strategy:

1.  Initialize the Git Repository: Start by initializing a single Git repository. This repository will house multiple ADF configurations, each tailored for specific pipelines.
2.  Branching Blueprint: Designate a unique branch for every ADF, which will act as a collaboration branch. This setup will lead to the creation of distinct folders under the `adf_publish` branch. It's crucial to have separate branches for development to allow individual feature development, testing, and deployment.Important to note that we may not use this branch as we will use automated ARM tempalte publishing methood.
3.  Integrate Development Branches with Source Control: Only link the development branches with source control. This ensures continuous validation and checking of the code during its development phase. Keeping UAT/Production deployments separate ensures a clear demarcation between development and deployment phases.
4.  Pipeline Deployment: Utilize the ARM templates produced by ADF to deploy your pipelines, ensuring a uniform deployment process.
5.  Final Integration: Post thorough testing, merge the feature branches with the collaboration branch. The final version in the collaboration branch should be the one deployed to production.

## Advantages of Git Integration with Azure Data Factory

1\. **Enhanced Source Control:** As ADF tasks become increasingly critical, it’s essential to:

-   Seamlessly track and audit changes.
-   Effortlessly revert unwanted modifications.

2\. **Flexible Drafting:** Unlike direct authoring, which mandates validation for every save, Git integration allows:

-   Drafting or partial saves.
-   Incremental modifications without validation, ensuring only thoroughly tested changes are published.

3\. **Collaborative Environment & Role-Based Access:** Git facilitates:

-   Collaborative code reviews.
-   Differentiated permissions, dictating who can edit via Git and who has publishing rights.

4\. **Streamlined CI/CD Process:** Git aids in:

-   Automating release pipelines upon changes.
-   Customizing ARM template properties for cleaner configuration management.

5\. **Boosted Performance:** ADFs integrated with Git are significantly faster, loading up to a whopping 10 times quicker due to efficient resource downloading.

It’s worth noting that direct authoring in the Azure Data Factory UI becomes disabled once a Git repository is integrated. However, modifications made via PowerShell or SDK are directly published to the Data Factory service, bypassing Git.

## **Architecture Flow diagram**

![](https://miro.medium.com/v2/resize:fit:700/1*z3Maq-fWswhWLoPDNva7fA.gif)

## Connecting to a Git Repository

Configuration using Management Hub:

-   Navigate to the management hub within the ADF UI.
-   Under the Source control section, select Git configuration.
-   If no repository is linked, click on Configure.

When setting up Git in the Azure Portal, certain settings like project name and repository name need to be manually inputted.

![](https://miro.medium.com/v2/resize:fit:700/1*f5Qo3S3JmR4vclpCLWMQWA.png)

**Azure Repos Settings:**

The configuration pane will display various Azure Repos code repository settings. These settings are essential to apply the CI-CD template. For instance:

-   Repository Type: Specifies the type of the Azure Repos code repository.
-   Azure Active Directory: Your Azure AD tenant name.
-   Azure Repos Organization: Your Azure Repos organization name.
-   Project Name: Your Azure Repos project name.
-   Repository Name: Your Azure Repos code repository name.
-   Collaboration Branch: Your Azure Repos collaboration branch used for publishing.
-   Publish Branch: The branch where ARM templates related to publishing are stored.
-   Root Folder: Your root folder in your Azure Repos collaboration branch.

Ensure you enable the option in the management hub to include global parameters in the ARM template if you have declared any global parameters.

```yaml
# Parameter Definitions: Allows configuration without diving deep into the script.
parameters:
- name: envTarget
  displayName: 'Deployment Environment'
  type: string
  values:
  - Stage
  - Prod
  
- name: azureDFName
  displayName: 'Azure Data Factory Identifier'
  type: string
  
- name: gitADFPath
  displayName: 'Git Path for ADF Publishing'
  type: string
  
- name: azureRegion
  displayName: 'Azure Deployment Region'
  type: string
  
- name: azureResourceGroup
  displayName: 'Resource Group in Azure'
  type: string
  
- name: azureSubID
  displayName: 'Azure Subscription Identifier'
  type: string
  
- name: azureRMConnectionName
  displayName: 'Azure Resource Manager Connection Identifier'
  type: string

- name: sourceDFName
  displayName: 'Source Data Factory for ARM Template'
  type: string

- name: targetDFName
  displayName: 'Target Data Factory for Deployment'
  type: string

- name: modifyGlobalParams
  displayName: 'Modify Global Parameters'
  type: boolean
  default: false

# Build Phase: Validate and Create ARM templates for Data Factory using npm.
stages:
- stage: Construct
  displayName: 'Compile and Confirm'
  jobs:
  - job: CompileAndCheck
    displayName: 'Compile and Confirm Azure Data Factory'
    pool:
      vmImage: 'ubuntu-latest'
      
    steps:
      # Set up Node.js for npm tasks.
      - task: NodeTool@0
        inputs:
          versionSpec: '14.x'
        displayName: 'Set up Node.js'
      
      # Set up required npm packages for Data Factory.
      - task: Npm@1
        inputs:
          command: 'install'
          verbose: true
          workingDir: '$(Build.Repository.LocalPath)/data-factory/'
        displayName: 'Set up npm modules'
      
      # Confirm Data Factory setup.
      - task: Npm@1
        inputs:
          command: 'custom'
          workingDir: '$(Build.Repository.LocalPath)/data-factory/'
          customCommand: 'run build validate $(Build.Repository.LocalPath)/data-factory /subscriptions/$(azureSubID)/resourceGroups/$(azureResourceGroup)/providers/Microsoft.DataFactory/factories/$(azureDFName)'
        displayName: 'Confirm Data Factory Setup'
      
      # Create ARM template for Data Factory.
      - task: Npm@1
        inputs:
          command: 'custom'
          workingDir: '$(Build.Repository.LocalPath)/data-factory/'
          customCommand: 'run build export $(Build.Repository.LocalPath)/data-factory /subscriptions/$(azureSubID)/resourceGroups/$(azureResourceGroup)/providers/Microsoft.DataFactory/factories/$(azureDFName) "ArmTemplate"'
        displayName: 'Create ARM template'
      
      # Share the created ARM template for later stages.
      - task: PublishPipelineArtifact@1
        inputs:
          targetPath: '$(Build.Repository.LocalPath)/data-factory/ArmTemplate'
          artifact: 'ArmTemplateArtifact'
          publishLocation: 'pipeline'
        displayName: 'Share ARM template'

# Deployment Phase: Deploy the Data Factory using ARM template.
- stage: DeployPhase
  jobs:
  - deployment: DeployToTarget
    displayName: 'Deploy to ${{ parameters.envTarget }} | ADF: ${{ parameters.azureDFName }}'
    dependsOn: Construct
    condition: succeeded()
    environment: ${{ parameters.envTarget }}
    pool:
      vmImage: 'ubuntu-latest'
    strategy:
      runOnce:
        deploy:
          steps:
            # Skip repo checkout for faster deployment.
            - checkout: none
            
            # Retrieve the ARM template from the build phase.
            - task: DownloadPipelineArtifact@2
              inputs:
                buildType: 'current'
                artifactName: 'ArmTemplateArtifact'
                targetPath: '$(Pipeline.Workspace)'
              displayName: "Retrieve ARM template"

            # Optionally modify global parameters if needed.
            - ${{ if eq(parameters.modifyGlobalParams, true) }}:
              - task: AzurePowerShell@5
                displayName: '(Optional) Modify Global Parameters'
                inputs:
                  azureSubscription: ${{ parameters.azureRMConnectionName }}
                  azurePowerShellVersion: 'LatestVersion'
                  ScriptType: 'FilePath'
                  ScriptPath: '$(Pipeline.Workspace)/GlobalParametersUpdateScript.ps1'
                  ScriptArguments: '-globalParametersFilePath "$(Pipeline.Workspace)/*_GlobalParameters.json" -resourceGroupName "${{ parameters.azureResourceGroup }}" -dataFactoryName "${{ parameters.sourceDFName }}"'

            # Deactivate ADF Triggers after deployment.
            - task: toggle-adf-trigger@2
              inputs:
                azureSubscription: ${{ parameters.azureRMConnectionName }}
                ResourceGroupName: ${{ parameters.azureResourceGroup }}
                DatafactoryName: ${{ parameters.targetDFName }}
                TriggerStatus: 'stop'

            # Deploy using the ARM template. Override source ADF name with target ADF name.
            - task: AzureResourceManagerTemplateDeployment@3
              displayName: 'Deploy using ARM Template'
              inputs:
                azureResourceManagerConnection: ${{ parameters.azureRMConnectionName }}
                subscriptionId: ${{ parameters.azureSubID }}
                resourceGroupName: ${{ parameters.azureResourceGroup }}
                location: ${{ parameters.azureRegion }}
                csmFile: '$(Pipeline.Workspace)/ARMTemplateForFactory.json'
                csmParametersFile: '$(Pipeline.Workspace)/ARMTemplateParametersForFactory.json'
                overrideParameters: '-factoryName "${{ parameters.targetDFName }}"'
              
            # Activate ADF Triggers after deployment.
            - task: toggle-adf-trigger@2
              inputs:
                azureSubscription: ${{ parameters.azureRMConnectionName }}
                ResourceGroupName: ${{ parameters.azureResourceGroup }}
                DatafactoryName: ${{ parameters.targetDFName }}
                TriggerStatus: 'start'
```

## Implementing the Pipeline Template

This guide provides a comprehensive walkthrough on setting up and utilizing the Azure Data Factory CI/CD pipeline as defined in the YAML file. The pipeline streamlines the build and deployment of ADF artifacts to designated environments.

**Prerequisites:**

-   Azure Data Factory Instance: An active ADF instance in Azure.
-   Azure DevOps: The YAML is tailored for Azure DevOps. Ensure you have an active Azure DevOps organization and project.
-   Azure DevOps Agent: The pipeline employs the `ubuntu-latest` VM image.
-   Node.js: The initial stage requires Node.js.
-   Azure Subscription: Necessary permissions on your Azure subscription are required.

To download necessery package for the npm, keep package.json file in the parent directory

```npm
{
    "scripts":{
        "build":"node node_modules/@microsoft/azure-data-factory-utilities/lib/index"
    },
    "dependencies":{
        "@microsoft/azure-data-factory-utilities":"^1.0.0"
    }
}
```

**Repository Structure:**

The ADF code should be housed in a folder named `data-factory-directory` at the root of your repository.

**Setup & Execution:**

1.  Azure Service Connection: Establish a service connection in Azure DevOps linked to your Azure subscription.
2.  GlobalParametersUpdateScript.ps1: If the `modifyGlobalParams` flag is set to true, ensure a PowerShell script named `GlobalParamsScript.ps1` is present at the root of your repository.
3.  Using the Pipeline: Upload the YAML file to your Azure DevOps repository, create a new pipeline, fill in the parameters, trigger the pipeline, and monitor the build and deployment.

**Running the Pipeline**

Push some changes to `development`branch. and the pipeline will get triggered automatically

![](https://miro.medium.com/v2/resize:fit:378/1*Mnhcym8CgT0JHrUtyJ3Gyg.png)

Once the pipeline finished see the artifact that got published.

![](https://miro.medium.com/v2/resize:fit:251/1*81EyoKuXbjacpHwoUPn--Q.png)

Similarly once the pipeline gets approval for deployment, it will deploy the updated template to production,

![](https://miro.medium.com/v2/resize:fit:328/1*1YrpZ6Xhv8BGBuERjN1k2g.png)

**Modifications & Best Practices:**

-   Global Parameter Update: Adjust the logic in the optional global parameter update task if needed.
-   Additional Tasks: Insert any extra tasks within the steps section of the stages.
-   Permissions: Not every team member should have update permissions. Implement a system where only a select few can publish to the Data Factory.
-   Using Azure Key Vault: For security, store connection strings or passwords in Azure Key Vault or use managed identity authentication for ADF Linked Services.

In conclusion, integrating CI/CD with Azure Data Factory not only streamlines the deployment process but also enhances collaboration, auditing, and overall efficiency. With the right setup and best practices, teams can ensure seamless and error-free deployments.

## Read my blogs : 
 
<a href="https://kunaldaskd.medium.com">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Medium_%28website%29_logo.svg/798px-Medium_%28website%29_logo.svg.png" alt="Medium Logo" height="20"width="100"/>
</a>
<a href="https://dev.to/kunaldas">
    <img src="https://dev-to-uploads.s3.amazonaws.com/uploads/logos/resized_logo_UQww2soKuUsjaOGNB38o.png" alt="Dev.to Logo" height="20"width="100"/>
</a>
<a href="https://kunaldas.hashnode.dev">
    <img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1675531271955/ALEtNA1cM.png?auto=compress" alt="Hashnode Logo" height="20"width="100"/>
</a>

## Connect with Me:

<p align="left">
<a href="https://twitter.com/kunald_official" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="kunald_official" height="30" width="40" /></a>
<a href="https://linkedin.com/in/kunaldaskd" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="kunaldaskd" height="30" width="40" /></a>
</p>