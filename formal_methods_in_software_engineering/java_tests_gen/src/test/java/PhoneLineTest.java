import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

class PhoneLineTest {
    PhoneLine p;

    @BeforeEach
    void setUp() {
        p = new PhoneLine();
    }

    @AfterEach
    void tearDown() {
        p = null;
    }

    // 1/0 4/6 4/6 3/5 4/6 4/6 2/4
    // offHook/soundDialTone {invalidNumber, 2}/playMessage {validNumber, 2}/slowBusyTone

    @Test
    public void TestCase2() {
        assertEquals(p.offHook(), "soundDialTone");
        try { Thread.sleep(100); } catch (Exception ex) {};
        assertEquals(p.invalidNumber(), "playMessage");
        try { Thread.sleep(100); } catch (Exception ex) {};
        assertEquals(p.validNumber(), "slowBusyTone");
    }
}