# Tables documentation
The data available at [ZENODO LINK] consists of five different tables, which will be introduced on this page.

## Metadata
```{list-table}
:header-rows: 1
* - Column
  - Explanation
  - Example
* - run_accession
  - Identifer for sequencing reads.
  - DRR000836
* - sample_accession
  - Identifer for sample.
  - SAMD00002573
* - project_accession
  - Identifer for project.
  - PRJDA61421 
* - country
  - Locality of sample isolation: country names, oceans or seas, followed by regions and localities.
  - N/A
* - location
  - Geographic location of isolation of the sample (latitude, longitude).
  - N/A
* - continent
  - Geographic region (land or water body)
  - N/A
* - collection_date
  - Date that the specimen was collected.
  - 2016-01-01
* - tax_id
  - NCBI taxon ID of the organism from which the sample was obtained.
  - 939928
* - host
  - Natural (as opposed to laboratory) host to the organism from which sample was obtained.
  - Homo sapiens
* - host_tax_id
  - NCBI taxon ID of the host
  - 9606
* - instrument_platform
  - Instrument platform used in sequencing experiment.
  - LS454
* - instrument_model
  - Instrument model used in sequencing experiment.
  - 454 GS FLX Titanium
* - library_layout
  - Sequencing library layout.
  - SINGLE
* - raw_reads
  - Number of raw sequencing reads.
  - 1268608
* - trimmed_reads
  - Number of trimmed sequencing reads.
  - 1247751
* - raw_bases
  - Number of bases in the raw sequencing reads.
  - 641025182
* - trimmed_bases
  - Number of bases in the trimmed sequencing reads. 
  - 1247751
* - trimmed_fragments
  - Number of trimmed read fragments that can be mapped.
  - 1247751
```

## ARG counts
```{list-table}
:header-rows: 1
* - Column 
  - Explanation
  - Example
* - run_accession
  - Identifer for sequencing reads.
  - DRR000836
* - sample_accession
  - Identifer for sample.
  - SAMD00002573
* - project_accession
  - Identifer for project.
  - PRJDA61421
* - trimmed_fragments
  - Total number of fragments.
  - 1247751
* - run_date
  - Date that KMA program ran.
  - 2020-11-10
* - kma_version
  - Version of KMA used.
  - 1.3.0 
* - refSequence
  - Name of template sequence.
  - blaACT-4_2_AJ311172 
* - refSequence_length
  - Length of template sequence in bp.
  - 1146
* - refCoveredPositions
  - The number of covered positions in the template with a minimum depth of 1.
  - 427
* - refConsensusSum
  - Total number of bases identical to the template.
  - 424
* - bpTotal
  - Total number of bases aligned to the template.
  - 1651
* - fragmentCountAln
  - Number of fragments mapped and aligned to the template.
  - 5
* - bacterial_fragment
  - Sum of rRNA fragments mappped and aligned for the dataset.
  - 1428
```

## rRNA counts
```{list-table}
:header-rows: 1
* - Column 
  - Explanation
  - Example
* - run_accession
  - Identifer for sequencing reads.
  - DRR000836
* - sample_accession
  - Identifer for sample.
  - SAMD00002573
* - project_accession
  - Identifer for project.
  - PRJDA61421
* - run_date
  - Date that KMA program ran.
  - 2020-11-10
* - kma_version
  - Version of KMA used.
  - 1.3.0
* - phylum_name
  - Name of phylum.
  - Bacteroidetes
* - phylum_tax
  - NCBI taxon ID of the phylum.
  - 976
* - genus_name
  - Name of genus.
  - Myroides
* - genus_tax
  - NCBI taxon ID of the genus.
  - 76831
* - fragmentCountAln
  - Sum of fragments aligned to rRNA genes belonging to the corresponding genus.
  - 10.7744
```

## Diversity measures
```{list-table}
:header-rows: 1
* - Column 
  - Explanation
  - Example
* - run_accession
  - Identifer for sequencing reads.
  - DRR000836
* - kma_version
  - Version of KMA used.
  - 1.3.0
* - category
  - What group of genes the diversity measures are for: ARG, Phyla or Genera.
  - ARG
* - total_fragments
  - Total fragments that could be mapped.
  - 1247751
* - category_fragments
  - Number of fragments aligned to the category genes.
  - 6.6925
* - n
  - Number of unique genes/taxon IDs in group (observed richness)
  - 3
* - Shannon
  - Shannon diversity index for category
  - 0.887324
* - Simpson
  - Simpson (1-D) diversity index for category
  - 0.604705 
```

## ResFinder annotation
```{list-table}
:header-rows: 1
* - Column 
  - Explanation
  - Example
* - gene
  - Name of gene (refSequence)
  - aac(2')-Ia_1_L06156
* - anno_type
  - What type of label is given for the gene (Class, gene_length, Phenotype, Mechanism)
  - Class
* - anno_value
  - The label for the annotation type
  - Aminoglycoside
```