# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from .tcp_segment import TcpSegment
from .udp_datagram import UdpDatagram
from .ipv4_packet import Ipv4Packet
class Ipv6Packet(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.version = self._io.read_bits_int(4)
        self.traffic_class = self._io.read_bits_int(8)
        self.flow_label = self._io.read_bits_int(20)
        self._io.align_to_byte()
        self.payload_length = self._io.read_u2be()
        self.next_header_type = self._io.read_u1()
        self.hop_limit = self._io.read_u1()
        self.src_ipv6_addr = self._io.read_bytes(16)
        self.dst_ipv6_addr = self._io.read_bytes(16)
        _on = self.next_header_type
        if _on == 17:
            self.next_header = UdpDatagram(self._io)
        elif _on == 0:
            self.next_header = self._root.OptionHopByHop(self._io, self, self._root)
        elif _on == 4:
            self.next_header = Ipv4Packet(self._io)
        elif _on == 6:
            self.next_header = TcpSegment(self._io)
        elif _on == 59:
            self.next_header = self._root.NoNextHeader(self._io, self, self._root)
        self.rest = self._io.read_bytes_full()

    class NoNextHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass


    class OptionHopByHop(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.next_header_type = self._io.read_u1()
            self.hdr_ext_len = self._io.read_u1()
            self.body = self._io.read_bytes((self.hdr_ext_len - 1))
            _on = self.next_header_type
            if _on == 0:
                self.next_header = self._root.OptionHopByHop(self._io, self, self._root)
            elif _on == 6:
                self.next_header = TcpSegment(self._io)
            elif _on == 59:
                self.next_header = self._root.NoNextHeader(self._io, self, self._root)



