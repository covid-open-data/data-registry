# Data Type Schemas and Validation

## Type: "casecount"

**Description:** Daily cumulative counts of cases and deaths at different levels of geographic resolution.

- Case counts can be provided at the global, continent, WHO region, admin0 (country/territory), admin1 (state/province), and admin2 (county) level.
- Administrative level 1 and 2 files are provided on a per-country basis, as these will generally only be added one at a time for a select subset of countries.
- Valid "casecount" csv files must match the following names:
  - `global.csv`
  - `continents.csv`
  - `who_regions.csv`
  - `admin0.csv`
  - `admin1_**.csv` (** is ISO2 code for the country)
  - `admin2_**.csv` (** is ISO2 code for the country)
- These file names indicate a geographic hierarchy (global -> who_region/continent -> admin0 -> admin1 -> admin2)
- At each level of geographic resolution, it is required to provide a code identifying each entity's own geography as well as that of its parent geographic entity. In the case of admin1 and admin2 datasets, it is necessary to provide codes all the way up to admin0 because admin1 and admin2 codes can be non-unique across countries.
- If the filename is global.csv, it must have the following schema:
  - `date`: ISO 8601 (e.g. 2020-01-30) date format
  - `cases`: non-negative integer
  - `deaths`: non-negative integer
- If the filename is continents.csv, it must have the following schema:
  - `continent_code`: one of AF|AS|EU|NA|OC|SA|AN
  - `date`: ISO 8601 (e.g. 2020-01-30) date format
  - `cases`: non-negative integer
  - `deaths`: non-negative integer
- If the filename is `who_regions.csv`, it must have the following schema:
  - `who_region_code`: one of AMRO|EMRO|AFRO|EURO|WPRO|SEARO
  - `date`: ISO 8601 (e.g. 2020-01-30) date format
  - `cases`: non-negative integer
  - `deaths`: non-negative integer
- If the filename is `admin0.csv`, it must have the following schema:
  - `admin0_code`: A valid ISO2 country code (too many to enumerate - probably safe to not strictly validate)
  - `date`: ISO 8601 (e.g. 2020-01-30) date format
  - `cases`: non-negative integer
  - `deaths`: non-negative integer
- If the filename is `admin1_**.csv`, it must have the following schema:
  - `admin0_code`: A valid ISO2 country code (too many to enumerate)
  - `admin1_code`: A country-specific admin1 code (code standard can vary by country)
  - `date`: ISO 8601 (e.g. 2020-01-30) date format
  - `cases`: non-negative integer
  - `deaths`: non-negative integer
- If the filename is `admin2_**.csv`, it must have the following schema:
  - `admin0_code`: A valid ISO2 country code (too many to enumerate)
  - `admin1_code`: A country-specific admin1 code (code standard can vary by country)
  - `admin2_code`: A country-specific admin2 code (code standard can vary by country)
  - `date`: ISO 8601 (e.g. 2020-01-30) date format
  - `cases`: non-negative integer
  - `deaths`: non-negative integer
- It is acceptable for additional columns to exist, they will just be ignored.

Sources include:

- WHO
- [JHU CSSE](https://github.com/CSSEGISandData/COVID-19)
- [European CDC](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
- [Worldometer](https://www.worldometers.info/coronavirus/)
- [New York Times (US)](https://github.com/nytimes/covid-19-data)

## Type: "mobility"

**Description:** Daily mobility trends (percent change in usual mobility behavior) by different modalities.

Schema description to come...

Potential sources include:

- [Apple](https://www.apple.com/covid19/mobility)
- [Google](https://www.google.com/covid19/mobility/)

## Type: "admin_stats"

**Description:** Administrative statistics at different levels of geographic resolution.

Schema description to come...

Potential sources include:

- [INFORM GRI](https://drmkc.jrc.ec.europa.eu/inform-index)
- [UN WPP](https://population.un.org/wpp/)
- [SEDAC GRUMP](https://sedac.ciesin.columbia.edu/data/collection/grump-v1)
- [WorldBank poverty](https://www.worldbank.org/en/topic/poverty)
- [WorldPop](https://www.worldpop.org)
- [SADC Food Security](https://data.humdata.org/dataset/sadc-food-security-vulnerable-population)
- [WHO SSA Health Facilities](https://www.who.int/malaria/areas/surveillance/public-sector-health-facilities-ss-africa/en/)

## Type: "model"

**Description:** Projected cases and deaths (hospital resources, other?) with confidence bounds.

Schema description to come...

Potential sources include:

- [IHME](https://covid19.healthdata.org/united-states-of-america)
- [Imperial College](https://github.com/mrc-ide/global-lmic-reports/)

<!-- https://mrc-ide.github.io/covid19-short-term-forecasts/index.html -->
