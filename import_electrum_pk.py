import hashlib
import base58
import binascii
import sys
import csv

f = open(sys.argv[1], 'rb')
reader = csv.reader(f)
for row in reader:
	if row[0] == 'address':
		continue
	private_key_WIF = row[1]
	first_encode = base58.b58decode(private_key_WIF)
	private_key_full = binascii.hexlify(first_encode)
	private_key = private_key_full[2:-8]
	private_key_static = private_key.upper()
	extended_key = "96"+private_key_static
	first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
	second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
	final_key = extended_key+second_sha256[:8]
	WIF = base58.b58encode(binascii.unhexlify(final_key))
	print "NavCoin Address: {} Private Key: {}".format(row[0], WIF)

f.close()
