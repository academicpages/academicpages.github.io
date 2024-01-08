[

![Kunal Das](https://miro.medium.com/v2/resize:fill:44:44/1*kfaefcgQPHrPsNobjuiiSg.jpeg)



](https://kunaldaskd.medium.com/?source=post_page-----775832a94f6e--------------------------------)

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

```
<span id="a22e" data-selectable-paragraph=""><br><span>parameters:</span><br><span>-</span> <span>name:</span> <span>envTarget</span><br>  <span>displayName:</span> <span>'Deployment Environment'</span><br>  <span>type:</span> <span>string</span><br>  <span>values:</span><br>  <span>-</span> <span>Stage</span><br>  <span>-</span> <span>Prod</span><br>  <br><span>-</span> <span>name:</span> <span>azureDFName</span><br>  <span>displayName:</span> <span>'Azure Data Factory Identifier'</span><br>  <span>type:</span> <span>string</span><br>  <br><span>-</span> <span>name:</span> <span>gitADFPath</span><br>  <span>displayName:</span> <span>'Git Path for ADF Publishing'</span><br>  <span>type:</span> <span>string</span><br>  <br><span>-</span> <span>name:</span> <span>azureRegion</span><br>  <span>displayName:</span> <span>'Azure Deployment Region'</span><br>  <span>type:</span> <span>string</span><br>  <br><span>-</span> <span>name:</span> <span>azureResourceGroup</span><br>  <span>displayName:</span> <span>'Resource Group in Azure'</span><br>  <span>type:</span> <span>string</span><br>  <br><span>-</span> <span>name:</span> <span>azureSubID</span><br>  <span>displayName:</span> <span>'Azure Subscription Identifier'</span><br>  <span>type:</span> <span>string</span><br>  <br><span>-</span> <span>name:</span> <span>azureRMConnectionName</span><br>  <span>displayName:</span> <span>'Azure Resource Manager Connection Identifier'</span><br>  <span>type:</span> <span>string</span><br><br><span>-</span> <span>name:</span> <span>sourceDFName</span><br>  <span>displayName:</span> <span>'Source Data Factory for ARM Template'</span><br>  <span>type:</span> <span>string</span><br><br><span>-</span> <span>name:</span> <span>targetDFName</span><br>  <span>displayName:</span> <span>'Target Data Factory for Deployment'</span><br>  <span>type:</span> <span>string</span><br><br><span>-</span> <span>name:</span> <span>modifyGlobalParams</span><br>  <span>displayName:</span> <span>'Modify Global Parameters'</span><br>  <span>type:</span> <span>boolean</span><br>  <span>default:</span> <span>false</span><br><br><br><span>stages:</span><br><span>-</span> <span>stage:</span> <span>Construct</span><br>  <span>displayName:</span> <span>'Compile and Confirm'</span><br>  <span>jobs:</span><br>  <span>-</span> <span>job:</span> <span>CompileAndCheck</span><br>    <span>displayName:</span> <span>'Compile and Confirm Azure Data Factory'</span><br>    <span>pool:</span><br>      <span>vmImage:</span> <span>'ubuntu-latest'</span><br>      <br>    <span>steps:</span><br>      <br>      <span>-</span> <span>task:</span> <span>NodeTool@0</span><br>        <span>inputs:</span><br>          <span>versionSpec:</span> <span>'14.x'</span><br>        <span>displayName:</span> <span>'Set up Node.js'</span><br>      <br>      <br>      <span>-</span> <span>task:</span> <span>Npm@1</span><br>        <span>inputs:</span><br>          <span>command:</span> <span>'install'</span><br>          <span>verbose:</span> <span>true</span><br>          <span>workingDir:</span> <span>'$(Build.Repository.LocalPath)/data-factory/'</span><br>        <span>displayName:</span> <span>'Set up npm modules'</span><br>      <br>      <br>      <span>-</span> <span>task:</span> <span>Npm@1</span><br>        <span>inputs:</span><br>          <span>command:</span> <span>'custom'</span><br>          <span>workingDir:</span> <span>'$(Build.Repository.LocalPath)/data-factory/'</span><br>          <span>customCommand:</span> <span>'run build validate $(Build.Repository.LocalPath)/data-factory /subscriptions/$(azureSubID)/resourceGroups/$(azureResourceGroup)/providers/Microsoft.DataFactory/factories/$(azureDFName)'</span><br>        <span>displayName:</span> <span>'Confirm Data Factory Setup'</span><br>      <br>      <br>      <span>-</span> <span>task:</span> <span>Npm@1</span><br>        <span>inputs:</span><br>          <span>command:</span> <span>'custom'</span><br>          <span>workingDir:</span> <span>'$(Build.Repository.LocalPath)/data-factory/'</span><br>          <span>customCommand:</span> <span>'run build export $(Build.Repository.LocalPath)/data-factory /subscriptions/$(azureSubID)/resourceGroups/$(azureResourceGroup)/providers/Microsoft.DataFactory/factories/$(azureDFName) "ArmTemplate"'</span><br>        <span>displayName:</span> <span>'Create ARM template'</span><br>      <br>      <br>      <span>-</span> <span>task:</span> <span>PublishPipelineArtifact@1</span><br>        <span>inputs:</span><br>          <span>targetPath:</span> <span>'$(Build.Repository.LocalPath)/data-factory/ArmTemplate'</span><br>          <span>artifact:</span> <span>'ArmTemplateArtifact'</span><br>          <span>publishLocation:</span> <span>'pipeline'</span><br>        <span>displayName:</span> <span>'Share ARM template'</span><br><br><br><span>-</span> <span>stage:</span> <span>DeployPhase</span><br>  <span>jobs:</span><br>  <span>-</span> <span>deployment:</span> <span>DeployToTarget</span><br>    <span>displayName:</span> <span>'Deploy to $<span>{{ parameters.envTarget }}</span> | ADF: $<span>{{ parameters.azureDFName }}</span>'</span><br>    <span>dependsOn:</span> <span>Construct</span><br>    <span>condition:</span> <span>succeeded()</span><br>    <span>environment:</span> <span>${{</span> <span>parameters.envTarget</span> <span>}}</span><br>    <span>pool:</span><br>      <span>vmImage:</span> <span>'ubuntu-latest'</span><br>    <span>strategy:</span><br>      <span>runOnce:</span><br>        <span>deploy:</span><br>          <span>steps:</span><br>            <br>            <span>-</span> <span>checkout:</span> <span>none</span><br>            <br>            <br>            <span>-</span> <span>task:</span> <span>DownloadPipelineArtifact@2</span><br>              <span>inputs:</span><br>                <span>buildType:</span> <span>'current'</span><br>                <span>artifactName:</span> <span>'ArmTemplateArtifact'</span><br>                <span>targetPath:</span> <span>'$(Pipeline.Workspace)'</span><br>              <span>displayName:</span> <span>"Retrieve ARM template"</span><br><br>            <br>            <span>-</span> <span>${{</span> <span>if</span> <span>eq(parameters.modifyGlobalParams,</span> <span>true</span><span>)</span> <span>}}:</span><br>              <span>-</span> <span>task:</span> <span>AzurePowerShell@5</span><br>                <span>displayName:</span> <span>'(Optional) Modify Global Parameters'</span><br>                <span>inputs:</span><br>                  <span>azureSubscription:</span> <span>${{</span> <span>parameters.azureRMConnectionName</span> <span>}}</span><br>                  <span>azurePowerShellVersion:</span> <span>'LatestVersion'</span><br>                  <span>ScriptType:</span> <span>'FilePath'</span><br>                  <span>ScriptPath:</span> <span>'$(Pipeline.Workspace)/GlobalParametersUpdateScript.ps1'</span><br>                  <span>ScriptArguments:</span> <span>'-globalParametersFilePath "$(Pipeline.Workspace)/*_GlobalParameters.json" -resourceGroupName "$<span>{{ parameters.azureResourceGroup }}</span>" -dataFactoryName "$<span>{{ parameters.sourceDFName }}</span>"'</span><br><br>            <br>            <span>-</span> <span>task:</span> <span>toggle-adf-trigger@2</span><br>              <span>inputs:</span><br>                <span>azureSubscription:</span> <span>${{</span> <span>parameters.azureRMConnectionName</span> <span>}}</span><br>                <span>ResourceGroupName:</span> <span>${{</span> <span>parameters.azureResourceGroup</span> <span>}}</span><br>                <span>DatafactoryName:</span> <span>${{</span> <span>parameters.targetDFName</span> <span>}}</span><br>                <span>TriggerStatus:</span> <span>'stop'</span><br><br>            <br>            <span>-</span> <span>task:</span> <span>AzureResourceManagerTemplateDeployment@3</span><br>              <span>displayName:</span> <span>'Deploy using ARM Template'</span><br>              <span>inputs:</span><br>                <span>azureResourceManagerConnection:</span> <span>${{</span> <span>parameters.azureRMConnectionName</span> <span>}}</span><br>                <span>subscriptionId:</span> <span>${{</span> <span>parameters.azureSubID</span> <span>}}</span><br>                <span>resourceGroupName:</span> <span>${{</span> <span>parameters.azureResourceGroup</span> <span>}}</span><br>                <span>location:</span> <span>${{</span> <span>parameters.azureRegion</span> <span>}}</span><br>                <span>csmFile:</span> <span>'$(Pipeline.Workspace)/ARMTemplateForFactory.json'</span><br>                <span>csmParametersFile:</span> <span>'$(Pipeline.Workspace)/ARMTemplateParametersForFactory.json'</span><br>                <span>overrideParameters:</span> <span>'-factoryName "$<span>{{ parameters.targetDFName }}</span>"'</span><br>              <br>            <br>            <span>-</span> <span>task:</span> <span>toggle-adf-trigger@2</span><br>              <span>inputs:</span><br>                <span>azureSubscription:</span> <span>${{</span> <span>parameters.azureRMConnectionName</span> <span>}}</span><br>                <span>ResourceGroupName:</span> <span>${{</span> <span>parameters.azureResourceGroup</span> <span>}}</span><br>                <span>DatafactoryName:</span> <span>${{</span> <span>parameters.targetDFName</span> <span>}}</span><br>                <span>TriggerStatus:</span> <span>'start'</span></span>
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

```
<span id="2b97" data-selectable-paragraph=""><span>{</span><br>    <span>"scripts"</span><span>:</span><span>{</span><br>        <span>"build"</span><span>:</span><span>"node node_modules/@microsoft/azure-data-factory-utilities/lib/index"</span><br>    <span>}</span><span>,</span><br>    <span>"dependencies"</span><span>:</span><span>{</span><br>        <span>"@microsoft/azure-data-factory-utilities"</span><span>:</span><span>"^1.0.0"</span><br>    <span>}</span><br><span>}</span></span>
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