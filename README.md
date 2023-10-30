# pp_cmd_rename
Postprocessing command "rename"
## Description
Command renames dataframe columns

### Arguments
- col - positional infinite argument with "as" syntax, where left value is column name, right value is new column name

### Usage example
```
`... | rename _time AS Time, p50 AS Median, p25 AS Quartile `
```

## Getting started
### Installing
1. Create virtual environment with post-processing sdk
```bash
    make dev
```
That command
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory

2. Configure `otl_v1` command. Example:
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run rename
Use `pp` to run rename command:
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  rename _time as Time
```
## Deploy
 Unpack archive `pp_cmd_rename` to postprocessing commands directory
 ## Test
Use `make test` and all test will run in Docker container. Please turn the vpn on so all the OTL dependencies would download.