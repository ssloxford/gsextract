# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class PureBb(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None, matype_crib=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        if matype_crib is not None:
            self._m_matype_crib = matype_crib
        self._read()

    def _read(self):
        self.bbframe = self._root.Bbframe(self._io, self, self._root)

    class Matype2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.input_stream_identifier = self._io.read_bits_int(8)


    class Bbframe(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bbheader = self._root.Bbheader(self._io, self, self._root)
            if self.bbheader.matype_2 == 0:
                self.data_field = self._io.read_bytes((self.bbheader.data_field_length_bytes - 4))

            if self.bbheader.matype_2 == 0:
                self.crc32 = self._io.read_bytes(4)

            if self.bbheader.matype_2 != 0:
                self.corrupt_data = []
                i = 0
                while True:
                    _ = self._root.JunkData(self._io, self, self._root)
                    self.corrupt_data.append(_)
                    if _.next_byte == self._root.matype_crib:
                        break
                    i += 1



    class JunkData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.junkbyte = self._io.read_u1()

        @property
        def next_byte(self):
            if hasattr(self, '_m_next_byte'):
                return self._m_next_byte if hasattr(self, '_m_next_byte') else None

            _pos = self._io.pos()
            self._io.seek(self._io.pos())
            self._m_next_byte = self._io.read_bits_int(16)
            self._io.seek(_pos)
            return self._m_next_byte if hasattr(self, '_m_next_byte') else None


    class Bbheader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.matype_1 = self._root.Matype1(self._io, self, self._root)
            self.matype_2 = self._io.read_bits_int(8)
            if self.matype_2 == 0:
                self.user_packet_length = self._io.read_bits_int(16)

            if self.matype_2 == 0:
                self.data_field_length = self._io.read_bits_int(16)

            if self.matype_2 == 0:
                self.sync = self._io.read_bits_int(8)

            if self.matype_2 == 0:
                self.syncd = self._io.read_bits_int(16)

            if self.matype_2 == 0:
                self.crc8 = self._io.read_bits_int(8)


        @property
        def data_field_length_bytes(self):
            if hasattr(self, '_m_data_field_length_bytes'):
                return self._m_data_field_length_bytes if hasattr(self, '_m_data_field_length_bytes') else None

            self._m_data_field_length_bytes = self.data_field_length // 8
            return self._m_data_field_length_bytes if hasattr(self, '_m_data_field_length_bytes') else None


    class Matype1(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ts_gs_field = self._io.read_bits_int(2)
            self.sis_mis_field = self._io.read_bits_int(1) != 0
            self.ccm_acm_field = self._io.read_bits_int(1) != 0
            self.issyi = self._io.read_bits_int(1) != 0
            self.npd = self._io.read_bits_int(1) != 0
            self.ro = self._io.read_bits_int(2)


    @property
    def matype_crib(self):
        """This value is used to recover from broken bbheader streams by looking for the next valid bbheader.
        It can be manually edited or specified by modifying the generated constructor like so:
        def __init__(self, _io, _parent=None, _root=None, matype_crib=None):
          self._io = _io
          self._parent = _parent
          self._root = _root if _root else self
          if matype_crib is not None:
              self._m_matype_crib = matype_crib
          self._read()
        """
        if hasattr(self, '_m_matype_crib'):
            return self._m_matype_crib if hasattr(self, '_m_matype_crib') else None

        self._m_matype_crib = 16896
        return self._m_matype_crib if hasattr(self, '_m_matype_crib') else None


