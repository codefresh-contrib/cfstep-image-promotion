import json
import os
import requests
import sys
import subprocess

def run_command(full_command):
    proc = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = proc.communicate()
    print(output)
    if proc.returncode != 0:
        sys.exit(1)
    return b''.join(output).strip().decode()  # only save stdout into output, ignore stderr


def main():
    codefresh_api_address = os.getenv('CODEFRESH_API_URL', 'https://g.codefresh.io')
    codefresh_api_token = os.getenv('CF_API_KEY')
    codefresh_build_initiator = os.getenv('CF_BUILD_INITIATOR')
    codefresh_username = os.getenv('CODEFRESH_USERNAME', codefresh_build_initiator)
    candidate_image = os.getenv('IMAGE')
    candidate_tag = os.getenv('TAG')
    promote_image = os.getenv('PROMOTE_IMAGE', candidate_image)
    promote_tag = os.getenv('PROMOTE_TAG', candidate_tag)
    registry = os.getenv('REGISTRY', 'cfcr')

    # Get Codefresh Image ID
    
    image_id = run_command("codefresh get image --image-name {} --tag {} -o id".format(candidate_image, candidate_tag))

    image_id = image_id.split('\n', 1)[0]

    # POST to Codefresh API

    # curl -X POST \
    # https://g.codefresh.io/api/images/19df55fdf2db/promote \
    # -H 'Authorization: API_KEY' \
    # -H 'Content-Type: application/json' \
    # -H 'cache-control: no-cache' \
    # -d '{
    #     "user": "dustinvanbuskirk",
    #     "imageId": "19df55fdf2db",
    #     "tagNames": "from-api",
    #     "registry": "cfcr",
    #     "imageName": "example-voting-app/vote"
    # }'

    json_data = { 
        "user": codefresh_username, 
        "imageId": image_id, 
        "tagNames": promote_tag,
        "registry": registry,
        "imageName": promote_image
    }

    r = requests.post('{}/api/images/{}/promote'.format(codefresh_api_address, image_id), json=json_data, headers={'Authorization': codefresh_api_token})
    
    print ("Promoted via Codefresh pipeline: {}".format(r.text))

if __name__ == "__main__":
    main()
