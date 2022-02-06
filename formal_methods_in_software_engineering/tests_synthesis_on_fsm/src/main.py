from unittest import TestCase
from automatic_door_fsm import AutomaticDoor


def test_fsm(input_seq):
    door = AutomaticDoor()
    out = str()
    transits = input_seq.split(' ')
    for t in transits:
        trigger = t.split('/')[0]
        eval(''.join(['door.', trigger, '()']))
        out += door.out + ' '
    return out[:-1]


class FSMTest(TestCase):
    def test_0(self):
        self.assertEqual(test_fsm('open/ALARM open/NULL open/NULL'), 'ALARM NULL NULL')

    def test_1(self):
        self.assertEqual(test_fsm('open/ALARM open/NULL lock/NULL open/NULL'), 'ALARM NULL NULL NULL')

    def test_2(self):
        self.assertEqual(test_fsm('open/ALARM open/NULL unlock/NULL'), 'ALARM NULL NULL')

    def test_3(self):
        self.assertEqual(test_fsm('open/ALARM close/NULL open/NULL'), 'ALARM NULL NULL')

    def test_4(self):
        self.assertEqual(test_fsm('open/ALARM close/NULL lock/NULL open/NULL'), 'ALARM NULL NULL NULL')

    def test_5(self):
        self.assertEqual(test_fsm('open/ALARM close/NULL unlock/NULL'), 'ALARM NULL NULL')

    def test_6(self):
        self.assertEqual(test_fsm('open/ALARM lock/NULL open/NULL'), 'ALARM NULL NULL')

    def test_7(self):
        self.assertEqual(test_fsm('open/ALARM lock/NULL lock/NULL open/NULL'), 'ALARM NULL NULL NULL')

    def test_8(self):
        self.assertEqual(test_fsm('open/ALARM lock/NULL unlock/NULL'), 'ALARM NULL NULL')

    def test_9(self):
        self.assertEqual(test_fsm('open/ALARM unlock/NULL open/NULL'), 'ALARM NULL NULL')

    def test_10(self):
        self.assertEqual(test_fsm('open/ALARM unlock/NULL lock/NULL open/NULL'), 'ALARM NULL NULL NULL')

    def test_11(self):
        self.assertEqual(test_fsm('open/ALARM unlock/NULL unlock/NULL'), 'ALARM NULL NULL')

    def test_12(self):
        self.assertEqual(test_fsm('close/NULL open/ALARM'), 'NULL ALARM')

    def test_13(self):
        self.assertEqual(test_fsm('close/NULL lock/NULL open/ALARM'), 'NULL NULL ALARM')

    def test_14(self):
        self.assertEqual(test_fsm('close/NULL unlock/BIP_1'), 'NULL BIP_1')

    def test_15(self):
        self.assertEqual(test_fsm('lock/NULL open/ALARM'), 'NULL ALARM')

    def test_16(self):
        self.assertEqual(test_fsm('lock/NULL lock/NULL open/ALARM'), 'NULL NULL ALARM')

    def test_17(self):
        self.assertEqual(test_fsm('lock/NULL unlock/BIP_1'), 'NULL BIP_1')

    def test_18(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL open/NULL open/NULL'), 'BIP_1 NULL NULL NULL')

    def test_19(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL open/NULL lock/BIP_2 open/NULL'),
                         'BIP_1 NULL NULL BIP_2 NULL')

    def test_20(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL open/NULL unlock/NULL'), 'BIP_1 NULL NULL NULL')

    def test_21(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL close/NULL open/NULL'), 'BIP_1 NULL NULL NULL')

    def test_22(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL close/NULL lock/BIP_2 open/ALARM'),
                         'BIP_1 NULL NULL BIP_2 ALARM')

    def test_23(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL close/NULL unlock/NULL'), 'BIP_1 NULL NULL NULL')

    def test_24(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 open/NULL open/NULL'),
                         'BIP_1 NULL BIP_2 NULL NULL')

    def test_25(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 open/NULL lock/NULL open/NULL'),
                         'BIP_1 NULL BIP_2 NULL NULL NULL')

    def test_26(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 open/NULL unlock/BIP_1'),
                         'BIP_1 NULL BIP_2 NULL BIP_1')

    def test_27(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 close/NULL open/ALARM'),
                         'BIP_1 NULL BIP_2 NULL ALARM')

    def test_28(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 close/NULL lock/NULL open/ALARM'),
                         'BIP_1 NULL BIP_2 NULL NULL ALARM')

    def test_29(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 close/NULL unlock/BIP_1'),
                         'BIP_1 NULL BIP_2 NULL BIP_1')

    def test_30(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 lock/NULL open/NULL'),
                         'BIP_1 NULL BIP_2 NULL NULL')

    def test_31(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 lock/NULL lock/NULL open/NULL'),
                         'BIP_1 NULL BIP_2 NULL NULL NULL')

    def test_32(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 lock/NULL unlock/BIP_1'),
                         'BIP_1 NULL BIP_2 NULL BIP_1')

    def test_33(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 unlock/BIP_1 open/NULL'),
                         'BIP_1 NULL BIP_2 BIP_1 NULL')

    def test_34(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 unlock/BIP_1 lock/BIP_2 open/NULL'),
                         'BIP_1 NULL BIP_2 BIP_1 BIP_2 NULL')

    def test_35(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL lock/BIP_2 unlock/BIP_1 unlock/NULL'),
                         'BIP_1 NULL BIP_2 BIP_1 NULL')

    def test_36(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL unlock/NULL open/NULL'), 'BIP_1 NULL NULL NULL')

    def test_37(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL unlock/NULL lock/BIP_2 open/NULL'),
                         'BIP_1 NULL NULL BIP_2 NULL')

    def test_38(self):
        self.assertEqual(test_fsm('unlock/BIP_1 open/NULL unlock/NULL unlock/NULL'), 'BIP_1 NULL NULL NULL')

    def test_39(self):
        self.assertEqual(test_fsm('unlock/BIP_1 close/NULL open/NULL'), 'BIP_1 NULL NULL')

    def test_40(self):
        self.assertEqual(test_fsm('unlock/BIP_1 close/NULL lock/BIP_2 open/ALARM'), 'BIP_1 NULL BIP_2 ALARM')

    def test_41(self):
        self.assertEqual(test_fsm('unlock/BIP_1 close/NULL unlock/NULL'), 'BIP_1 NULL NULL')

    def test_42(self):
        self.assertEqual(test_fsm('unlock/BIP_1 lock/BIP_2 open/ALARM'), 'BIP_1 BIP_2 ALARM')

    def test_43(self):
        self.assertEqual(test_fsm('unlock/BIP_1 lock/BIP_2 lock/NULL open/ALARM'), 'BIP_1 BIP_2 NULL ALARM')

    def test_44(self):
        self.assertEqual(test_fsm('unlock/BIP_1 lock/BIP_2 unlock/BIP_1'), 'BIP_1 BIP_2 BIP_1')

    def test_45(self):
        self.assertEqual(test_fsm('unlock/BIP_1 unlock/NULL open/NULL'), 'BIP_1 NULL NULL')

    def test_46(self):
        self.assertEqual(test_fsm('unlock/BIP_1 unlock/NULL lock/BIP_2 open/ALARM'), 'BIP_1 NULL BIP_2 ALARM')

    def test_47(self):
        self.assertEqual(test_fsm('unlock/BIP_1 unlock/NULL unlock/NULL'), 'BIP_1 NULL NULL')
