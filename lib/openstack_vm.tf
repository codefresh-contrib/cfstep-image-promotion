# Configure the OpenStack Provider
# https://www.terraform.io/docs/providers/openstack/index.html
provider "openstack" {
  user_name   = var.user_name
  tenant_name = var.tenant_name
  password    = var.password
  auth_url    = var.auth_url
  region      = var.region
}

# Create VM
# https://www.terraform.io/docs/providers/openstack/r/compute_instance_v2.html
resource "openstack_compute_instance_v2" "basic" {
  name            = "basic"
  image_id        = "ad091b52-742f-469e-8f3c-fd81cadf0743"
  flavor_id       = "3"
  key_pair        = "my_key_pair_name"
  security_groups = ["default"]

  network {
    name = "my_network"
  }

  # Run Chef (Chef Provisioner)
  # https://www.terraform.io/docs/provisioners/chef.html
  #provisioner "chef" {
  #  attributes_json = <<EOF
  #    {
  #      "key": "value",
  #      "app": {
  #        "cluster1": {
  #          "nodes": [
  #            "webserver1",
  #            "webserver2"
  #          ]
  #        }
  #      }
  #    }
  #  EOF

  #  environment     = "_default"
  #  run_list        = ["cookbook::recipe"]
  #  node_name       = "webserver1"
  #  secret_key      = "${file("../encrypted_data_bag_secret")}"
  #  server_url      = "https://chef.company.com/organizations/org1"
  #  recreate_client = true
  #  user_name       = "bork"
  #  user_key        = "${file("../bork.pem")}"
  #  version         = "12.4.1"
  #  # If you have a self signed cert on your chef server change this to :verify_none
  #  ssl_verify_mode = ":verify_peer"
  #}
}