#Run first two lines seperately. To make directory then to edit file

mkdir /data/docker/pihole/config
#original code had a -p after mkdir (what for?)

nano /data/docker/pihole/config/docker-compose.yaml

# mapping file. Changes from original pihole script.
## 0.0.0.0 has been added before each port's mapping. 
## Port 8080 added instead of 80 to not interfere with HiFiBerry interface
version: "3"

# More info at https://github.com/pi-hole/docker-pi-hole/ and https://docs.pi-hole.net/
services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    # For DHCP it is recommended to remove these ports and instead add: network_mode: "host"
    ports:
      - "0.0.0.0:53:53/tcp"
      - "0.0.0.0:53:53/udp"
      - "0.0.0.0:67:67/udp" # Only required if you are using Pi-hole as your DHCP server
      - "8080:80/tcp"
    environment:
      TZ: 'America/Chicago'
    WEBPASSWORD: 'password' #enter password or will be randomised
    # Volumes store your data between container upgrades
    volumes:
      - './etc-pihole:/etc/pihole'
      - './etc-dnsmasq.d:/etc/dnsmasq.d'    
    #   https://github.com/pi-hole/docker-pi-hole#note-on-capabilities
    cap_add:
      - NET_ADMIN # Recommended but not required (DHCP needs NET_ADMIN)      
    restart: unless-stopped
