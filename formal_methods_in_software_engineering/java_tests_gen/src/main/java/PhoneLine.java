import java.util.Timer;
import java.util.TimerTask;

public class PhoneLine {
    private PhoneLineContext _fsm;

    private String _responce;

    private Timer _timer;

    private TimerTask _timerTask;

    public PhoneLine() {
        _fsm = new PhoneLineContext(this);
    }

    public PhoneLineContext getContext() {
        return _fsm;
    }

    public String offHook() {
        _fsm.offHook();
        return _responce;
    }

    public String onHook() {
        _fsm.onHook();
        return _responce;
    }

    public String validNumber() {
        _fsm.validNumber();
        return _responce;
    }

    public String invalidNumber() {
        _fsm.invalidNumber();
        return _responce;
    }

    public void soundDialTone() {
        _responce = "soundDialTone";
    }

    public void disconnectedLine() {
        _responce = "disconnectedLine";
    }

    public void slowBusyTone() {
        _responce = "slowBusyTone";
    }

    public void fastBusyTone() {
        _responce = "fastBusyTone";
    }

    public void playMessage() {
        _responce = "playMessage";
    }

    public void findConnection() {
        _responce = "findConnection";
    }

    public void continues() {
        _responce = "continues";
    }

    public void startTimer() {
        _timer = new Timer();
        _timerTask = new TimerTask() {
            @Override
            public void run() {
                _fsm.getState().Exit(_fsm);
                _fsm.clearState();
                _fsm.setState(PhoneLineContext.PhoneLineFSM.Warning);
                _fsm.getState().Entry(_fsm);
            }
        };

        _timer.schedule(_timerTask, 300);
    }

    public void stopTimer() {
        _timerTask.cancel();
        _timerTask = null;
        _timer.cancel();
        _timer = null;
    }

}