import json
import os
from unicodedata import normalize
from core.models import Usuario

data = [
	{
		"name": "Melanie Bernard",
		"email": "morbi.quis.urna@icloud.edu"
	},
	{
		"name": "Lareina Cook",
		"email": "et.ipsum.cursus@yahoo.edu"
	},
	{
		"name": "Theodore Hopkins",
		"email": "urna.ut@google.ca"
	},
	{
		"name": "Yasir Caldwell",
		"email": "pharetra.sed@google.com"
	},
	{
		"name": "Lareina Cote",
		"email": "sit@outlook.com"
	},
	{
		"name": "Elijah Molina",
		"email": "eleifend.cras@outlook.org"
	},
	{
		"name": "Shana Rivera",
		"email": "feugiat@google.org"
	},
	{
		"name": "Lavinia Cooper",
		"email": "mollis.dui@yahoo.ca"
	},
	{
		"name": "Debra Stevens",
		"email": "luctus@icloud.ca"
	},
	{
		"name": "Hilary Fitzgerald",
		"email": "vitae.semper.egestas@google.ca"
	},
	{
		"name": "Petra Meadows",
		"email": "ornare@protonmail.com"
	},
	{
		"name": "Tanek Ingram",
		"email": "faucibus.id.libero@google.org"
	},
	{
		"name": "Zia Moreno",
		"email": "et.libero@yahoo.org"
	},
	{
		"name": "Beck Clarke",
		"email": "lacinia.orci@protonmail.ca"
	},
	{
		"name": "Kermit Ratliff",
		"email": "elementum.at@hotmail.org"
	},
	{
		"name": "Merrill Hendrix",
		"email": "pellentesque.habitant.morbi@protonmail.ca"
	},
	{
		"name": "Bryar Harrington",
		"email": "dis.parturient@hotmail.com"
	},
	{
		"name": "Madonna Deleon",
		"email": "nisi.a@aol.couk"
	},
	{
		"name": "Brock Vang",
		"email": "ullamcorper.eu@hotmail.edu"
	},
	{
		"name": "Uriel Holt",
		"email": "pellentesque.habitant@protonmail.ca"
	},
	{
		"name": "Phillip Russo",
		"email": "odio.nam.interdum@aol.net"
	},
	{
		"name": "Karleigh Rios",
		"email": "nisi.nibh@yahoo.org"
	},
	{
		"name": "Francesca Mullen",
		"email": "magna.ut.tincidunt@google.ca"
	},
	{
		"name": "Illiana Flynn",
		"email": "orci.lobortis@icloud.edu"
	},
	{
		"name": "Cally Andrews",
		"email": "integer.tincidunt.aliquam@hotmail.edu"
	},
	{
		"name": "Timothy Medina",
		"email": "mus.proin@hotmail.ca"
	},
	{
		"name": "Moses Keller",
		"email": "sapien.aenean@hotmail.ca"
	},
	{
		"name": "Fatima Adkins",
		"email": "nulla.ante@hotmail.org"
	},
	{
		"name": "Chelsea Winters",
		"email": "aliquam.ornare@protonmail.edu"
	},
	{
		"name": "Ian Roy",
		"email": "nibh.vulputate@hotmail.ca"
	},
	{
		"name": "Colt Davidson",
		"email": "odio.a.purus@yahoo.ca"
	},
	{
		"name": "Indigo Romero",
		"email": "elit.pellentesque.a@protonmail.com"
	},
	{
		"name": "Avye Leach",
		"email": "et.risus.quisque@yahoo.com"
	},
	{
		"name": "Lars Conway",
		"email": "egestas@protonmail.org"
	},
	{
		"name": "Octavius Olsen",
		"email": "ac@aol.com"
	},
	{
		"name": "Addison Mcknight",
		"email": "ornare.sagittis@protonmail.edu"
	},
	{
		"name": "Zena Cantu",
		"email": "accumsan.neque@google.com"
	},
	{
		"name": "Thane Benson",
		"email": "ac.facilisis.facilisis@yahoo.net"
	},
	{
		"name": "Rooney Perez",
		"email": "vel.sapien.imperdiet@outlook.net"
	},
	{
		"name": "Todd Heath",
		"email": "quis.turpis.vitae@google.org"
	},
	{
		"name": "Hoyt Soto",
		"email": "fringilla.porttitor@yahoo.couk"
	},
	{
		"name": "Grady Russell",
		"email": "justo.eu@hotmail.net"
	},
	{
		"name": "Arthur Albert",
		"email": "nibh.lacinia@outlook.edu"
	},
	{
		"name": "Malcolm Charles",
		"email": "libero.at@google.org"
	},
	{
		"name": "Cullen Ross",
		"email": "integer.aliquam@outlook.net"
	},
	{
		"name": "Cyrus Hodge",
		"email": "nonummy.ultricies@hotmail.ca"
	},
	{
		"name": "Vernon Decker",
		"email": "lobortis.tellus.justo@protonmail.com"
	},
	{
		"name": "Vincent French",
		"email": "orci@aol.ca"
	},
	{
		"name": "Fletcher Garrison",
		"email": "pretium@google.org"
	},
	{
		"name": "Axel Barr",
		"email": "porttitor@icloud.com"
	}
]

def tirar_acento(text):
	clean_text = normalize('NFKD',text).encode('ASCII','ignore').decode('ASCII')
	return clean_text

for i in data:
	username = tirar_acento(i['name']).replace(' ','')
	name = i['name']
	email = i['email']
	pwd = '12345678'
	user = Usuario.objects.create(username=username, email=email, password=pwd, name=name)
	user.save()