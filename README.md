### Communication:
**MsgpackRPC**<br>
Files are looked up and named by their **IDs** on Naming server's database<br>
**Calls:**<br>
init()-completely clear and return available space size <br>
create(id: str) - create empty file <br>
write(id: str, contents) - create file filled by the data <br>
read(id: str) - read data at the file <br>
delete(ids: list) - delete files <br>

### Running<br>
1) docker-compose up -d<br>
2) docker exec storageserver python main.py [args]<br>
Where **args** are:<br>
"-ss_host" - storage server's IPv4 address<br>
"-ss_port" - storage server's port<br>
"-ss_dir" - path to local storage directorн<br>
"-ss_cap" - capacity of storage server in bytes<br>
"-ns_host" - naming server's IPv4 address
"-ns_port" - naming server's port
"-connector" - enpoint to storage server