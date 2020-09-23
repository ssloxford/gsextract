import enum
import struct


"""
Copyright (c) 2017 Salah Gherdaoui

Modifications (c) 2019: James Pavur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Description: Python PCAP Library
"""

class Network(enum.IntEnum):
    NULL = 0
    EN10MB = 1
    IEEE802 = 6
    ARCNET = 7
    SLIP = 8
    PPP = 9
    FDDI = 10
    ATM_RFC1483 = 11
    RAW_12 = 12
    PPP_SERIAL = 50
    PPP_ETHER = 51
    RAW_101 = 101
    C_HDLC = 104
    IEEE802_11 = 105
    LOOP = 108
    LINUX_SLL = 113
    LTALK = 114


class FileFormatError(Exception):
    pass

class Writer:
    MAJ_VER = 2
    MIN_VER = 4
    THISZONE = 0
    SIGFIGS = 0
    SNAPLEN = 65535

    def __init__(self, network=Network.RAW_101, big_endian=True):
        self.network = network
        self._magic_number = 0xa1b2c3d4
        if big_endian:
            self._hdr_fmt = '> I H H I I I I'
            self._pkt_fmt = '> I I I I'
        else:
            self._hdr_fmt = '< I H H I I I I'
            self._pkt_fmt = '< I I I I'

    def create_header(self, pcap_file):
        global_hdr_bin = struct.pack(
            self._hdr_fmt,
            self._magic_number, self.MAJ_VER, self.MIN_VER, self.THISZONE, self.SIGFIGS, self.SNAPLEN, self.network
        )
        pcap_file.write(global_hdr_bin)

    def write(self, packets_iterable, pcap_file):
        """Writes the packets in the PCAP file"""
        for *pkt_hdr, pkt_data in packets_iterable:
            pkt_hdr_bin = struct.pack(self._pkt_fmt, *pkt_hdr)
            pcap_file.write(pkt_hdr_bin)
            pcap_file.write(pkt_data)


