# Deploying Azure Data Factory, Azure Data bricks, Azure Data Lake storage & MySql DB using Terraform

![Kunal Das, Author](https://miro.medium.com/v2/resize:fill:44:44/1*kfaefcgQPHrPsNobjuiiSg.jpeg)


Here I am going to share some terraform code to deploy ADF, ADLS, ADB, and several other necessary resources.

## Table of Contents
- [Deploying Azure Data Factory, Azure Data bricks, Azure Data Lake storage \& MySql DB using Terraform](#deploying-azure-data-factory-azure-data-bricks-azure-data-lake-storage--mysql-db-using-terraform)
  - [Table of Contents](#table-of-contents)
  - [Resource Group](#resource-group)
  - [**Azure Data Factory:**](#azure-data-factory)
  - [**Azure Data Bricks:**](#azure-data-bricks)
  - [Virtual network:](#virtual-network)
  - [Network Security group for ADB:](#network-security-group-for-adb)
  - [Public subnet for Databricks:](#public-subnet-for-databricks)
  - [Private subnet for Databricks:](#private-subnet-for-databricks)
  - [Network security group for Public subnet:](#network-security-group-for-public-subnet)
  - [Network security group for Privatesubnet:](#network-security-group-for-privatesubnet)
  - [Data Lake storage account:](#data-lake-storage-account)
  - [Storage account container:](#storage-account-container)
  - [Storage Admin password:](#storage-admin-password)
  - [SQL server :](#sql-server-)
  - [SQL Database:](#sql-database)

Let’s start with a resource group where we will store all the resources required.

## Resource Group
```tf
data "azurerm_client_config" "Current" {}
resource "azurerm_resource_group" "RG" {
  name     = var.ResourceGroup.Name
  location = var.ResourceGroup.Location
}
```

_points to note that we will fetch the RG name and RG location in the next resource declaration._

## **Azure Data Factory:**
```tf
resource "azurerm_data_factory" "DataFactory" {
  name                = "DataFactory Name"
  location            = azurerm_resource_group.RG.location
  resource_group_name = azurerm_resource_group.RG.name

  identity {
    type = "SystemAssigned"
  }
}
```

## **Azure Data Bricks:**
```tf
resource "azurerm_databricks_workspace" "Databricks" {
  location                      = azurerm_resource_group.RG.location
  name                          = "Databricks Name"
  resource_group_name           = azurerm_resource_group.RG.name
  managed_resource_group_name   = "Databricks Managed Resource Group"
  sku                           = "Databricks Sku"

  custom_parameters {
    no_public_ip        = true
    virtual_network_id  = azurerm_virtual_network.DatabricksVnet.id
    public_subnet_name  = azurerm_subnet.DatabricksSubnetPublic.name
    private_subnet_name = azurerm_subnet.DatabricksSubnetPrivate.name
  }

  depends_on = [
    azurerm_subnet_network_security_group_association.public,
    azurerm_subnet_network_security_group_association.private
  ]
}
```
## Virtual network:
```tf
resource "azurerm_virtual_network" "DatabricksVnet" {
  name                     = "VNET NAME"
  resource_group_name      = azurerm_resource_group.RG.name
  location                 = azurerm_resource_group.RG.location
  address_space            = ["VNET CIDR"]
}
```
## Network Security group for ADB:
```
resource "azurerm_network_security_group" "DatabricksNSG" {
  name                     = "VirtualNetwork NSG Name"
  resource_group_name      = azurerm_resource_group.RG.name
  location                 = azurerm_resource_group.RG.location
}
```
## Public subnet for Databricks:
```
resource "azurerm_subnet" "DatabricksSubnetPublic" {
  name                 = "VirtualNetwork PublicSubnet Name"
  resource_group_name  = azurerm_resource_group.RG.name
  virtual_network_name = azurerm_virtual_network.DatabricksVnet.name
  address_prefixes     = ["VirtualNetwork PublicSubnet CIDR"]
  service_endpoints    = ["Microsoft.Storage"]

  delegation {
    name = "Microsoft.Databricks.workspaces"
    service_delegation {
      name = "Microsoft.Databricks/workspaces"
      actions = [
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/virtualNetworks/subnets/prepareNetworkPolicies/action",
        "Microsoft.Network/virtualNetworks/subnets/unprepareNetworkPolicies/action"]
    }
  }
}
```
## Private subnet for Databricks:
```
resource "azurerm_subnet" "DatabricksSubnetPrivate" {
  name                 = "VirtualNetwork PrivateSubnet Name"
  resource_group_name  = azurerm_resource_group.RG.name
  virtual_network_name = azurerm_virtual_network.DatabricksVnet.name
  address_prefixes     = ["VirtualNetwork PrivateSubnet CIDR"]

  delegation {
    name = "Microsoft.Databricks.workspaces"
    service_delegation {
      name = "Microsoft.Databricks/workspaces"
      actions = [
        "Microsoft.Network/virtualNetworks/subnets/join/action",
        "Microsoft.Network/virtualNetworks/subnets/prepareNetworkPolicies/action",
        "Microsoft.Network/virtualNetworks/subnets/unprepareNetworkPolicies/action"]
    }
  }
}
```
## Network security group for Public subnet:
```
resource "azurerm_subnet_network_security_group_association" "public" {
  subnet_id                 = azurerm_subnet.DatabricksSubnetPublic.id
  network_security_group_id = azurerm_network_security_group.DatabricksNSG.id
}
```
## Network security group for Privatesubnet:
```
resource "azurerm_subnet_network_security_group_association" "private" {
  subnet_id                 = azurerm_subnet.DatabricksSubnetPrivate.id
  network_security_group_id = azurerm_network_security_group.DatabricksNSG.id
}
```
Now as all the associated network configuration done let’s move to the DATA LAKE STORAGE account creation

## Data Lake storage account:
```
resource "azurerm_storage_account" "DataLake" {
  name                     = "DataLake Name"
  resource_group_name      = azurerm_resource_group.RG.name
  location                 = azurerm_resource_group.RG.location
  account_tier             = "DataLake Tier"
  account_replication_type = "DataLake Replication"
  is_hns_enabled           = true
  min_tls_version          = "DataLake TLSVersion"

  network_rules {
    # bypass                     = "AzureServices"
    default_action             = "Allow"    
  }
}
```
## Storage account container:
```
resource "azurerm_storage_container" "DataLakeContainer" {  
  for_each              = "DataLake Container"
  name                  = each.key
  storage_account_name  = azurerm_storage_account.DataLake.name
  container_access_type = "private"
}
```

Now, let us create SQL related resources

## Storage Admin password:
```
resource "random_string" "SQLAdminPassword" {
  length      = 5
  special     = true
  min_upper   = 2
  min_numeric = 2
  min_special = 2
}
```
## SQL server :
```
resource "azurerm_mssql_server" "SQLServer" {
  name                         = "SQLServer Name"
  resource_group_name          = azurerm_resource_group.RG.name
  location                     = azurerm_resource_group.RG.location
  version                      = "SQLServer Version"
  administrator_login          = "SQLServer AdministratorLogin"
  administrator_login_password = random_string.SQLAdminPassword.result
  minimum_tls_version          = "SQLServer  TLS Version"
}
```
## SQL Database:
```
resource "azurerm_mssql_database" "SQLDatabase" {
  name           = "SQLDatabase Name"
  server_id      = azurerm_mssql_server.SQLServer.id
  collation      = "SQL_collation"
  max_size_gb    = "SQLDatabase MaxSizeGB"
  sku_name       = "SQLDatabase SKU"
  zone_redundant = "SQLDatabase ZoneRedundant"
}
```

This is a complete part by part snippets to create a running ADB ADF system, feel free to reach me in case any clarification required!
## Read my blogs:
[![Medium](https://i.imgur.com/TgYYM9w.png)](https://kunaldaskd.medium.com)
[![DEV](https://i.imgur.com/bp3qHWb.png)](https://dev.to/kunaldas)
[![Hashnode](https://i.imgur.com/iwZwo2S.png)](https://kunaldas.hashnode.dev)

## Connect with Me:
[![Twitter](https://i.imgur.com/VaorXDP.png)](https://twitter.com/kunald_official)
[![LinkedIn](https://i.imgur.com/ktIHVxm.png)](https://linkedin.com/in/kunaldaskd)
