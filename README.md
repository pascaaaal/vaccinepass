# vaccinepass
This is just a PoC project for a vaccine pass. It works with some RSA keys ;)
# How does it work
## Step 1
The server generates a public and private key (Just like a normal RSA Keypair).
## Step 2
A authorized doctor that vaccinated a user sends a hashed version of the userdata to the server to be encrypted.
After that a QRCode with the client information and the encrypted hash is saved on the clients device.
## Step 3
If someone wants to check the integrety of the QRCode he just creates his own hash of the data, decrypts the hash with the public key and check if they match.
# Why do it like that
The big advantage is that it is anonymous. Nobody wants that an organisation (governmental or not) to have such power over data.
With a centralized Database one could possibly get the geoip addresses and create a location history, nobody wants that ;)
This problem is solved by just one public key. All clients just download the public key and check the hash locally. No server connection is needed.
On the otherside this concept is secure, at least if the private key is kept protected, but we can deal with that on the web so why not with that.
