# Outputs format
This is a simple file that shows the format on how the context is formed

## Invalid for RDAP Protocol.

    {
        "is_rdap" : False, *
        "is_available" : False,
        "host" : None,
        "content" : {
            "domain" : "example.com",
            "dns" : UNDEFINED_DATA,
            "create_at" : UNDEFINED_DATA,
            "expire_at" : UNDEFINED_DATA,
            "update_at" : UNDEFINED_DATA,
            "update_at_rdap" : UNDEFINED_DATA,
            "entity" : UNDEFINED_DATA,
            "registrant_id" : UNDEFINED_DATA,
            "name" : UNDEFINED_DATA,
        }
    }

## Valid and domain is available to register.

    {
        "is_rdap" : True,
        "is_available" : True,
        "host" : "host_url",
        "content" : {
            "domain" : "example.com",
            "dns" : UNDEFINED_DATA,
            "create_at" : UNDEFINED_DATA,
            "expire_at" : UNDEFINED_DATA,
            "update_at" : UNDEFINED_DATA,
            "update_at_rdap" : UNDEFINED_DATA,
            "entity" : UNDEFINED_DATA,
            "registrant_id" : UNDEFINED_DATA,
            "name" : UNDEFINED_DATA,
        }
    }

## Valid but domain is not available to register.

    {
        "is_rdap" : True,
        "is_available" : False,
        "host" : "host_url",
        "content" : {
            "domain" : "example.com",
            "dns" : "some_nameservers_string",
            "create_at" : "datetime_as_string",
            "expire_at" : datetime_as_string,
            "update_at" : datetime_as_string,
            "update_at_rdap" : datetime_as_string,
            "entity" : "entity_name",
            "registrant_id" : "it_could_be_a_string" or None,
            "name" : "name_of_the_owner" or None,
        }
    }

