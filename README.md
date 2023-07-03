<h1><p align="center">debank-balance-checker</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker (image)](#Docker-image)
    - [Docker (building)](#Docker-building)
    - [Source code](#Source-code)
- [Updating](#Updating)
  - [Windows](#Windows-1)
  - [GitHub image](#GitHub-image)
  - [Self-built image](#Self-built-image)
  - [Source code](#Source-code-1)
- [Useful commands](#Useful-commands)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program allows you to get balances of multiple addresses in major EVM networks.

⠀You will get a file with address balances (it's a random address from the explorer) in the form of:
```
Checking time: 18.12.2022 17:46
Total addresses: 2
Total balance: $2 326,8
------------------------ Address 0x15B328F211B7a9387CA4da4a6DB4990eAF37b1b4 ($2 326,8)

------------ arb ($2 148,23)
Tokens (12):
	85,01545735697975 LINK ($506,23)
	0,1998371833314386 ETH ($238,45)
	60,34684755015808 MAGIC ($39,74)
	0,153232291 UMAMI ($4,17)
	0,011875982337469945 DPX ($3,11)
	0,42336718595517076 LPT ($2,43)
	2,1442310441348003 VSTA ($0,64)
	13,751385031520602 DBL ($0,54)
	0,9914809481477813 SYN ($0,47)
	22,666208278561268 MYC ($0,33)
	13,375809378345153 SWPR ($0,23)
	13,364228884033292 TCR ($0,19)


Projects (3):
	GMX https://gmx.io: ($1 302,54)
		Staked ($1 302,54): 27,080201307800596 GMX ($1 250,99)

	Shell V2 https://shellprotocol.io: ($41,93)
		Staked ($10,0): 9,995943 USDT ($10,0)
		Staked ($10,03): 6,587954883250013 DAI ($6,58) + 3,443411599988287 USDC ($3,44)
		Staked ($9,98): 9,988044249488647 DAI ($9,98)
		Staked ($11,93): 0,01 ETH ($11,93)

	Stargate https://stargate.finance: ($7,23)
		Locked ($7,23): 20,374894323180875 STG ($7,23)



NFTs (7):
	1 pcs, #8969, collection: Government Toucans, avg. price: 0,015000900000000001 ETH ($19,57)
	1 pcs, #209745, collection: Arbitrum Odyssey NFT, avg. price: 0,01789938861111111 ETH ($0,19)
	1 pcs, imToken & EtherPOAP, collection: imToken & EtherPOAP Community AMA, avg. price: 0,000299 ETH ($0,07)
	1 pcs, NovaNaut 898, collection: NovaNauts, avg. price: 0,00245 ETH ($0,05)
	1 pcs, Robonaut 2027, collection: Robonaut, avg. price: 0,0029 ETH ($0,09)
	1 pcs, Robonaut 2026, collection: Robonaut, avg. price: 0,0029 ETH ($0,09)
	1 pcs, Robonaut 2028, collection: Robonaut, avg. price: 0,0029 ETH ($0,09)


------------ op ($145,21)
Tokens (6):
	52,427568581635704 sUSD ($53,08)
	0,04324848188698601 ETH ($51,6)
	35,101183813126625 DAI ($35,07)
	3,7273421352763108 OP ($3,51)
	1,942618 USDC ($1,94)
	4,933268470528e-06 BAL ($0,0)


Projects (1):
	Polynomial https://earn.polynomial.fi: ($0,0)
		Yield ($0,0): 3,7177394773287843e-06 sUSD ($0,0)



NFTs (13):
	1 pcs, Optiape #44, collection: Optimism Ape Yacht Club, avg. price: 0,046156410256410256 ETH ($0,0)
	1 pcs, #18534, collection: Early Optimists, avg. price: 0,018685537740740756 ETH ($0,0)
	1 pcs, Introducing the Optimism Collective 49281/524120, collection: Introducing the Optimism Collective, avg. price: 0,008898730177369986 ETH ($0,0)
	1 pcs, Velodrome Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, Synapse Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, Granary Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, Polynomial Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, Pika Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, #1594914, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, UniSwap Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, Rubicon Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, Stargate Op quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)
	1 pcs, PoolTogether Op Quest, collection: Optimism Quests, avg. price: 0,0047534222601566915 ETH ($0,0)


------------ nova ($28,87)
Tokens (4):
	17,617687 USDC ($17,62)
	0,004908081200000027 ETH ($5,86)
	49,20133201114597 MOON ($4,27)
	176,4812871650478 BRICK ($1,12)


------------ matic ($3,72)
Tokens (5):
	2,677383264639221 MATIC ($2,2)
	0,001001198082711628 WETH ($1,19)
	0,4 WMATIC ($0,33)
	0,003863 USDC ($0,0)
	10,0 CP ($0,0)


NFTs (38):
	1 pcs, Post by @lensbeats.lens, collection: lensbeats.lens-Collect-5, avg. price: 1,0 MATIC ($0,09)
	1 pcs, valcryptoast.lens's follower NFT, collection: valcryptoast.lens-Follower, avg. price: 0,25 MATIC ($0,01)
	1 pcs, cryptoast.lens's follower NFT, collection: cryptoast.lens-Follower, avg. price: 0,0 MATIC ($0,01)
	1 pcs, Arbitrum Odyssey Hopper, collection: Galxe OAT, avg. price: 1,292370385561254 MATIC ($0,0)
	1 pcs, SyncSwap Testnet Badge, collection: Galxe OAT, avg. price: 1,292370385561254 MATIC ($0,0)
	1 pcs, Pooly Floatie, collection: ICE Poker Tournament Wearables, avg. price: 1,3143900159627069 MATIC ($0,0)
	1 pcs, SyncSwap Testnet Voter, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Galxe Rebrand Celebration OAT, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)
	1 pcs, Mint Square Test & Earn Badge, collection: Galaxy OAT - TJiioVCGDQ, avg. price: 0,8115108729316179 MATIC ($0,0)


------------ eth ($0,77)
Tokens (1):
	0,000645402034316293 ETH ($0,77)


NFTs (2):
	1 pcs, Galxe ETH Merge NFT, collection: Galxe ETH Merge NFT, avg. price: 0,001 ETH ($2,13)
	1 pcs, Regenesis: Open Edition, collection: The Merge: Regenesis, avg. price: 0,0014999999999999998 ETH ($1,66)



------------------------ Address 0x15B328F211B7a9387CA4da4a6DB4990eAF37b1b3 ($0)
ERROR

Not parsed balances (1):
0x15B328F211B7a9387CA4da4a6DB4990eAF37b1b3
```



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[debank-balance-checker](https://github.com/SecorD0/debank-balance-checker)

⠀[DeBank](https://debank.com/)

⠀[DeBank async library](https://github.com/SecorD0/py-debank-async)

⠀[DeBank sync library](https://github.com/SecorD0/py-debank)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `addresses.txt` — a text file with addresses to be checked;
  - `errors.log` — a log file with errors that occurred during the work;
  - `proxies.txt` — a text file with HTTP IPv4/IPv6 proxies;
  - `result.txt` — a text file with the results in a readable form;
  - `settings.json` — a JSON file for program setup.
- `debank-balance-checker.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/debank-balance-checker/releases).
2. Create a folder and put the EXE file in it.
3. Run the program the first time and press `Enter` to create necessary files.
4. Insert addresses to be checked into the `addresses.txt` file.
5. Insert HTTP IPv4/IPv6 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
The optimal `address:proxy` ratio when checking without NFTs would be 1:2 (10 addresses + 20 proxies), when checking with NFTs 1:3.
6. Configure the `settings.json` if you want:
   - `threads` — the number of threads (>10 not recommended);
   - `parse_nfts` — whether to parse NFTs (`true` or `false`).
7. Run the program.
8. You can see the following statuses:
   - `[V]` — the balance was parsed successfully;
   - `[X]` — the balance was parsed unsuccessfully three times.
This can happen if you get a balance from 1 IP too often.
9. Delete already parsed addresses from the `addresses.txt` file and repeat steps 7-9 after some time,
if there are still addresses whose balances couldn't be parsed.
10. Open the `result.txt` file and look at the result of the program.


<h2><p align="center">Docker (image)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run the program the first time and press `Enter` to create necessary files:
```sh
docker run -it --rm -v $HOME/debank-balance-checker/files:/program/files --name debank-balance-checker ghcr.io/secord0/debank-balance-checker:main
```
3. Insert addresses to be checked into the `addresses.txt` file.
4. Insert HTTP IPv4/IPv6 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
The optimal `address:proxy` ratio when checking without NFTs would be 1:2 (10 addresses + 20 proxies), when checking with NFTs 1:3.
5. Configure the `settings.json` if you want:
   - `threads` — the number of threads (>10 not recommended);
   - `parse_nfts` — whether to parse NFTs (`true` or `false`).
6. Run the program:
```sh
docker run -it --rm -v $HOME/debank-balance-checker/files:/program/files --name debank-balance-checker ghcr.io/secord0/debank-balance-checker:main
```
7. You can see the following statuses:
   - `[V]` — the balance was parsed successfully;
   - `[X]` — the balance was parsed unsuccessfully three times.
This can happen if you get a balance from 1 IP too often.
8. Delete already parsed addresses from the `addresses.txt` file and repeat step 9-11 after some time,
if there are still addresses whose balances couldn't be parsed.
9. Open the `result.txt` file and look at the result of the program.


<h2><p align="center">Docker (building)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
cd; git clone https://github.com/SecorD0/debank-balance-checker
```
3. Go to the repository:
```sh
cd debank-balance-checker
```
4. Build an image:
```sh
docker build -t debank-balance-checker .
```
5. Run the program the first time and press `Enter` to create necessary files:
```sh
docker run -it --rm -v $HOME/debank-balance-checker/:/program --name debank-balance-checker debank-balance-checker
```
6. Insert addresses to be checked into the `addresses.txt` file.
7. Insert HTTP IPv4/IPv6 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
The optimal `address:proxy` ratio when checking without NFTs would be 1:2 (10 addresses + 20 proxies), when checking with NFTs 1:3.
8. Configure the `settings.json` if you want:
   - `threads` — the number of threads (>10 not recommended);
   - `parse_nfts` — whether to parse NFTs (`true` or `false`).
9. Run the program:
```sh
docker run -it --rm -v $HOME/debank-balance-checker/:/program --name debank-balance-checker debank-balance-checker
```
10. You can see the following statuses:
   - `[V]` — the balance was parsed successfully;
   - `[X]` — the balance was parsed unsuccessfully three times.
    This can happen if you get a balance from 1 IP too often.
11. Delete already parsed addresses from the `addresses.txt` file and repeat step 9-11 after some time,
if there are still addresses whose balances couldn't be parsed.
12. Open the `result.txt` file and look at the result of the program.


<h2><p align="center">Source code</p></h2>

1. Install [Python 3.8](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/debank-balance-checker
```
3. Go to the repository:
```sh
cd debank-balance-checker
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py` the first time and press `Enter` to create necessary files.
7. Insert addresses to be checked into the `addresses.txt` file.
8. Insert HTTP IPv4/IPv6 proxies in the `login:password@ip:port` format into the `proxies.txt` file.
The optimal `address:proxy` ratio when checking without NFTs would be 1:2 (10 addresses + 20 proxies), when checking with NFTs 1:3.
9. Configure the `settings.json` if you want:
   - `threads` — the number of threads (>10 not recommended);
   - `parse_nfts` — whether to parse NFTs (`true` or `false`).
10. Run the `app.py`.
11. You can see the following statuses:
    - `[V]` — the balance was parsed successfully;
    - `[X]` — the balance was parsed unsuccessfully three times.
    This can happen if you get a balance from 1 IP too often.
12. Delete already parsed addresses from the `addresses.txt` file and repeat steps 10-12 after some time,
if there are still addresses whose balances couldn't be parsed.
13. Open the `result.txt` file and look at the result of the program.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn debank-balance-checker -i images/icons/app.ico --add-binary "images/icons;images/icons"
```



<h1><p align="center">Updating</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file of the new version from the [releases page](https://github.com/SecorD0/debank-balance-checker/releases) and replace the old one with it.


<h2><p align="center">GitHub image</p></h2>

1. Stop the container:
```sh
docker stop debank-balance-checker
```
2. Remove the container:
```sh
docker rm debank-balance-checker
```
3. Update the image:
```sh
docker pull ghcr.io/secord0/debank-balance-checker:main
```


<h2><p align="center">Self-built image</p></h2>

1. Stop the container:
```sh
docker stop debank-balance-checker
```
2. Remove the container:
```sh
docker rm debank-balance-checker
```
3. Go to the repository:
```sh
cd debank-balance-checker
```
4. Update the local files:
```sh
git pull
```
5. Rebuild the image:
```sh
docker build -t debank-balance-checker .
```


<h2><p align="center">Source code</p></h2>

1. Go to the repository:
```sh
cd debank-balance-checker
```
2. Update the local files:
```sh
git pull
```



<h1><p align="center">Useful commands</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀To run the program (GitHub image):
```sh
docker run -it --rm -v $HOME/debank-balance-checker/files:/program/files --name debank-balance-checker ghcr.io/secord0/debank-balance-checker:main
```

⠀To run the program (self-built image):
```sh
docker run -it --rm -v $HOME/debank-balance-checker/:/program --name debank-balance-checker debank-balance-checker
```

⠀To remove the container:
```sh
docker stop debank-balance-checker; docker rm debank-balance-checker
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/debank-balance-checker/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Address of EVM networks (Ethereum, Polygon, BSC, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
