# The trick to not using a self-hosted agent in Azure DevOps

![Kunal Das, Author](https://miro.medium.com/v2/resize:fill:44:44/1*kfaefcgQPHrPsNobjuiiSg.jpeg)

Read on : 
 
<a href="https://kunaldaskd.medium.com/?source=post_page-----986bb257ea4--------------------------------">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Medium_%28website%29_logo.svg/798px-Medium_%28website%29_logo.svg.png" alt="Medium Logo" width="200"/>
</a>


![](https://miro.medium.com/v2/resize:fit:700/0*abFuG6O6narmeqHG.png)



Well, when you want to design the build and release pipeline for any software development the one thing that comes to mind is where to do the whole operation.  
apparently, There are two ways of doing it,  
The **free** and easy way is to use a Microsoft Hosted build agent,  
But in some cases, we may need to use a Self-hosted build agent,  
let’s see what Microsoft has to say about self-hosted build agents.

> “_An agent that you set up and manage on your own to run jobs is a self-hosted agent. You can use self-hosted agents in Azure Pipelines or Azure DevOps Server, formerly named Team Foundation Server (TFS). Self-hosted agents give you more control to install dependent software needed for your builds and deployments. Also, machine-level caches and configuration persist from run to run, which can boost speed._”

So, Self-hosted build agents do provide some benefits, but in my experience, some of these benefits can be achieved in Microsoft-hosted build agents as well.

For instance, if you have a relatively small build/release pipeline there’s no need to cache dependencies as it may give you a faster build time but do you really need it?

Now let’s see what a Microsoft hosted agent is as per them,

> “If your pipelines are in Azure Pipelines, then you’ve got a convenient option to run your jobs using a Microsoft-hosted agent. With Microsoft-hosted agents, maintenance and upgrades are taken care of for you. Each time you run a pipeline, you get a fresh virtual machine for each job in the pipeline. The virtual machine is discarded after one job (which means any change that a job makes to the virtual machine file system, such as checking out code, will be unavailable to the next job). Microsoft-hosted agents can run jobs [directly on the VM](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/phases?view=azure-devops) or [in a container](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/container-phases?view=azure-devops).”

So as you can see these agents are ephemeral by nature so we can not use them for something permanent right?  
well, yes but there are some other wat to look at it.

In this article, I have a solution for a different problem, which is using a self-hosted build agent to overcome firewall restrictions set in different azure resources.  
But first, let’s understand the problem.

![](https://miro.medium.com/v2/resize:fit:700/1*rwz0eIvDmzvio7MFr43h3A.png)

Firewall restriction in a Synapse workspace

In the image, you can see public network access can be disabled. in that case, you will not be able to connect to this resource from the DevOps pipeline,  
In some places, I have seen people using a self-hosted agent just for this purpose but actually, this is not required.

The process here is adding the IP address as a rule into the firewall

![](https://miro.medium.com/v2/resize:fit:700/1*g2IzHucCpL6hTXDkObsuNQ.png)

and you can do just that from the CI/CD pipeline itself,  
Let’s look at how to achieve that.

I am taking the example of Synapse,  
So just before the deployment task add an Azure CLI task in the pipeline.

![](https://miro.medium.com/v2/resize:fit:700/1*YgKInr79mSDS2UZ7BkKwCw.png)

and write the PowerShell script to add the build agent IP into the synapse workspace, needless to say, you need to give the service connection proper role to perform the action.
```bash
az synapse workspace firewall-rule create --name devops-build-agent-ip\
--workspace-name synapse-prod --resource-group synapse-prod-rg\
--start-ip-address  (Invoke-RestMethod http://ipinfo.io/json | Select -exp ip) \
--end-ip-address  (Invoke-RestMethod http://ipinfo.io/json | Select -exp ip)
```
If you like to use Yaml then here is the code!
```yaml
steps:
- task: AzureCLI@2
  displayName: 'Add Build agent Ip to firewall'
  inputs:
    azureSubscription: 'sp-dev'
    scriptType: ps
    scriptLocation: inlineScript
    inlineScript: 'az synapse workspace firewall-rule create --name devops-build-agent-ip --workspace-name qa1-ause-asy-01 --resource-group QA1-AUSE-ASY-ARG-01 --start-ip-address  (Invoke-RestMethod http://ipinfo.io/json | Select -exp ip) --end-ip-address  (Invoke-RestMethod http://ipinfo.io/json | Select -exp ip)'

```
Now, as we can add the firewall rule we can delete the rule too, for that use the below code
```bash
az synapse workspace firewall-rule create --name devops-build-agent-ip\
--workspace-name synapse-prod --resource-group synapse-prod-rg --yes
```
and that is it.  
once you run the deployment it will copy the IP to the build agent add it into the firewall rule then run the deployment and then delete it, but

Feel free to reach me incase of any issues!!  
adios