# GSExtract
GSExtract is a tool for converting imperfect satellite radio captures of internet traffic transmitted using Generic Stream Encapsulation (GSE) over DVB-S into usable *.pcap files.

You can learn more about the tool and its capabilites by [watching](https://www.youtube.com/watch?v=ku0Q_Wey4K0) the corresponding Black Hat USA 2020 / DEFCON 28 briefings.

The tool was first presented at IEEE S&P 2020 in [this paper](https://doi.ieeecomputersociety.org/10.1109/SP40000.2020.00056). 

>:warning: **Disclaimer**: This tool is provided as a research proof of concept and it is the user's responsibility to ensure that they have appropriate permissions and authority for its use. Take care to adhere to regulations regarding radio communications interception if evaluating this tool in real-world systems.

## Installation
You can install from PyPI as follows:
```bash
pip install gsextract
``` 

You can also install directly from github as follows:
```bash
git clone https://github.com/ssloxford/gsextract
pip install ./gsextract
```

This will add the command ``gsextract`` to your python path. 

## Usage
Basic usage of GSExtract requires a binary file containing continuous DVB-S BBFrames as input and a file to output the resulting pcap into.

```bash
gsextract [satellite_recording.ts] [output.pcap]
```

You can also stream from a live recording of satellite traffic continuously using the ``--stream`` option. This will cause gsextract to watch the input file for new BBFrames and process them as they arrive.
```bash
gsextract --stream [satellite_recording.ts] [output.pcap]
```

### Caveats and Additional Features
#### Header Extensions
Some service providers use proprietary header extensions for GSE. Generally, parsing traffic with such extensions will require modifying the kaitai struct used for GSE data extraction (you can find it in ``gsextract/parsers/pure_gse.ksy`` and ``gsextract/parsers/pure_gse.py``).

A simple feature to try and force the addition of semi-valid IP headers can be enabled with the ``--no-reliable`` flag. This can increase the number of packets extracted with unusual GSE header extensions but can also result in false IP headers.
```bash
gsextract --no-reliable [satellite_recording.ts] [output.pcap]
```
#### Mod Codes and Multiple Input Streams
As written, GSExtract works best with streams that use the modcode 0x4200. This is by far the most common format for GSE-based services that we have encountered. However, it can also be manually overwritten in ``gsextract/parsers/pure_bb.ksy`` and ``gsextract/parsers/pure_bb.py``. Multiple input streams are not supported in this release as GSExtract requires a "crutch" Mod Code to resync with corrupt feeds. You will need to choose a single code to synchronize to at a time but can, of course, run gsextract multiple times on a given file as a workaround. Pull requests adding multiple input stream support in a smoother way are very much welcome.

#### TCP Hijacking
The command line version of the tool does not include support for TCP hijacking by default as many of the implementation details are scenario and network specific. However, you can find an example of TCP hijacking using GSExtract at the bottom of the ``gsextract/gse_parser.py`` file as a starting model.

#### Sample Data
For privacy reasons, I cannot provide sample recordings of real-world GSE streams. For testing purposes a small sanitized GSE recording is provided as ``sample.ts``. IP addresses and payloads have been overwritten. Running gsextract in normal mode should recover a pcap with two packets from this file. Running it with the ``--no-reliable`` flag should recover two additional packets.

## Logistics
### Authors
This tool was developed by James Pavur. It is part of a larger research initiative on satellite communications security conducted in partnership between the University of Oxford's [Systems Secuirty Lab](https://seclab.cs.ox.ac.uk/) and armasuisse's [Cyber-Defense Campus](https://www.ar.admin.ch/en/armasuisse-wissenschaft-und-technologie-w-t/cyber-defence_campus.html).

### Contributing
Pull requests are always welcome. Some particularly desirable additions include:
* Support for more GSE header extensions in the kaitai struct
* Mod Code flexibility in the CLI tool
* Support for multiple input streams in a single run

### Citing This Tool
If you happen to use GSExtract for academic research, we would greatly appreciate a citation to the paper where it originally appeared:
> J. Pavur, D. Moser, M. Strohmeier, V. Lenders and I. Martinovic,  "A Tale of Sea and Sky On the Security of Maritime VSAT Communications," in 2020 IEEE Symposium on Security and Privacy (SP), San Francisco, CA, US, 2020 pp. 1384-1400. doi: 10.1109/SP40000.2020.00056

### Acknowledgements
This tool would have been a million times more complex and difficult to build if not for the awesome Katiai Struct langauge. Check it out at [kaitai.io](https://kaitai.io/).

This tool also contains a modified version of Salah Gherdaoui's [pcaplib](https://pypi.org/project/pcaplib/#description). It makes it easy for GSExtract to dump IP packets to *.pcap files in real-time. For more deep (but slower) traffic parsing, we also use the venerable [scapy](https://scapy.net/).

## License
[MIT](https://choosealicense.com/licenses/mit/)