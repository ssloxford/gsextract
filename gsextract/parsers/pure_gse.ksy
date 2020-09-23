meta:
  id: pure_gse
  file-extension: pure_gse
seq:
  - id: gse_packet
    type: gse_packet
types:
  gse_packet:
    seq:
      - id: gse_header
        type: gse_header
      - id: gse_payload
        type: gse_payload
        size: 'gse_header.payload_size > 2 ? gse_header.payload_size - 2: gse_header.payload_size'
        if: not gse_header.is_padding_packet
  gse_header:
    seq:
      - id: start_indicator
        type: b1
      - id: end_indicator
        type: b1
      - id: label_type_indicator
        type: b2
      - id: padding_bits
        type: b4
        if: is_padding_packet
      - id: gse_length
        type: b12
        if: not is_padding_packet
      - id: frag_id
        type: b8
        if: has_frag_id
      - id: total_length
        type: b16
        if: has_total_length
      - id: protocol_type
        type: b16
        if: has_protocol_type
      - id: label
        size: label_size
        if: has_label
    instances:
      is_padding_packet:
        value: not start_indicator and not end_indicator and label_type_indicator == 0
      has_frag_id:
        value: not is_padding_packet and (not start_indicator or not end_indicator)
      has_total_length:
        value: not is_padding_packet and (start_indicator and not end_indicator)
      has_protocol_type:
        value: not is_padding_packet and start_indicator
      has_label:
        value: not is_padding_packet and start_indicator and label_type_indicator <= 1 and gse_length > 12
      label_size:
        value: '(has_label ? 1 : 0) * (label_type_indicator == 0 ? 6 : (label_type_indicator == 1 ? 3 : 0))'
      payload_size:
        value: 'is_padding_packet ? 0 : gse_length - (has_frag_id ? 1 : 0) - (has_total_length ? 2 : 0) - (has_protocol_type ? 2 : 0) - label_size'
  gse_payload:
    seq:
      - id: extension_headers
        if: _parent.gse_header.has_protocol_type
        type:
          switch-on: _parent.gse_header.protocol_type
          cases:
            2: npa_header
            _: null_extension
      - id: data
        size-eos: true
  npa_header:
    seq:
      - id: npa_address
        size: 3
  bridged_sndu_header:
    seq:
      - id: mac_address
        size: 6
  null_extension:
    seq:
      - id: empty
        size: 0