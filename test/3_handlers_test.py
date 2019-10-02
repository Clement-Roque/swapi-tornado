import parameters
import sys
sys.path.append('./project')

import requests
import json
import handlers
import schemas
import dictionary

def test_get_peoples():

	resp = requests.get(parameters.api_url)
	people = json.loads(resp.text)
	
	assert resp.status_code == 200

def test_get_people():

	resp_200 = requests.get(parameters.api_url+parameters.json_r2d2[dictionary.people_id])
	people = json.loads(resp_200.text)
	
	assert handlers.validate_json_schema(people, schemas.people_json_schema) is None
	assert resp_200.status_code == 200

	resp_404 = requests.get(parameters.api_url+parameters.json_unknow[dictionary.people_id])
	
	assert resp_404.status_code == 404

def test_delete_post_people():

	delete_resp_200 = requests.delete(parameters.api_url+parameters.json_r2d2[dictionary.people_id])
	
	assert delete_resp_200.status_code == 200

	delete_resp_404 = requests.delete(parameters.api_url+parameters.json_unknow[dictionary.people_id])
	
	assert delete_resp_404.status_code == 404

	post_resp_400 = requests.post(parameters.api_url, data=json.dumps(parameters.bad_json_r2d2))

	assert post_resp_400.status_code == 400

	post_resp_200 = requests.post(parameters.api_url, data=json.dumps(parameters.json_r2d2))

	assert post_resp_200.status_code == 200

	post_resp_403 = requests.post(parameters.api_url, data=json.dumps(parameters.json_r2d2))

	assert post_resp_403.status_code == 403

def test_put_people():

	put_resp_400 = requests.put(parameters.api_url, data=json.dumps(parameters.bad_json_r2d2))

	assert put_resp_400.status_code == 400

	put_resp_200 = requests.put(parameters.api_url, data=json.dumps(parameters.json_r2d2))

	assert put_resp_200.status_code == 200

	put_resp_404 = requests.put(parameters.api_url, data=json.dumps(parameters.json_unknow))

	assert put_resp_404.status_code == 404


