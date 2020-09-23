meta:
  id: pure_bb
  file-extension: pure_bb
  ks-version: 0.8
  xref:
    etsi: "ETSI EN 302 307 V1.3.1"
    url: "https://www.dvb.org/resources/public/standards/a83-1_dvb-s2_den302307v141.pdf"
seq:
  - id: bbframe
    type: bbframe
types:
  bbframe:
    seq:
      - id: bbheader
        type: bbheader
      - id: data_field
        size: bbheader.data_field_length_bytes - 4
        if: bbheader.matype_2 == 0
      - id: crc32
        size: 4
        if: bbheader.matype_2 ==0
      - id: corrupt_data
        type: junk_data
        repeat: until
        repeat-until: _.next_byte == _root.matype_crib
        if: bbheader.matype_2 != 0
  bbheader:
    seq:
      - id: matype_1
        type: matype_1
      - id: matype_2
        type: b8
      - id: user_packet_length
        type: b16
        if: matype_2 == 0
      - id: data_field_length
        type: b16
        if: matype_2 == 0
      - id: sync
        type: b8
        if: matype_2 == 0
      - id: syncd
        type: b16
        if: matype_2 == 0
      - id: crc8
        type: b8
        if: matype_2 == 0
    instances:
      data_field_length_bytes:
        value: data_field_length / 8
  matype_1:
    seq:
      - id: ts_gs_field
        type: b2
      - id: sis_mis_field
        type: b1
      - id: ccm_acm_field
        type: b1
      - id: issyi
        type: b1
      - id: npd
        type: b1
      - id: ro
        type: b2
  matype_2:
    seq:
      - id: input_stream_identifier
        type: b8
  junk_data:
    seq:
      - id: junkbyte
        type: u1
    instances:
      next_byte:
        pos: _io.pos
        type: b16
        consume: false
instances:
  matype_crib:
    value: 0x4200
    doc: |
      This value is used to recover from broken bbheader streams by looking for the next valid bbheader.
      It can be manually edited or specified by modifying the generated constructor like so:
      def __init__(self, _io, _parent=None, _root=None, matype_crib=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        if matype_crib is not None:
            self._m_matype_crib = matype_crib
        self._read()
