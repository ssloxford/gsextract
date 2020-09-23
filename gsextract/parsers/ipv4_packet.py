# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from .tcp_segment import TcpSegment
from .udp_datagram import UdpDatagram
from .icmp_packet import IcmpPacket
class Ipv4Packet(KaitaiStruct):

    class ProtocolEnum(Enum):
        hopopt = 0
        icmp = 1
        igmp = 2
        ggp = 3
        ipv4 = 4
        st = 5
        tcp = 6
        cbt = 7
        egp = 8
        igp = 9
        bbn_rcc_mon = 10
        nvp_ii = 11
        pup = 12
        argus = 13
        emcon = 14
        xnet = 15
        chaos = 16
        udp = 17
        mux = 18
        dcn_meas = 19
        hmp = 20
        prm = 21
        xns_idp = 22
        trunk_1 = 23
        trunk_2 = 24
        leaf_1 = 25
        leaf_2 = 26
        rdp = 27
        irtp = 28
        iso_tp4 = 29
        netblt = 30
        mfe_nsp = 31
        merit_inp = 32
        dccp = 33
        x_3pc = 34
        idpr = 35
        xtp = 36
        ddp = 37
        idpr_cmtp = 38
        tp_plus_plus = 39
        il = 40
        ipv6 = 41
        sdrp = 42
        ipv6_route = 43
        ipv6_frag = 44
        idrp = 45
        rsvp = 46
        gre = 47
        dsr = 48
        bna = 49
        esp = 50
        ah = 51
        i_nlsp = 52
        swipe = 53
        narp = 54
        mobile = 55
        tlsp = 56
        skip = 57
        ipv6_icmp = 58
        ipv6_nonxt = 59
        ipv6_opts = 60
        any_host_internal_protocol = 61
        cftp = 62
        any_local_network = 63
        sat_expak = 64
        kryptolan = 65
        rvd = 66
        ippc = 67
        any_distributed_file_system = 68
        sat_mon = 69
        visa = 70
        ipcv = 71
        cpnx = 72
        cphb = 73
        wsn = 74
        pvp = 75
        br_sat_mon = 76
        sun_nd = 77
        wb_mon = 78
        wb_expak = 79
        iso_ip = 80
        vmtp = 81
        secure_vmtp = 82
        vines = 83
        iptm = 84
        nsfnet_igp = 85
        dgp = 86
        tcf = 87
        eigrp = 88
        ospfigp = 89
        sprite_rpc = 90
        larp = 91
        mtp = 92
        ax_25 = 93
        ipip = 94
        micp = 95
        scc_sp = 96
        etherip = 97
        encap = 98
        any_private_encryption_scheme = 99
        gmtp = 100
        ifmp = 101
        pnni = 102
        pim = 103
        aris = 104
        scps = 105
        qnx = 106
        a_n = 107
        ipcomp = 108
        snp = 109
        compaq_peer = 110
        ipx_in_ip = 111
        vrrp = 112
        pgm = 113
        any_0_hop = 114
        l2tp = 115
        ddx = 116
        iatp = 117
        stp = 118
        srp = 119
        uti = 120
        smp = 121
        sm = 122
        ptp = 123
        isis_over_ipv4 = 124
        fire = 125
        crtp = 126
        crudp = 127
        sscopmce = 128
        iplt = 129
        sps = 130
        pipe = 131
        sctp = 132
        fc = 133
        rsvp_e2e_ignore = 134
        mobility_header = 135
        udplite = 136
        mpls_in_ip = 137
        manet = 138
        hip = 139
        shim6 = 140
        wesp = 141
        rohc = 142
        reserved_255 = 255
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.b1 = self._io.read_u1()
        self.b2 = self._io.read_u1()
        self.total_length = self._io.read_u2be()
        self.identification = self._io.read_u2be()
        self.b67 = self._io.read_u2be()
        self.ttl = self._io.read_u1()
        self.protocol = self._root.ProtocolEnum(self._io.read_u1())
        self.header_checksum = self._io.read_u2be()
        self.src_ip_addr = self._io.read_bytes(4)
        self.dst_ip_addr = self._io.read_bytes(4)
        self._raw_options = self._io.read_bytes((self.ihl_bytes - 20))
        io = KaitaiStream(BytesIO(self._raw_options))
        self.options = self._root.Ipv4Options(io, self, self._root)
        _on = self.protocol
        if _on == self._root.ProtocolEnum.tcp:
            self._raw_body = self._io.read_bytes((self.total_length - self.ihl_bytes))
            io = KaitaiStream(BytesIO(self._raw_body))
            self.body = TcpSegment(io)
        elif _on == self._root.ProtocolEnum.icmp:
            self._raw_body = self._io.read_bytes((self.total_length - self.ihl_bytes))
            io = KaitaiStream(BytesIO(self._raw_body))
            self.body = IcmpPacket(io)
        elif _on == self._root.ProtocolEnum.udp:
            self._raw_body = self._io.read_bytes((self.total_length - self.ihl_bytes))
            io = KaitaiStream(BytesIO(self._raw_body))
            self.body = UdpDatagram(io)
        else:
            self.body = self._io.read_bytes((self.total_length - self.ihl_bytes))

    class Ipv4Options(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(self._root.Ipv4Option(self._io, self, self._root))
                i += 1



    class Ipv4Option(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.b1 = self._io.read_u1()
            self.len = self._io.read_u1()
            self.body = self._io.read_bytes(((self.len - 2) if self.len > 2 else 0))

        @property
        def copy(self):
            if hasattr(self, '_m_copy'):
                return self._m_copy if hasattr(self, '_m_copy') else None

            self._m_copy = ((self.b1 & 128) >> 7)
            return self._m_copy if hasattr(self, '_m_copy') else None

        @property
        def opt_class(self):
            if hasattr(self, '_m_opt_class'):
                return self._m_opt_class if hasattr(self, '_m_opt_class') else None

            self._m_opt_class = ((self.b1 & 96) >> 5)
            return self._m_opt_class if hasattr(self, '_m_opt_class') else None

        @property
        def number(self):
            if hasattr(self, '_m_number'):
                return self._m_number if hasattr(self, '_m_number') else None

            self._m_number = (self.b1 & 31)
            return self._m_number if hasattr(self, '_m_number') else None


    @property
    def version(self):
        if hasattr(self, '_m_version'):
            return self._m_version if hasattr(self, '_m_version') else None

        self._m_version = ((self.b1 & 240) >> 4)
        return self._m_version if hasattr(self, '_m_version') else None

    @property
    def ihl(self):
        if hasattr(self, '_m_ihl'):
            return self._m_ihl if hasattr(self, '_m_ihl') else None

        self._m_ihl = (self.b1 & 15)
        return self._m_ihl if hasattr(self, '_m_ihl') else None

    @property
    def ihl_bytes(self):
        if hasattr(self, '_m_ihl_bytes'):
            return self._m_ihl_bytes if hasattr(self, '_m_ihl_bytes') else None

        self._m_ihl_bytes = (self.ihl * 4)
        return self._m_ihl_bytes if hasattr(self, '_m_ihl_bytes') else None


