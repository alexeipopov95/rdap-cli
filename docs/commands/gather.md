# GATHER

## Gather command
Gather is a simple command that is in charge of obtaining the relevant information about a domain. Information such as the expiration date, the nameservers,
creation date on registry database, last updates on when it was updated by the owner or in the RDAP records.
Additionally to it in some special cases (I.e Argentinian domains) it will show the individual taxpayer identification number (CUIT) and the owner itself.

The way of casting the command is the next:

> `$ rdap gather example.com`

Then you will see the next result

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

## Gather has some usefull options!
------------------------------------------------------------

Yes, like i said, if you wish to save the output into a file you simply can specify the name of the file and thats it! The CLI will format the data into a user friendly format (or dev friendly format) and thats it.

**Take in mind that the formats that we support for this action are:**
* JSON
* TEXT

You need to pass the next order:

> `$ rdap gather example.com --file=my_file.json`

    [DONE] - File saved successfully.

And thats it... That you will find the file in your current working directory.

### Return value from shell - [JSON]
------------------------------------------------------------
This is going to be the output saved in your `.json` file:

    {
        "is_rdap": true,
        "status": false,
        "host": "https://verisign.com/",
        "query_host": "https://rdap.verisign.com/com/v1/domain/example.com","content": {
            "domain": "example.com",
            "dns": "a.iana-servers.net, b.iana-servers.net",
            "create_at": "1995-08-14 04:00",
            "expire_at": "2021-08-13 04:00",
            "update_at": null,
            "update_at_rdap": "2021-06-17 09:34",
            "entity": "RESERVED-Internet Assigned Numbers Authority",
            "registrant_id": null,
            "name": null
        }
    }

### Return value from shell - [TEXT]
------------------------------------------------------------
This is going to be the output saved in your `.json` file:

    is_rdap: True
    status: False
    host: https://verisign.com/
    query_host: https://rdap.verisign.com/com/v1/domain/example.com
    domain: example.com
    dns: a.iana-servers.net, b.iana-servers.net
    create_at: 1995-08-14 04:00
    expire_at: 2021-08-13 04:00
    update_at: None
    update_at_rdap: 2021-06-17 09:34
    entity: RESERVED-Internet Assigned Numbers Authority
    registrant_id: None
    name: None


## Unexpected Cases
--------------------------------------------------------

In those cases where the file format is not supported you will receive a prompt notifying you that is not supported yed.

> `$ rdap gather example.com --save=my_file.yml`

    [ERROR] - The fileformat [yml] is not supported yet.

--------------------------------------------------------

Take in mind that the CLI will raise some exceptions if you dont give propperly the domain name. For example:

> `rdap check https://blog.myexample.com/web/images/pic1.jpg`

It will raise `DomainWithHttp` | `DomainValidationError` | `DomainWithSubdomain`. This are the three main validations that the CLI do to avoid malformed domain names. \
Dont worry, if you did not read this part and pass anyway the domain with all those errors the CLI will try to help you to form it good.

## Examples:
------------------------------------------------------------
> `rdap check https://myexample.com`

    [ERROR] Only admits valid domain names. Try deleting 'https://' and try again please.

> `rdap check blog.myexample.com`

    [ERROR] Only admits valid domain names, subdomain are not included. Try deleting 'blog.' and try again please.

> `rdap check myexample.com/web/images/pic1.jpg`

    [ERROR] Only admits valid domain names. Please try only typing myexample.com and try again please.

--------------------------------------------------------

## HELP
If you wish to read about the commands from the CLI dont forget you can just type

> `$ rdap gather --help`

And you will see a bunch of help text with a short description about the command and its options.
