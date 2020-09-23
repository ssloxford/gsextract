# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class PureGse(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.gse_packet = self._root.GsePacket(self._io, self, self._root)

    class NpaHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.npa_address = self._io.read_bytes(3)


    class NullExtension(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.empty = self._io.read_bytes(0)


    class GsePayload(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._parent.gse_header.has_protocol_type:
                _on = self._parent.gse_header.protocol_type
                if _on == 2:
                    self.extension_headers = self._root.NpaHeader(self._io, self, self._root)
                else:
                    self.extension_headers = self._root.NullExtension(self._io, self, self._root)

            self.data = self._io.read_bytes_full()


    class GsePacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.gse_header = self._root.GseHeader(self._io, self, self._root)
            if not (self.gse_header.is_padding_packet):
                self._raw_gse_payload = self._io.read_bytes(((self.gse_header.payload_size - 2) if self.gse_header.payload_size > 2 else self.gse_header.payload_size))
                io = KaitaiStream(BytesIO(self._raw_gse_payload))
                self.gse_payload = self._root.GsePayload(io, self, self._root)



    class GseHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.start_indicator = self._io.read_bits_int(1) != 0
            self.end_indicator = self._io.read_bits_int(1) != 0
            self.label_type_indicator = self._io.read_bits_int(2)
            if self.is_padding_packet:
                self.padding_bits = self._io.read_bits_int(4)

            if not (self.is_padding_packet):
                self.gse_length = self._io.read_bits_int(12)

            if self.has_frag_id:
                self.frag_id = self._io.read_bits_int(8)

            if self.has_total_length:
                self.total_length = self._io.read_bits_int(16)

            if self.has_protocol_type:
                self.protocol_type = self._io.read_bits_int(16)

            self._io.align_to_byte()
            if self.has_label:
                self.label = self._io.read_bytes(self.label_size)


        @property
        def has_label(self):
            if hasattr(self, '_m_has_label'):
                return self._m_has_label if hasattr(self, '_m_has_label') else None

            self._m_has_label =  ((not (self.is_padding_packet)) and (self.start_indicator) and (self.label_type_indicator <= 1) and (self.gse_length > 12)) 
            return self._m_has_label if hasattr(self, '_m_has_label') else None

        @property
        def is_padding_packet(self):
            if hasattr(self, '_m_is_padding_packet'):
                return self._m_is_padding_packet if hasattr(self, '_m_is_padding_packet') else None

            self._m_is_padding_packet =  ((not (self.start_indicator)) and (not (self.end_indicator)) and (self.label_type_indicator == 0)) 
            return self._m_is_padding_packet if hasattr(self, '_m_is_padding_packet') else None

        @property
        def payload_size(self):
            if hasattr(self, '_m_payload_size'):
                return self._m_payload_size if hasattr(self, '_m_payload_size') else None

            self._m_payload_size = (0 if self.is_padding_packet else ((((self.gse_length - (1 if self.has_frag_id else 0)) - (2 if self.has_total_length else 0)) - (2 if self.has_protocol_type else 0)) - self.label_size))
            return self._m_payload_size if hasattr(self, '_m_payload_size') else None

        @property
        def has_frag_id(self):
            if hasattr(self, '_m_has_frag_id'):
                return self._m_has_frag_id if hasattr(self, '_m_has_frag_id') else None

            self._m_has_frag_id =  ((not (self.is_padding_packet)) and ( ((not (self.start_indicator)) or (not (self.end_indicator))) )) 
            return self._m_has_frag_id if hasattr(self, '_m_has_frag_id') else None

        @property
        def has_total_length(self):
            if hasattr(self, '_m_has_total_length'):
                return self._m_has_total_length if hasattr(self, '_m_has_total_length') else None

            self._m_has_total_length =  ((not (self.is_padding_packet)) and ( ((self.start_indicator) and (not (self.end_indicator))) )) 
            return self._m_has_total_length if hasattr(self, '_m_has_total_length') else None

        @property
        def has_protocol_type(self):
            if hasattr(self, '_m_has_protocol_type'):
                return self._m_has_protocol_type if hasattr(self, '_m_has_protocol_type') else None

            self._m_has_protocol_type =  ((not (self.is_padding_packet)) and (self.start_indicator)) 
            return self._m_has_protocol_type if hasattr(self, '_m_has_protocol_type') else None

        @property
        def label_size(self):
            if hasattr(self, '_m_label_size'):
                return self._m_label_size if hasattr(self, '_m_label_size') else None

            self._m_label_size = ((1 if self.has_label else 0) * (6 if self.label_type_indicator == 0 else (3 if self.label_type_indicator == 1 else 0)))
            return self._m_label_size if hasattr(self, '_m_label_size') else None


    class BridgedSnduHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mac_address = self._io.read_bytes(6)



