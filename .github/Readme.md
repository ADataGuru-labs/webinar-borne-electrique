

TODO : 

1 - Lancer le job lors d'un push sur une branche differente de main

### Build

2 - Cloner le projet Github dans la machine

3 - Installer python sur la machine

4 - Installer les dependances

5 - Verifier la syntaxe du code

6 - Executer les tests

### Package

7 - Cloner le projet Github dans la machine

8 - Installer packer sur la machine

      - uses: myci-actions/add-deb-repo@10
        with:
          repo: deb [arch=amd64] https://apt.releases.hashicorp.com focal main
          keys-asc: https://apt.releases.hashicorp.com/gpg
          update: true
          install: packer

9 - Créer une image Ami avec le code

    packer build infrastructure/image/packer/setup_api.pkr.hcl

### Deploiement

10 - Cloner le projet Github dans la machine

11 - Installer Terraform sur la machine

12 - Initialiser Terraform

13 - Créer une instance  


### Commands:

act -n --workflows .github/workflows/test.yml