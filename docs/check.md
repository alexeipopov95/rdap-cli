# CHECK

## Check command
Check command is more simpler than gather in some ways. It is designed to only know if the queryed domain is available or not to be registered. Including the host name where it did the query and the complete URL if you want to access and see more detailed information.

The way of casting the command is the next:

> `$ rdap check example.com`

Then you will see the next result

    Domain: EXAMPLE.COM
    Status: UNAVAILABLE
    Rdap Host: https://verisign.com/
    Query host: https://rdap.verisign.com/com/v1/domain/example.com


## Unexpected Cases
--------------------------------------------------------

Take in mind that the CLI will raise some exceptions if you dont give propperly the domain name. For example: 

> `rdap check https://blog.myexample.com/web/images/pic1.jpg`

It will raise `DomainWithHttp` | `DomainValidationError` | `DomainWithSubdomain`. This are the three main validations that the CLI do to avoid malformed domain names. \
Dont worry, if you did not read this part and pass anyway the domain with all those errors the CLI will try to help you to form it good.


## Examples:
--------------------------------------------------------
> `rdap check https://myexample.com`

    [ERROR] Only admits valid domain names. Try deleting 'https://' and try again please.

> `rdap check blog.myexample.com`

    [ERROR] Only admits valid domain names, subdomain are not included. Try deleting 'blog.' and try again please.

> `rdap check myexample.com/web/images/pic1.jpg`

    [ERROR] Only admits valid domain names. Please try only typing myexample.com and try again please.


## HELP
--------------------------------------------------------
If you wish to read about the commands from the CLI dont forget you can just type:

> `$ rdap check --help`

And you will see a bunch of help text with a short description about the command and its options.