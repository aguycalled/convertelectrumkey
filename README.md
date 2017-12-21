# convertelectrumkey

Instructions:

1. Go to NavCoin Electrum
2. Wallet -> Private Keys -> Export
3. Enter your password
3. Format: CSV
4. Choose Location where Private Keys will be saved
5. Export.
6. Go to a terminal (Unix/Mac) and type:
```
git clone https://github.com/aguycalled/convertelectrumkey && cd convertelectrumkey
python import_electrum_pk.py /Location/Where/Private/Keys.Are.Saved.csv
```
Sample Output:
```
$ python convert ../electrum-private-keys.csv 
NavCoin Address: NR9eUDCyWGX3W89NDXvNRaV1uFBzHZ8acb Private Key: PGeYWC4vojjeQgUN9g9sJWLLk7GRR42JHjGT42bwTuX8PLANNmju
NavCoin Address: NWFv9XiurZ2NNQ93TYihtAxGu9pE6d9aKx Private Key: PEKCxr5UumXa11tYmnNgDWkTKgjQgRWy5dhhTvUtXUS7PrbG6ciH
NavCoin Address: NXTyigN9qDZuTi27uyLXzoegYJkt5DqBoE Private Key: PD44ud5b89d4sz4FV3BXHiJJDDvNoPVTSeNmp5aNwgn8noTXRCsJ
NavCoin Address: NdgQZtSTyzJPSkgd6av4NccuLQgcjEsXZH Private Key: PCHXHZ82ua4Zop9sokbc3Z2cvnP7UuHyr9zGPakzpTpNzbvYNsC9
```
7. Go to NavCoin Core Wallet
8. Help -> Debug Window
9. Import the different private keys using 'importprivkey'. e.g:
```
importprivkey PD1SKRBoKftg9fqGVUasfVUtu4iDVsSoMb68ZRgFKce8PUKt29tr
```
