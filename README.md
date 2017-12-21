# convertelectrumkey

## What is this?
This is a tool to help users get their coins out of the NavCoin Electrum Wallet. It allows you to convert your electrum Private Key to a format the [NavCoin Core Wallet](https://github.com/NAVCoin/navcoin-core/) can accept.

## Requirements
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (optional)
- [Python v2.7.10](https://www.python.org/downloads/release/python-2710/)
- Python Package `base58` (See Troubleshooting below for install instructions)

## Instructions:

0. Make sure you have the Requirements installed.
1. Go to NavCoin Electrum
2. Wallet -> Private Keys -> Export
3. Enter your password
3. Format: CSV
4. Choose Location where Private Keys will be saved
5. Export
6. Download this repo:
  - (Without using git) Download this git repo as a zip and extract it. In your terminal navigate to the extracted directory.
  - (Using git) Open a terminal (Unix/Mac) or CMD/Powershell (Windows) and type:
```
git clone https://github.com/aguycalled/convertelectrumkey && cd convertelectrumkey
```
7. After downloading and extracting, in your terminal run
```
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

## Common issues


- I'm getting an error like ` File ".\import_electrum_pk.py", line 2, in <module>   import base58` ?
  - You're missing the base58 package. Run the following to install it:
    - Windows: (Run Powershell/CMD as Administrator)
    ```
    pip install --upgrade pip
    pip install base58
    ```
    - Unix/Mac
    ```
    sudo pip install --upgrade pip
    sudo pip install base58
    ```

- I'm getting an `SyntaxError: invalid syntax` error?
 - Make sure you have Python Version 2.7.10

- Python/Git can't be found even though I have installed them?
  - After installing you may need to close and reopen your terminal/CMD/Powershell.
  - For Windows your PATH may not be configured correctly. In this case running the following in Powershell, then closing and reopening Powershell will fix the issue (if you used the default installation path for Python):
  ```
    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")
  ```


For further troubleshooting assistance, visit the [NavCoin Discord](https://discordapp.com/invite/y4Vu9jw)
