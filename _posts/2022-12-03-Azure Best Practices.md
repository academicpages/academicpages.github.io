# Azure Best Practices



![Kunal Das, Author](https://miro.medium.com/v2/resize:fill:44:44/1*kfaefcgQPHrPsNobjuiiSg.jpeg)


![](https://miro.medium.com/v2/resize:fit:700/0*JFxFUjxO8pAiWsq0.png)


- [Azure Best Practices](#azure-best-practices)
  - [Security:](#security)
  - [Enable Azure AD Conditional Access and enforce MFA](#enable-azure-ad-conditional-access-and-enforce-mfa)
  - [Disable RDP/SSH from the Internet](#disable-rdpssh-from-the-internet)
  - [Management:](#management)
  - [Operations:](#operations)
  - [Cost Optimization:](#cost-optimization)
  - [Services:](#services)
  - [Database](#-database)
  - [AppService:](#-appservice)
  - [Conclusion:](#conclusion)
  - [Credits:](#credits)


Azure best practices assist businesses in making the most of Azure resources to create and maintain scalable, cost-efficient, and secure solutions on the Microsoft Azure cloud. Having the correct Azure best practices can make or ruin a firm because Azure serves as the foundation of many modern organizations. I’ve covered the fundamental best practices that every Azure administrator needs to be aware of in this document. I’ve also provided advice on how to create a secure, reliable, and effective Azure infrastructure. These best practices must be followed in tandem because none of them by themselves can adequately secure the systems. You must select the best security alternatives based on your surroundings and demands, as is always the case.

## Security:

the most important thing before anything else is security, The recommendations below can help assure more robust Azure security, but they cannot serve as a complete substitute. The top practices that I believe will help you strengthen and safeguard your Azure are listed below.

## Enable Azure AD Conditional Access and enforce MFA

Azure AD Conditional Access assists administrators in enabling users to be productive whenever and wherever they choose while simultaneously safeguarding the assets of the company. Automating access control based on security, business, and compliance requirements are made possible via conditional access. Access to data and applications is protected by the addition of a crucial security layer provided by Azure AD Multi-Factor Authentication. To design an Azure Active Directory conditional access deployment and evaluate deployment considerations for Azure AD Multi-Factor Authentication, go to these Azure documentation sites (MFA).

![](https://miro.medium.com/v2/resize:fit:700/1*ujYvSNEzVu05zQDpAmkkjQ.png)

## Disable RDP/SSH from the Internet

Use JIT and Azure Bastion Do not expose RDP and SSH access over the Internet in order to provide remote access to Windows and Linux VMs in Azure from anywhere in the world without compromising security. To provide safe remote access to Azure virtual machines, use one of these techniques:

✓ **Enable site-to-site VPN or ExpressRoute connections for Just-In-Time (JIT) VM access:**

JIT offers time-limited VM access through RDP and SSH, which lessens the exposure to brute force assaults. In essence, Network Security Groups (NSGs) lock off RDP and SSH ports and only permit authorized users to access them for a predetermined time. Users can request access to JIT VMs using Azure AD and role-based Access Control (RBAC) permissions.

**✓ Configure Azure Bastion inside your virtual network.**

Direct RDP/SSH communication to your VMs over TLS from the Azure interface is made possible by Azure Bastion. The PaaS service Azure Bastion does away with the requirement for VMs to have public IP addresses, agents, or specialized client software.

![](https://miro.medium.com/v2/resize:fit:700/1*yHCrH7KDdmEHkkpwLYhQbg.png)

**Secure privileged access with Azure AD PIM**

Azure AD Privileged Identity Management enables management, control, and monitoring of access to vital resources in Azure, Microsoft 365, and Intune (PIM). Admins must activate or elevate their privilege through PIM in order to use it for a brief period of time.

![](https://miro.medium.com/v2/resize:fit:700/1*QSUyijEFHVX-AiE5FA9eqg.png)

## Management:

**Use Resource Groups; Tag individual resources:**

Create a resource group strategy that meets your company’s needs, then plan, create, and implement it. Resource groups, which are logical collections of Azure resources, containerize related resources in a group for administration simplicity, security, and cost tracking for your workloads.

![](https://miro.medium.com/v2/resize:fit:700/1*F7hE-TH6xttMSB9m2_wQWg.png)

A best practice resource group strategy should include the following: Group resources by

Environment: prod, dev, uat,stg,perf,sit

Application: BI,DWH

Business Unit: ML,DS

**Follow a well-defined naming standard**

Include resource type, application or business unit, environment, Azure region, and consecutive entity number etc.

For example, dev-ause-asy-01 means Azure Synapse Workspace in Australia South East Region which is in DEV environment.

**Leverage Resource tagging**

Tag all resources inside resource groups to communicate valuable information to your teams, discover resources, and manage costs and it is easy to delete resources as well.

![](https://miro.medium.com/v2/resize:fit:627/1*2ci7kwnh5Untp4I65UVGuw.png)

## Operations:

**Use Azure Advisor:**

Azure Advisor offers individualised, practical advice for cost, security, dependability, operational excellence, and performance. Organizations can optimise their deployments with Azure Advisor in accordance with Microsoft best practises. These suggestions are based on Microsoft best practises that are successful for most businesses and were compiled using resource configuration analysis and usage telemetry in your Azure tenant.

## Cost Optimization:

**Use reserved instances:**

Reserved instances are useful in certain circumstances, such as when you frequently employ the same VM size across several VMs. Domain controllers operating on Azure are an excellent example. On these VMs, three-year reserved instances offer savings of up to 72%.

**Delete unneeded resources:**

After VMs are decommissioned, orphan resources are frequently forgotten about and left in a tenant. These resources are pricey! Common examples of these Azure orphan resources include network cards and OS discs. Fortunately, the Azure Portal assists in reminding administrators to delete unnecessary resources at provisioning and deletion time.

## Services:

In this section let us see in detail the most used resources and the best way to use those,

➢ Virtual Machine

✓ Enforce multi-factor authentication (MFA) and complex passwords. MFA can help limit the threat of compromised credentials. Complex passwords help reduce the effectiveness of brute-force password attacks. ✓ Use just-in-time (JIT) virtual machine access. JIT access works with NSGs and the Azure firewall and helps you layer in role-based access controls (RBAC) and time-bindings on access to virtual machines.

✓ Have a patch process in place. If you’re not patching your workloads, all your other efforts may be for nothing. A single unpatched vulnerability can lead to a breach. A patch process to keep your operating systems and applications up to date helps you mitigate this risk.

✓ Lock down administrative ports. Unless necessary, restrict access to SSH, RDP, WinRM, and other administrative ports.

✓ Use the Azure firewall and network security groups (NGSs) to limit access to workloads. Consistent with the principle of least privilege, use NSGs and the Azure firewall to restrict workload access.

✓ Apply the Latest OS Patches Ensure that the latest OS patches available for Microsoft Azure virtual machines are applied.

✓ Approved Azure Machine Image in Use Ensure that all your Azure virtual machine instances are launched from approved machine images only.

✓ Enable Auto-Shutdown Configure your Microsoft Azure virtual machines to automatically shut down on a daily basis.

**➢ Storage**

✓ Restrict database and storage access. UseFirewalls and access controls to limit what level of access users, devices, and services have to your databases and storage blobs.

✓ Leverage auditing. Turn on auditing for your Azure databases. Doing so enables you to gain visibility into all database changes.

✓ Configure threat detection for Azure SQL. If you use Azure SQL, activating threat detection helps you identify security issues faster and limit dwell time.

✓ Set log alerts in Azure Monitor. It isn’t enough to simply log events. Make sure you are alerting against security-related events in Azure Monitor so you can remediate issues quickly (and automatically when possible).

✓ Enable Azure Defender for your storage accounts. Azure Defender provides you with hardening and securing your Azure storage accounts.

✓ Use soft deletes. Soft deletes help you ensure data is still retrievable (for 14 days) in the event a malicious actor (or user error) leads to data you wanted to keep — getting deleted.

✓ Use shared access signatures (SAS). SAS enables you to implement granular access controls and time limits on client access to data.

✓ Disable Anonymous Access to Blob Containers Ensure that anonymous access to blob containers is disabled within your Azure Storage account.

✓ Disable public access to storage accounts with blob containers Ensure that public access to blob containers is disabled for your Azure storage accounts to override any ACL configurations allowing access.

**➢ Network**

✓ Encrypt data in transit. As we mentioned in the encryption and data security section: encryption of data in transit (and at rest) is a must. Leverage modern encryption protocols for all network traffic.

✓ Implement zero trust. By default, network policies should deny access unless there is an explicit allow rule.

✓ Limit open ports and Internet-facing endpoints. Unless there is a well-defined business reason for a port to be open or workload to be Internet-facing, don’t let it happen.

✓ Monitor device access. Monitoring access to your workloads and devices (e.g. using a SIEM or Azure Monitor) helps you proactively detect threats

✓ Segment your networks. Logical network segmentation can help improve visibility, make your networks easier to manage and limit east-west movement in the event of a breach.

✓ Check for NSG Flow Log Retention Period Ensure that the Network Security Group (NSG) flow log retention period is greater than or equal to 90 days.

✓ Check for Network Security Groups with Port Ranges Ensure there are no network security groups with a range of ports opened to allow incoming traffic.

✓ Enable DDoS Standard Protection for Virtual Networks Ensure that DDoS standard protection is enabled for production Azure virtual networks.

✓ Monitor Network Security Group Configuration Changes Network security group changes have been detected in your Microsoft Azure cloud account.

✓ Review Network Interfaces with IP Forwarding Enabled Ensure that the Azure network interfaces with IP forwarding enabled are regularly reviewed.

## ➢ Database

➢ **Cosmos DB:**

✓ Enable Advanced Threat Protection Ensure that Advanced Threat Protection is enabled for all Microsoft Azure Cosmos DB accounts.

✓ Enable Automatic Failover Enable automatic failover for Microsoft Azure Cosmos DB accounts.

✓ Restrict Default Network Access for Azure Cosmos DB Accounts Ensure that default network access (i.e. public access) is denied within your Azure Cosmos DB accounts configuration.

**➢ SQL:**

✓ Advanced Data Security for SQL Servers Ensure that Advanced Data Security (ADS) is enabled at the Azure SQL database server level.

✓ Check for Publicly Accessible SQL Servers Ensure that Azure SQL database servers are accessible via private endpoints only.

✓ Check for Sufficient Point in Time Restore (PITR) Backup Retention Period Ensure there is a sufficient PITR backup retention period configured for Azure SQL databases.

✓ Check for Unrestricted SQL Database Access Ensure that no SQL databases allow unrestricted inbound access from 0.0.0.0/0 (any IP address).

✓ Configure “AuditActionGroup” for SQL Server Auditing Ensure that “AuditActionGroup” property is well configured at the Azure SQL database server level.

✓ Configure Emails for Vulnerability Assessment Scan Reports and Alerts Ensure that “Send scan reports to” setting is configured for SQL database servers.

✓ Detect Create, Update, and Delete SQL Server Firewall Rule Events SQL Server firewall rule changes have been detected in your Microsoft Azure cloud account.

✓ Enable All Types of Threat Detection on SQL Servers Enable all types of threat detection for your Microsoft Azure SQL database servers.

✓ Enable Auditing for SQL Servers Ensure that database auditing is enabled at the Azure SQL database server level.

✓ Enable Auto-Failover Groups Ensure that your Azure SQL database servers are configured to use auto-failover groups.

✓ Enable Automatic Tuning for SQL Database Servers Ensure that Automatic Tuning feature is enabled for Microsoft Azure SQL database servers.

✓ Enable Transparent Data Encryption for SQL Databases Ensure that Transparent Data Encryption (TDE) is enabled for every Azure SQL database.

✓ Enable Vulnerability Assessment Email Notifications for Admins and Subscription Owners Ensure that the Vulnerability Assessment setting “Also send email notification to admins and subscription owners” is enabled. Enable Vulnerability Assessment Periodic Recurring Scans Ensure that the Vulnerability Assessment Periodic Recurring Scans setting is enabled for SQL database servers.

✓ Enable Vulnerability Assessment for Microsoft SQL Servers Ensure that Vulnerability Assessment is enabled for Microsoft SQL database servers.

✓ SQL Auditing Retention Ensure that SQL database auditing has a sufficient log data retention period configured.

✓ Use Azure Active Directory Admin for SQL Authentication Ensure that an Azure Active Directory (AAD) admin is configured for SQL authentication.

✓ Use BYOK for Transparent Data Encryption Use Bring Your Own Key (BYOK) support for Transparent Data Encryption (TDE).

**➢ PostgreSQL**

✓ Check for PostgreSQL Log Retention Period Ensure that PostgreSQL database servers have a sufficient log retention period configured.

✓ Check for PostgreSQL Major Version Ensure that PostgreSQL database servers are using the latest major version of PostgreSQL database.

✓ Enable “CONNECTION\_THROTTLING” Parameter for PostgreSQL Servers Ensure that “connection\_throttling” parameter is set to “ON” within your Azure PostgreSQL server settings.

✓ Enable “LOG\_CHECKPOINTS” Parameter for PostgreSQL Servers Enable “log\_checkpoints” parameter for your Microsoft Azure PostgreSQL database servers.

✓ Enable “LOG\_CONNECTIONS” Parameter for PostgreSQL Servers Enable “log\_connections” parameter for your Microsoft Azure PostgreSQL database servers.

✓ Enable “LOG\_DISCONNECTIONS” Parameter for PostgreSQL Servers Enable “log\_disconnections” parameter for your Microsoft Azure PostgreSQL database servers.

✓ Enable “LOG\_DURATION” Parameter for PostgreSQL Servers Enable “log\_duration” parameter on your Microsoft Azure PostgreSQL database servers.

✓ Enable “log\_checkpoints” Parameter for PostgreSQL Flexible Servers Enable “log\_checkpoints” parameter for your Microsoft Azure PostgreSQL flexible database servers.

✓ Enable In-Transit Encryption for PostgreSQL Database Servers Ensure that in-transit encryption is enabled for your Azure PostgreSQL database servers.

✓ Enable Infrastructure Double Encryption for Single Servers Ensure that infrastructure double encryption is enabled for Single Server Azure PostgreSQL database servers.

✓ Use Azure Active Directory Admin for PostgreSQL Authentication Ensure that an Azure Active Directory (AAD) admin is configured for PostgreSQL authentication.

**➢ MySQL:**

✓ Configure TLS Version for MySQL Flexible Database Servers Ensure that the ‘tls\_version’ parameter is set to a minimum of ‘TLSV1.2’ for all MySQL flexible database servers.

✓ Enable In-Transit Encryption for MySQL Servers Ensure that in-transit encryption is enabled for your Azure MySQL database servers.

## ➢ AppService:

✓ Check for Latest Version of .NET Framework Enable HTTP to HTTPS redirects for your Microsoft Azure App Service web applications.

✓ Check for Latest Version of Java Ensure that Azure App Service web applications are using the latest stable version of Java.

✓ Check for Latest Version of PHP Ensure that Azure App Service web applications are using the latest version of PHP.

✓ Check for Latest Version of Python Ensure that Azure App Service web applications are using the latest version of Python.

✓ Check for Sufficient Backup Retention Period Ensure there is a sufficient backup retention period configured for Azure App Services applications.

✓ Check for TLS Protocol Latest Version Ensure that Azure App Service web applications are using the latest version of TLS encryption.

✓ Disable Plain FTP Deployment Ensure that FTP access is disabled for your Azure App Services web applications.

✓ Disable Remote Debugging Disable Remote Debugging feature for your Microsoft Azure App Services web applications.

✓ Enable Always On Ensure that your Azure App Services web applications stay loaded all the time by enabling the Always On feature.

✓ Enable App Service Authentication Ensure that App Service Authentication is enabled within your Microsoft Azure cloud account.

✓ Enable Application Insights Ensure that Azure App Services applications are configured to use Application Insights feature.

✓ Enable Automated Backups Ensure that all your Azure App Services applications are using the Backup and Restore feature.

✓ Enable FTPS-Only Access Enable FTPS-only access for your Microsoft Azure App Services web applications.

✓ Enable HTTP/2 Ensure that Azure App Service web applications are using the latest stable version of HTTP.

✓ Enable HTTPS-Only Traffic Enable HTTP to HTTPS redirects for your Microsoft Azure App Service web applications.

✓ Enable Incoming Client Certificates Ensure that Azure App Service web applications are using incoming client certificates.

✓ Enable Registration with Azure Active Directory Ensure that registration with Azure Active Directory is enabled for Azure App Service applications.

✓ Use Key Vaults to Store App Service Application Secrets Ensure that Azure Key Vaults are used to store App Service application secrets.

**➢ KeyVault**

✓ App Tier Customer-Managed Key In Use Ensure that a Customer-Managed Key is created for your Azure cloud application tier.

✓ Check for Allowed Certificate Key Types Ensure that Azure Key Vault certificates are using the appropriate key type(s).

✓ Check for Azure Key Vault Keys Expiration Date Ensure that your Azure Key Vault encryption keys are renewed prior to their expiration date.

✓ Check for Azure Key Vault Secrets Expiration Date Ensure that your Azure Key Vault secrets are renewed prior to their expiration date.

✓ Check for Certificate Minimum Key Size Ensure that Azure Key Vault RSA certificates are using the appropriate key size.

✓ Check for Key Vault Full Administrator Permissions Ensure that no Azure user, group or application has full permissions to access and manage Key Vaults.

✓ Check for Sufficient Certificate Auto-Renewal Period Ensure there is a sufficient period configured for the SSL certificates auto-renewal.

✓ Database Tier Customer-Managed Key In Use Ensure that a Customer-Managed Key is created for your Microsoft Azure cloud database tier.

✓ Enable AuditEvent Logging for Azure Key Vaults Ensure that AuditEvent logging is enabled for your Microsoft Azure Key Vaults.

✓ Enable Certificate Transparency Ensure that certificate transparency is enabled for all your Azure Key Vault certificates.

✓ Enable Key Vault Recoverability Ensure that your Microsoft Azure Key Vault instances are recoverable.

✓ Enable SSL Certificate Auto-Renewal Ensure that Auto-Renewal feature is enabled for your Azure Key Vault SSL certificates.

✓ Enable Trusted Microsoft Services for Key Vault Access Allow trusted Microsoft services to access your Azure Key Vault resources (i.e. encryption keys, secrets and certificates).

✓ Restrict Default Network Access for Azure Key Vaults Ensure that default network access (i.e. public access) rule is set to “Deny” within your Azure Key Vaults configuration.

✓ Set Azure Secret Key Expiration Ensure that an expiration date is set for all your Microsoft Azure secret keys.

✓ Set Encryption Key Expiration Ensure that an expiration date is configured for all your Microsoft Azure encryption keys.

✓ Web Tier Customer-Managed Key In Use Ensure that a Customer-Managed Key is created for your Microsoft Azure cloud web tier

## Conclusion:

There are numerous Azure features and services that require ongoing maintenance in terms of security. There are countless ways to attack a system, and poorly protected systems are the ones that hackers most frequently target. By keeping a few simple things in mind, you can strengthen your network considerably. With some investment and your work, you can make your Azure secure and robust by using a variety of Azure services.

## Credits:

[https://learn.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns](https://learn.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns)


## Read my blogs:
[![Medium](https://i.imgur.com/TgYYM9w.png)](https://kunaldaskd.medium.com)
[![DEV](https://i.imgur.com/bp3qHWb.png)](https://dev.to/kunaldas)
[![Hashnode](https://i.imgur.com/iwZwo2S.png)](https://kunaldas.hashnode.dev)

## Connect with Me:
[![Twitter](https://i.imgur.com/VaorXDP.png)](https://twitter.com/kunald_official)
[![LinkedIn](https://i.imgur.com/ktIHVxm.png)](https://linkedin.com/in/kunaldaskd)

