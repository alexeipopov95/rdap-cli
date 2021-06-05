# Commands

## CHECK
This command is in charge of gather the availability of the domain. It return a friendly user message depending of the status of the domain.

    $ rdap check --domain=google.com
    # [ERROR] - google.com it is not available.

    $ rdap check --domain=myavailabledomain.com
    # [INFO] - myavailabledomain.com is available to register. For more information you can got here: {HOST}

    $ rdap check --help
    # [INFO] - check if the domain is available or not.

One thing that is very important is the next option '--file'. You can provide a valid file format such as JSON or TXT with the next format:

### JSON
    {
        "domains" : ["example.org", "example.net", "example.com.ar"]
    }

### TXT
    example.com
    example.net
    example.org
    ...


## GATHER
This command is in charge of gather the domain information and show the the result about the query in the shell screen. If the domain is not registered it will return a message saying that the domain is availble for registration.

    $ rdap gather --domain=google.com

        Domain: google.com
        Nameservers: ['ns1.google.com', 'ns2.google.com', 'ns3.google.com', 'ns4.google.com']
        Entity: MarkMonitor Inc.
        ID: Undefined
        Owner: Undefined
        Creation date: 1997-09-15 04:00:00
        Expiration date: 2028-09-14 04:00:00
        Last updated: Undefined
        Last updated in RDAP: 2021-06-05 09:20:35

    $ rdap gather --help
    # [INFO] - Gather the domain data, dns, events, owner, entity.

## SAVE
This command is designed to save the payload about a domain in a specific file. By the way the only available formats that the CLI supports are JSON and TXT. YML is still WIP.

    $ rdap save --domain=google.com --file=myfile.json or myfile.txt
    # [SUCCESS] - Saved [json] /path/to/user/user/myfile.json

You can specify the path in the --file option such as '../myfile.json'
or paths like this one '--file=/my/custom/special/path/myfile.json'

### Output as JSON
    {
        "domain": "google.com",
        "dns": ["ns1.google.com", "ns2.google.com", "ns3.google.com", "ns4.google.com"],
        "create_at": "1997-09-15 04:00:00",
        "expire_at": "2028-09-14 04:00:00",
        "update_at": "Undefined",
        "update_at_rdap": "2021-06-05 09:20:35",
        "entity": "MarkMonitor Inc.",
        "id": "Undefined",
        "name": "Undefined"
    }

### Output as TXT

    domain: google.com
    dns: ['ns1.google.com', 'ns2.google.com', 'ns3.google.com', 'ns4.google.com']
    create_at: 1997-09-15 04:00:00
    expire_at: 2028-09-14 04:00:00
    update_at: Undefined
    update_at_rdap: 2021-06-05 09:20:35
    entity: MarkMonitor Inc.
    id: Undefined
    name: Undefined

## HISTORY (comming soon)
This commands its still work in progress, you can check the history of your last searches and look again the information about the domain.