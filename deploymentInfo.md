### Deploying our app to the public
There are many ways we can deploy an app and have it serve public traffic.
One such option is using Google App Engine. Google App Engine even helps us with SSL configuration so we can serve over HTTPS.
Below I will outline the steps I took to deploy this app using Google App Engine.

Prerequisites:

* A Google Cloud Platform account

* Google Cloud SDK is installed and configured on your machine

* Access to the source code in this repository

Expected outcomes:

* Our app is accessible via the public internet

* Attempting to access the app via HTTP either fails or redirects to HTTPS

Out of scope (for now):

* Repeatable infrastructure

* Automated deployment

* Auth, logging, security (except for SSL/HTTPS)

* Proxy setup (GCE Ingress, NGINX, Caddy, etc.)

### What is Google App Engine?
Google App Engine (GAE) deploys apps according to an `app.yaml`
configuration file. This file describes the expected environment for the service, such as:

- the runtime, e.g. _Python v3.8_
- server instance type
- scaling settings
- environment variables
- route handlers
- the entrypoint/command used to run the app
- ... and other resource settings (refer to documenation)

Please see the `app.yaml` config file in this repo for reference.

### Deploying the app

Assuming we have this repo and the GCP SDK/CLI configured for this project, we can deploy by simply running `gcloud app deploy` from this repository's base directory (and confirm the deployment by entering `Y` when prompted).

If successful, the CLI will output the app's publicly accessible URL. You may also run `gcloud app browse` which will open the app's URL in your default browser.

### Forcing HTTPS / disallowing HTTP

We've configured our app to auto-upgrade HTTP requests to use HTTPS.

This is achieved by the following handler specification:
```
handlers:
- url: /.*
  secure: always
  redirect_http_response_code: 301
  script: auto
```

The above effectively says "for any request matching this url pattern (any), upgrade to HTTPS". The _secure: always_ enables the following:

```
Requests for a URL that match this handler that do not use HTTPS are automatically redirected to the HTTPS URL with the same path. Query parameters are preserved for the redirect.

[https://cloud.google.com/appengine/docs/standard/python3/config/appref#handlers_http_headers]
```


### Other Deployment Considerations

* Since this app is not expected to serve heavy traffic, I chose the smallest server instance type available for Google App Engine - `F1`.

### Additional considerations for a Production service

* Authentication and authorization of users.

* Access control: configure who can access the service in GCP. Follow the _principle of least privilege_. Role-Based Access Control (RBAC) may be a suitable approach.

* Use a database suitable for your application's needs. For example, you may want a Cloud SQL instance (or cluster) running Postgres.

* Observability: increase understanding of the service's performance and behavior by building logging, metrics, monitoring, alerting, etc. This can help identify "problems" before they become bigger problems as well as debug issues that occurred.

* Split traffic between two (or more) versions of the app for A/B testing.

* CI/CD pipeline with automated testing and (possibly) auto or semi-auto deployment.

* Containerize the app allowing for repeatable builds.

* Profile your app for performance bottlenecks.

* Perform a sensible amount of User Acceptance Testing (UAT) to have at least some degree of confidence the service behaves as expected.

### Resources / Documentation

https://cloud.google.com/appengine/docs/standard/python3/configuration-files

https://cloud.google.com/appengine/docs/standard/python3/config

https://cloud.google.com/appengine/docs/standard/python3/application-security

https://cloud.google.com/appengine/docs/standard/python3/splitting-traffic