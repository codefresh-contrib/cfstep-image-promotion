# WIP cfstep-image-promotion
Promote Codefresh built Docker images to Docker registry.

Can promote to a new tag or promote to another Docker registry.

YAML Step
``` yaml
  PromoteImage:
    image: codefreshplugins/cfstep-image-promotion:latest
    environment:
      - IMAGE=codefresh/demochat # Replace with Candidate Docker image name
      - TAG=${{CF_BRANCH_TAG_NORMALIZED}} # Candidate tag
      - PROMOTE_TAG=release-candidate # Tag to promote
```

## Variable List

| ENVIRONMENT VARIABLE | DEFAULT | TYPE | REQUIRED | DESCRIPTION |
|----------------------------|----------|---------|----------|---------------------------------------------------------------------------------------------------------------------------------|
| CODEFRESH_API_URL | https://g.codefresh.io | string | No | Codefresh API URL |
| CF_API_KEY | null | string | Yes | Codefresh API Key (Supplied by Codefresh pipeline) |
| CF_BUILD_INITIATOR | null | string | Yes | Codefresh Build Initiator (Supplied by Codefresh pipeline) |
| CODEFRESH_USERNAME | CF_BUILD_INITIATOR | string | Yes | Codefresh Username (Supplied by Codefresh pipeline) |
| IMAGE | null | string | Yes | Name of Image to Promote |
| PROMOTE_IMAGE | IMAGE | string | Yes | Name of Promoted Image |
| PROMOTE_TAG | TAG | string | Yes | Tag of Promoted Image |
| REGISTRY | cfcr | string | Yes | Registry to promote image to |
| TAG | null | string | Yes | Tag of Image to Promote |
