## Todo qui a servi pour packager  l'infrastructure



- [ ] Création d'une machine ec2 sur la console et installer dessus l'application
  
    -  Création ec2 sur la console AWS
    -  Se connecter dessus et faire les installs à la main
    
        - sudo apt update -y
        - sudo apt install python3-pip -y
        - git clone https://github.com/ADataGuru-labs/webinar-python-borne-electrique.git
        - pip install -r application/requirements.txt
        - pip install -e .
        - python3 -m flask  --app application/normalisation/src/point_entree.py run --host=0.0.0.0
    
    - Lancer le call @ip:5000 
    - Changer le security group en ajoutant une rule 
    - AJouter l'instance profile
    - Lancer le call @ip:5000 
  
- [ ] Automatiser l'installation avec ansible
   - Créer un playbook qui installe python et l'application dans la machine
     - Créer un playbook
     - Créer une tache pour installer python3
     - Créer une tache clone le repo git 
     - Créer une tache pour installer les dependances python
    

- [ ] Création d'une ami avec packer et Ansible
   - Créer l'ami en lançant le build packer
    

- [ ] Création d'une ec2 avec l'ami 
  - Creer les ressources suivantes avec Terraform:
    - Ressource SSH aws_key_pair
    - Ressource VPC
    - Ressource Security Group avec les ingress  tcp 22 et 5000 / egress all
    - Ressource IAM ROLE 
    - Ressource IAM POLICY 
    - Ressource IAM INSTANCE PROFILE 
    - Ressource EC2 
    
    


# Commands
 - chmod 400 sshKey.pem
 - ssh -i sshKey.pem ubuntu@ip-public
 - ssh-keygen
 - terraform apply --var-file=example.tfvars



