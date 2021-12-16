import math

from utils.math import hex_to_bin

OPERATORS = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda vals: 1 if vals[0] > vals[1] else 0,
    6: lambda vals: 1 if vals[0] < vals[1] else 0,
    7: lambda vals: 1 if vals[0] == vals[1] else 0,
}

class Packet:
    def __init__(self):
        self.version = None
        self.type = None
        self.value = None
        self.subpackets = []
    def sum_version(self):
        version_sum = self.version
        for sp in self.subpackets:
            version_sum += sp.sum_version()
        return version_sum

def decode_packet(transmission):
    packet = Packet()
    length = 0

    packet.version = int(transmission[:3], base=2)
    transmission = transmission[3:]
    length += 3

    packet.type = int(transmission[:3], base=2)
    transmission = transmission[3:]
    length += 3

    if packet.type == 4:
        is_last = False
        value_string = '0b'
        while not is_last:
            group = transmission[:5]
            if group[0] == '0':
                is_last = True
            value_string += group[1:]
            transmission = transmission[5:]
            length += 5
        packet.value = int(value_string, base=2)
    else:
        length_type = transmission[0]
        transmission = transmission[1:]
        length += 1
        if length_type == '0':
            sub_length_total = int(transmission[:15], base=2)
            transmission = transmission[15:]
            length += 15

            sub_length_start = length
            while length - sub_length_start != sub_length_total:
                sp, l = decode_packet(transmission)
                length += l
                packet.subpackets.append(sp)
                transmission = transmission[l:]
        else:
            sub_count = int(transmission[:11], base=2)
            transmission = transmission[11:]
            length += 11

            for _ in range(0, sub_count):
                sp, l = decode_packet(transmission)
                length += l
                packet.subpackets.append(sp)
                transmission = transmission[l:]

        subpacket_vals = [sp.value for sp in packet.subpackets]
        packet.value = OPERATORS[packet.type](subpacket_vals)

    return packet, length

def part_1(hex_transmission):
    packet, _ = decode_packet(hex_to_bin(hex_transmission))
    return packet.sum_version()

def part_2(hex_transmission):
    packet, _ = decode_packet(hex_to_bin(hex_transmission))
    return packet.value


if __name__ == '__main__':
    with open('input', 'r') as f:
        packet = f.readline().rstrip()
        print(part_1(packet))
        print(part_2(packet))
