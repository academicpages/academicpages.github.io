---
title: "PhenCards Project (2019)"
excerpt: "Description of [PhenCards](https://phencards.org/) Project<br/><img src='/images/500x300.png'>"
collection: portfolio
---

For this Project, I applied PySpark to merge databases from several sources and used Docker to build images of the project. Here is an overview of the data sorces I used:
  
| INDEX | EXTERNAL-DATABASE-NAME  | SOURCE-LINK  | INSTRUCTIONS  |  COMMENTS |
|---|---|---|---|---|
| 1 | ICD-10  | ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2020/icd10cm_order_2020.txt  |    No permission required| Use the link to download  |
| 2  |  ICD-9 |  ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD-9/ucod.txt |    No permission required| Use the link to download  |
| 3  | ICD-O  | https://github.com/philipsales/icdoncology-3/blob/master/icd-oncology.v3.json  |    No permission required| Use the link to download  |
| 4  |  SNOMEDCT_US |https://download.nlm.nih.gov/umls/kss/IHTSDO20200131/SnomedCT_InternationalRF2_PRODUCTION_20200131T120000Z.zip |  If `account`/`password` is needed, use the following: ``/`` |  Need account information for download permission, around 500M|
| 5  | UMLS  | https://download.nlm.nih.gov/umls/kss/2019AB/umls-2019AB-full.zip  |  If `account`/`password` is needed, use the following: ``/`` |  Need account information for download permission, around 4GB; here is a useful tool to download using cluster: https://askubuntu.com/questions/29079/how-do-i-provide-a-username-and-password-to-wget|
| 6  | MeSH  | ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/xmlmesh/desc2020.gz  |    No permission required| Use the link to download  |
|  7 | DOID  |  http://purl.obolibrary.org/obo/doid.owl | No permission required  |  This is an HTML format file, need attention for parsing |
