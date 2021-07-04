# HISTORY

## History command
This is the history command, you can find a really good use of it if you wish to see your last searchs.
There is a file in the files of the CLI that is in change of saving the outputs from your searches.  (Yes those searches are results from gather and check).
The history has a limit of 50 records, then the the first record is going to be replaced by the lattest.

The way of casting the command is the next:

> `$ rdap history`

Then you will see a nice table showing the next values

|IS RDAP |  STATUS  | DOMAIN |    HOST    |   HOSTQUERY HOST  |  ID  |TIMESTAMP |
|:-----: |:--------:|:------:|:----------:|:-----------------:|:----:|:--------:|
|Yes     | Taken    |domain.com|example.com | example.com/host/ | uuid | datetime |
|No      | Taken    |domain.net|Unknown     | Unknown           | uuid | datetime |
|Yes     | Available|domain.org|example.com | example.com/host/ | uuid | datetime |

## Detail
--------------------------------------------------------

The detail subcommand is designed to see again the records saved from your last search. If you see in your history your results, you can check the detail of that query based on the ID column.

> `$ rdap history detail uuid`

And the expected output is going to be:

        Domain: EXAMPLE.COM
        Status: UNAVAILABLE

        Nameservers: a.iana-servers.net
                     b.iana-servers.net

        Create date: 1995-08-14 04:00
        Expire date: 2021-08-13 04:00
        Update date: None
        Update date (RDAP): Undefined

        Entity: RESERVED-Internet Assigned Numbers Authority
        Name: None
        Registrant ID: None


## Download
--------------------------------------------------------

The download command is used to download all the history that one has accumulated so far.

> `$ rdap history download my_file.json`

    [DONE] - File saved successfully to /path/to/file/my_file.json

Take in mind that the download subcommand takes as argument a `str` file name. And the only formats it supports are `.json` and `.txt`.


## Clear
--------------------------------------------------------

The clear subcommand is used to just clean your history.

> `$ rdap history clear`

    [DONE] - Cleaned succesfully.


## Unexpected Cases
--------------------------------------------------------

If you want to check the history without searching a domain before and this is your first time you will see a message telling the next:

    [INFO] - No records available yet. Make a query first.


If the domain is not part of the RDAP Protocol the CLI cannot guarante if its really taken or not because the Top level domain of the queryed domain is not part yet of this protocol.


## HELP
--------------------------------------------------------
If you wish to read about the commands from the CLI dont forget you can just type:

> `$ rdap history --help`

And you will see a bunch of help text with a short description about the command and its options.
