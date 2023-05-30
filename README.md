# openthebox API

### Overview

The openthebox.be API makes it possible to integrate the data of openthebox.be into your own application. 

All information that is available on the openthebox.be website is also available from the API.

### API Endpoint

API endpoints exists for retrieving different types of information. These endpoints are documented on https://openthebox.be/api-docs/index.html. The documentation is interactive so you can play around with it and immediately see what information it returns.

### Authentication

Some of the endpoints can be used for a limited number of requests without any authentication. To get access to the advanced endpoints in an unlimited fashion you should provide an api token in the header of your requests:
```authorization: Bearer {your api token}``` 

You can generate an api token from the client id and client secret that comes with your openthebox.be subscription as following:

```curl
curl --request POST \
  --url https://openthebox.be/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"{your client id}","client_secret":"{your client secret}","audience":"https://openthebox.be/api","grant_type":"client_credentials"}'
```

[Examples in other languages](https://auth0.com/docs/api/management/v2/get-access-tokens-for-production)

This token will expire after 24 hours so a new token should be generated before then  

