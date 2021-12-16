import pytest

import solutions.day_16

def test_decode_packet_literal():
    packet, length = solutions.day_16.decode_packet('110100101111111000101000')
    assert packet.version == 6
    assert packet.type == 4
    assert packet.value == 2021

def test_decode_packet_operator_length():
    packet, length = solutions.day_16.decode_packet('00111000000000000110111101000101001010010001001000000000')
    assert packet.version == 1
    assert packet.type == 6
    assert len(packet.subpackets) == 2
    assert packet.subpackets[0].value == 10
    assert packet.subpackets[1].value == 20

def test_decode_packet_operator_count():
    packet, length = solutions.day_16.decode_packet('11101110000000001101010000001100100000100011000001100000')
    assert packet.version == 7
    assert packet.type == 3
    assert len(packet.subpackets) == 3
    assert packet.subpackets[0].value == 1
    assert packet.subpackets[1].value == 2
    assert packet.subpackets[2].value == 3


@pytest.mark.parametrize("packet,expected", [
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31),
])
def test_part_1(packet, expected):
    assert solutions.day_16.part_1(packet) == expected


@pytest.mark.parametrize("packet,expected", [
    ('C200B40A82', 3),
    ('04005AC33890', 54),
    ('880086C3E88112', 7),
    ('CE00C43D881120', 9),
    ('D8005AC2A8F0', 1),
    ('F600BC2D8F', 0),
    ('9C005AC2F8F0', 0),
    ('9C0141080250320F1802104A08', 1),
])
def test_part_2(packet, expected):
    assert solutions.day_16.part_2(packet) == expected
